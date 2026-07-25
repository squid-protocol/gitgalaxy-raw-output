# gitgalaxy-raw-output

Source of truth for the raw products of the [gitgalaxy](https://github.com/squid-protocol/gitgalaxy) scanner — every scan batch, unmodified, kept versioned over time.

This repo does **not** contain analysis code. Aggregation and population-level analysis (clustering, the threat classifier, the merged master database, etc.) live in a separate repo, `gitgalaxy-population-analyses`, which reads its raw inputs from here.

## Layout

One folder per scanner version, each holding the per-repo output bundles flat, matching gitgalaxy's own `updated_results_*` convention:

```
gitgalaxy-raw-output/
├── v2.4.5/
│   ├── linux_galaxy_audit.json.gz
│   ├── linux_galaxy_master.db.gz
│   ├── linux_galaxy_graph.sqlite.gz
│   ├── linux_galaxy_gpu.json          (uncompressed)
│   ├── linux_galaxy_llm.md            (uncompressed)
│   └── ... (× 716 repos)
└── v2.4.6/   (next batch, same shape)
```

**Why some files are gzipped and others aren't:** `_galaxy_audit.json`, `_galaxy_master.db`, and `_galaxy_graph.sqlite` can individually exceed GitHub's 100MB per-file push limit (audit.json alone has hit 1.2GB uncompressed on a single large repo). They also compress extremely well — gzip alone took a 20.6GB/716-repo batch down to ~2.65GB with zero files left over 100MB, so no Git LFS is needed. `_galaxy_gpu.json` and `_galaxy_llm.md` are always small and stay uncompressed for easy inline viewing.

## Corpus

`corpus/` pins the exact set of source repositories a given scan batch was run against, so the input corpus is reproducible on another machine:

- `corpus/v1/manifest.json` — every repo's name, origin URL, and the exact commit it was scanned at.
- `corpus/setup_corpus.py` — clones every repo in a manifest at its pinned commit.

```
python3 corpus/setup_corpus.py v1 --dest /path/to/gitgalaxy/data
```

This lets someone else stand up the same scanning environment without needing the corpus repos handed to them directly.
