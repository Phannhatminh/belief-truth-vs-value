"""Build the human rating form (pilot/human_form.html) from the pilot stimuli.

Usage: .venv/bin/python pilot/build_form.py
"""

import json
from pathlib import Path

from stimuli import ITEMS, QUESTIONS, contexts

HERE = Path(__file__).parent

data = []
for it in ITEMS:
    ctx = contexts(it)
    data.append(dict(
        id=it["id"],
        target=f"{it['name']} believes that {it['p']}.",
        ctx={k: ctx[k] for k in ["TS", "VD", "IR"]},
        q={k: t.format(**it) for k, t in QUESTIONS.items()},
    ))

checks = [
    dict(id="check_color", passage="Rosa painted her kitchen door bright yellow last weekend. She is pleased with how it turned out.",
         q="Did Rosa paint her kitchen door blue?", expect="no"),
    dict(id="check_train", passage="Hugo takes the early train to work every day because it is less crowded. He likes to read on the way.",
         q="Does Hugo take the train to work?", expect="yes"),
]

template = (HERE / "human_form.template.html").read_text()
html = template.replace("__DATA__", json.dumps(data)).replace("__CHECKS__", json.dumps(checks))
(HERE / "human_form.html").write_text(html)
print(f"{len(data)} items -> {HERE / 'human_form.html'}")
