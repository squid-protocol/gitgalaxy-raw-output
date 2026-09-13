#!/usr/bin/env python3
"""Reassemble a ``batch_scan_master_*.log`` from committed artifacts + a run log.

WHY THIS EXISTS
---------------
The Speed Telemetry pipeline (``tools/generate_speed_telemetry.py`` +
``.github/workflows/speed-telemetry.yml``) is driven entirely by a
``v*/batch_scan_master_*.log`` that carries a "MISSION COMPLETE: GALAXYOSCOPE
BATCH TELEMETRY REPORT" block: a ``Rank | Repository | LOC Scanned |
Rate (LOC/s) | Engine Time`` table plus a totals block. The workflow only fires
on a push that touches such a log, and the generator hard-fails without it.

The v2.7.0 batch was produced by a *parallel* driver that discarded galaxyscope's
per-repo telemetry (stdout), and the interim logs were removed during cleanup.
The engine does **not** persist per-repo scan time or rate in its artifacts
(only LOC survives, in each ``*_galaxy_master.db``/report), so the table cannot be
recovered from the outputs alone. Rather than re-run a multi-hour scan, this
script reassembles the log from the two real sources we still have.

WHAT IT REASSEMBLES FROM
------------------------
  * per-repo LOC  -> ``Total LOC`` in each ``v<ver>/<repo>/<repo>_galaxy_llm.md``
                     (exact; the engine's own reported figure).
  * per-repo time -> the wall-clock ``✅ <repo> (<n>s)`` lines in the batch run
                     log passed as --run-log.

CAVEAT (read before trusting the chart)
---------------------------------------
Those per-repo times were measured under N-way worker concurrency, so they are
wall times, NOT single-process engine time: the derived LOC/s is roughly 1/N of
the engine's true throughput and is a LOWER BOUND. It is therefore NOT directly
comparable to sequentially-measured batches (v2.4.6/v2.4.7). For a clean,
cross-version-comparable chart, run the SEQUENTIAL batch_process_restored.py,
which emits this log natively with real single-process rates.

WHAT THE PIPELINE NEEDS TO OPERATE
----------------------------------
A ``v<ver>/batch_scan_master_<YYYYMMDD>_<HHMMSS>.log`` whose MISSION COMPLETE
table has exactly ``Total Repositories Scanned`` data rows, each matching
``^\\d+ | name | loc | rate | time.s$`` (rate integer, time float+"s"), followed
by the totals block ("Total Repositories Scanned/LOC Scanned/Clock Time Taken/
Global Average Scan Rate") and a "Failed Repositories:" line. Pushing that file
to main triggers the workflow; ``workflow_dispatch`` re-processes on demand.

Usage:
    python tools/reassemble_telemetry_log.py \\
        --version-dir v2.7.0 --run-log <parallel_run.log> --wall-clock 7294 \\
        [--concurrency 2] [--exclude redis]
"""
import argparse
import datetime
import pathlib
import re

TIME_RE = re.compile(r"✅\s+(\S+)\s+\(([\d.]+)s\)")
LOC_RE = re.compile(r"Total LOC\s*\|\s*([\d,]+)")


