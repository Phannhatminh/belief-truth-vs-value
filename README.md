# Two readings of "believe" in language models

Research notes and a behavioral pilot on one question:

> When the word *believe* is identical and only the context decides whether it is **truth-seeking** belief or **value-driven** belief (believing because holding the belief improves one's prospects, while one's credence stays low), do language models tell the two readings apart?

Example of the value-driven reading: a patient facing a 10% chance of surgical success believes the operation will succeed, because patients who go in believing it recover better. Their credence stays at 0.1; what they choose is the attitude.

## Contents

- `note.md` — project notes (in Vietnamese): problem statement, formalization, literature, novelty checks, cost estimates, pilot design and results.
- `pilot/` — behavioral pilot (level 1 of 3: behavior, representation, causal use).
  - `stimuli.py` — 24 items across 4 domains, each in conditions TS (truth-seeking), IR (belief against evidence, no stake), VD (IR + one sentence saying the belief helps), plus lexical controls VDn and IRf.
  - `run.py` — scores P(Yes) on the first answer token with an MLX model.
  - `analyze.py` — condition means, bootstrap CIs, paired Wilcoxon contrasts.
  - `human_form.template.html`, `build_form.py` — rating form for the human baseline (3 Latin-square lists).
  - `human.py` — summarizes human ratings and compares them with model outputs.
  - `results_*.jsonl` — raw model outputs.

## Pilot results so far

Qwen2.5-7B-Instruct and Qwen3-4B-Instruct-2507, 4-bit MLX, n = 24 items. P(Yes) by condition, TS / VD / IR:

| Question | Qwen2.5-7B | Qwen3-4B |
|---|---|---|
| Does the person think it is likely? | 1.00 / 0.71 / 0.27 | 1.00 / 1.00 / 0.80 |
| Is the belief reasonable? | 0.94 / 0.44 / 0.08 | 1.00 / 0.63 / 0.18 |
| Would they drop it given bad evidence? | 0.76 / 0.11 / 0.52 | 0.52 / 0.06 / 0.56 |

The models treat value-driven belief as resistant to evidence and more reasonable than belief against evidence, but they still attribute high credence to it, more than to belief against evidence. Rewording the stake sentence without "convinced" does not change this.

**Not yet interpretable:** there is no human baseline yet, the stimuli were drafted with an AI assistant and have not been validated, and there is one question template per question. See `note.md` §9 for all limitations.

## Reproduce

```
uv venv .venv --python 3.11 && uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python pilot/stimuli.py
.venv/bin/python pilot/run.py mlx-community/Qwen2.5-7B-Instruct-4bit pilot/results_qwen25_7b.jsonl
.venv/bin/python pilot/analyze.py pilot/results_qwen25_7b.jsonl
```

Requires Apple Silicon (MLX).
