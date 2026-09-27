"""Summarize human ratings and compare them with model P(Yes).

Save each rater's pasted results as pilot/human/<name>.json, then run:
  .venv/bin/python pilot/human.py [pilot/results_*.jsonl ...]
Scores 1-7 are rescaled to 0-1 so they sit on the same axis as P(Yes).
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
QS = ["credence", "reasonable", "evidence"]
CONDS = ["TS", "VD", "IR"]

raters, excluded = [], []
for f in sorted((HERE / "human").glob("*.json")):
    r = json.loads(f.read_text())
    ok = all((c["score"] <= 3) if c["expect"] == "no" else (c["score"] >= 5) for c in r["checks"])
    (raters if ok else excluded).append((f.name, r))
print(f"raters kept: {len(raters)}   excluded by attention checks: {[n for n, _ in excluded]}")
if not raters:
    sys.exit("no usable ratings in pilot/human/")

# h[q][cond][item] -> list of rescaled scores
h = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
for _, r in raters:
    for a in r["answers"]:
        h[a["q"]][a["cond"]][a["item"]].append((a["score"] - 1) / 6)

print("\nHuman mean (0-1), averaged over items; n raters per cell in brackets")
print(f"{'question':<12}" + "".join(f"{c:>16}" for c in CONDS))
for q in QS:
    cells = []
    for c in CONDS:
        per_item = [np.mean(v) for v in h[q][c].values()]
        n = sum(len(v) for v in h[q][c].values())
        cells.append(f"{np.mean(per_item):.2f} [{n}]" if per_item else "-")
    print(f"{q:<12}" + "".join(f"{s:>16}" for s in cells))

for path in sys.argv[1:]:
    rows = [json.loads(l) for l in open(path)]
    m = defaultdict(dict)
    for r in rows:
        if r["with_target"] and r["cond"] in CONDS:
            m[(r["question"], r["cond"])][r["item"]] = r["p_yes"]
    xs, ys = [], []
    for q in QS:
        for c in CONDS:
            for item, scores in h[q][c].items():
                xs.append(np.mean(scores))
                ys.append(m[(q, c)][item])
    r_ = np.corrcoef(xs, ys)[0, 1]
    print(f"\n{rows[0]['model']}: item-level correlation with humans r = {r_:.2f} (n = {len(xs)} cells)")
    print(f"{'question':<12}" + "".join(f"{c:>16}" for c in CONDS) + "   (model minus human)")
    for q in QS:
        cells = []
        for c in CONDS:
            its = list(h[q][c])
            if its:
                d = np.mean([m[(q, c)][i] for i in its]) - np.mean([np.mean(h[q][c][i]) for i in its])
                cells.append(f"{d:+.2f}")
            else:
                cells.append("-")
        print(f"{q:<12}" + "".join(f"{s:>16}" for s in cells))
