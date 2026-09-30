# Lit-Review.md — Two Readings of "Believe": Truth-Seeking vs. Value-Driven Belief in Language Models

No existing public dataset or benchmark directly tests whether language models can tell truth-seeking belief from value-driven belief when the verb "believe" and the propositional content are held fixed and only the context differs. The closest resources are human-subject stimulus sets from experimental philosophy and psychology (Vesga, Van Leeuwen & Lombrozo 2025; Cusimano & Lombrozo 2021/2023; Armor, Massey & Sackett 2008; Buckwalter, Rose & Turri 2015) and LLM epistemic benchmarks that test a different distinction (KaBLE: belief vs. knowledge vs. fact). The project should therefore build its own benchmark, anchored to those human paradigms so models can be scored against published human response patterns.

## TL;DR

- **The gap is real.** I found no 2023–2026 LLM benchmark that holds belief content constant and varies only whether the belief is held for evidential or practical/value reasons. The nearest LLM work covers other distinctions: belief vs. knowledge (KaBLE, *Nature Machine Intelligence* 2025), identity-congruent motivated reasoning under assigned personas (Dash et al. 2025), and fact vs. opinion claim types (CheckThat!, CDCP).\[1\] The nearest *human* evidence is Vesga, Van Leeuwen & Lombrozo (2025, *JEP: General*): laypeople attribute distinct epistemic and non-epistemic kinds of belief even when content and certainty are held constant — the contrast the repo's pilot tests.
- **The repo's pilot points at one specific failure.** Qwen models rate value-driven (VD) belief as evidence-resistant and more "reasonable" than belief against evidence, and human data predict both judgments. But the models also attribute *high credence* to the VD believer (Qwen2.5-7B: 0.71 vs. 0.27 for IR; Qwen3-4B: 1.00 vs. 0.80). They fold *acceptance/commitment* into *credence* — the thick-vs-thin, credence-vs-acceptance distinction philosophers draw. The credence probe is the diagnostic one; the other two may just reproduce human-like normative intuitions.
- **Recommended benchmark: "TwoBelieve", a factorial minimal-pair benchmark with a human baseline.** ~600 validated items across ≥6 domains, each in matched TS / IR / VD / lexical-control variants, probed on credence, evidence-responsiveness, reasonableness, action prediction and "think" vs. "believe" choice, with Prolific rating distributions as soft labels. Add a first-person track in which belief holders state their own reasons and what would change their mind. Naturally occurring text (ChangeMyView, eRulemaking) is useful only as a secondary, repurposed evaluation.

---

## Summary

**What the repo does.** `Phannhatminh/belief-truth-vs-value` ("Two readings of 'believe' in language models") asks: *"When the word believe is identical and only the context decides whether it is truth-seeking belief or value-driven belief (believing because holding the belief improves one's prospects, while one's credence stays low), do language models tell the two readings apart?"*\[2\] The worked example is a patient facing a 10% chance of surgical success who "believes" the operation will succeed because believing it improves recovery; credence stays at 0.1 and the belief is a chosen attitude.\[2\] The project plans three levels — behavior, representation, causal use — and has run the level-1 behavioral pilot.\[2\]

**Main findings.**
1. The repo's construct is narrower than generic "evidence vs. values": it is *pragmatically/prudentially motivated belief with low credence*. It sits at the intersection of pragmatism about reasons for belief, prescribed optimism (Armor et al. 2008), thick vs. thin belief (Buckwalter et al. 2015), Van Leeuwen's credence vs. factual belief, and Vesga et al.'s epistemic vs. non-epistemic belief attribution.
2. Human work gives directly usable predictions: laypeople use "believe" more for non-epistemic, religious-style attitudes and "think" more for factual ones (Heiphetz, Landers & Van Leeuwen 2021; Van Leeuwen, Weisman & Luhrmann 2021); they expect non-epistemic beliefs to be less evidence-responsive (Vesga et al. 2025; Metz, Liquin & Lombrozo 2023); and they often endorse morally or prudentially motivated beliefs (Cusimano & Lombrozo 2021, 2023; Armor et al. 2008).
3. LLM work shows adjacent weaknesses — poor first-person false-belief attribution (Suzgun et al. 2025), identity-congruent motivated reasoning under personas (Dash et al. 2025), sycophancy and unfaithful rationalization — but none tests the repo's contrast.
4. **Suitable data do not exist off the shelf.** CDCP, Hidey et al. CMV, Touché23-ValueEval, CheckThat! subjectivity, KaBLE and Aroyehun et al.'s EMI resources can be repurposed for auxiliary tracks, but none labels *why* a belief is held or *how it would respond to evidence* with content held fixed.

---

## 1. Repo overview

**Access note.** The repository is public. I could read the README and file listing. The other files — `note.md` (Vietnamese notes: problem statement, formalization, literature, novelty checks, cost estimates, pilot design and results), `direction.md`, `problems.md`, `revised_plan_believe.md`, `COMMITS.md`, `problem1/` and the `pilot/` source — were not retrievable under this environment's fetch restrictions. Everything below comes from the README. The repo's own literature list and its limitations list (`note.md` §9) should be merged in by a collaborator with direct access; this is the main open uncertainty in this review.

| Aspect | What the repo states |
|---|---|
| Research question | Do LMs distinguish truth-seeking from value-driven readings of "believe" when the verb is identical and only context disambiguates? |
| Truth-seeking (TS) | Belief formed to track evidence; credence matches the belief. |
| Value-driven (VD) | "Believing because holding the belief improves one's prospects, while one's credence stays low." Operationalized as IR + one sentence stating the belief helps.\[2\] |
| Control: IR | Belief against evidence, no stake. |
| Lexical controls | VDn (stake sentence reworded without "convinced"); IRf (lexical control for IR). |
| Stimuli | `pilot/stimuli.py`: 24 items across 4 domains × TS, IR, VD, VDn, IRf. Drafted with an AI assistant; not yet validated.\[2\] |
| Models | Qwen2.5-7B-Instruct and Qwen3-4B-Instruct-2507, 4-bit MLX, Apple Silicon.\[2\] |
| Scoring | P(Yes) on the first answer token (`run.py`); condition means, bootstrap CIs, paired Wilcoxon contrasts (`analyze.py`).\[2\] |
| Probes | (Q1) Does the person think it is likely? (credence) (Q2) Is the belief reasonable? (Q3) Would they drop it given bad evidence? |
| Human baseline | Planned: `human_form.template.html`, `build_form.py` (3 Latin-square lists), `human.py`. Not yet collected.\[2\] |
| Roadmap | Behavior → representation (probing) → causal use (interventions). |

**Pilot results (P(Yes), TS / VD / IR):**

| Probe | Qwen2.5-7B | Qwen3-4B |
|---|---|---|
| Thinks it is likely? | 1.00 / 0.71 / 0.27 | 1.00 / 1.00 / 0.80 |
| Reasonable? | 0.94 / 0.44 / 0.08 | 1.00 / 0.63 / 0.18 |
| Drop it given bad evidence? | 0.76 / 0.11 / 0.52 | 0.52 / 0.06 / 0.56 |