def repo_loc(version_dir: pathlib.Path, repo: str):
    llm = version_dir / repo / f"{repo}_galaxy_llm.md"
    if not llm.exists():
        return None
    m = LOC_RE.search(llm.read_text(errors="replace"))
    return int(m.group(1).replace(",", "")) if m else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--version-dir", required=True, help="e.g. v2.7.0")
    ap.add_argument("--run-log", required=True, help="batch run log with '✅ <repo> (<n>s)' lines")
    ap.add_argument("--wall-clock", type=float, required=True, help="real total wall-clock seconds of the batch run")
    ap.add_argument("--concurrency", type=int, default=1, help="worker concurrency the run used (for the header note)")
    ap.add_argument("--exclude", nargs="*", default=[],
                    help="repos whose logged time does not correspond to the committed output (e.g. a shadowed stub)")
    args = ap.parse_args()

    vdir = pathlib.Path(args.version_dir)
    run_log = pathlib.Path(args.run_log)
    excl = set(args.exclude)

    times = {}
    for line in run_log.read_text(errors="replace").splitlines():
        m = TIME_RE.search(line)
        if m:
            times[m.group(1)] = float(m.group(2))

    rows, omitted = [], []
    for repo, t in sorted(times.items()):
        if repo in excl:
            omitted.append((repo, "excluded: logged time was for a shadowed/duplicate scan, not the committed output"))
            continue
        loc = repo_loc(vdir, repo)
        if loc is None:
            omitted.append((repo, "no committed report / LOC not found"))
            continue
        if not loc or loc <= 0:
            omitted.append((repo, "zero scanned LOC (docs/data-only repo — not plottable on a log axis)"))
            continue
        if t <= 0:
            omitted.append((repo, "non-positive time"))
            continue
        rows.append({"name": repo, "loc": loc, "rate": round(loc / t), "time": t})

    rows.sort(key=lambda r: -r["rate"])
    total_loc = sum(r["loc"] for r in rows)
    n = len(rows)
    avg_rate = round(total_loc / args.wall_clock) if args.wall_clock else 0
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = vdir / f"batch_scan_master_{ts}.log"

    L = []
    L.append("=" * 78)
    L.append(f"REASSEMBLED TELEMETRY LOG — {vdir.name}")
    L.append("=" * 78)
    L.append("This log was RE-ASSEMBLED after the fact, not emitted by a live batch run,")
    L.append("so the Speed Telemetry pipeline has an input to render this version's chart.")
    L.append("")
    L.append("Why: the batch was scanned with a parallel driver that discarded galaxyscope's")
    L.append("per-repo telemetry (stdout), and the interim batch_scan_master logs were removed.")
    L.append("The engine does not persist per-repo scan time/rate in its artifacts, so the")
    L.append("table below could not be recovered from the outputs alone.")
    L.append("")
    L.append("Reassembled from:")
    L.append(f"  - per-repo LOC : 'Total LOC' in each {vdir.name}/<repo>/<repo>_galaxy_llm.md (exact).")
    L.append(f"  - per-repo time: '✅ <repo> (<n>s)' wall times in {run_log.name}.")
    L.append("")
    L.append(f"CAVEAT: times were measured under {args.concurrency}-way worker concurrency, so they are")
    L.append(f"wall times, not single-process engine time — the derived LOC/s is ~1/{args.concurrency} of the")
    L.append("engine's true throughput and is a LOWER BOUND. NOT directly comparable to the")
    L.append("sequentially-measured v2.4.6/v2.4.7 batches. For a clean, comparable chart, re-run")
    L.append("the sequential batch_process_restored.py (it emits this log natively).")
    L.append(f"Coverage: {n} repos with per-repo timing reassembled" + (f"; {len(omitted)} omitted." if omitted else "."))
    for repo, why in omitted:
        L.append(f"  - omitted {repo}: {why}")
    L.append("")
    L.append("What the pipeline needs: this MISSION COMPLETE block — a Rank|Repo|LOC|Rate|Time")
    L.append("table whose row count equals 'Total Repositories Scanned', plus the totals block.")
    L.append("=" * 78)
    L.append("")
    L.append("=" * 80)
    L.append("MISSION COMPLETE: GALAXYOSCOPE BATCH TELEMETRY REPORT")
    L.append("=" * 80)
    L.append(f"{'Rank':<5} | {'Repository':<30} | {'LOC Scanned':<12} | {'Rate (LOC/s)':<12} | Engine Time")
    L.append("-" * 80)
    for i, r in enumerate(rows, 1):
        name = r["name"] if len(r["name"]) <= 28 else r["name"][:25] + "..."
        L.append(f"{i:<5} | {name:<30} | {r['loc']:<12,} | {r['rate']:<12,} | {r['time']:.2f}s")
    L.append("-" * 80)
    L.append(f"Total Repositories Scanned : {n}")
    L.append(f"Total LOC Scanned          : {total_loc:,}")
    L.append(f"Total Clock Time Taken     : {args.wall_clock:.2f} seconds")
    L.append(f"Global Average Scan Rate   : {avg_rate:,} LOC/s")
    L.append("")
    L.append("=" * 80)
    L.append(" 🚨 BATCH ANOMALY & ERROR REPORT")
    L.append("=" * 80)
    L.append("❌ Failed Repositories: 0")
    L.append("")

    out.write_text("\n".join(L))
    print(f"Wrote {out} — {n} repos, {total_loc:,} LOC, avg {avg_rate:,} LOC/s, {len(omitted)} omitted.")


if __name__ == "__main__":
    main()
