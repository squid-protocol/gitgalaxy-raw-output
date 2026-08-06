#!/usr/bin/env python3
"""
Parse a version's batch_scan_master_*.log MISSION COMPLETE telemetry report and
BATCH ANOMALY & ERROR REPORT into structured data, append a row to the repo-wide
speed_history.csv, and render the LOC-vs-engine-time triangle-cluster chart.

Usage:
    python tools/generate_speed_telemetry.py v2.4.6
    python tools/generate_speed_telemetry.py --all
"""
import argparse
import csv
import json
import math
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
HISTORY_CSV = REPO_ROOT / "speed_history.csv"
HISTORY_FIELDS = [
    "version", "log_file", "run_date", "total_repos", "failed_repos",
    "total_loc", "total_time_s", "avg_rate_loc_s", "slow_files_gt10s",
    "typosquat_hits", "typosquat_repos",
]

FONT_CANDIDATES_SANS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans.ttf",
]
FONT_CANDIDATES_SANS_BOLD = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
]
FONT_CANDIDATES_MONO = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/dejavu/DejaVuSansMono.ttf",
]


def find_font(candidates):
    for c in candidates:
        if Path(c).exists():
            return c
    raise SystemExit(
        f"No usable font found among: {candidates}\n"
        "Install fonts-dejavu-core (apt-get install -y fonts-dejavu-core) before running this script."
    )


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

ROW_RE = re.compile(r'^\s*(\d+)\s*\|\s*(.+?)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d.]+)s\s*$')
SLOW_RE = re.compile(r'\s*-\s*\[([^\]]+)\]\s*:\s*(.+?)\s*\(([\d.]+)s\)')
TYPO_REPO_RE = re.compile(r'\s*-\s*\[([^\]]+)\]')


def pick_canonical_log(version_dir: Path) -> Path:
    """A version folder can hold more than one batch_scan_master_*.log (e.g. an
    aborted early run plus the full one). Prefer the one that actually reached
    MISSION COMPLETE; if several did, take the longest (most repos scanned)."""
    candidates = sorted(version_dir.glob("batch_scan_master_*.log"))
    if not candidates:
        raise SystemExit(f"No batch_scan_master_*.log found in {version_dir}")
    complete = []
    for log in candidates:
        with open(log, "r", errors="replace") as f:
            text = f.read()
        if "MISSION COMPLETE: GALAXYOSCOPE BATCH TELEMETRY REPORT" in text:
            complete.append((log, len(text)))
    if not complete:
        raise SystemExit(
            f"No log in {version_dir} reached MISSION COMPLETE "
            f"(checked: {[c.name for c in candidates]})"
        )
    complete.sort(key=lambda t: -t[1])
    return complete[0][0]


def parse_log(log_path: Path) -> dict:
    lines = log_path.read_text(errors="replace").splitlines(keepends=True)

    start = next(i for i, l in enumerate(lines) if "MISSION COMPLETE" in l)
    end = next(i for i in range(start, len(lines)) if lines[i].startswith("Total Repositories Scanned"))

    rows = []
    for l in lines[start:end]:
        m = ROW_RE.match(l)
        if m:
            rank, repo, loc, rate, t = m.groups()
            rows.append({
                "rank": int(rank),
                "repo": repo.strip(),
                "loc": int(loc.replace(",", "")),
                "rate": int(rate.replace(",", "")),
                "time": float(t),
            })

    totals_block = "".join(lines[end:end + 5])
    total_repos = int(re.search(r"Total Repositories Scanned\s*:\s*([\d,]+)", totals_block).group(1).replace(",", ""))
    total_loc = int(re.search(r"Total LOC Scanned\s*:\s*([\d,]+)", totals_block).group(1).replace(",", ""))
    total_time = float(re.search(r"Total Clock Time Taken\s*:\s*([\d.]+)", totals_block).group(1))
    avg_rate = int(re.search(r"Global Average Scan Rate\s*:\s*([\d,]+)", totals_block).group(1).replace(",", ""))

    if len(rows) != total_repos:
        raise SystemExit(
            f"Parsed {len(rows)} repo rows but log reports {total_repos} total_repos "
            f"in {log_path} -- parser is out of sync with the log format, fix ROW_RE before trusting output."
        )

    # ---- anomaly & error report ----
    failed_repos = 0
    fm = re.search(r"Failed Repositories:\s*(\d+)", "".join(lines))
    if fm:
        failed_repos = int(fm.group(1))

    slow_files = []
    try:
        slow_start = next(i for i, l in enumerate(lines) if "Slow Files > 10s" in l)
        for l in lines[slow_start + 1:]:
            if l.strip().startswith(("=", "⚠")) or l.strip() == "":
                break
            m = SLOW_RE.match(l)
            if m:
                slow_files.append({"repo": m.group(1), "file": m.group(2), "seconds": float(m.group(3))})
    except StopIteration:
        pass

    typo_total, typo_repos = 0, 0
    try:
        typo_start = next(i for i, l in enumerate(lines) if "Typosquatting Attempts" in l)
        seen_repos = set()
        for l in lines[typo_start + 1:]:
            if l.strip().startswith("="):
                break
            m = TYPO_REPO_RE.match(l)
            if m:
                typo_total += 1
                seen_repos.add(m.group(1))
        typo_repos = len(seen_repos)
    except StopIteration:
        pass

    run_date_m = re.search(r"batch_scan_master_(\d{8})_(\d{6})", log_path.name)
    run_date = f"{run_date_m.group(1)[:4]}-{run_date_m.group(1)[4:6]}-{run_date_m.group(1)[6:]}" if run_date_m else ""

    return {
        "log_file": log_path.name,
        "run_date": run_date,
        "total_repos": total_repos,
        "total_loc": total_loc,
        "total_time_s": total_time,
        "avg_rate_loc_s": avg_rate,
        "failed_repos": failed_repos,
        "slow_files": slow_files,
        "typosquat_hits": typo_total,
        "typosquat_repos": typo_repos,
        "repos": rows,
    }


