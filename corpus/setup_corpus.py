#!/usr/bin/env python3
"""
Clones every repo listed in a corpus manifest (corpus/<version>/manifest.json)
at its pinned commit, so a fresh machine can reproduce the exact set of repos
gitgalaxy was scanning at that snapshot.

Usage:
    python3 setup_corpus.py v1 --dest /srv/storage_16tb/projects/gitgalaxy/data
    python3 setup_corpus.py v1 --dest ./corpus_data --only corpus_python
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()


def load_manifest(version):
    manifest_path = SCRIPT_DIR / version / "manifest.json"
    if not manifest_path.exists():
        print(f"❌ No manifest found at {manifest_path}")
        sys.exit(1)
    return json.loads(manifest_path.read_text())


def clone_and_pin(repo, dest_root):
    target = dest_root / repo["clone_path"]
    if target.exists():
        print(f"⏩ Skipping (already exists): {repo['clone_path']}")
        return True

    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"⬇️  Cloning {repo['name']} -> {target}")
    clone = subprocess.run(
        ["git", "clone", "--quiet", repo["url"], str(target)],
        capture_output=True, text=True,
    )
    if clone.returncode != 0:
        print(f"❌ Clone failed for {repo['name']}: {clone.stderr.strip()}")
        return False

    checkout = subprocess.run(
        ["git", "-C", str(target), "checkout", "--quiet", repo["commit"]],
        capture_output=True, text=True,
    )
    if checkout.returncode != 0:
        print(f"⚠️  Checkout of pinned commit failed for {repo['name']} "
              f"({repo['commit']}): {checkout.stderr.strip()}")
        return False

    return True


def main():
    parser = argparse.ArgumentParser(description="Reproduce a pinned gitgalaxy scan corpus.")
    parser.add_argument("version", help="Corpus version to install, e.g. v1")
    parser.add_argument("--dest", required=True, help="Directory to clone repos into")
    parser.add_argument("--only", default=None,
                         help="Only clone repos in this group (e.g. corpus_python), or top-level repos if 'root'")
    parser.add_argument("--scan", action="store_true", help="Trigger GitGalaxy batch scan after cloning/pinning corpus")
    parser.add_argument("--output", default=None, help="Output destination folder for scan artifacts when --scan is used")
    args = parser.parse_args()

    manifest = load_manifest(args.version)
    dest_root = Path(args.dest).resolve()
    dest_root.mkdir(parents=True, exist_ok=True)

    repos = manifest["repos"]
    if args.only:
        want_group = None if args.only == "root" else args.only
        repos = [r for r in repos if r["group"] == want_group]

    print(f"🚀 Installing corpus {args.version}: {len(repos)} repos -> {dest_root}")
    if manifest.get("excluded_non_git_paths"):
        print(f"ℹ️  {len(manifest['excluded_non_git_paths'])} entries in the original snapshot "
              f"were not git repos and are not reproducible by this script (see manifest).")

    failures = []
    for repo in repos:
        if not clone_and_pin(repo, dest_root):
            failures.append(repo["name"])

    print("\n" + "=" * 50)
    print(f"Done. {len(repos) - len(failures)}/{len(repos)} repos ready at their pinned commit.")
    if failures:
        print(f"❌ Failed: {', '.join(failures)}")
        
    if args.scan:
        print("\n🚀 Initiating GitGalaxy Batch Scan...")
        batch_script = Path("/srv/storage_16tb/projects/gitgalaxy/v6/utilities/batch_process.py")
        if not batch_script.exists():
            print(f"❌ Batch process script not found at {batch_script}")
            sys.exit(1)
        
        scan_cmd = [sys.executable, str(batch_script), str(dest_root)]
        if args.output:
            scan_cmd.extend(["--output", str(Path(args.output).resolve())])
        
        proc = subprocess.run(scan_cmd)
        if proc.returncode != 0:
            print(f"⚠️ Batch scan completed with exit code {proc.returncode}")
    
    print("=" * 50)


if __name__ == "__main__":
    main()

