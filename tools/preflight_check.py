#!/usr/bin/env python3
"""Pre-upload guard for a v<version>/ batch folder.

Blocks the exact failure modes we hit on v2.7.0. Run before committing/pushing a batch:

    python tools/preflight_check.py v2.7.0

Exits non-zero (and prints why) if any of these hold:
  * no batch_scan_master_*.log        -> the Speed Telemetry AND Population Analysis
                                          workflows cannot run (both trigger on and parse it).
  * a committed-format compressible artifact left un-gzipped
    (_audit.json/_master.db/_graph.sqlite/_sarif.json/_sbom.json).
  * any file >= 100 MB                 -> GitHub rejects the push.
  * a stray .gitgalaxy/ cache or merged population DB in the tree.
"""
import pathlib
import sys

COMPRESSIBLE = ("_galaxy_audit.json", "_galaxy_master.db", "_galaxy_graph.sqlite",
                "_galaxy_sarif.json", "_galaxy_sbom.json")
HARD_LIMIT = 100 * 1024 * 1024  # GitHub per-file hard limit


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: preflight_check.py v<version>")
    v = pathlib.Path(sys.argv[1])
    if not v.is_dir():
        sys.exit(f"❌ {v} is not a directory")

    problems = []

    if not list(v.glob("batch_scan_master_*.log")):
        problems.append(
            "no batch_scan_master_*.log — Speed Telemetry & Population Analysis workflows "
            "cannot run (they trigger on and parse it). Scan with the sequential "
            "batch_process_restored.py, or reassemble one (tools/reassemble_telemetry_log.py)."
        )

    raw = [p for p in v.rglob("*") if p.is_file() and any(p.name.endswith(e) for e in COMPRESSIBLE)]
    if raw:
        problems.append(f"{len(raw)} un-gzipped compressible artifact(s), e.g. {raw[0]} — gzip them (level 6).")

    big = [(p, p.stat().st_size) for p in v.rglob("*") if p.is_file() and p.stat().st_size >= HARD_LIMIT]
    if big:
        problems.append(f"{len(big)} file(s) >= 100 MB (GitHub push limit), e.g. {big[0][0]} ({big[0][1]/1e6:.0f} MB).")

    strays = [p for p in v.rglob(".gitgalaxy")] + [p for p in v.rglob("*_master.db") if p.is_file()]
    if strays:
        problems.append(f"stray cache/merged-DB artifact(s), e.g. {strays[0]} — must not be committed.")

    if problems:
        print(f"❌ {v} FAILED pre-upload checks:")
        for p in problems:
            print(f"   - {p}")
        sys.exit(1)

    n_repos = sum(1 for _ in v.glob("*/*_galaxy_gpu.json"))
    log = next(iter(v.glob("batch_scan_master_*.log"))).name
    print(f"✅ {v} OK — {n_repos} repos, log present ({log}), all artifacts gzipped, none >=100 MB.")


if __name__ == "__main__":
    main()
