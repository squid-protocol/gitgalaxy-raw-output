# Batch scan → upload → telemetry runbook

How to produce a `v<version>/` batch, upload it, and get the Speed Telemetry and
Population Analysis charts to generate — without the failure modes we hit on v2.7.0.
Read this before running a batch.

## TL;DR (the five rules that keep it from breaking)

1. **Scan with the sequential driver** `gitgalaxy-population-analyses/batch_process_restored.py`.
   It captures galaxyscope's per-repo `Processed X at Y LOC/s` telemetry **and** emits the
   `batch_scan_master_*.log` both CI workflows depend on. **Do NOT** use an ad-hoc parallel
   driver that discards stdout — the engine does not persist per-repo scan time/rate anywhere,
   so if the driver drops it, the speed numbers are gone and can only be approximated.
2. **The `v<version>/batch_scan_master_*.log` is load-bearing. Never delete it.** It is the
   *only* trigger + input for `speed-telemetry.yml` **and** `population-analysis-audit.yml`,
   and both parse its "MISSION COMPLETE" table. No log ⇒ no charts, no audit.
3. **Full precision.** Scan with a venv that has `networkx tiktoken numpy pyyaml` so
   `is_zero_dependency_mode = 0` (else network metrics null out silently).
4. **Gzip + size before push.** Every `_audit.json`/`_master.db`/`_graph.sqlite`/`_sarif.json`/
   `_sbom.json` gzipped; `_gpu.json` + `_llm.md` raw. No file > 100 MB.
5. **Push in < 2 GB chunks over SSH.** GitHub rejects any single push pack > 2 GB, and this
   repo's remote must be SSH (HTTPS has no password auth).

## 1. Scan

```bash
FP=<gitgalaxy>/.crucible_venvs/full_precision/bin/python   # full-deps venv
ENGINE=<gitgalaxy worktree checked out at the release tag, e.g. v2.7.0>
export GITGALAXY_LICENSE_KEY="COMMUNITY_FREE_TIER"   # ← REQUIRED for timing (see below)
# The driver runs each repo one at a time and writes batch_scan_master_<ts>.log to --output.
PYTHONPATH="$ENGINE" "$FP" batch_process_restored.py \
    /srv/storage_16tb/projects/gitgalaxy/data \
    --output /srv/storage_16tb/projects/gitgalaxy-raw-output/v<version>
```

- **License key — set it or every timing is +5s.** `licensing.py::enforce_licensing_guard()`
  injects a fixed **5-second `time.sleep`** per process when no valid `GITGALAXY_LICENSE_KEY`
  is present (10s if a key is FORGED). Unset ⇒ every repo's wall-time is inflated by 5s,
  which wrecks the small-repo end of the rate model and any outlier analysis. Export the
  honor-system value `COMMUNITY_FREE_TIER` (documented in `gitgalaxy/README.md`) — or a valid
  commercial key — before scanning; both skip the delay. Do **not** remove the delay itself.

- **Engine:** check out the release **tag** in a worktree and point at it (via `PYTHONPATH`
  and the driver's `project_root`). Do not assume `v6` equals the tag — it drifts.
- **Sequential is deliberate:** single-process timings are what make the speed chart
  comparable across versions. A parallel run's wall-times are ~1/N of true throughput and are
  **not** comparable (this is why v2.7.0's first telemetry was only a labeled lower bound).
- **Corpus hygiene:** the driver now namespaces colliding basenames (`resolve_output_names`,
  see #4/#12 of the analyses repo) so two targets that share a name (e.g. the `redis` server
  vs the `redis-py` client, or two projects both named `core`) land in distinct output dirs
  instead of one silently shadowing the other. Keep basenames unique in `data/` regardless.
- Verify on the first repo's `master.db`: `SELECT is_zero_dependency_mode FROM repo_data` → `0`.

## 2. Pre-upload checklist

```bash
V=v<version>
# gzip any leftover raw compressibles (killed scans skip the compress step)
find $V -type f \( -name '*_galaxy_audit.json' -o -name '*_galaxy_master.db' \
  -o -name '*_galaxy_graph.sqlite' -o -name '*_galaxy_sarif.json' -o -name '*_galaxy_sbom.json' \) \
  -exec gzip -6 {} \;
test $(find $V -type f -size +95M | wc -l) -eq 0            # no file near 100 MB
test -n "$(ls $V/batch_scan_master_*.log 2>/dev/null)"      # THE LOG EXISTS  ← blocks upload if not
```

- **The last check is the guardrail against the v2.7.0 mistake.** If there is no
  `batch_scan_master_*.log` in the version dir, stop — the telemetry pipeline cannot run.
- Do **not** commit the merged population-analysis DB (multi-GB) or per-repo `.gitgalaxy/`
  caches. Only the 7-artifact bundle per repo + the log.

## 3. Upload (chunked, SSH)

```bash
git remote set-url origin git@github.com:squid-protocol/gitgalaxy-raw-output.git  # SSH, not HTTPS
git checkout -b batch/v<version> origin/main
# Commit + push in ~1.1 GB chunks so each pack stays < 2 GB (GitHub's hard push limit).
# See the chunking loop used for v2.7.0 (scratchpad/chunked_push.sh): greedily bucket the
# repo dirs by `du -sm`, and `git add <bucket>; git commit; git push` per bucket.
```

Open a PR into `main`; merging it triggers the two workflows below.

## 4. What the CI does on merge (both keyed on the log)

Both trigger on `push` to `main` touching `v*/batch_scan_master_*.log` (+ `workflow_dispatch`):

- **`speed-telemetry.yml`** (fast, ~2 min): parses the log's MISSION COMPLETE table →
  `speed_summary.json`, a `speed_history.csv` row, and `speed_charts/*` (+ `speed_charts/latest/`).
- **`population-analysis-audit.yml`** (heavy, up to ~4 h): merges every per-repo DB into one
  multi-GB database in runner scratch and runs the analysis suite → `v<version>/analysis/`.
  Because the batch log is already on `main` by the time you'd want to (re)run it for an
  existing version, re-run it with **`workflow_dispatch`, `version=v<version>`** (that path
  skips the change-detection jq).

Both derive the version from the pushed log; the auto-detect jq is null-safe for merge events
(#13). If you ever push a batch **without** a log, neither runs — that is the v2.7.0 bug.

## 5. If telemetry was lost (recovery, not the happy path)

If a batch shipped without a usable log (e.g. a parallel run discarded telemetry), you can
approximate it with `tools/reassemble_telemetry_log.py` — it rebuilds a MISSION COMPLETE log
from committed per-repo `Total LOC` + per-repo wall-times from the run log. **Its output is a
labeled lower bound, not comparable across versions** (see that script's header). The correct
fix is to re-scan sequentially per §1. Prefer re-scanning for any numbers that matter.