**Interpretation.** The probes do not carry equal diagnostic weight.
- **Q2 and Q3.** VD > IR on reasonableness, and VD least likely to be dropped, is probably what humans would say: people prescribe optimism in such scenarios (Armor et al. 2008), let moral or prudential value lower the evidential threshold (Cusimano & Lombrozo 2021), and predict non-epistemic beliefs to be less evidence-responsive (Vesga et al. 2025).\[3\]\[4\]\[5\] A human-like model *should* show this, so it is not evidence of confusion.
- **Q1 is the real test.** By construction the VD believer's credence is low (same as IR). A model that separates acceptance from credence should give VD ≤ IR on Q1. Both models give VD > IR, Qwen3-4B at ceiling. Models appear to read "believes + has a reason to" as "is confident that", resembling KaBLE's finding that models struggle to keep what someone believes apart from what is true or likely.\[6\]
- **Artifacts to rule out.** Q3 for TS is oddly low (0.76, 0.52) and Q1 for IR is high in Qwen3 (0.80), suggesting yes-bias and literal-reading artifacts. Balanced polarity and multiple templates per probe are needed first.
- **Humans might not show the clean pattern.** Vesga et al. (2025) held certainty constant by design, so whether humans attribute low credence to the VD believer is untested.\[4\] The human baseline is essential, not a formality.

---

## 2. Conceptual foundations and definitions

### 2.1 The target contrast

The repo's contrast is best stated as **credence vs. acceptance under practical motivation**, not "fact vs. value proposition". The proposition is factual ("the operation will succeed"); what differs is the *attitude* and its *basis*:

| Dimension | Truth-seeking (epistemic) belief | Value-driven (non-epistemic) belief |
|---|---|---|
| Basis | Evidence, testimony, inference | Practical benefit, morality, loyalty, identity, hope, signaling |
| Credence | Tracks evidence | Can be low or decoupled; agent may know the odds |
| Evidential vulnerability | Revised by counter-evidence | Resistant; counter-evidence often already known |
| Practical-setting dependence | Guides action in all settings | Guides action in some settings (going into surgery) but not others (making a will) |
| Voluntariness | Largely involuntary | Experienced as partly chosen or cultivated |
| Folk vocabulary | More "thinks" | More "believes", "believes in", "chooses to believe" |

The rows combine Van Leeuwen's (2014) markers of factual belief (practical-setting independence, cognitive governance, evidential vulnerability) with the dimensions tested by Vesga et al. (2025) and Vesga, Van Leeuwen & Lombrozo (CogSci 2024): think/believe wording, binary vs. probabilistic framing, voluntariness, objectivity and evidence-responsiveness.

### 2.2 Philosophy and cognitive science of belief types

