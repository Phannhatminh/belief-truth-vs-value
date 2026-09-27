"""Score each stimulus as P(Yes) / (P(Yes) + P(No)) on the first answer token.

Usage: .venv/bin/python pilot/run.py <mlx model repo> <out.jsonl>
"""

import json
import sys
from pathlib import Path

import mlx.core as mx
from mlx_lm import load

model_id, out_path = sys.argv[1], sys.argv[2]
model, tok = load(model_id)

yes_id = tok.encode("Yes", add_special_tokens=False)[0]
no_id = tok.encode("No", add_special_tokens=False)[0]

rows = [json.loads(l) for l in (Path(__file__).parent / "stimuli.jsonl").read_text().splitlines()]
with open(out_path, "w") as f:
    for i, r in enumerate(rows):
        user = f"{r['passage']}\n\nQuestion: {r['q_text']}\nAnswer with only Yes or No."
        prompt = tok.apply_chat_template([{"role": "user", "content": user}],
                                         add_generation_prompt=True, tokenize=False)
        ids = mx.array(tok.encode(prompt, add_special_tokens=False))[None]
        logits = model(ids)[0, -1].astype(mx.float32)
        logp = logits - mx.logsumexp(logits)
        ly, ln = logp[yes_id].item(), logp[no_id].item()
        r.update(model=model_id, p_yes=float(mx.sigmoid(mx.array(ly - ln)).item()),
                 mass_yes_no=float(mx.exp(mx.array(ly)).item() + mx.exp(mx.array(ln)).item()))
        f.write(json.dumps(r) + "\n")
        if i % 50 == 0:
            print(i, len(rows), flush=True)
print("done", out_path)