# ---------------------------------------------------------------------------
# History CSV (one row per version, upserted)
# ---------------------------------------------------------------------------

def upsert_history(version: str, summary: dict):
    rows = []
    if HISTORY_CSV.exists():
        with open(HISTORY_CSV, newline="") as f:
            rows = list(csv.DictReader(f))
    rows = [r for r in rows if r["version"] != version]
    rows.append({
        "version": version,
        "log_file": summary["log_file"],
        "run_date": summary["run_date"],
        "total_repos": summary["total_repos"],
        "failed_repos": summary["failed_repos"],
        "total_loc": summary["total_loc"],
        "total_time_s": summary["total_time_s"],
        "avg_rate_loc_s": summary["avg_rate_loc_s"],
        "slow_files_gt10s": len(summary["slow_files"]),
        "typosquat_hits": summary["typosquat_hits"],
        "typosquat_repos": summary["typosquat_repos"],
    })
    rows.sort(key=lambda r: r["version"])
    with open(HISTORY_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HISTORY_FIELDS)
        w.writeheader()
        w.writerows(rows)


# ---------------------------------------------------------------------------
# Chart: LOC vs engine time, triangle-cluster label layout (square, white bg)
# ---------------------------------------------------------------------------

def render_loc_vs_time_chart(version: str, summary: dict, out_path: Path):
    rows = summary["repos"]

    f_title = ImageFont.truetype(find_font(FONT_CANDIDATES_SANS_BOLD), 33)
    f_sub = ImageFont.truetype(find_font(FONT_CANDIDATES_SANS), 15)
    f_tick = ImageFont.truetype(find_font(FONT_CANDIDATES_MONO), 14)
    f_axis = ImageFont.truetype(find_font(FONT_CANDIDATES_SANS), 25)
    f_label = ImageFont.truetype(find_font(FONT_CANDIDATES_SANS_BOLD), 19)

    COL_BG = (255, 255, 255)
    COL_PLOT_BORDER = (215, 222, 228)
    COL_GRID = (232, 236, 240)
    COL_TICK = (140, 148, 158)
    COL_AXIS = (76, 88, 102)
    COL_TITLE = (16, 21, 27)
    COL_SUB = (108, 118, 130)
    COL_DOT = (42, 120, 214)
    COL_DOT_RING = (255, 255, 255)
    COL_LINE = (203, 211, 220)
    COL_LABEL = (40, 46, 54)

    PLOT_W = PLOT_H = 1000
    loc_vals = [r["loc"] for r in rows]
    time_vals = [r["time"] for r in rows]
    LOC_DOMAIN = (max(1, min(loc_vals) * 0.7), max(loc_vals) * 1.3)
    TIME_DOMAIN = (max(0.01, min(time_vals) * 0.5), max(time_vals) * 1.3)

    def nice_ticks(domain, steps):
        lo, hi = math.log10(domain[0]), math.log10(domain[1])
        out = []
        for v, lbl in steps:
            if lo <= math.log10(v) <= hi:
                out.append((v, lbl))
        return out

    x_step_candidates = [(10, '10'), (100, '100'), (1000, '1K'), (10000, '10K'),
                          (100000, '100K'), (1000000, '1M'), (10000000, '10M'), (100000000, '100M')]
    y_step_candidates = [(0.1, '0.1s'), (1, '1s'), (10, '10s'), (100, '100s'), (1000, '1000s'), (10000, '10000s')]
    X_TICKS = nice_ticks(LOC_DOMAIN, x_step_candidates)
    Y_TICKS = nice_ticks(TIME_DOMAIN, y_step_candidates)

    def logx(v):
        return (math.log10(v) - math.log10(LOC_DOMAIN[0])) / (math.log10(LOC_DOMAIN[1]) - math.log10(LOC_DOMAIN[0])) * PLOT_W

    def logy(v):
        return PLOT_H - (math.log10(v) - math.log10(TIME_DOMAIN[0])) / (math.log10(TIME_DOMAIN[1]) - math.log10(TIME_DOMAIN[0])) * PLOT_H

    pts = [{"repo": r["repo"], "loc": r["loc"], "time": r["time"], "x": logx(r["loc"]), "y": logy(r["time"])} for r in rows]

    def text_w(text, font):
        bbox = font.getbbox(text)
        return bbox[2] - bbox[0]

    LABEL_H = 25

    n = len(pts)
    sx = sum(p["x"] for p in pts); sy = sum(p["y"] for p in pts)
    sxx = sum(p["x"] ** 2 for p in pts); sxy = sum(p["x"] * p["y"] for p in pts)
    denom = (n * sxx - sx * sx) or 1e-9
    m = (n * sxy - sx * sy) / denom
    b = (sy - m * sx) / n

    def line_y(x):
        return m * x + b

    for p in pts:
        p["side"] = "top" if p["y"] < line_y(p["x"]) else "bottom"
    top_pts = [p for p in pts if p["side"] == "top"]
    bot_pts = [p for p in pts if p["side"] == "bottom"]

    def pick_spread(group, n_bins):
        if not group:
            return []
        xs = [p["x"] for p in group]
        xmin, xmax = min(xs), max(xs)
        cells = {}
        for p in group:
            idx = 0 if xmax == xmin else min(n_bins - 1, int((p["x"] - xmin) / (xmax - xmin) * n_bins))
            if idx not in cells or p["loc"] > cells[idx]["loc"]:
                cells[idx] = p
        return list(cells.values())

    top_sel = pick_spread(top_pts, 130)
    bot_sel = pick_spread(bot_pts, 200)

    MARGIN = 22
    DOT_R = 2.6
    XJ = (0, -12, 12, -24, 24, -38, 38, -54, 54, -72, 72, -92, 92, -114, 114,
          -138, 138, -164, 164, -190, 190, -220, 220)

    def in_bounds(x0, y0, x1, y1):
        return x0 >= 2 and y0 >= 2 and x1 <= PLOT_W - 2 and y1 <= PLOT_H - 2

    def valid_side(x, y, side):
        ly = line_y(x)
        return y < ly - MARGIN if side == "top" else y > ly + MARGIN

    placed_boxes, placed = [], []

    def overlaps(box, boxes, pad=5):
        x0, y0, x1, y1 = box
        for bx0, by0, bx1, by1 in boxes:
            if x0 - pad < bx1 and x1 + pad > bx0 and y0 - pad < by1 and y1 + pad > by0:
                return True
        return False

    def overlaps_dots(box, pad=5):
        x0, y0, x1, y1 = box
        for p in pts:
            if (x0 - pad < p["x"] + DOT_R and x1 + pad > p["x"] - DOT_R and
                    y0 - pad < p["y"] + DOT_R and y1 + pad > p["y"] - DOT_R):
                return True
        return False

    def try_place_one(p, side):
        vdir = -1 if side == "top" else 1
        w = text_w(p["repo"], f_label)
        h = LABEL_H
        for step in range(0, 130):
            offset = 14 + step * 7
            for xj in XJ:
                lx, ly = p["x"] + xj, p["y"] + vdir * offset
                x0, y0, x1, y1 = lx - w / 2, ly - h / 2, lx + w / 2, ly + h / 2
                if not in_bounds(x0, y0, x1, y1):
                    continue
                if not valid_side(lx, y0 if side == "bottom" else y1, side):
                    continue
                box = (x0, y0, x1, y1)
                if overlaps(box, placed_boxes) or overlaps_dots(box):
                    continue
                placed_boxes.append(box)
                placed.append({**p, "lx": lx, "ly": ly, "lw": w})
                return True
        return False

    TARGET_PER_SIDE = 100
    top_count = bot_count = 0
    for p in sorted(top_sel, key=lambda p: p["x"]):
        if top_count >= TARGET_PER_SIDE:
            break
        if try_place_one(p, "top"):
            top_count += 1
    for p in sorted(bot_sel, key=lambda p: p["x"]):
        if bot_count >= TARGET_PER_SIDE:
            break
        if try_place_one(p, "bottom"):
            bot_count += 1

    ML, MR, MT, MB = 92, 92, 112, 72
    assert ML + MR == MT + MB
    W = H = ML + PLOT_W + MR
    img = Image.new("RGB", (W, H), COL_BG)
    d = ImageDraw.Draw(img)

    def tx(x): return x + ML
    def ty(y): return y + MT

    px0, py0, px1, py1 = tx(0), ty(0), tx(PLOT_W), ty(PLOT_H)

    for pl in placed:
        d.line([(tx(pl["x"]), ty(pl["y"])), (tx(pl["lx"]), ty(pl["ly"]))], fill=COL_LINE, width=1)

    d.rectangle([px0, py0, px1, py1], outline=COL_PLOT_BORDER, width=1)
    for val, lbl in X_TICKS:
        x = tx(logx(val))
        d.line([(x, py0), (x, py1)], fill=COL_GRID, width=1)
        tw = text_w(lbl, f_tick)
        d.text((x - tw / 2, py1 + 8), lbl, font=f_tick, fill=COL_TICK)
    for val, lbl in Y_TICKS:
        y = ty(logy(val))
        d.line([(px0, y), (px1, y)], fill=COL_GRID, width=1)
        tw = text_w(lbl, f_tick)
        d.text((px0 - tw - 10, y - 8), lbl, font=f_tick, fill=COL_TICK)

    xlab = "LOC scanned (log scale)"
    tw = text_w(xlab, f_axis)
    d.text(((px0 + px1) / 2 - tw / 2, py1 + 34), xlab, font=f_axis, fill=COL_AXIS)

    ylab_text = "Engine time, seconds (log scale)"
    ylab_w = text_w(ylab_text, f_axis) + 8
    ylab_img = Image.new("RGBA", (ylab_w, 34), (255, 255, 255, 0))
    yd = ImageDraw.Draw(ylab_img)
    yd.text((0, 0), ylab_text, font=f_axis, fill=COL_AXIS)
    ylab_img = ylab_img.rotate(90, expand=True)
    img.paste(ylab_img, (int(px0 - 62), int((py0 + py1) / 2 - ylab_img.height / 2)), ylab_img)

    for p in pts:
        x, y = tx(p["x"]), ty(p["y"])
        d.ellipse([x - 2.6, y - 2.6, x + 2.6, y + 2.6], fill=COL_DOT)
    for pl in placed:
        x, y = tx(pl["x"]), ty(pl["y"])
        d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=COL_DOT_RING)
        d.ellipse([x - 2.8, y - 2.8, x + 2.8, y + 2.8], fill=COL_DOT)
    for pl in placed:
        lx, ly = tx(pl["lx"]), ty(pl["ly"])
        d.text((lx - pl["lw"] / 2, ly - LABEL_H / 2 + 1), pl["repo"], font=f_label, fill=COL_LABEL)

    d.text((tx(0), ty(-98)), "Total LOC vs. engine time", font=f_title, fill=COL_TITLE)
    d.text((tx(0), ty(-58)),
           f"{len(rows)} repos, log–log scale — {len(placed)} labeled "
           f"({top_count} above / {bot_count} below trend) — GitGalaxy {version} batch, {summary['run_date']}",
           font=f_sub, fill=COL_SUB)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "PNG")
    return out_path