- **Van Leeuwen: factual belief vs. religious/group "credence".** Van Leeuwen (2014, *Cognition* 133(3):698–715) argues factual beliefs guide action in all practical settings, govern inferences from other attitudes, and are evidentially vulnerable; religious credences have a perceived normative orientation, are open to free elaboration, and are vulnerable to special authority.\[7\] *Religion as Make-Believe* (Harvard UP, 2023) treats credence as an imagination-like attitude that defines group identity;\[8\] the 2025 *Philosophia* précis notes it could equally be called "ideological credence".\[9\] **Relevance:** operational markers — evidential vulnerability matches Q3, and practical-setting dependence suggests an *action-prediction* probe. Critiques: Levy (2024, *Mind & Language*) argues content, not attitude, often explains the departures;\[10\] Talmont-Kaminski (2016, *Frontiers in Psychology*) disputes whether the traits co-occur.\[7\]
- **Van Leeuwen & Lombrozo (2023), "The Puzzle of Belief", *Cognitive Science* 47(2):e13245, DOI 10.1111/cogs.13245.** *Belief pluralism*: distinct "property clusters" in a multidimensional space constitute varieties of believing, discoverable empirically.\[11\] **Relevance:** licence for two readings of "believe" and for a multi-probe design.
- **Buckwalter, Rose & Turri (2015), "Belief through Thick and Thin", *Noûs* 49(4):748–775, DOI 10.1111/nous.12048.** "Thin" belief is a bare representational attitude; "thick" belief adds emotion, endorsement or conviction; folk psychology tracks the difference.\[12\] **Relevance:** VD resembles thick endorsement without thin representation.\[13\] Supplementary materials contain vignettes.
- **Sperber's intuitive vs. reflective beliefs** (Sperber 1997, *Mind & Language* 12(1):67–83). Reflective beliefs are held via a validating context ("the priest says that…"), without evidential tracking. **Relevance:** a third reading (belief on authority) to keep separate from VD.
- **Epistemic vs. practical reasons.** Evidentialism allows only evidence; pragmatism (James's "Will to Believe") allows practical reasons — the surgery case is textbook pragmatism. **Moral encroachment** (e.g., Basu & Schroeder 2019): moral stakes raise evidential thresholds. **Doxastic partiality** (Stroud 2006, *Ethics*; Keller 2004): friendship licenses believing well beyond the evidence. **Relevance:** these define VD *sub-types* (prudential, moral, relational, identity) for a secondary label.
- **Socially adaptive, signaling or "tribal" beliefs.** Williams (2021, "Socially adaptive belief", *Mind & Language* 36(3)); Funkhouser on beliefs as costly signals. **Relevance:** the identity/signaling sub-type that Vesga et al. manipulated.
- **Belief-that vs. belief-in.** "Believing in" expresses trust or commitment ("The many meanings of belief", *Synthese* 2025).\[14\] **Relevance:** a lexical confound; keep *believe that* fixed and treat *believe in* as a control.
- **"Believe" vs. "think".** Heiphetz, Landers & Van Leeuwen (2021, *Psychology of Religion and Spirituality* 13(3):287–297, DOI 10.1037/rel0000238): "believe that" has many religious collocates, "think that" none; people prefer "believe" for religious credences and "think" for factual statements.\[15\]\[16\] Van Leeuwen, Weisman & Luhrmann (2021, *Open Mind* 5:91–99, DOI 10.1162/opmi_a_00044) replicated this in the US, Ghana, Thailand, China and Vanuatu, "even when the ascribed belief contents were held constant and only the surrounding context varied".\[17\] **Relevance:** a ready-made *forced-choice probe* ("She ___ that the operation will succeed") with cross-cultural human baselines — and a warning that "believe" itself is a lexical cue.

### 2.3 Operational definitions

- **TS (label E):** the agent accepts P; context makes clear credence is high *because of* evidence and would be revised given counter-evidence.
- **VD (label V):** the agent accepts P; credence is low or unchanged by the practical reason; a non-evidential reason for accepting P is given (prudential, moral, relational, identity, religious).
- **IR (label I):** the agent accepts P against the evidence, no stated reason.
- **Mixed (label M):** both kinds of reason present, with relative weight recorded.

**Secondary labels:** (1) justification type: evidential / testimonial-authority / prudential / moral / relational / identity-signaling / religious / intuitive-affective; (2) proposition type: fact / value / policy / mixed (following CDCP and Hollihan & Baaske); (3) evidence sensitivity: what would change the agent's mind; (4) attributed credence (0–100); (5) practical-setting scope.

---

## 3. Literature review by theme

### 3.1 Psychology: folk conceptions of belief

| Work | Summary | Relevance |
|---|---|---|
| **Vesga, Van Leeuwen & Lombrozo (2025)**, *JEP: General* 154(8):2241–2256, DOI 10.1037/xge0001765 | Three studies, N = 1,843 US adults. Laypeople attribute different kinds of belief depending on whether it plays epistemic roles (truth-tracking) or non-epistemic roles (social signaling); the kinds support different predictions about values and behavior "even when the believed content and attributed level of certainty about that content are held constant".\[4\] Precursor (CogSci 2024): epistemic-aim beliefs described more with "thinks", framed more probabilistically, seen as less voluntary. |\[18\] **Closest human analog.** Template for stimuli, probes and baselines. They hold certainty constant; the repo lets credence differ. Request OSF materials. |
| **Metz, Liquin & Lombrozo (2023)**, *Cognitive Science* 47(11):e13370, DOI 10.1111/cogs.13370 | 707 participants. Religious contexts raise endorsement of ethical, affiliative and intuitive justifications; in religion, more religious or intuitive justification goes with lower openness to revision. Counter-consensus beliefs about contentious science (climate, vaccines) have religion-like profiles.\[19\]\[20\]\[21\] | Justification taxonomy; shows "value-driven" is not just "religious". |
| **Cusimano & Lombrozo (2021)**, *Cognition* 209:104513, DOI 10.1016/j.cognition.2020.104513 | People treat moral considerations as legitimate grounds for belief; morally beneficial beliefs need less evidence; people sometimes prescribe evidentially poor beliefs.\[3\] | Predicts humans will rate VD beliefs fairly "reasonable" (Q2). Vignettes adaptable. |
| **Cusimano & Lombrozo (2023)**, *Cognition* 234:105379, DOI 10.1016/j.cognition.2023.105379 | People recognize moral influences on their beliefs and still judge their reasoning ideal.\[22\] | Supports first-person ground truth. |
| **Armor, Massey & Sackett (2008)**, *Psychological Science* 19(4):329–331, DOI 10.1111/j.1467-9280.2008.02089.x | Across four scenarios, participants judged optimistically biased predictions better than accurate ones.\[5\] Replicated (OSF osf.io/qlzap; Tenney, Logg & Moore 2015).\[23\] Miller, Park, Smith & Windschitl (2021, *Psychological Science* 32(10):1605–1616, DOI 10.1177/09567976211004545) found that "although people favored prescriptions of optimism, they also prescribed likelihood estimates that were essentially pessimistic"; 151 of 208 participants prescribed optimism yet also prescribed accuracy or underestimation for at least one of three scenarios. | **Directly relevant to the surgery case.** Miller et al.'s dissociation is the human version of "credence stays low". |
| **Heiphetz, Spelke, Harris & Banaji (2013)**, *J. Exp. Social Psychology* 49(3):559–565 | Ideological (religious) beliefs treated as intermediate between facts and preferences. | Proposition-type axis with human data. |
| **Goodwin & Darley (2008)**, *Cognition* 106(3):1339–1366, DOI 10.1016/j.cognition.2007.06.007 | Three experiments: "individuals tend to regard ethical statements as clearly more objective than social conventions and tastes, and almost as objective as scientific facts"; religious grounding predicted objectivism.\[24\] | Objectivity paradigm to control proposition type. |
| **Kunda (1990)**, *Psychological Bulletin* 108(3):480–498 | Accuracy vs. directional goals; directional goals bias reasoning within plausible-justification limits. | VD belief is an extreme case where the directional goal is *open*. |
| **Kahan, Peters, Dawson & Slovic (2017)**, *Behavioural Public Policy* 1(1):54–86, DOI 10.1017/bpp.2016.2 | N = 1,111 US adults. Covariance inference from a 2×2 table framed as skin cream vs. concealed-carry ban; responses "became politically polarized – and even less accurate" under the gun frame, and polarization *increased* with numeracy.\[25\] | Reused by Dash et al. (2025) for LLM personas; ready-made evidence-update task.\[26\] |
| **Pennycook & Rand (2019)**, *Cognition* 188; **Tappin, Pennycook & Rand (2020)**, *Curr. Opin. Behav. Sci.*; **Druckman & McGrath (2019)**, *Nature Climate Change* 9 | Whether "motivated" patterns reflect directional motivation or Bayesian updating from different priors and source trust. | **Caution:** a belief can look value-driven yet be Bayesian; fix priors and evidence explicitly in context. |
| **Scales:** AOT-E (Pennycook et al. 2020, *JDM* 15(4)); Moralized Rationality (Ståhl, Zaal & Skitka 2016, *PLoS ONE*) | Individual differences in evidence norms and moralized rationality. | Rater covariates; Dash et al. administered AOT to personas.\[27\] |

**Consensus and debate.** Folk psychology distinguishes epistemic from non-epistemic belief (Vesga et al.; Heiphetz et al.; Van Leeuwen et al.; Buckwalter et al.), and people often *endorse* non-epistemic belief (Cusimano & Lombrozo; Armor et al.). Disputed: whether these are distinct *mental states* or folk categories (Van Leeuwen vs. Levy; Vesga et al. agnostic), and whether apparent motivated reasoning is directional (Kahan vs. Tappin/Pennycook/Rand/Druckman).

### 3.2 Political science and computational social science

- **Expressive responding.** Bullock, Gerber, Hill & Huber (2015, *QJPS* 10(4)) and Prior, Sood & Khanna (2015, *QJPS* 10(4)): paying for correct answers shrinks partisan gaps, so part of stated "belief" is expressive. Schaffner & Luks (2018, *POQ* 82(1)) and Berinsky (2018, *Journal of Politics* 80(1)) find it limited but real. **Relevance:** *professed* belief without credence looks like VD on the surface; incentive-compatible elicitation is a design idea for first-person data.
- **Pew Research Center (2018), "Distinguishing Between Factual and Opinion Statements in the News"** (Mitchell, Gottfried, Barthel & Sumida). N = 5,035 US adults classified five factual and five opinion statements; a majority got at least three of five right in each set, "only a little better than random guesses", and partisans called statements factual more often when they favored their side.\[28\] **Relevance:** human baseline for *proposition type*, not *basis of belief*.
- **Lasser, Aroyehun, Carrella, Simchon, Garcia & Lewandowsky (2023)**, *Nature Human Behaviour* 7(12):2140–2151, DOI 10.1038/s41562-023-01691-w. Separates "belief-speaking" (sincerity to one's beliefs and feelings) from "fact-speaking" (accuracy to evidence) using dictionaries and embeddings on congressional tweets (2011–2022).\[29\]
- **Aroyehun, Simchon, Carrella, Lasser, Lewandowsky & Garcia (2025)**, *Nature Human Behaviour* 9(6):1122–1133, DOI 10.1038/s41562-025-02136-2. The paper analyzes "8 million congressional speech transcripts between 1879 and 2022" (145 years of floor speeches): evidence-based language has declined since the mid-1970s, with legislative productivity, alongside rising polarization and income inequality. It introduces the **Evidence-Minus-Intuition (EMI)** score, built from 49 evidence-based and 35 intuition-based keywords. The **592 human-annotated segments** rated on separate Likert scales for evidence- and intuition-based language come from the 2025 paper itself and are reused for EMI validation in follow-ups (Aroyehun, Lewandowsky & Garcia 2026, arXiv 2604.19699; arXiv 2609.11865; arXiv 2608.05075). **Relevance:** EMI is a *rhetorical-style* measure, not belief basis — useful as a **lexical-shortcut baseline** that a good benchmark should defeat. Public release of dictionaries and annotations could not be confirmed; check data-availability statements and OSF.

### 3.3 NLP and argument mining

| Resource/work | What it annotates | Relevance |
|---|---|---|
| **CDCP** (Park & Cardie 2018, LREC; ACL L18-1257) | 731 comments on the CFPB debt-collection rule; 4,931 units; 1,221 support relations.\[30\] FACT, TESTIMONY, VALUE (≈45%), POLICY (≈17%), REFERENCE; REASON vs. EVIDENCE. HF `DFKI-SLT/cdcp`.\[31\]\[32\] | REASON vs. EVIDENCE is the closest existing "justification type" label — but on *propositions*, not believers' attitudes. |
| **Hidey, Musi, Hwang, Muresan & McKeown (2017)**, ArgMining@EMNLP, ACL W17-5102 | 78 CMV threads (39 with Δ, 39 without). Premises: ethos/logos/pathos; claims: interpretation / evaluation-rational / evaluation-emotional / agreement / disagreement. α > 0.63 for claims, premises, premise types; 0.46 for claim types. GitHub `chridey/change-my-view-modes`.\[33\] | Justification *mode* on natural persuasion; low α warns of annotation difficulty. |
| **IBM Debater evidence types** (Rinott et al. 2015, EMNLP) | Study / Expert / Anecdotal evidence for claims. | Evidence-side taxonomy. |
| **Webis-Editorials-16** (Al-Khatib et al. 2016, COLING) | 300 editorials; units typed anecdote, statistics, testimony, common ground, assumption. | Evidence/assumption typing. |
| **Touché23-ValueEval / SemEval-2023 Task 4** (Kiesel et al. 2023, DOI 10.18653/v1/2023.semeval-1.313; Zenodo 10.5281/zenodo.6814563, CC BY 4.0; builds on Kiesel et al. 2022, ACL) | 9,324 arguments from 6 sources (main 8,865); premise + conclusion + stance; 3 crowdworkers each; 54 values → 20 Schwartz-based categories; 39 teams.\[34\] | Labels *which* value an argument invokes, not whether a belief is value-*based*. Useful for VD sub-types and topic sampling. |
| **Subjectivity:** MPQA (Wiebe, Wilson & Cardie 2005); **CLEF CheckThat! Task 1** 2023–2025 | CheckThat! 2025: >14k news sentences in 9 languages (Arabic 4,697; Bulgarian 1,247; English 2,076; German 1,862; Italian 3,041; Greek 284; Polish 315; Romanian 206; Ukrainian 297), SUBJ/OBJ; Zenodo 18524864.\[35\] | Surface property; good shortcut control. |
| **Committed belief/factuality:** LDC Committed Belief (Diab et al. 2009); FactBank (Saurí & Pustejovsky 2009); CommitmentBank (de Marneffe, Simons & Tonhauser 2019, Sinn und Bedeutung 23); TAC KBP BeSt | Speaker commitment levels; event factuality; CommitmentBank is "a corpus of 1,200 naturally occurring discourses whose final sentence contains a clause-embedding predicate under an entailment canceling operator", covering 48 clause-embedding predicates (including "believe", "think"). | Closest NLP notion of *credence*; CommitmentBank-style graded rating fits Q1. LDC resources are paid. |
| **Value-based argumentation** (Bench-Capon 2003, *J. Logic and Computation* 13(3)) | Arguments succeed relative to audience value orderings. | Formal model of rational value-driven acceptance. |

**Takeaway.** NLP has rich taxonomies for *proposition type*, *support type* and *speaker commitment*, but almost nothing on the *doxastic basis* of an attributed belief.

### 3.4 LLM-specific work

**Belief, knowledge and fact.** **Suzgun, Gur, Bianchi, Ho, Icard, Jurafsky & Zou (2025)**, "Language models cannot reliably distinguish belief from knowledge and fact", *Nature Machine Intelligence* 7(11):1780–1790, DOI 10.1038/s42256-025-01113-8 (arXiv 2410.21195). KaBLE: 13,000 questions, 13 tasks (GitHub; HF `turingmachine/kable`); 24 LMs.\[1\]\[36\]\[37\] "All models tested systematically fail to acknowledge first-person false beliefs, with GPT-4o dropping from 98.2% to 64.4% accuracy and DeepSeek R1 plummeting from over 90% to 14.4%"; third-person false beliefs fare better (95% vs. 62.6% for newer models).\[1\]\[38\] **Relevance:** strongest evidence that *world truth* leaks into *belief attribution*; the repo's Q1 result is a related leak from *stated acceptance* into *attributed credence*. KaBLE is the natural baseline. **Mechanisms (2026):** arXiv 2607.11945, "Belief-reality separation lives in routing over a shared value slot in language models", intervenes on Qwen2.5 (3B–32B), Mistral-7B and OLMo-2-7B with asserted vs. derived belief and belief-vs-reality queries\[39\] — directly usable for the repo's levels 2–3 (preprint).

**Motivated reasoning and identity-congruent reasoning.** **Dash, Reymond, Spiro & Caliskan (2025/2026)**, arXiv 2506.20020: 8 personas across 4 political and socio-demographic attributes; "Political personas specifically are up to 90% more likely to correctly evaluate scientific evidence on gun control when the ground truth is congruent with their induced political identity", and prompt-based debiasing is largely ineffective.\[26\]\[40\] **Relevance:** LLMs can *enact* value-driven reasoning; the repo asks whether they *recognize* it in others. Related 2026 preprints: "Replicating Human Motivated Reasoning Studies with LLMs" (arXiv 2601.16130), "Can LLMs Emulate Human Belief Dynamics?" (arXiv 2605.18781), "Do LLMs have core beliefs?" (arXiv 2605.03255),\[41\] "Accommodation and Epistemic Vigilance" (arXiv 2601.04435).\[42\] Also: **content effects** (Dasgupta et al. 2022, arXiv 2207.07051; *PNAS Nexus* 2024), **unfaithful CoT** (Turpin et al. 2023, NeurIPS, arXiv 2305.04388), **sycophancy** (Sharma et al. 2024, ICLR, arXiv 2310.13548).\[41\] Sycophancy toward the VD believer could inflate attributed credence, so include user-stance controls.

**Debatable vs. factual questions and pluralism.** DebateQA (Xu et al. 2024, arXiv 2408.01419), DELPHI (Sun et al. 2023, EMNLP Findings), ConflictingQA (Wan, Wallace & Klein 2024, ACL, arXiv 2402.11782: models weight relevance over stylistic features), Sorensen et al. (2024, ICML, arXiv 2402.05070; Overton pluralism). These address the proposition-type axis, not the attitude axis.

**Moral and opinion benchmarks.** MoralChoice (Scherrer et al. 2023, NeurIPS), ETHICS (Hendrycks et al. 2021, ICLR), Social Chemistry 101 (Forbes et al. 2020, EMNLP), ValuePrism (Sorensen et al. 2024, AAAI), OpinionQA (Santurkar et al. 2023, ICML), GlobalOpinionQA (Durmus et al. 2023), WorldValuesBench (Zhao et al. 2024, LREC-COLING), PRISM (Kirk et al. 2024, NeurIPS D&B). Sources of value-laden propositions and human value distributions; none labels belief basis.

**Persuasion and belief change.** **Costello, Pennycook & Rand (2024)**, *Science* 385(6714):eadq1814, DOI 10.1126/science.adq1814: 2,190 conspiracy believers had three-round dialogues with GPT-4 Turbo; per the structured abstract, "The treatment reduced participants' belief in their chosen conspiracy theory by 20% on average" (16.8 points more than the control condition, per the authors' manuscript), and the effect lasted at least 2 months (Dryad 10.5061/dryad.v6wwpzh4h). **Caution:** *Science* issued an Editorial Expression of Concern on 11 June 2026 (DOI 10.1126/science.aej2383) over inconsistent screening and "extraneous spliced rows caused by a code-merging error"; the authors report corrected results match in direction and significance.\[43\] Treat effect sizes as provisional. **Relevance:** evidence dialogues moving identity-laden beliefs complicates "value-driven beliefs are evidence-immune"; participants' own conspiracy descriptions could seed first-person items.\[44\] DeliberationBench (arXiv 2603.10018; 4,088 US participants, 65 policy proposals) offers a normative standard for LLM influence.\[45\]

**Do LLMs have beliefs?** Herrmann & Levinstein ("Standards for belief representations in LLMs", *Minds and Machines*, arXiv 2405.21030); Marks & Tegmark ("The Geometry of Truth", COLM 2024, arXiv 2310.06824); Burns et al. (CCS, ICLR 2023, arXiv 2212.03827); Kassner et al. (BeliefBank, EMNLP 2021, arXiv 2109.14723);\[46\] Keeling & Street (arXiv 2407.08388).\[47\] **Relevance:** level 2 needs a probe for a *character's attributed credence*, not the model's own truth judgment; Zhu et al. ("Language models represent beliefs of self and others", ICML 2024, arXiv 2402.18496) is the starting point.\[41\]

**Theory of mind.** ToMi, BigToM, FANToM test false-belief tracking about world states, not attitude type. LaBToM (Ying et al., TACL 2025, arXiv 2408.12022) models graded epistemic language; its graded-plausibility format fits Q1.\[48\]\[49\]

### 3.5 Gap check (2023–2026)

Searching arXiv, the ACL Anthology, COLM, CogSci and PsyArXiv-indexed venues, I found **no paper or benchmark testing LLMs on distinguishing evidence-based from value-driven attitudes toward the same proposition**, including the repo's case of practically motivated belief with low credence. The nearest LLM work (a) tests belief vs. knowledge vs. fact (KaBLE), (b) induces motivated reasoning *in* the model (Dash et al.), (c) classifies *propositions or sentences* (CheckThat!, CDCP, DebateQA), or (d) studies internal belief/reality routing (arXiv 2607.11945). Vesga et al. (2025) has not, as far as I found, been ported to LLMs. **The precise gap:** contrast-controlled evaluation of *attitude-type attribution*, with dissociated credence and acceptance, scored against human distributions. A final check of CogSci 2026 proceedings and PsyArXiv is advisable before submission.

---

## 4. Existing datasets and benchmarks

**Plain statement: no dataset directly matches the project.** Everything below is repurposable or tangential.

| Name | Link | Size | Unit | Labels (source) | Lang. | Access | Fit | Limitations |
|---|---|---|---|---|---|---|---|---|
| Vesga, Van Leeuwen & Lombrozo 2025 | DOI 10.1037/xge0001765 | N = 1,843, 3 studies | Vignette | Epistemic vs. non-epistemic role; think/believe; predicted evidence-responsiveness, behavior (manipulation + ratings) | EN | Paywalled; OSF materials likely (verify) | **Closest (near-direct)** | Certainty held constant; few items; contamination |
| Heiphetz et al. 2021; Van Leeuwen et al. 2021 | DOI 10.1037/rel0000238; 10.1162/opmi_a_00044 | Corpus + experiments; 5 countries | Sentence completion | Verb choice by context (participants) | EN + 4 | Open Mind OA | Repurposable (lexical probe) | Religious vs. matter-of-fact only |
| Cusimano & Lombrozo 2021/2023 | DOI 10.1016/j.cognition.2020.104513; …2023.105379 | 3 studies each | Vignette | Evidence vs. moral belief prescriptions; thresholds (ratings) | EN | Paywalled; check OSF | Repurposable (moral VD) | Moral, not prudential stakes |
| Armor et al. 2008; Miller et al. 2021 | DOI 10.1111/j.1467-9280.2008.02089.x; 10.1177/09567976211004545; osf.io/qlzap | 4 scenarios; n = 127 | Scenario | Prescribed optimism; likelihoods (ratings) | EN (+NL) | OSF open | **Repurposable, strong fit** | Only 4 scenarios |
| Metz, Liquin & Lombrozo 2023 | DOI 10.1111/cogs.13370 | 707 participants | Own beliefs | Justification types; openness to revision; objectivity (**first-person**) | EN | Check OSF | Repurposable (first-person template) | Domain-level contrast |
| Buckwalter, Rose & Turri 2015 | DOI 10.1111/nous.12048 | ~13 vignette sets | Vignette | Thin vs. thick attributions (ratings) | EN | Wiley supp. | Repurposable | Knowledge-entailment focus |
| Kahan et al. 2017 | DOI 10.1017/bpp.2016.2 | N = 1,111 | 2×2 problem | Correct inference × frame × politics | EN | No public data found | Repurposable (evidence update) | Contamination |
| KaBLE | arXiv 2410.21195; HF `turingmachine/kable` | 13,000 Qs | Templated statement | Belief/knowledge/fact (templated) | EN | Open | Baseline | Belief vs. truth, not belief type |
| CDCP | ACL L18-1257 | 731 comments; 4,931 units | Proposition | Fact/testimony/value/policy; reason/evidence (expert) | EN | Research use | Repurposable | One domain; no attitudes |
| Hidey et al. 2017 | ACL W17-5102 | 78 threads | Claim/premise | ethos/logos/pathos; claim types (trained + MTurk) | EN | GitHub (license unchecked) | Repurposable | Small; α = 0.46 claim types |
| Touché23-ValueEval | Zenodo 10.5281/zenodo.6814563 | 9,324 args | Argument | 20 value categories (3 crowdworkers) | EN | CC BY 4.0 | Tangential | Values invoked, not basis |
| CheckThat! 2025 T1 | Zenodo 18524864 | >14k sentences | Sentence | SUBJ/OBJ (expert) | 9 langs | Open | Shortcut control | Surface subjectivity |
| FactBank / LDC CB / BeSt; CommitmentBank | LDC; SuperGLUE (CB) | FactBank 208 docs; CommitmentBank 1,200 discourses, 48 clause-embedding predicates (de Marneffe et al. 2019) | Event/clause | Factuality; graded commitment | EN (+ZH, ES) | LDC paid; CB open | Repurposable (credence format) | Commitment ≠ attitude type |
| IBM Debater evidence; Webis-Editorials-16 | EMNLP 2015; COLING 2016 | Webis: 300 editorials | Evidence unit | Evidence types (expert) | EN | Open/research | Tangential | Evidence side only |
| Aroyehun et al. 2025 EMI | DOI 10.1038/s41562-025-02136-2 | 8M speech transcripts (1879–2022); 592 rated segments | Speech/segment | Evidence vs. intuition language | EN (later DE) | Release unverified | Lexical baseline | Style, not basis |
| Pew 2018 | pewresearch.org | N = 5,035; 12 statements | Statement | Factual/opinion/borderline | EN | Free report | Tangential | Proposition type only |
| Costello et al. 2024 | Dryad 10.5061/dryad.v6wwpzh4h | 2,190 participants | Belief + dialogue | Pre/post belief (first-person) | EN | Open (PII-filtered); **EoC** | Repurposable (seeds) | Data errors flagged 2026 |
| Opinion/moral benchmarks (§3.4) | various | 1k–350k | Question/situation | Opinions, moral judgments, values | Mostly EN | Mostly open | Tangential (topic pools) | No basis labels; contamination |

**Contamination.** Published human stimulus sets (Armor, Kahan, Cusimano, Heiphetz, Van Leeuwen) are widely discussed online and probably in pretraining data. Use *adapted* items (new surface forms of the same design) and keep originals only as a "known-item" diagnostic.

---

## 5. Gap analysis

1. **Construct gap.** No resource labels *attitude type* with the proposition fixed; existing labels describe propositions, sentences, rhetorical style (EMI) or values invoked (ValueEval).
2. **Dissociation gap.** No resource dissociates *acceptance* from *credence*, exactly where the pilot shows models fail. Vesga et al. held certainty constant, so the repo can supply the missing human data point.
3. **Ground-truth gap.** Third-party labels for "why someone believes X" are inference. Only first-person designs (Metz et al.; Cusimano & Lombrozo 2023) get labels from belief holders, and none exists at NLP scale.
4. **Shortcut gap.** "Believe" vs. "think", "chooses to", and emotional vocabulary are strong cues (Heiphetz et al. 2021). Without adversarial contrast sets, a benchmark measures lexical association.
5. **Normative ambiguity.** Humans endorse some VD beliefs, so "reasonable?" must be scored against human *distributions*, not gold labels.
6. **What the project fills.** The first contrast-controlled, human-baselined benchmark of attitude-type attribution in LMs, with a behavior → representation → causal pipeline connecting to mechanistic work (arXiv 2607.11945; Geometry of Truth).

---

## 6. Building a benchmark: "TwoBelieve"

### 6.1 Task definition

Each item has a **scenario** and a **target belief sentence** identical across conditions ("X believes that P"):

- **TS**: evidence supports P; X believes P because of it.
- **IR**: evidence against P; X believes P; no reason.
- **VD**: evidence against P (X knows the odds); a practical/value reason is given. Sub-types: prudential/self-fulfilling, moral (Cusimano-style), relational/loyalty, identity/signaling (Vesga-style), religious/sacred.
- **VD-explicit-credence**: VD plus X's stated probability — a positive control for Q1.
- **Lexical controls** (extending VDn/IRf): TS with value-sounding vocabulary; VD with scientific-sounding vocabulary ("studies show optimism improves recovery" — evidence about the *benefits of believing*, not about P; the most diagnostic adversarial case); verb swaps ("thinks" / "is convinced" / "believes in").

**Probes** (≥3 paraphrase templates each, balanced polarity, plus graded 0–100 formats): (1) attributed credence; (2) evidence-responsiveness to *new* counter-evidence; (3) action prediction across practical settings (bet money, update a will, sign consent); (4) reasonableness, scored only against human distributions; (5) verb choice (thinks/believes); (6) explicit classification (evidence vs. benefits of holding it).

### 6.2 Construction strategies

| Strategy | How | Pros | Cons | Cost/effort |
|---|---|---|---|---|
| **1. Mining natural belief statements** (CMV, forums, Congressional Record, Reddit, survey open-ends) + expert/crowd annotation | Retrieve "I believe / I choose to believe" sentences with context; annotate basis, evidence sensitivity, proposition type | Ecological validity | Labels are inference; low agreement (cf. Hidey α = 0.46); contamination; privacy | ~$3–6k for 3k items; 2–3 months |
| **2. First-person ground truth (Prolific)** | Participants state beliefs in seeded domains; report credence (0–100), reasons (Metz et al. checklist), what would change their mind, and whether they hold it *because it is good to*; optional incentive-compatible credence (Bullock et al.; Prior et al.) | Labels from belief holders; directly tests the dissociation; novel | Self-report and desirability bias; IRB | ~600 × 15 min ≈ $2.5–3.5k; 1–2 months |
| **3. Factorial minimal pairs** | Templates × domains × conditions; LLM drafts, humans edit; adversarial variants; human validation and probe ratings | Clean contrasts; scalable; shortcut-controlled; extends the pilot | Artificiality; LLM style artifacts | 600 items × 5 conditions; ~$2–4k; 1–2 months |
| **4. Adapting psychology paradigms** | Port Vesga vignettes, Armor/Miller scenarios, Cusimano dilemmas, Kahan tasks, Goodwin & Darley items, Heiphetz completions as novel surface variants | Published human baselines; theory-anchored | Small pools; contamination; ask authors for materials | ~$1–2k; 2–4 weeks |

**Recommendation.** Core = Strategies 3 + 4 (where the pilot already sits); Strategy 2 as the flagship first-person track; Strategy 1 as a small out-of-distribution test set.

### 6.3 Annotation guidelines and agreement

- Decision rules: (1) is credence stated or inferable? (2) is the reason *about P's truth* or *about the value of believing P*? (3) would the reason survive learning P is false? Edge cases: "believing the evidence that optimism helps" is VD about P; testimony counts as E unless loyalty is the basis; hope without belief is excluded; "believe in" is labeled separately.
- Targets: manipulation checks ≥85% intended reading; categorical labels on natural text Krippendorff's α ≥ 0.67 (≥ 0.80 high), expecting ~0.5–0.6 and reporting it honestly; graded credence ICC(2,k) ≥ 0.75.

### 6.4 Handling inherent disagreement

Keep **full rating distributions** as soft labels (≥20 raters per item for normative probes, ≥10 for manipulation checks). Follow perspectivist / human-label-variation practice: keep rater metadata (politics, religiosity, AOT-E, Moralized Rationality) to evaluate against subgroup distributions. Treat reasonableness as opinion-distribution matching (like OpinionQA), not accuracy.

### 6.5 Task formats

Graded probes (token probability or verbalized value); balanced binary/multiple-choice; **pairwise** ("In which scenario is X more confident that P?", robust to calibration); **evidence-update** (compare TS vs. VD update magnitudes); **generation** ("What would change X's mind?", rubric-judged); level 2–3 hooks (identical prompts allow residual-stream probing and activation patching between TS and VD contexts).

### 6.6 Metrics

- **Primary contrasts:** ΔCredence(VD−IR) ≤ 0 if acceptance and credence are separated; ΔResponsiveness(TS−VD); ΔAction. Paired effects with bootstrap CIs and Wilcoxon tests (as in `analyze.py`), plus mixed-effects models with item and template random effects.
- **Human alignment:** Jensen–Shannon or Wasserstein distance to human rating distributions; correlation of model vs. human condition effects.
- **Classification:** macro-F1; calibration (ECE, Brier).
- **Robustness:** variance across templates; verb-swap consistency; invariance to topic and political valence; accuracy on adversarial contrast sets.
- **Shortcut baselines:** bag-of-words, EMI-style dictionary, CheckThat!-trained subjectivity classifier — valid items keep these near chance.

### 6.7 Shortcut and contamination controls

Minimal pairs differing by one length-matched clause; randomized stake-sentence position; vocabulary fully crossed with condition; contrast sets (Gardner et al. 2020 style); private test split with canary strings; regenerated surface forms per version; original-vs-adapted comparisons to detect memorization.

### 6.8 Topic and political balance

≥6 domains: health, sports/performance, relationships/loyalty, law/guilt, religion, politics/identity, contentious science, finance/entrepreneurship. Balance left- and right-coded propositions and pro- and anti-consensus stances (Metz et al. show counter-consensus science beliefs have religion-like profiles, so cross stance with condition).\[19\] Include non-US and non-Christian contexts (following Van Leeuwen et al. 2021).

### 6.9 Ethics and IRB

IRB or exempt review, informed consent, fair pay (~$12/h). The first-person track collects sensitive beliefs: no identifiers, skippable items, PII screening before release (as in the Costello et al. Dryad release).\[50\] Avoid asking about participants' own serious illness. Frame release around evaluation (misuse risk: persuasion training). Disclose LLM-assisted item drafting.

### 6.10 Phased plan

| Phase | Content | Size | Timing |
|---|---|---|---|
| 0 — Fix pilot | Balanced polarity, 3 templates/probe, graded credence, VD-explicit-credence and adversarial controls; 4–6 open models + 2 API models | 24 → 60 items × 7 conditions | 2–3 weeks |
| 1 — Human baseline pilot | Prolific, Latin-square lists (`build_form.py`); adapt 4 Armor scenarios and 6–10 Vesga/Cusimano vignettes | ~120 raters; ~20 ratings per item-condition | 3–4 weeks |
| 2 — Core v1 | Validated factorial items with soft labels | ~600 items (~3,500 variants); ~1,000 raters | 2–3 months |
| 3 — First-person track | Self-reported beliefs, credences, reasons, mind-change conditions | ~600 participants → ~3,000 records | parallel, 2 months |
| 4 — OOD track + release | ~1,000 annotated natural statements; public train/dev, private test; level-2 probing | v1.0 | +2 months |

### 6.11 Datasheet outline

1. **Motivation:** construct, gap, funders. 2. **Composition:** tracks, conditions, domains, counts, label fields (condition, basis sub-type, proposition type, rating distributions, rater aggregates). 3. **Collection:** templates, LLM-drafting disclosure, human editing, sampling frame, pay, dates. 4. **Preprocessing:** PII filtering, exclusions, attention checks. 5. **Uses:** evaluation and probing; not persuasion training or profiling. 6. **Distribution:** CC BY 4.0 items (ratings CC BY-NC if IRB requires), canary string, private test. 7. **Maintenance:** versioning, regeneration, error reporting. 8. **Limitations:** US/English skew, normative ambiguity, residual lexical cues, self-report limits.

---

## 7. Recommended next steps

1. **Collect the human baseline before scaling models.** If humans also give VD > IR on credence, the models are human-like and the paper's claim changes.
2. **Re-weight the claims.** Present Q1 and a new action-across-settings probe as diagnostic; treat Q2 and Q3 as human-alignment measures with predictions from Cusimano & Lombrozo, Armor et al. and Vesga et al.
3. **Add three controls now:** VD with explicit low credence, VD with scientific-sounding reasons, TS with emotional wording — plus balanced polarity and ≥3 templates per probe.
4. **Email authors for materials:** Vesga/Van Leeuwen/Lombrozo, Cusimano, Miller/Windschitl, Aroyehun/Garcia (EMI dictionaries, 592 annotations).
5. **Use KaBLE and Dash et al. as reference points:** test whether the credence leak correlates with KaBLE first-person false-belief failure.
6. **Plan level 2 around arXiv 2607.11945 methods:** probe and patch attributed credence between TS and VD contexts on Qwen2.5 base and instruct models.
7. **Merge `note.md`:** reconcile this review with the repo's own literature, novelty and §9 limitations sections.

---

## Caveats

- **Repo coverage:** only the README and file list were readable; the Vietnamese notes, planning files, `problem1/` and pilot code were not inspected, so repo-internal definitions or citations may differ.
- **Verification status:** key papers were checked against publisher, PubMed, arXiv or ACL pages (Vesga et al. 2025, Metz et al. 2023, Cusimano & Lombrozo 2021/2023, Van Leeuwen & Lombrozo 2023, Heiphetz et al. 2021, Van Leeuwen et al. 2021, Buckwalter et al. 2015, Armor et al. 2008, Suzgun et al. 2025, Dash et al. 2025, Aroyehun et al. 2025, Lasser et al. 2023, CDCP, Hidey et al. 2017, Touché23-ValueEval, CheckThat! 2025, Kahan et al. 2017, Pew 2018, Goodwin & Darley 2008, Costello et al. 2024). Classic references and the LLM benchmark papers listed in §3.4 without fresh lookups (e.g., Kunda, Sperber, Pennycook & Rand, expressive-responding papers, Rinott, MPQA, FactBank, CommitmentBank, Bench-Capon, Williams, DebateQA, MoralChoice, OpinionQA, Turpin, Sharma, Herrmann & Levinstein, Marks & Tegmark) are given from standard bibliographic knowledge and should be double-checked before submission.
- **2026 preprints** (arXiv 2607.11945, 2601.16130, 2605.18781, 2605.03255, 2601.04435, 2603.10018, 2609.11865, 2608.05075) are mostly not peer-reviewed.
- **Costello et al. 2024** is under an Editorial Expression of Concern (June 2026); numbers are provisional.
- **Cost and size estimates** in §6 are planning approximations.

## Sources

1. [Language models cannot reliably distinguish belief from knowledge and fact](https://www.nature.com/articles/s42256-025-01113-8)
2. [GitHub - Phannhatminh/belief-truth-vs-value: Do language models tell truth-seeking belief from value-driven belief when only context decides? Notes and a behavioral pilot. · GitHub](https://github.com/Phannhatminh/belief-truth-vs-value)
3. [Corey Cusimano & Tania Lombrozo, Morality justifies motivated reasoning in the folk ethics of belief - PhilPapers](https://philpapers.org/rec/CUSMJM)
4. [Alejandro Vesga, Neil Van Leeuwen & Tania Lombrozo, Evidence for multiple kinds of belief in theory of mind - PhilArchive](https://philarchive.org/rec/VESEFM)
5. ["Prescribed Optimism: Is it Right to be Wrong About the Future?" by David A. Armor, Cade Massey et al.](https://ir.stthomas.edu/ocbmktgpub/27/)
6. [Mirac Suzgun - Belief in the Machine](https://sites.google.com/view/msuzgun/research/belief-in-the-machine)
7. [Commentary: Religious credence is not factual belief](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5061739/)
8. [Neil Van Leeuwen, \_Religion as Make-Believe: a theory of belief, imagination, and group identity\_ - PhilPapers](https://philpapers.org/rec/VANRAM-8)
9. [Précis of Religion as Make-Believe: A Theory of Belief, Imagination, and Group Identity](https://link.springer.com/article/10.1007/s11406-025-00923-9)
10. [There is more to belief than Van Leeuwen believes - Levy - 2024 - Mind & Language - Wiley Online Library](https://doi.org/10.1111/mila.12501?urlappend=%3Futm_source%3Dresearchgate.net)
11. [Neil Van Leeuwen & Tania Lombrozo, The Puzzle of Belief - PhilArchive](https://philarchive.org/rec/VANTPO-137)
12. [Belief through Thick and Thin - Buckwalter - 2015 - Noûs - Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/nous.12048)
13. [Against Beliefless Knowledge](https://www.cambridge.org/core/journals/episteme/article/against-beliefless-knowledge/4B7A578C11A1DE995782715A527E286C)
14. [The many meanings of belief](https://link.springer.com/article/10.1007/s11229-025-05316-9)
15. [Does Think Mean the Same Thing as Believe? Linguistic Insights Into Religious Cognition](https://www.ovid.com/journals/pors/abstract/10.1037/rel0000238~does-think-mean-the-same-thing-as-believe-linguistic)
16. [(PDF) Does Think Mean the Same Thing as Believe? Linguistic Insights Into Religious Cognition](https://www.researchgate.net/publication/328150207_Does_Think_Mean_the_Same_Thing_as_Believe_Linguistic_Insights_Into_Religious_Cognition)
17. [(PDF) To Believe is Not to Think: A Cross-Cultural Finding](https://academia.edu/50341651/To_Believe_is_Not_to_Think_A_Cross_Cultural_Finding_forthcoming_)
18. [cognition.princeton.edu](https://cognition.princeton.edu/document/671)
19. [S. Emlen Metz, Emily G. Liquin & Tania Lombrozo, Distinct Profiles for Beliefs About Religion Versus Science - PhilPapers](https://philpapers.org/rec/METDPF)
20. [Distinct Profiles for Beliefs About Religion Versus Science - Metz - 2023 - Cognitive Science - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1111/cogs.13370)
21. [Distinct Profiles for Beliefs About Religion Versus Science - PubMed](https://pubmed.ncbi.nlm.nih.gov/37971275)
22. [(PDF) THE MORALITY OF BELIEF I: HOW BELIEFS WRONG](https://www.researchgate.net/publication/371507521_THE_MORALITY_OF_BELIEF_I_HOW_BELIEFS_WRONG)
23. [OSF](https://osf.io/qlzap/wiki/home/)
24. <https://leeds-faculty.colorado.edu/mcgrawp/pdf/Goodwin.Darley.2008.Objectivity.pdf>
25. <https://rcgd.isr.umich.edu/wp-content/uploads/2018/07/motivated_numeracy_and_enlightened_selfgovernment.pdf>
26. [\[2506.20020\] Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning](https://arxiv.org/abs/2506.20020)
27. [\[2506.20020\] Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning](https://ar5iv.labs.arxiv.org/html/2506.20020)
28. [Distinguishing Between Factual and Opinion Statements in the News](https://www.pewresearch.org/journalism/2018/06/18/distinguishing-between-factual-and-opinion-statements-in-the-news/)
29. [Use Of Facts And Evidence-Based Rhetoric At All-Time Low In Congressional Speech](https://www.iflscience.com/use-of-facts-and-evidence-based-rhetoric-at-all-time-low-in-congressional-speech-78785)
30. [LREC 2018 Proceedings](http://www.lrec-conf.org/proceedings/lrec2018/summaries/679.html)
31. [DFKI-SLT/cdcp · Datasets at Hugging Face](https://huggingface.co/datasets/DFKI-SLT/cdcp)
32. [Multi-Task Attentive Residual Networks for Argument Mining](https://arxiv.org/pdf/2102.12227)
33. <http://www.cs.columbia.edu/nlp/papers/2017/hidey_semantic_arguments.pdf>
34. <https://aclanthology.org/2023.semeval-1.313.pdf>
35. [Overview of the CLEF-2025 CheckThat! Lab Task 1 on Subjectivity in News Articles](https://zenodo.org/records/18524864)
36. [GitHub - suzgunmirac/belief-in-the-machine: Belief in the Machine: Investigating Epistemological Blind Spots of Language Models · GitHub](https://github.com/suzgunmirac/belief-in-the-machine)
37. [Belief in the Machine: InvestigatingEpistemological Blind Spots of Language Models](https://arxiv.org/html/2410.21195)
38. [Language models cannot reliably distinguish belief from knowledge and fact](https://www.researchgate.net/publication/397215922_Language_models_cannot_reliably_distinguish_belief_from_knowledge_and_fact)
39. [Belief-reality separation lives in routing over a shared value slot in language models](https://arxiv.org/pdf/2607.11945)
40. [(PDF) Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning](https://www.researchgate.net/publication/393022707_Persona-Assigned_Large_Language_Models_Exhibit_Human-Like_Motivated_Reasoning)
41. [Do LLMs have core beliefs?](https://arxiv.org/pdf/2605.03255)
42. [Accommodation and Epistemic Vigilance: A Pragmatic Account of](https://arxiv.org/pdf/2601.04435)
43. [Editorial Expression of Concern on 2024 Research Article “Durably reducing conspiracy beliefs through dialogues with AI”](https://www.eurekalert.org/news-releases/1131247)
44. <https://atelierdesfuturs.org/wp-content/uploads/2024/11/CostelloPennycookRand_ConspiracyReductionwithAI.pdf>
45. [Accepted to IASEAI’26 DeliberationBench:](https://arxiv.org/pdf/2603.10018)
46. [Belief Revision: The Adaptability of Large Language Models Reasoning](https://arxiv.org/pdf/2406.19764)
47. [\[2407.08388\] On the attribution of confidence to large language models](https://arxiv.org/abs/2407.08388)
48. [\[2408.12022\] Understanding Epistemic Language with a Language-augmented Bayesian Theory of Mind](https://arxiv.org/abs/2408.12022)
49. [Understanding Epistemic Language with a Language-augmented Bayesian Theory of Mind](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00752/131586/Understanding-Epistemic-Language-with-a-Language)
50. [Dryad | Data: Durably reducing conspiracy beliefs through dialogues with AI](https://datadryad.org/dataset/doi:10.5061/dryad.v6wwpzh4h)
