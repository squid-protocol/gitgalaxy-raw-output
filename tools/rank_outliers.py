#!/usr/bin/env python3
"""Rank repos by how far their ACTUAL scan time deviates from the version's own
rate-model equation -- the residual `actual / predicted`. This is the method
that first surfaced the ghostty ReDoS (26x over the line in v2.7.0): repos far
above the fit harbor a superlinear / pathological hot path worth investigating;
repos far below are unusually cheap for their size.

Reuses the canonical telemetry the speed pipeline already produces:
  <version>/speed_charts/rate_model.json   (the two-regime fit)
  <version>/speed_summary.json             (per-repo loc / rate / time)

Prediction mirrors generate_speed_telemetry's model:
  time <= knee_loc            -> floor_seconds
  time  > knee_loc            -> power_C * LOC ** power_p

Only repos at/above the model's `power_fit_threshold` are ranked by default:
below it the floor dominates and the ratio is noise. Writes
<version>/speed_charts/outliers.json and prints the top deviators.

Usage:
  python tools/rank_outliers.py v2.8.1 [--top 20] [--min-loc N]
"""
import argparse
import json
import statistics
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def predict(loc, m):
    if loc <= m["knee_loc"]:
        return m["floor_seconds"]
    return m["power_C"] * loc ** m["power_p"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("version", help="version dir, e.g. v2.8.1")
    ap.add_argument("--top", type=int, default=20, help="how many top deviators to print (default 20)")
    ap.add_argument("--min-loc", type=int, default=None, help="override the LOC floor (default: model's power_fit_threshold)")
    args = ap.parse_args()

    vdir = REPO_ROOT / args.version
    model = json.loads((vdir / "speed_charts" / "rate_model.json").read_text())
    summary = json.loads((vdir / "speed_summary.json").read_text())
    floor_loc = args.min_loc if args.min_loc is not None else model["power_fit_threshold"]

    rows = []
    for r in summary["repos"]:
        loc, t = r["loc"], r["time"]
        if loc <= 0 or t <= 0:
            continue
        pt = predict(loc, model)
        rows.append({
            "repo": r["repo"],
            "loc": loc,
            "actual_s": round(t, 2),
            "predicted_s": round(pt, 2),
            "ratio": round(t / pt, 3),
            "above_threshold": loc >= floor_loc,
        })

    ranked = sorted([x for x in rows if x["above_threshold"]], key=lambda x: -x["ratio"])
    med = statistics.median([x["ratio"] for x in ranked]) if ranked else float("nan")

    out = {
        "version": args.version,
        "equation": f"t = {model['power_C']:.3e} * LOC^{model['power_p']:.4f}",
        "knee_loc": model["knee_loc"],
        "floor_seconds": model["floor_seconds"],
        "loc_floor_for_ranking": floor_loc,
        "n_ranked": len(ranked),
        "median_ratio": round(med, 3),
        "outliers": ranked,          # slowest-vs-model first
        "all_rows": rows,            # full set (incl. below threshold) for charting
    }
    out_path = vdir / "speed_charts" / "outliers.json"
    out_path.write_text(json.dumps(out, indent=2))

    print(f"{args.version}: {out['equation']}  (ranking {len(ranked)} repos >= {floor_loc:,} LOC; median ratio {med:.2f}x)")
    print(f"{'repo':<28}{'LOC':>12}{'actual':>10}{'pred':>9}{'ratio':>8}")
    for x in ranked[: args.top]:
        print(f"{x['repo'][:27]:<28}{x['loc']:>12,}{x['actual_s']:>9.1f}s{x['predicted_s']:>8.1f}s{x['ratio']:>7.2f}x")
    print(f"\nwrote {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
