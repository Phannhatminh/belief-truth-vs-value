"""Summarize pilot results.

Usage: .venv/bin/python pilot/analyze.py results_*.jsonl
"""

import json
import sys
from collections import defaultdict

import numpy as np
from scipy.stats import wilcoxon

rng = np.random.default_rng(0)


def boot_ci(x, n=5000):
    x = np.asarray(x)
    means = rng.choice(x, (n, len(x))).mean(1)
    return np.percentile(means, [2.5, 97.5])


def fmt(x):
    lo, hi = boot_ci(x)
    return f"{np.mean(x):.2f} [{lo:.2f}, {hi:.2f}]"


for path in sys.argv[1:]:
    rows = [json.loads(l) for l in open(path)]
    print(f"\n=== {rows[0]['model']}  ({path})")
    print(f"mean P(Yes)+P(No) mass: {np.mean([r['mass_yes_no'] for r in rows]):.3f}")

    # v[question][cond][item] = p_yes (with target); c[cond][item] = credence without target
    v = defaultdict(lambda: defaultdict(dict))
    c = defaultdict(dict)
    mech = {}
    for r in rows:
        mech[r["item"]] = r["mech"]
        if r["with_target"]:
            v[r["question"]][r["cond"]][r["item"]] = r["p_yes"]
        else:
            c[r["cond"]][r["item"]] = r["p_yes"]
    items = sorted(mech)

    print("\nP(Yes), mean [95% bootstrap CI] over items")
    conds = [k for k in ["TS", "VD", "IR", "VDn", "IRf"] if k in v["credence"]]
    print(f"{'question':<12}" + "".join(f"{k:>22}" for k in conds) + "   expected TS/VD/IR")
    expected = {"credence": "Y / N / Y", "reasonable": "Y / Y / N", "evidence": "Y / N / N"}
    for q in ["credence", "reasonable", "evidence"]:
        cells = [fmt([v[q][k][i] for i in items]) for k in conds]
        print(f"{q:<12}" + "".join(f"{s:>22}" for s in cells) + f"   {expected[q]}")

    print("\nPaired contrasts (mean diff over items, Wilcoxon p)")

    def contrast(label, a, b, sub=None):
        its = [i for i in items if sub is None or mech[i] == sub]
        d = np.array([a[i] - b[i] for i in its])
        p = wilcoxon(d).pvalue if np.any(d != 0) else 1.0
        print(f"  {label:<48} {d.mean():+.3f}  (p={p:.3g}, n={len(d)})")

    contrast("credence   VD - IR  (distinguish => < 0)", v["credence"]["VD"], v["credence"]["IR"])
    contrast("reasonable VD - IR  (distinguish => > 0)", v["reasonable"]["VD"], v["reasonable"]["IR"])
    contrast("evidence   VD - TS  (distinguish => < 0)", v["evidence"]["VD"], v["evidence"]["TS"])
    contrast("evidence   VD - IR", v["evidence"]["VD"], v["evidence"]["IR"])
    if "VDn" in conds:
        for q in ["credence", "reasonable", "evidence"]:
            contrast(f"{q:<10} VDn - VD  (lexical cue effect)", v[q]["VDn"], v[q]["VD"])
            contrast(f"{q:<10} VDn - IR", v[q]["VDn"], v[q]["IR"])
            contrast(f"{q:<10} IRf - IR  (extra-sentence effect)", v[q]["IRf"], v[q]["IR"])
    for cond in conds:
        contrast(f"credence shift from belief report, {cond}", v["credence"][cond], c[cond])
    for m in ["a", "b"]:
        contrast(f"credence VD - IR, mech={m}", v["credence"]["VD"], v["credence"]["IR"], sub=m)
        contrast(f"reasonable VD - IR, mech={m}", v["reasonable"]["VD"], v["reasonable"]["IR"], sub=m)
