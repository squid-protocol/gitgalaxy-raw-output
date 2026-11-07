# Engine for this batch

- **Engine:** squid-protocol/gitgalaxy `origin/main` @ `b64f42bfcfb7d91ccc71ed62637c6c73bfb1238d` (untagged; base release v2.12.0, tag `04fca555935a`)
- **Commit:** 2026-11-07 02:48:35 +0000  det/CICS: a file name the region did not define answers FILENOTFOUND (Part of #7487) (#7960)
- **Python:** `/srv/storage_16tb/projects/gitgalaxy/v6/.crucible_venvs/full_precision` (full precision: networkx, tiktoken, numpy, pyyaml present), with `PYTHONPATH` and the engine cwd set to the pinned worktree `/srv/storage_16tb/projects/gitgalaxy-worktrees/batch-b64f42bfcfb7`
- **Driver:** `gitgalaxy-population-analyses/batch_process_restored.py` from origin/main @ `5685ec2965917d56f6b8cbb4125bbf1d58db41ea`, run as a copy whose only change is `project_root` → the pinned worktree (the driver has no engine-root override)
- **Corpus:** `/srv/storage_16tb/projects/gitgalaxy/data` (→ `/nvme-data/gitgalaxy-data`), sequential, `GITGALAXY_LICENSE_KEY=COMMUNITY_FREE_TIER` (set by the driver)
- **Started:** 2026-11-06 23:03 EST

## Storage exception: two master databases are xz, not gzip

`linux/linux_galaxy_master.db.xz` and `freebsd-src/freebsd-src_galaxy_master.db.xz` are **xz**-compressed (93 MB / 85 MB):
gzipped they were 153 MB / 139 MB, over GitHub's 100 MB file limit (this engine records more per function than v2.9.x,
whose linux DB was ~80 MB gzipped). Decompress with `xz -d`. Tools that glob `*_galaxy_master.db.gz` (e.g.
population-analyses `build_master_db.py`, the population-analysis-audit workflow) will skip these two repos until
they also accept `.xz`. All other artifacts follow the runbook (gzip, < 100 MB). Empty SQLite `-shm`/`-wal` side files
(0 bytes) left by the scanner were not committed.
