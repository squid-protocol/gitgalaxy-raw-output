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
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
HISTORY_CSV = REPO_ROOT / "speed_history.csv"
LATEST_DIR = REPO_ROOT / "speed_charts" / "latest"
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
FONT_CANDIDATES_MONO_BOLD = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "/usr/share/fonts/dejavu/DejaVuSansMono-Bold.ttf",
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
# Two-regime rate model: flat overhead floor below a knee, power-law scan
# time above it. See the methodology note in compute_rate_model()'s docstring.
# ---------------------------------------------------------------------------

def _loglog_fit(rows):
    """log10(time) = p*log10(loc) + logC, via least squares. Returns (p, logC, r2, n)."""
    xs = [math.log10(r["loc"]) for r in rows]
    ys = [math.log10(r["time"]) for r in rows]
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    p = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    logC = (sy - p * sx) / n
    y_mean = sy / n
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    ss_res = sum((y - (p * x + logC)) ** 2 for x, y in zip(xs, ys))
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
    return p, logC, r2, n


def compute_rate_model(rows: list) -> dict:
    """Fit the two-regime rate model this repo actually observes:

    - Below a "knee" LOC, scan time is flat -- dominated by fixed per-run
      overhead (process start, ingestion checks, DB writes), not by how much
      there is to scan. Floor = median time of the smallest ~10% of repos by
      LOC, which are essentially guaranteed to be overhead-dominated.
    - Above the knee, time follows a power law: time(s) = C * LOC^p. A single
      global log-log fit across all repos is biased toward the flat/overhead
      regime (it has the most points), so p is found by: (1) fit p_ref on the
      cleanest "definitely large" repos (top LOC quartile) as a reference,
      then (2) search LOC thresholds and pick the smallest one whose
      above-threshold fit exponent is closest to p_ref -- i.e. the earliest
      point where the true large-repo scaling behavior has already kicked in,
      keeping as much data as honestly possible.
    - The knee itself is *derived*, not assumed: the LOC where the power-law
      curve's predicted time crosses the flat floor.

    Returns a dict with both regimes' numbers plus fit diagnostics (R^2, n,
    LOC range) so nothing here is asserted without the evidence alongside it.
    """
    rows_sorted = sorted(rows, key=lambda r: r["loc"])
    n_total = len(rows_sorted)

    floor_n = max(20, n_total // 10)
    floor_sample = rows_sorted[:floor_n]
    floor_times = sorted(r["time"] for r in floor_sample)
    floor_seconds = floor_times[len(floor_times) // 2]

    top_quartile_cut = rows_sorted[int(n_total * 0.75)]["loc"]
    ref_sample = [r for r in rows if r["loc"] >= top_quartile_cut]
    p_ref, _, _, n_ref = _loglog_fit(ref_sample)

    candidates = [500, 1000, 1500, 2000, 3000, 5000, 7500, 10000,
                  15000, 20000, 30000, 50000, 75000, 100000]
    best = None
    for t in candidates:
        big = [r for r in rows if r["loc"] >= t]
        if len(big) < 100:
            continue
        p, logC, r2, n = _loglog_fit(big)
        diff = abs(p - p_ref)
        if best is None or diff < best[0]:
            best = (diff, t, p, logC, r2, n, big)
    if best is None:
        raise SystemExit("compute_rate_model: no LOC threshold had >=100 repos above it -- corpus too small")
    _, threshold, p, logC, r2, n, fit_sample = best
    C = 10 ** logC

    knee_loc = (floor_seconds / C) ** (1 / p)
    fit_loc_min = min(r["loc"] for r in fit_sample)
    fit_loc_max = max(r["loc"] for r in fit_sample)

    return {
        "floor_seconds": floor_seconds,
        "floor_sample_n": floor_n,
        "floor_sample_loc_max": floor_sample[-1]["loc"],
        "knee_loc": knee_loc,
        "power_p": p,
        "power_C": C,
        "power_r2": r2,
        "power_fit_n": n,
        "power_fit_loc_min": fit_loc_min,
        "power_fit_loc_max": fit_loc_max,
        "power_fit_threshold": threshold,
        "reference_p": p_ref,
        "reference_n": n_ref,
        "reference_loc_min": top_quartile_cut,
        "total_repos": n_total,
    }


def render_rate_model_card(version: str, summary: dict, model: dict, out_path: Path):
    """A wide 'hero' stat card for the README: the two-regime rate model in
    big, bold numbers, matching the scatter chart's visual language."""
    f_sans = lambda sz: ImageFont.truetype(find_font(FONT_CANDIDATES_SANS), sz)
    f_bold = lambda sz: ImageFont.truetype(find_font(FONT_CANDIDATES_SANS_BOLD), sz)
    f_mono_bold = lambda sz: ImageFont.truetype(find_font(FONT_CANDIDATES_MONO_BOLD), sz)

    f_kicker = f_bold(16)
    f_title = f_bold(30)
    f_range = f_bold(23)
    f_body = f_sans(17)
    f_foot = f_sans(14)

    COL_BG = (255, 255, 255)
    COL_CARD = (246, 249, 255)
    COL_BORDER = (215, 222, 228)
    COL_KICKER = (0, 110, 255)
    COL_TITLE = (16, 21, 27)
    COL_RANGE = (16, 21, 27)
    COL_HEADLINE = (0, 78, 199)
    COL_BODY = (55, 64, 75)
    COL_FOOT = (120, 129, 140)

    def text_w(text, font):
        bbox = font.getbbox(text)
        return bbox[2] - bbox[0]

    def wrap(text, font, max_w):
        words, lines, cur = text.split(), [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if text_w(trial, font) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def fit_headline(text, max_w, start_size=34, min_size=18):
        for sz in range(start_size, min_size - 1, -1):
            font = f_mono_bold(sz)
            if text_w(text, font) <= max_w:
                return font
        return f_mono_bold(min_size)

    W, H = 1272, 620
    PAD = 40
    GAP = 28
    CARD_W = (W - 2 * PAD - GAP) // 2
    CARD_H = 420
    CARD_TOP = 150

    img = Image.new("RGB", (W, H), COL_BG)
    d = ImageDraw.Draw(img)

    d.text((PAD, 32), "GITGALAXY SCAN RATE MODEL", font=f_kicker, fill=COL_KICKER)
    d.text((PAD, 58), "Total LOC vs. engine time, fit as two regimes", font=f_title, fill=COL_TITLE)

    TEXT_W = CARD_W - 52  # inner width available for wrapped/fitted text

    def draw_card(x0, kicker, headline_text, body_text, foot_text):
        x1, y1 = x0 + CARD_W, CARD_TOP + CARD_H
        d.rounded_rectangle([x0, CARD_TOP, x1, y1], radius=14, fill=COL_CARD, outline=COL_BORDER, width=1)
        y = CARD_TOP + 26
        d.text((x0 + 26, y), kicker, font=f_range, fill=COL_RANGE)
        y += 46
        headline_font = fit_headline(headline_text, TEXT_W)
        d.text((x0 + 26, y), headline_text, font=headline_font, fill=COL_HEADLINE)
        y += headline_font.size + 20
        for line in wrap(body_text, f_body, TEXT_W):
            d.text((x0 + 26, y), line, font=f_body, fill=COL_BODY)
            y += 25
        foot_lines = wrap(foot_text, f_foot, TEXT_W)
        y = y1 - 20 - 18 * len(foot_lines)
        for line in foot_lines:
            d.text((x0 + 26, y), line, font=f_foot, fill=COL_FOOT)
            y += 18

    knee = model["knee_loc"]
    draw_card(
        PAD,
        f"1 – {knee:,.0f} LOC",
        f'≈ {model["floor_seconds"]:.2f}s flat',
        "Fixed per-run overhead (process start, ingestion checks, DB writes) "
        "dominates -- time barely depends on repo size here.",
        f'Floor = median time of the {model["floor_sample_n"]} smallest repos '
        f'(≤{model["floor_sample_loc_max"]:,} LOC) by LOC in this batch.',
    )

    eq = f'time(s) ≈ {model["power_C"]:.3g} × LOC^{model["power_p"]:.3f}'
    draw_card(
        PAD + CARD_W + GAP,
        f"{knee:,.0f}+ LOC",
        eq,
        f'Scan-bound, near-linear: R²={model["power_r2"]:.2f} on '
        f'{model["power_fit_n"]} repos from {model["power_fit_loc_min"]:,} to '
        f'{model["power_fit_loc_max"]:,} LOC. Individual repos vary with '
        "language mix and comment density -- this is the central trend, not a guarantee.",
        f'Exponent cross-checked at {model["reference_p"]:.3f} on just the top-quartile-by-LOC '
        f'repos ({model["reference_n"]}, ≥{model["reference_loc_min"]:,} LOC) as a bias check.',
    )

    foot = (f'GitGalaxy {version} batch, {summary["run_date"]} — {model["total_repos"]} repos. '
            "Fit is cross-repo (different languages/repos), not one repo measured at multiple sizes -- "
            "read it as strong evidence of near-linear scaling, not a proven worst-case bound.")
    for i, line in enumerate(wrap(foot, f_foot, W - 2 * PAD)):
        d.text((PAD, H - 54 + i * 18), line, font=f_foot, fill=COL_FOOT)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "PNG")
    return out_path


# ---------------------------------------------------------------------------
# Chart: LOC vs engine time, triangle-cluster label layout (square, white bg)
# ---------------------------------------------------------------------------

def render_loc_vs_time_chart(version: str, summary: dict, out_path: Path):
    rows = summary["repos"]

    LABEL_FONT_SIZE = 19  # repo point-labels -- the floor every other chart font must meet

    f_title = ImageFont.truetype(find_font(FONT_CANDIDATES_SANS_BOLD), 33)
    f_sub = ImageFont.truetype(find_font(FONT_CANDIDATES_SANS), LABEL_FONT_SIZE)
    f_tick = ImageFont.truetype(find_font(FONT_CANDIDATES_MONO_BOLD), LABEL_FONT_SIZE + 2)
    f_axis = ImageFont.truetype(find_font(FONT_CANDIDATES_SANS_BOLD), max(28, LABEL_FONT_SIZE + 2))
    f_label = ImageFont.truetype(find_font(FONT_CANDIDATES_SANS_BOLD), LABEL_FONT_SIZE)

    COL_BG = (255, 255, 255)
    COL_PLOT_BORDER = (215, 222, 228)
    COL_GRID = (232, 236, 240)
    COL_TICK = (90, 99, 110)
    COL_AXIS = (35, 43, 53)
    COL_TITLE = (16, 21, 27)
    COL_SUB = (108, 118, 130)
    COL_DOT = (0, 110, 255)
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
    top_pts = sorted((p for p in pts if p["side"] == "top"), key=lambda p: p["x"])
    bot_pts = sorted((p for p in pts if p["side"] == "bottom"), key=lambda p: p["x"])

    MARGIN = 22
    DOT_R = 2.6
    # How far a label can drift from its own point, both sideways and along the
    # connector line. Generous on purpose: the top triangle has more open room
    # than the bottom one, and letting lines run longer is what lets a label
    # actually reach into that leftover space instead of giving up early.
    XJ = tuple(range(-280, 281, 14))
    MAX_OFFSET_STEPS = 160
    OFFSET_STEP_PX = 7

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
        for step in range(0, MAX_OFFSET_STEPS):
            offset = 14 + step * OFFSET_STEP_PX
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

    def fill_side(side_pts, side, stride=7):
        """Walk the side's points taking every `stride`-th one, then repeat with
        the next starting offset (1st, 8th, 15th... then 2nd, 9th, 16th...) so
        the label set is spread evenly across the whole LOC range -- covering
        small, mid, and huge repos alike -- rather than biased toward whichever
        repos happen to be biggest, and keep going until nothing more fits."""
        n = len(side_pts)
        count = 0
        for phase in range(stride):
            for i in range(phase, n, stride):
                if try_place_one(side_pts[i], side):
                    count += 1
        return count

    top_count = fill_side(top_pts, "top")
    bot_count = fill_side(bot_pts, "bottom")

    # Margins are sized around the actual font metrics rather than fixed constants,
    # since every font here is pinned to (or derived from) LABEL_FONT_SIZE and a
    # hardcoded margin that fit the old, smaller tick/subtitle fonts clips or
    # overlaps once those fonts grow to match the label size floor.
    GAP_TICK_AXIS = 10
    GAP_TICK_YLABEL = 14
    GAP_YLABEL_EDGE = 14
    max_ytick_w = max(text_w(lbl, f_tick) for _, lbl in Y_TICKS)
    ylabel_thickness = f_axis.size + 16
    ML = MR = GAP_TICK_AXIS + max_ytick_w + GAP_TICK_YLABEL + ylabel_thickness + GAP_YLABEL_EDGE

    tick_line_h = f_tick.size + 6
    GAP_TICK_XLAB = 12
    BOTTOM_PAD = 16
    MB = GAP_TICK_AXIS - 2 + tick_line_h + GAP_TICK_XLAB + f_axis.size + BOTTOM_PAD

    PAD_TOP = 14
    GAP_TITLE_SUB = 14
    GAP_SUB_PLOT = 22
    MT = PAD_TOP + f_title.size + GAP_TITLE_SUB + f_sub.size + GAP_SUB_PLOT

    # keep the outer canvas square by padding out whichever margin pair is smaller
    if ML + MR > MT + MB:
        MB += (ML + MR) - (MT + MB)
    else:
        extra = (MT + MB) - (ML + MR)
        ML += extra // 2
        MR += extra - extra // 2
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
        d.text((x - tw / 2, py1 + GAP_TICK_AXIS - 2), lbl, font=f_tick, fill=COL_TICK)
    for val, lbl in Y_TICKS:
        y = ty(logy(val))
        d.line([(px0, y), (px1, y)], fill=COL_GRID, width=1)
        tw = text_w(lbl, f_tick)
        d.text((px0 - tw - GAP_TICK_AXIS, y - f_tick.size / 2), lbl, font=f_tick, fill=COL_TICK)

    xlab = "LOC scanned (log scale)"
    tw = text_w(xlab, f_axis)
    d.text(((px0 + px1) / 2 - tw / 2, py1 + GAP_TICK_AXIS - 2 + tick_line_h + GAP_TICK_XLAB),
           xlab, font=f_axis, fill=COL_AXIS)

    ylab_text = "Engine time, seconds (log scale)"
    ylab_w = text_w(ylab_text, f_axis) + 8
    ylab_img = Image.new("RGBA", (ylab_w, ylabel_thickness), (255, 255, 255, 0))
    yd = ImageDraw.Draw(ylab_img)
    yd.text((0, 0), ylab_text, font=f_axis, fill=COL_AXIS)
    ylab_img = ylab_img.rotate(90, expand=True)
    ylab_x = px0 - GAP_TICK_AXIS - max_ytick_w - GAP_TICK_YLABEL - ylabel_thickness
    img.paste(ylab_img, (int(ylab_x), int((py0 + py1) / 2 - ylab_img.height / 2)), ylab_img)

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

    d.text((tx(0), PAD_TOP), "Total LOC vs. engine time", font=f_title, fill=COL_TITLE)
    d.text((tx(0), PAD_TOP + f_title.size + GAP_TITLE_SUB),
           f"{len(rows)} repos, log–log scale — {len(placed)} labeled "
           f"({top_count} above / {bot_count} below trend) — GitGalaxy {version} batch, {summary['run_date']}",
           font=f_sub, fill=COL_SUB)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "PNG")
    return out_path


# ---------------------------------------------------------------------------

def version_key(version_dir_name: str):
    """'v2.4.10' -> (2, 4, 10), so this sorts numerically, not lexically."""
    parts = re.findall(r"\d+", version_dir_name)
    return tuple(int(p) for p in parts) if parts else (0,)


def is_highest_version(version: str) -> bool:
    all_versions = [p.name for p in REPO_ROOT.glob("v*") if p.is_dir()]
    if not all_versions:
        return True
    return version_key(version) == max(version_key(v) for v in all_versions)


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

    model = compute_rate_model(summary["repos"])
    model_json_path = version_dir / "speed_charts" / "rate_model.json"
    with open(model_json_path, "w") as f:
        json.dump(model, f, indent=2)

    model_txt_path = version_dir / "speed_charts" / "rate_model.txt"
    knee = model["knee_loc"]
    model_txt = (
        f"GitGalaxy Scan Rate Model\n"
        f"{version} batch, {summary['run_date']} ({model['total_repos']} repos)\n"
        f"\n"
        f"Regime 1 -- Fixed overhead:  1 - {knee:,.0f} LOC  ->  ~{model['floor_seconds']:.2f}s (flat)\n"
        f"  Floor = median time of the {model['floor_sample_n']} smallest repos "
        f"(<={model['floor_sample_loc_max']:,} LOC).\n"
        f"\n"
        f"Regime 2 -- Scan-bound:      {knee:,.0f}+ LOC  ->  "
        f"time(s) ~= {model['power_C']:.4g} * LOC^{model['power_p']:.4f}\n"
        f"  R^2={model['power_r2']:.3f}, n={model['power_fit_n']}, "
        f"fit range {model['power_fit_loc_min']:,}-{model['power_fit_loc_max']:,} LOC.\n"
        f"  Reference exponent (top-quartile-by-LOC repos only, n={model['reference_n']}, "
        f">={model['reference_loc_min']:,} LOC): {model['reference_p']:.4f}\n"
    )
    model_txt_path.write_text(model_txt)
    print(f"[{version}] wrote {model_json_path.relative_to(REPO_ROOT)} and {model_txt_path.name}")

    card_path = version_dir / "speed_charts" / "rate_model.png"
    render_rate_model_card(version, summary, model, card_path)
    print(f"[{version}] wrote {card_path.relative_to(REPO_ROOT)}")

    # speed_charts/latest/ is a stable path the README embeds directly, so the
    # README's markdown never needs editing -- only ever overwritten by whichever
    # version is numerically newest, so reprocessing an older version by hand
    # (e.g. --all backfill) can't clobber it with stale data.
    if is_highest_version(version):
        LATEST_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(chart_path, LATEST_DIR / "loc_vs_time.png")
        shutil.copyfile(card_path, LATEST_DIR / "rate_model.png")
        shutil.copyfile(model_json_path, LATEST_DIR / "rate_model.json")
        shutil.copyfile(model_txt_path, LATEST_DIR / "rate_model.txt")
        with open(LATEST_DIR / "version.json", "w") as f:
            json.dump({"version": version, "run_date": summary["run_date"]}, f, indent=2)
        print(f"[{version}] updated {LATEST_DIR.relative_to(REPO_ROOT)}/ (highest version)")
    else:
        print(f"[{version}] not the highest version present -- left speed_charts/latest/ alone")


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