# ---------------------------------------------------------------------------

def process_version(version_dir: Path):
    version = version_dir.name
    log_path = pick_canonical_log(version_dir)
    print(f"[{version}] parsing {log_path.name}")
    summary = parse_log(log_path)

    summary_path = version_dir / "speed_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"[{version}] wrote {summary_path.relative_to(REPO_ROOT)}")

    upsert_history(version, summary)
    print(f"[{version}] updated {HISTORY_CSV.relative_to(REPO_ROOT)}")

    chart_path = version_dir / "speed_charts" / "loc_vs_time.png"
    render_loc_vs_time_chart(version, summary, chart_path)
    print(f"[{version}] wrote {chart_path.relative_to(REPO_ROOT)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("version", nargs="?", help="version folder name, e.g. v2.4.6")
    ap.add_argument("--all", action="store_true", help="process every v*/ folder in the repo")
    args = ap.parse_args()

    if args.all:
        version_dirs = sorted(p for p in REPO_ROOT.glob("v*") if p.is_dir())
        if not version_dirs:
            raise SystemExit("No v*/ version folders found.")
        for vd in version_dirs:
            process_version(vd)
    elif args.version:
        version_dir = REPO_ROOT / args.version
        if not version_dir.is_dir():
            raise SystemExit(f"No such version folder: {version_dir}")
        process_version(version_dir)
    else:
        ap.error("pass a version folder (e.g. v2.4.6) or --all")


if __name__ == "__main__":
    main()
