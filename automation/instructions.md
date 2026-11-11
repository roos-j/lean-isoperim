# Instructions: formalization of [DIR] and [DIRX]

Local instructions for this repository. They supersede conflicting guidance in the
`autoformalize` skill (`.claude/skills/autoformalize/SKILL.md`, `.agents/skills/autoformalize/SKILL.md`).
The user's current explicit instructions take precedence over both. Raw prompts are logged in
`automation/raw.md` (ignored by Git); distilled prompts are below.

## Sources and scope

- **[DIR]** P. Durcik, P. Ivanisvili, J. Roos, *Sharp isoperimetric inequalities on the Hamming cube
  near the critical exponent*, arXiv:2407.12674v2 (revised version, August 2026).
  TeX: `sources/DIR/main-v2.tex`.
- **[DIRX]** P. Durcik, P. Ivanisvili, J. Roos, X. Xie, *Sharp isoperimetric inequalities on the
  Hamming cube II: The critical exponent*, arXiv:2602.20462v1. TeX: `sources/DIRX/main.tex`.
- Companion code (numerical claims): https://github.com/roos-j/dir24-isoperim.
- Scope: **full formalization of both papers**. Current phase: **setup** (repository structure and
  statements only; every claim proved `by sorry`). No proofs are to be attempted in this phase.
- Equation numbers follow the arXiv PDFs (not a naive TeX count): in [DIR] §6 there is no equation
  (6.4) (the counter skips it, an artifact of the `\auto` tag macro); auto-tagged (🚗) equations
  each take one number.

## Layout (user requirement, 2026-11-11)

```
Isoperim.lean                       # imports every module below
Isoperim/DIR/1_Introduction/Thm_1_1.lean, Thm_1_5.lean, Thm_1_6.lean, Thm_1_7.lean, Thm_1_10.lean
Isoperim/DIR/2_Envelope_Functions/2_0_Envelope_Functions.lean, 2_1_Computed_Envelopes.lean,
                                   2_2_Proofs_Theorems_1_1_1_5_1_7.lean
Isoperim/DIR/3_Variants_Bobkov_Inequality/3_0_Variants_Bobkov_Inequality.lean
Isoperim/DIR/4_Computer_Assisted_Proofs/4_1_Dyadic_Partitioning.lean, 4_2_Interval_Arithmetic.lean,
                                        4_3_Source_Code.lean
Isoperim/DIR/5_Auxiliary_Estimates/5_1_Small_Exponents_Large_Exponents.lean,
                                   5_2_Two_Point_Inequalities.lean, 5_3_Properties_L_Q.lean,
                                   5_4_Lower_Bounds_Gaussian_Isoperimetric_Profile.lean
Isoperim/DIR/6_Proof_Two_Point_Inequality/6_1_Case_J.lean ... 6_6_Case_QJ.lean
Isoperim/DIR/7_Proof_Poincare_Inequality/7_0_Proof_Poincare_Inequality.lean
Isoperim/DIRX/1_Introduction/Thm_1_1.lean, Thm_1_2.lean, Thm_1_3.lean
Isoperim/DIRX/2_Preliminaries/2_1_Reduction_Two_Point_Inequality.lean, 2_2_Properties_J.lean,
                              2_3_Properties_L_Q.lean, 2_4_Computer_Assisted_Proofs.lean
Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_1_Case_J.lean ... 3_6_Case_QJ.lean
Isoperim/DIRX/4_Proof_Poincare_Inequality/4_0_Proof_Poincare_Inequality.lean
Isoperim/DIRX/5_Connection_Hellinger_Conjecture/5_0_Connection_Hellinger_Conjecture.lean
```

Rules:
- One folder per paper (`DIR`, `DIRX`), one folder per section `<k>_<Short_Name>`.
- Introduction: one file per theorem-environment theorem (`Thm_1_1.lean`, ...). Corollaries go into
  the file of the theorem they follow from (DIR Corollary 1.9 and §1.4 are in DIR `Thm_1_1.lean`).
  Introductory text preceding a theorem (since the previous theorem's discussion) and the discussion
  following it go into that theorem's file.
- Other sections: one file per subsection `<k>_<m>_<Short_Name>.lean`. Text of a section before its
  first subsection goes into `<k>_0_<Section_Name>.lean` when it contains mathematical content,
  otherwise into a comment at the top of the first subsection file. A section without subsections
  is a single `<k>_0_<Section_Name>.lean`. Subsubsections become Lean `section`s.
- Shortened names: drop articles, prepositions and similar filler words, keep the key words
  (e.g. "Properties of the function J" → `Properties_J`).
- Module paths with leading digits are imported with guillemets:
  `public import Isoperim.DIR.«1_Introduction».Thm_1_1`.
- Imports: each file imports only the earlier files (in paper order) whose declarations it uses.

## Content conventions (user requirement)

- Follow the paper's order exactly; every piece of the paper is represented in its file in order.
- Every definition, lemma, proposition, theorem, corollary (numbered or not, in an environment or
  not, displayed or inline, including claims made inside proofs) becomes a Lean `def`/`theorem`.
  Claims not in an environment are `theorem`s by default. Precise but cited/historical claims are
  also stated (docstring says "cited from ..."). Conjectures are `def ... : Prop` (not claimed).
  Purely heuristic/numerical-evidence statements stay as comments.
- Every declaration has a docstring with the precise mathematical formulation from the paper
  (KaTeX `$...$`) and the location: `[DIR], Lemma 5.4`, `[DIR], (2.9)`, or for unnumbered items
  `[DIR], §6.1.1` / `[DIR], proof of Lemma 6.4`. Computer-verified claims carry the tag `(🚗)`.
- All other text of the paper is kept verbatim (LaTeX) in `/- ... -/` comments at the corresponding
  place; `\ref`s are annotated with the resolved number in brackets, e.g. `\ref{lem:holder} [5.1]`.
- Proof environments: `section Proof_Lemma_2_3 ... end Proof_Lemma_2_3` (also `Proof_Theorem_1_6`,
  `Proof_Proposition_3_3`, `Proof_Fact_4_1`, and for unnamed propositions e.g.
  `Proof_Proposition_6_8`). Sub-proofs such as "Proof of (1)" become nested sections
  (`Proof_Claim_1`).
- Names: numbered items `thm_1_1`, `lemma_5_4`, `prop_2_1`, `cor_2_5`, `rem_2_3`, `fact_4_1`,
  `eqn_2_9`, `conj_1_4`, without paper prefix; the paper is identified by the namespace
  (`Auto.DIR.thm_1_1`, `Auto.DIRX.thm_1_1`). Unnumbered claims: descriptive Mathlib-style
  snake_case names.
  Definitions: names suggestive of the paper's notation (`L`, `Q`, `J`, `b`, `G₁`, `Jw`, `w₀`...);
  [DIRX] definitions whose names would be ambiguous with [DIR] ones (DIRX opens `Auto.DIR`)
  get an `X` suffix in their Lean name (`LX`, `QX`, `JX`, `BX`, `G₁X`, ...) and are displayed via
  `local notation` in each [DIRX] file.
- All [DIR] code in `namespace Auto.DIR`, all [DIRX] code in `namespace Auto.DIRX` (user
  requirement of 2026-11-11T19:12, superseding "only `Auto`"); [DIRX] files `open Auto.DIR` to
  reuse its definitions; no other namespaces. Every file: Mathlib-linter-compliant header
  (copyright Joris Roos, `Authors: Claude`), `module`, `public import`s, module docstring starting
  with `This file was automatically generated by Claude.`, `@[expose] public section`.
- Every statement is proved `by sorry` in this phase.
- Statements must be mathematically faithful, including Lean junk values (restrict to the domain
  where the paper's object is defined, e.g. `x ∈ 𝒬` for `𝓑 β x`, intervals for `J`; use a single
  `sInf` over a set instead of nested `⨅` with `Prop` binders in `ℝ`; `Real.rpow` with `0 ^ 0 = 1`).
- Statements should look like the paper. Notation is introduced conservatively, at first use, and
  listed in the module docstring of the file introducing it. Current notation (DIR §1–§3):
  `{0,1}^n` (cube `Fin n → ZMod 2`, `x + e i` = bit flip), `h_{A}`, `𝐄 f`, `𝟏_{A}`, `|A|`
  (density; `|a|` stays `abs` otherwise), `log₂`, `|∇(A, B)|`, `𝓑 β x`, `𝒬`, `x⁎`, `‖f‖_[p]`,
  `∇f`, `G₁ β B x y`, `G₂`, `G`, `L β x`, `Q β x`, `b β x`, `c₀ • B`, `b̃`, `L̃`, `𝔅 β x`, `Mi`,
  `M`, `φ`, `Φ`, `I`, `Jw w x`, `w₀`, `x₀`, `β₀`, `c₀`; derivatives as `deriv f`,
  `deriv (deriv f)`, `iteratedDeriv k f` (the prime symbol `′` is unavailable: Mathlib uses `′′`).
  Tight lower bounds: `IsTightLowerBound₁ f fl a b`, `IsTightLowerBound₂ f fl a₁ b₁ a₂ b₂`
  (`Isoperim/DIR/4_Computer_Assisted_Proofs/4_1_Dyadic_Partitioning.lean`).

## Build

```
lake exe cache get
lake env lean Isoperim/DIR/1_Introduction/Thm_1_1.lean     # single file
lake env lean -Dweak.linter.mathlibStandardSet=true <file>  # header/style linters
lake build
```

## Git

- Work on branch `claude` (user requirement). Commit message `[claude] repo setup`, authored by
  Joris Roos, with trailer `Co-authored-by: Claude <noreply@anthropic.com>`.

## Distilled user prompts

- **2026-11-11T18:01+00:00** (initial request; raw entry 1 in `automation/raw.md`): create branch
  `claude`; set up the project; copy the newest `autoformalize` skill from sister repositories
  (found: `roos-j/lean-trilinearht` @ cc1999b, 2026-10-16) and update both copies in the spirit of
  the layout/content rules above (abstracted from these papers); scope = full formalization of
  [DIR] and [DIRX], but for now only repository structure and statements (all `sorry`); layout and
  content conventions as recorded above; commit as authored by the user, co-authored by Claude,
  message `[claude] repo setup`; record these instructions; do not stop before finishing.

- **2026-11-11T19:12+00:00** (raw entry 2): refactor to namespaces `Auto.DIR` and `Auto.DIRX`
  and remove the `dir_`/`dirx_` name prefixes.

## Settled decisions

- Proof-section claims reference later results only in comments (setup phase). When proofs are
  added, the import graph may need the proof-section files to import later sections; theorems of
  the introduction are restated/closed in the proof phase as decided then.
- `IsJ`/`J`, `w₀`, `I` are defined by `Classical.choose`/inverse functions with the
  characterizing existence/uniqueness claims stated as separate theorems.

## Current status / next step

Setup phase complete (2026-11-11): all 38 files of the layout exist, every claim is stated and
proved `by sorry`, `lake build` succeeds and the Mathlib style/header linters report only
`sorry` warnings. Faithfulness questions and possible gaps in the papers found while stating the
claims are listed in `automation/ErrorReport.md` (several need a decision before the proof
phase, e.g. the hypothesis `hJ : EqOn J (Jw w₀) ...` in [DIR] §6.6 and the possibly false tight
lower bound for $g_{QJQ,\beta}$ on the full rectangle in [DIR] §6.5).

Next step: proof phase, starting with the elementary results of [DIR] §5 and §3, in forward
logical order; first add fine-grained proof rows to `automation/Status.md`.
