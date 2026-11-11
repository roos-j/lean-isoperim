# Forward-reasoning audit of the [DIR]/[DIRX] scaffold

Date: 2026-11-11. Method: analysis of the papers' arguments only (no Lean proofs exist; every
claim is `sorry`). For every claim we determined the results/claims/definitions used in its proof
in the paper, and compared with the order of the formalization: the 38 files in paper order
(`Isoperim.lean`), and declaration order inside each file. Detailed per-claim tables are in
Parts A–D below (one per audit group); this first part summarizes them and analyses the import
structure.

## 1. Summary of forward instances

A *forward instance* is a claim that appears before (a) a prerequisite later in the same file, or
(b) a prerequisite in a later file.

| Group | Same-file instances | Later-file instances | Main later-file instances |
|---|---|---|---|
| [DIR] §1–§3 (Part A) | 8 | 29 | Thm 1.1, 1.5, 1.7 ← §2.2, Lemmas 5.1, 5.2, 5.9, 5.13, §6; Thm 1.6 ← §3; Thm 1.10 ← §7; Thm 2.2 ← all of §6; §2.1/§2.2 ← Lemmas 5.2, 5.9, 5.13; $J$ (existence) ← (3.4) in §3; $w_0$ ← Cor. 5.12 |
| [DIR] §4, §5, §7 (Part B) | (statement-then-proof only) | 5 | proof of Lemma 5.13 (5.4) uses the enclosure (6.2) of §6.1 |
| [DIR] §6 (Part C) | 30 | 0 | none (§6 only uses §3–§5 and earlier parts of §6) |
| [DIRX] (Part D) | 26 | 12 | Thm 1.1 ← §2.1, (2.4) ← §3.1–§3.6; Thm 1.3 ← §4, (2.5); (1.4) ← §4; Remarks 2.1, 2.2 ← §2.2, §3 |

Same-file instances are almost all of the form "theorem/proposition stated, then its proof
steps" (e.g. `Auto.DIR.prop_6_1` before `caseJ_I`, `caseJ_II`; `Auto.DIR.lemma_6_4`, whose proof is
postponed to the end of §6.2). They are harmless for a Lean development if each proof is placed
after its steps (or the steps are moved before the statement).

Cross-paper: [DIR] Remarks 1.2 and 2.6 (`Auto.DIR.rem_1_2`, `Auto.DIR.rem_2_6`) are the
$\beta=\frac12$ case of [DIRX] Theorem 1.1, which comes after all [DIR] files (and [DIRX] imports
[DIR]). They are citations; if they were to be *proved* from [DIRX], they would create a
cross-paper cycle, so they must stay cited (or be moved to [DIRX]).

Claims asserted without proof in the papers (not forward, but unsupported) are listed in each
part (e.g. [DIR] Remarks 1.8, 2.3, 5.10, 6.3, 7.2, the uniqueness of $J$, Lemma 6.4's second claim,
`I_upper`, Remark 5.14; [DIRX] Remarks 2.1, 2.2 "stronger").

## 2. Import dependency loops

**Statement imports** (what the files import now, to *state* their declarations) form an acyclic
graph; Lean enforces this.

**Proof dependencies.** If every file had to import all files that its claims' proofs use
(Parts A–D list these per file), the file graph would no longer be acyclic. Its strongly connected
components with more than one file are exactly:

1. **[DIR] core cycle (16 files):** `1_Introduction/Thm_1_1`, `Thm_1_5`, `Thm_1_7`,
   `2_0_Envelope_Functions`, `2_2_Proofs_Theorems_1_1_1_5_1_7`, `3_0_Variants_Bobkov_Inequality`,
   `5_1`, `5_2`, `5_3`, `5_4`, `6_1`–`6_6`. Generating loops:
   - `Thm_1_1` (proof of Thm 1.1 needs `2_0`/(2.6), `2_2`, `5_1`, `5_3`) while every one of these
     files imports `Thm_1_1` for the cube, $h_A$, $\mathbf E$, $|A|$, $\beta_0$;
   - `Thm_1_5` (Thm 1.5 ← (2.7), `2_2`) ↔ `2_0`, `2_2` (which import `Thm_1_5` for $\mathcal B_\beta$);
   - `Thm_1_7` (Thm 1.7 ← (2.8), (2.9), Lemma 5.13; existence of $J$ ← $J=J_{w_0}$ in `3_0`) ↔
     `2_0`, `3_0` (which import `Thm_1_7` for the definition of $J$). This loop exists already
     between *two definitions/claims of different files*: `existsUnique_J` (Thm_1_7) needs
     `Jw_spec`, `existsUnique_w₀` (3_0), while `eqn_3_4` (3_0) needs `J`/`existsUnique_J` (Thm_1_7);
   - `2_0` (Thm 2.2 ← all of §6) ↔ `6_1`–`6_6` (which import `2_0` for $G$, $b_\beta$, $L$, $Q$);
   - `3_0` (`w₀_mem`, `existsUnique_w₀`, Remark 3.7 ← Cor. 5.12, asymptotics of $I$ in `5_4`) ↔
     `5_4` (imports `3_0` for $I$, $J_w$, $w_0$).
   - `5_4` → `6_1` (enclosure (6.2) in the proof of Lemma 5.13) is forward but closes no loop
     by itself (`6_1` does not need `5_4`).
2. **[DIR] Poincaré:** `Thm_1_10` ↔ `7_0` (Thm 1.10 is proved in §7; `7_0` imports `Thm_1_10`
   for $\|\cdot\|_p$, $\nabla$).
3. **[DIRX] two-point core (9 files):** `2_1`, `2_2`, `2_3`, `3_1`–`3_6`: (2.4) in `2_1` is proved by
   the six cases of §3, which import `2_1` (and `2_2` via `2_1`) for $G$, $B_w$, $\mathrm J$.
4. **[DIRX] Poincaré:** `Thm_1_3` ↔ `4_0` (Thm 1.3 proved in §4; `4_0` uses the sensitivity facts
   stated in `Thm_1_3`).

Other forward file dependencies close no loop and only require departing from paper order:
`DIR/Thm_1_6` → `3_0`, `DIR/2_1`, `2_2` → `5_2`/`5_3`/`5_4`, `DIRX/Thm_1_1` → `DIRX/2_1`,
`DIRX/Thm_1_2` → `DIRX/Thm_1_1`.

**Outcome.** At the level of *individual claims* the dependency graph extracted from the papers'
arguments is acyclic: no claim is (directly or transitively) used in its own proof, and every loop
above passes through a file that contains both (i) definitions or early claims needed later, and
(ii) a claim whose proof comes later in the paper. So the loops are not *necessary*
mathematically; they are forced only by the paper-structured file layout (definitions, main
theorems and their proofs live in different files, ordered as in the paper). With the current
layout they are unavoidable: for example `DIR/Thm_1_1` must contain the definition of the cube
and Theorem 1.1, the definition is needed by §2–§6, and Theorem 1.1's proof needs §2–§6.

Ways to resolve this in the proof phase (decision needed from the user; none applied):
- (a) Keep the theorem statements in their paper files and prove them in the proof-section files
  under the same statement with a different name (e.g. `Auto.DIR.thm_1_1_proof` in `2_2`), the
  early declaration remaining `sorry` or being removed in favour of a re-export; or
- (b) Move the definitions (and only the definitions) used across files into the earliest file of
  each loop or a dedicated definitions file, so that the introduction files can import the proof
  files; this departs from the strict paper order for definitions (e.g. $J$ from §1.3, $J_w$, $I$
  from §3 together); or
- (c) Split each looping file into a "statements needed later" part and a "claims proved later"
  part (e.g. `Thm_1_1` → definitions/notation + Thm 1.1 statement), keeping paper order within
  each part.


## Part A: [DIR] §1–§3

Global order: `automation/tmp/paper_order.txt` (Thm_1_1 < Thm_1_5 < Thm_1_6 < Thm_1_7 <
Thm_1_10 < 2_0 < 2_1 < 2_2 < 3_0 < 4_x < 5_x < 6_x < 7_0 < DIRX...).
Only *direct* prerequisites of the paper's argument are listed (transitive ones follow from the
per-file dependency lists below). "Cited" = proof is in the literature (external prerequisite,
not a forward reference).

Short file names: `T11` = `Isoperim/DIR/1_Introduction/Thm_1_1.lean`, `T15`, `T16`, `T17`,
`T110` analogously; `2_0`, `2_1`, `2_2` = `Isoperim/DIR/2_Envelope_Functions/…`;
`3_0` = `Isoperim/DIR/3_Variants_Bobkov_Inequality/3_0_Variants_Bobkov_Inequality.lean`;
`5_1` … `5_4`, `6_1` … `6_6`, `7_0` = the corresponding [DIR] files; `X-T11` =
`Isoperim/DIRX/1_Introduction/Thm_1_1.lean`.

### Forward references (claim stated before a prerequisite)

#### Into later files

| Lean name (file) | Paper location | Prerequisite (paper ref, Lean name, file) | Explanation |
|---|---|---|---|
| `thm_1_1` (T11) | Thm 1.1 | Lemma 5.1, `lemma_5_1`, 5_1 | reduction to $\beta=\beta_0$ (§2.2) |
| `thm_1_1` (T11) | Thm 1.1 | (2.6), `cor_2_5`, 2_0; `eqn_1_1_β₀`, `b_eq_Q_ge_L`, 2_2 | proof of Thm 1.1 is in §2.2 |
| `thm_1_1` (T11) | Thm 1.1 | Lemma 5.9, `lemma_5_9`, 5_3 | $Q_{\beta_0}\ge L_{\beta_0}$ on $[\frac14,\frac12]$ |
| `eqn_1_1_mono` (T11) | §1 after Thm 1.1 | Lemma 5.1, `lemma_5_1`, 5_1 | Hölder monotonicity in $\beta$ |
| `rem_1_2` (T11) | Rem 1.2 | [DIRX] Thm 1.1, `Auto.DIRX.thm_1_1`, X-T11 | cited from [DIRX26] (external paper, but later in this repo) |
| `thm_1_5` (T15) | Thm 1.5 | (2.7), `cor_2_5`, 2_0; `b_half_two_pow`, `thm_1_5_lower`, `thm_1_5_upper`, 2_2 | proof in §2.2 |
| `thm_1_6` (T16) | Thm 1.6, (1.4) | Lemma 3.1 `lemma_3_1`, `L_half_eqn_3_2` (cited BIM23 L. 2.2), `L_half_eqn_3_1`, `proof_thm_1_6_chain`, `M_indicator`, 3_0 | proof of (1.4) is in §3 |
| `classical_isoperimetric` (T17) | §1.3 | — | (only (1.3) and `expect_hA_compl`, see below) |
| `existsUnique_J` (T17) | §1.3 "unique smooth function" | (3.4) `eqn_3_4`, `Jw_spec`, `existsUnique_w₀`, `I_characterization`, 3_0 | existence of $J$ is via $J=J_{w_0}$ (§3); uniqueness is not argued in the paper |
| `thm_1_7` (T17) | Thm 1.7 | (2.8) `eqn_2_8`, `isoProfile_ge_btilde`, 2_2; Prop 2.1 `prop_2_1`, 2_0 | proof in §2.2 |
| `thm_1_7` (T17) | Thm 1.7 | (2.9) `eqn_2_9`, 2_2 ← Lemma 5.13 `lemma_5_13`, 5_4 | $J>L_{\beta_0}(1-\cdot)$ |
| `eqn_1_5` (T17) | (1.5) | Thm 1.1 `thm_1_1` (T11, earlier); Thm 1.7 `thm_1_7`, Rem 1.8 `rem_1_8` (same file, later) | see "within a file"; $\beta>\beta_0$, $\lvert A\rvert>\frac12$ is a gap |
| `eqn_1_6_improves` (T17) | §1.3 after Thm 1.7 | Lemma 5.13, `lemma_5_13`, 5_4 | stated "see Lemma 5.13" |
| `rem_1_8` (T17) | Rem 1.8 | analogue of Rem 2.3 `rem_2_3` (2_0) for $\tilde b_\beta$ and of [BIM23, L. 2.3] for $\beta$; proof omitted | "details omitted" |
| `thm_1_10` (T110) | Thm 1.10 | (7.1) `eqn_7_1`, Prop 7.1 `prop_7_1`, 7_0; (2.6), (2.7) `cor_2_5`, 2_0 | proof in §7 (only $p=2\beta_0$ and $p=1$ are covered, see ErrorReport) |
| `poincareConstBool_bounds` (T110) | §1.5 before Thm 1.10 | Thm 1.10 `thm_1_10` (same file, later) | see "within a file" |
| `thm_2_2` (2_0) | Thm 2.2 | Props 6.1, 6.2, 6.6, 6.8, 6.9, 6.11, 6.12 (`prop_6_1` 6_1, `prop_6_2` 6_2, `prop_6_6` 6_3, `prop_6_8` 6_4, `prop_6_9` 6_5, `prop_6_11`, `prop_6_12` 6_6) and the §6 case reduction | proof is §6 (which uses §3 `J_eqn_3_2`/`cor_3_5`, §4, §5) |
| `rem_2_3` (2_0) | Rem 2.3 | §6 methods for general $\beta$ (not carried out) | claim with omitted proof |
| `rem_2_4_failure` (2_0) | Rem 2.4 | Rem 3.6 `rem_3_6`, (3.4) `eqn_3_4`, `w₀_mem`, 3_0 | failure of Bobkov-type inequality for $J$ at $x=\frac12<x_0$ (numerical) |
| `rem_2_6` (2_0) | Rem 2.6 | [DIRX] Thm 1.1, `Auto.DIRX.thm_1_1`, X-T11 | cited from [DIRX26] (later in repo) |
| `cor_2_5` (2_0) | Cor 2.5 | $J\ge0$ on $[\frac12,1]$ (from `eqn_3_4`, 3_0, or `IsJ`) | non-negativity of $b_\beta$ needed in Prop 2.1 (minor) |
| `twopt_max`, `twopt_iSup` (2_1) | §2.1 | Lemma 5.2, `lemma_5_2`, 5_2 | "consequence of monotonicity (see Lemma 5.2)" |
| `envelope_twopt` (2_1) | §2.1 | Lemma 5.2, `lemma_5_2`, 5_2 (via `twopt_iSup`) | sup of a family |
| `b_eq_Q_ge_L` (2_2) | §2.2 | Lemma 5.9, `lemma_5_9`, 5_3 | "proved in §5.3 (see Lemma 5.9)" |
| `eqn_2_8` (2_2) | (2.8) | Lemma 5.2, `lemma_5_2`, 5_2 | max of two Bellman candidates |
| `eqn_2_9` (2_2) | (2.9) | Lemma 5.13, `lemma_5_13`, 5_4 | "Lemma 5.13 shows" |
| `existsUnique_w₀`, `w₀_mem` (3_0) | §3 (3.4) | Cor 5.12 `cor_5_12` (5_4) restates uniqueness; numerical enclosure of $I$ (interval arithmetic §4.2) | "one computes $w_0\in[0.895,0.896]$" |
| `rem_3_7_asymp` (3_0) | Rem 3.7 | $I(x)\sim\sqrt2x\sqrt{\log(1/x)}$, `I_asymp` (5_4; well known) | asymptotic equivalence of the RHS to $J$ |

#### Within a file (claim stated before a prerequisite in the same file)

| Lean name (file) | Paper location | Prerequisite (later in same file) | Explanation |
|---|---|---|---|
| `cor_1_9` (T11) | Cor 1.9 | `cor_1_9_chain` (display after Cor 1.9) | the corollary is derived from the chain stated after it |
| `thm_1_6` (T16), asymptotic part | Thm 1.6 | `isoProfile_half_le_sqrt`, `isoProfile_one_asymp` | upper bound "follows from Cauchy–Schwarz and the characterization of $\mathcal B_1$" (stated after) |
| `classical_isoperimetric` (T17) | §1.3 | `expect_hA_compl` | case $\lvert A\rvert>\frac12$ uses $\mathbf E h_A=\mathbf E h_{A^c}$ (stated after); otherwise from (1.3) `eqn_1_3` (T15) |
| `eqn_1_5` (T17) | (1.5) | `thm_1_7`, `eqn_1_5_of_thm_1_7`, `rem_1_8` | case $\lvert A\rvert\ge\frac12$ |
| `poincareConstBool_bounds` (T110) | §1.5 sentence before Thm 1.10 | `thm_1_10`, `IsHalfCube` | announcement of Thm 1.10 (placed in paper order) |
| `eqn_2_8` (2_2) | (2.8) | `eqn_2_9`, `btilde_eq_max`, `Ltilde_twopt` (cited BIM23 L. 2.3), `b_lt_Ltilde_imp` | proof of (2.8) follows its statement |
| `existsUnique_w₀` (3_0) | §3 (3.4) | `lemma_3_2` (concavity of $I$) | $w\mapsto wI(\frac1{2w})$ increasing needs $I(u)\ge uI'(u)$ (concavity); not argued in paper |
| `cor_3_5` (3_0) | Cor 3.5 | `rem_3_6` | Prop 3.3 needs $J_w'\le0$ on $[1-\frac w2,1]$, recorded in Rem 3.6 |

#### Cited (external prerequisites, not forward references)

`cor_1_9_kahn_park` [KP20]; `cor_1_9_bim` [BIM23]; `no_dimension_free_bound` [BIM23 §3];
`eqn_1_3` [Hart76]; `isoProfile_one_nowhere_differentiable` (no proof/citation in paper; follows
from (1.3), Takagi-type analysis); `conj_1_4_kahn_park` [KP20]; `conj_1_4_bim`,
`conj_1_4_bim_one` [BIM23]; `talagrand` [Tal93]; `bobkov_goetze` [BG99]; `bim_cor_1_7` [BIM23];
`eqn_1_5_bim` [BIM23]; `poincareConst_one_bounds` [BELP08, ILvHV]; `poincareConstBool_one_bim`
[BIM23]; `prop_2_1`, `prop_2_1_dyadic` [KP20]; `Ltilde_twopt` [BIM23 L. 2.3]; `lemma_3_1`
[Bob97 L. 1, BG99 L. 2.1]; `L_half_eqn_3_2` [BIM23 L. 2.2]; `eqn_3_3`, `I_maximal` [Bob97];
`rem_1_2`, `rem_2_6` [DIRX26 Thm 1.1] (also forward in the repo, listed above);
`isoProfile_one_eq_envelope` (uses that $\mathcal B_1$ satisfies (2.2) on $\mathcal Q$; not
argued in the paper).

No forward references: all remaining declarations (elementary or depending only on earlier
declarations), e.g. `dens_mem_dyadic`, `edge_boundary_iff_induced_edges`,
`edge_equivalence_fails`, `isoProfile_two_pow_le`, `isoProfile_one_two_pow` (from `eqn_1_3`),
`conj_1_4_of_ge_β₀` (`thm_1_1` + `isoProfile_two_pow_le`), `isoProfile_half_*`,
`best_constant_C*`, `eqn_1_4_at_half`, `expect_hA_*`, `eqn_1_5_of_thm_1_7`, `poincareConst_two`,
`two_mul_β₀`, `Q_spec`, `rem_2_4_local`, `isoProfile_ge_envelope` (via `prop_2_1_dyadic`),
`eqn_1_1_β₀`, `b_half_two_pow`, `thm_1_5_lower/upper`, `J_half_eq_L_half`, `btilde_eq_max`,
`b_lt_Ltilde_imp`, `isoProfile_ge_btilde`, and in 3_0 `M_indicator`, `eqn_3_2*`,
`L_half_eqn_3_1`, `proof_thm_1_6_chain`, `I_characterization`, `Jw_spec`, `eqn_3_4`, Lemma 3.2 and
Prop 3.3 with their proof parts, `rem_3_4`, `rem_3_6`, `eqn_3_6`, `J_eqn_3_2`, `rem_3_7_J`,
`rem_3_7_isoperim`.

### Per-file proof dependencies (files needed to prove all claims, beyond statement imports)

Direct dependencies; "(+ transitive)" means their own proof dependencies are also needed.

- **T11** (statement import: Mathlib): 5_1 (`lemma_5_1`), 2_0 (`cor_2_5` ← `thm_2_2`), 2_2
  (`eqn_1_1_β₀`, `b_eq_Q_ge_L`), 5_3 (`lemma_5_9`), hence (+ transitive) 6_1–6_6, 4_1–4_3, 5_2–5_4,
  3_0; X-T11 for `rem_1_2` (cited).
- **T15** (imports T11): T11 (`thm_1_1` for `conj_1_4_of_ge_β₀`), 2_0, 2_2 (for `thm_1_5`),
  hence (+ transitive) the same as T11.
- **T16** (imports T15): 3_0 (proof of (1.4)); otherwise T15 (`eqn_1_3`).
- **T17** (imports T15): 3_0 (`eqn_3_4`, `Jw_spec`, `existsUnique_w₀`, `lemma_3_2` for
  `existsUnique_J`), 2_0 (`prop_2_1`, `thm_2_2`), 2_2 (`eqn_2_8`, `eqn_2_9`, `isoProfile_ge_btilde`),
  5_2 (`lemma_5_2`), 5_4 (`lemma_5_13`), T11 (`thm_1_1` for (1.5)), hence (+ transitive) 6_x, 4_x,
  5_x; `rem_1_8` (and thus `eqn_1_5` for $\beta>\beta_0$) has no proof in the paper.
- **T110** (imports T11): 7_0 (`eqn_7_1`, `prop_7_1`), 2_0 (`cor_2_5`), hence (+ transitive) 6_x,
  5_x (incl. 5_4 `cor_5_12`), 4_x, 3_0; the case $p>2\beta_0$ has no proof in the paper.
- **2_0** (imports T15, T17): 6_1–6_6 (`thm_2_2`), hence 3_0, 4_1–4_3, 5_1–5_4; 3_0 (`rem_3_6`,
  `eqn_3_4` for `rem_2_4_failure`); X-T11 (`rem_2_6`, cited).
- **2_1** (imports 2_0): 5_2 (`lemma_5_2`), T15 (`eqn_1_3` for `isoProfile_one_eq_envelope`).
- **2_2** (imports 2_0): 5_2 (`lemma_5_2`), 5_3 (`lemma_5_9`), 5_4 (`lemma_5_13`), 2_0
  (`cor_2_5`, `thm_2_2`, `prop_2_1`), T15 (`isoProfile_two_pow_le`), hence (+ transitive) 6_x, 4_x.
- **3_0** (imports 2_0): T17 (`existsUnique_J` for `eqn_3_4`), 5_4 (`I_asymp`, `cor_5_12` for
  `rem_3_7_asymp`, `existsUnique_w₀`), 4_2 (numerical enclosure for `w₀_mem`, `eqn_3_6`; the
  paper only says "one computes"), 2_0 (`b`, `G₁` definitions only).

## Part B: [DIR] §4, §5, §7

Files: `4_1_Dyadic_Partitioning`, `4_2_Interval_Arithmetic`, `4_3_Source_Code`,
`5_1_Small_Exponents_Large_Exponents`, `5_2_Two_Point_Inequalities`, `5_3_Properties_L_Q`,
`5_4_Lower_Bounds_Gaussian_Isoperimetric_Profile`, `7_0_Proof_Poincare_Inequality` (all under
`Isoperim/DIR/`). The analysis follows the paper's arguments, not the Lean code. Global order is
`automation/tmp/paper_order.txt`.

### 1. Genuine forward references (prerequisite in a later file)

All of them come from the proof of Lemma 5.13, which uses the enclosure (6.2) of §6.1.1.

| Lean claim (file) | Paper location | Prerequisite (paper ref, Lean name, file) | Explanation |
|---|---|---|---|
| `g_JL_lo` (def, 5_4) | proof of Lemma 5.13 | (6.2) $\overline J$, `J_hi`, 6_1 | The definition of $\underline{g_{JL,\beta}}$ uses $\overline J$, which is defined only in §6.1.1. *Statement-level fix:* the formula of $\overline J$ is now written out in `g_JL_lo`, so 5_4 no longer imports 6_1. |
| `g_JL_lo_tight` (5_4) | proof of Lemma 5.13 | (6.2) enclosure property, `eqn_6_2`, 6_1 (also $J$ increasing on $[\frac12,x_0]$, decreasing on $[x_0,1]$: `J_monotoneOn_antitoneOn`, 6_1) | The lower bound $2/J\ge2/\overline J$ needs the enclosure (6.2). |
| `eqn_5_11` (5_4) | (5.11) (🚗) | `eqn_6_2`, 6_1 (via `g_JL_lo_tight`) | Partition₁ on $\underline{g_{JL,\beta_0}}$ only proves (5.11) once $\underline{g_{JL,\beta_0}}$ is a lower bound. |
| `lemma_5_13_case_1` (5_4) | proof of Lemma 5.13 | (5.11) hence `eqn_6_2`, 6_1 | Strict concavity comes from (5.11). |
| `lemma_5_13` (5_4) | Lemma 5.13 | `eqn_6_2`, 6_1 (via case 1) | Case $\frac12<x\le\frac{2047}{2048}$. |

No forward references were found in 4_1, 4_2, 4_3, 5_1, 5_2, 5_3 or 7_0 (7_0 is the last [DIR]
file; everything it uses comes earlier).

### 2. Forward references inside a file that only reflect "statement, then proof"

The paper states a result and then proves it, so each of these claims comes before the proof steps
it relies on, in the same file. They are listed for completeness; none of them is a logical problem.

- 4_1: `fact_4_1` before `fact_4_1_if`, `fact_4_1_eps`, `fact_4_1_only_if`.
- 5_1: `lemma_5_1` before `lemma_5_1_holder`.
- 5_2: `lemma_5_2` before `lemma_5_2_chain`; `lemma_5_3` before `lemma_5_3_div`,
  `lemma_5_3_reduction`, `lemma_5_3_at_one`, `lemma_5_3_strictAnti`; `lemma_5_4` before
  `lemma_5_4_taylor`, `lemma_5_4_expansion` (and before `rem_5_5`, which it does not use).
- 5_3: `lemma_5_6` before `lemma_5_6_2_*`, `lemma_5_6_3_steps`, `lemma_5_6_4_*`; `lemma_5_8` before
  `lemma_5_8_2_rewrite`, `lemma_5_8_2_dbeta`, `lemma_5_8_3_dbeta`; `lemma_5_9` before `lemma_5_9_1_*`
  and `lemma_5_9_2_*`.
- 5_4: `prop_5_11` before `prop_5_11_*` and `εI`; `cor_5_12` before `J_one_sub`, `eqn_5_10` and
  `two_one_sub_εJ`; `lemma_5_13` before `eqn_5_11`, `lemma_5_13_case_1`, `lemma_5_13_case_2`,
  `lemma_5_13_u_range`, `eqn_5_12`, `lemma_5_13_used`, `lemma_5_13_frac_poly_bound`,
  `lemma_5_13_roots`, `eqn_5_12_small`.
- 7_0: `prop_7_1` before `G_P_symm`, `prop_7_1_case_I*`, `eqn_7_2`, `prop_7_1_case_II_mono`,
  `g_P_2_lo_tight`, `eqn_7_3`, `prop_7_1_case_III_*`, `g_P_3_formula`, `g_P_3_lo_tight`, `eqn_7_4`.

### 3. Prerequisites of each claim (paper arguments)

The prerequisite file is given in brackets when it is not the claim's own file; "lit." means
cited from the literature or standard (external, not a forward reference).

#### 4_1 (§4, §4.1)
- `fact_4_1`: `fact_4_1_if`, `fact_4_1_eps`, `fact_4_1_only_if`; Heine–Borel (lit.; with the gap noted
  in err_B, Cousin's lemma is what is needed).
- `fact_4_1_if`: definitions only. `fact_4_1_eps`: tightness definition.
  `fact_4_1_only_if`: `fact_4_1_eps`, compactness (lit.).
- `rem_4_2`: tightness definition (elementary).
- `rem_4_3`: definitional (`IsTightLowerBound₂`).
- `partition_admissible`: definitions of `partitionAux`/`children` (induction on fuel).
- `partition_succeeds`: `fact_4_1_eps` plus a bisection/König argument (see err_B).

#### 4_2 (§4.2)
- `interval_order_partial`: elementary. `IsIntervalEnclosure`: definition. Remark 4.4 is a comment.

#### 4_3 (§4.3)
- No claims.

#### 5_1 (§5.1)
- `lemma_5_1`: `lemma_5_1_holder`; Hölder's inequality (lit./Mathlib); definitions of $h_A$, $|A|$
  [Thm_1_1]. The "in particular" part uses $B(t)=t(\log_2\frac1t)^{\beta_0}$ only.
- `lemma_5_1_holder`: Hölder (lit.), support of $h_A$ in $A$.

#### 5_2 (§5.2)
- `eqn_5_1_max`, `lemma_5_2`, `lemma_5_2_chain`: monotonicity of $\mathcal L$ (elementary).
- `lemma_5_3` and its steps: calculus (elementary).
- `G_eq_cases`: `lemma_5_3`; definitions (2.1) `G`, `G₁`, `G₂` [2_0].
- `G₁_diag`: definition of `G₁` [2_0].
- `lemma_5_4`: `lemma_5_4_taylor`, `lemma_5_4_expansion`; Taylor's theorem (lit.); `G₁` [2_0].
- `rem_5_5`: concavity (elementary).

#### 5_3 (§5.3)
- `eqn_5_2`–`eqn_5_4`: calculus on `L` [2_0].
- `lemma_5_6`: (1) `eqn_5_3`; (2) `lemma_5_6_2_*` (with `eqn_5_3`); (3) `eqn_5_4`,
  `lemma_5_6_3_steps`; (4) `lemma_5_6_4_*` (with `eqn_5_4`).
- `rem_5_7`: numerics.
- `eqn_5_5`, `α₁_pos_iff`, `eqn_5_6`–`eqn_5_9`: elementary; `Q` [2_0].
- `lemma_5_8`: (1) `eqn_5_9`; (2) `lemma_5_8_2_rewrite` (with `eqn_5_6`), `lemma_5_8_2_dbeta`;
  (3) `eqn_5_7`, `eqn_5_8`, `lemma_5_8_3_dbeta`.
- `lemma_5_9`: `lemma_5_6` ((3) for $L'''>0$ on $(0,\frac14]$ via `rem_5_7`, (4) for
  $L^{(4)}<0$), `lemma_5_8` ((3) for $Q'''$, (2) for $Q'(0)$), `lemma_5_9_1_*`, `lemma_5_9_2_*`,
  `Q_spec` [2_0] for the values at $0,\frac14,\frac12$. Note: Lemma 5.9 allows
  $\beta=\log_2(\frac32)$, which Lemma 5.8 excludes; at that endpoint only $Q'''=-16\alpha_1=0\le0$
  (from (5.8)) is needed, so this is harmless.
- `rem_5_10`: **no proof in the paper** (for $\beta>\log_2\frac32$ Lemma 5.8 no longer applies, since
  $\alpha_1<0$).

#### 5_4 (§5.4)
- `I_asymp`: lit. ("well-known"); `I`, `φ`, `Φ` [3_0].
- `prop_5_11`: `prop_5_11_ibp`, `prop_5_11_Phi_le`, `prop_5_11_apply_I` (with $I$ increasing on
  $[0,\frac12]$, elementary from $I'=-\Phi^{-1}$), `prop_5_11_t_formula`, `prop_5_11_t_bounds`,
  `prop_5_11_log_bound`, `prop_5_11_eps`, `prop_5_11_eps_small`, `prop_5_11_final`; the
  surjectivity of $t\mapsto|t|^{-1}\varphi(t)$ onto $(0,\frac12]$ (implicit, elementary).
- `I_upper`: **no proof in the paper** ("along the same lines").
- `cor_5_12`: `eqn_5_10`, `two_one_sub_εJ`.
- `J_one_sub`: (3.4) `eqn_3_4`, `Jw` [3_0].
- `eqn_5_10`: `J_one_sub`, `prop_5_11`, `w₀_mem` [3_0] (for $x/w_0\le\frac15$).
- `two_one_sub_εJ`: `w₀_mem` [3_0], numerics.
- `lemma_5_13`: `lemma_5_13_case_1`, `lemma_5_13_case_2`, `lemma_5_13_u_range`, `eqn_5_12`,
  `lemma_5_13_used`, `lemma_5_13_frac_poly_bound`, `lemma_5_13_roots`, `eqn_5_12_small`.
- `g_JL_lo_tight`: (5.3) `eqn_5_3` [5_3]; $J''J=-2$ (`IsJ` [Thm_1_7], `Jw_spec` [3_0]);
  **(6.2) `eqn_6_2` [6_1] (forward)**.
- `eqn_5_11` (🚗): `g_JL_lo_tight`, `fact_4_1` [4_1], computer verification.
- `lemma_5_13_case_1`: `eqn_5_11`; $J(\frac12)=\frac12$ [Thm_1_7]; numerical value of
  $J(\frac{2047}{2048})$ (computation, via (3.4) [3_0]).
- `lemma_5_13_case_2`: `eqn_5_10`; definition of `L` [2_0].
- `lemma_5_13_u_range`, `lemma_5_13_used`, `lemma_5_13_frac_poly_bound`: `w₀_mem` [3_0], numerics.
- `lemma_5_13_roots`: Descartes' rule of signs for fractional polynomials ([Jam06], lit.), IVT.
- `eqn_5_12`: `lemma_5_13_frac_poly_bound`, `lemma_5_13_roots`, `eqn_5_12_small`.
- `eqn_5_12_small`: only sketched ("follows the same argument").
- `rem_5_14`: **heuristic, no rigorous proof in the paper** (would need sharp two-sided
  asymptotics of $J$, e.g. `prop_5_11`, `I_upper`, (3.4)).

#### 7_0 (§7)
- `boolean_eq_indicator`, `indicator_norms`, `eqn_7_1`: definitions `pNorm`, `gradNorm` [Thm_1_10],
  `hA`, `dens` [Thm_1_1] (elementary).
- `grad_norm_ge`: `eqn_7_1`; $|A^c|=1-|A|$ (elementary).
- `prop_7_1`: `G_P_symm`, `prop_7_1_case_I`, `eqn_7_3`, `prop_7_1_case_III_eq`, `eqn_7_4`.
- `rem_7_2`: **no proof in the paper** ("same methods"; Lemma 5.8 is unavailable for
  $\beta\ge\log_2\frac32$).
- `G_P_symm`: `b`, `Q_spec` [2_0] ($Q_\beta(\frac12)=\frac12$), $J(1)=0$ [Thm_1_7].
- `prop_7_1_case_I_eq`, `prop_7_1_case_III_eq`: definition of `b` [2_0], `Q_spec` [2_0].
- `prop_7_1_case_I_chain`: **Corollary 5.12 `cor_5_12` [5_4]**; monotonicity of $L_\beta$ in
  $\beta$ (elementary).
- `eqn_7_2`: `w₀_mem` [3_0], numerics. `prop_7_1_case_I`: `prop_7_1_case_I_chain`, `eqn_7_2`.
- `prop_7_1_case_II_mono`: `eqn_3_6` [3_0] ($x_0\in[0.552,0.553]$), `J_monotoneOn_antitoneOn` [6_1].
- `g_P_2_lo_tight`: `prop_7_1_case_II_mono`, monotonicity of $L_{1/2}$ on $[\frac1{64},\frac14]$
  (`eqn_5_2` [5_3]), the chain of `prop_7_1_case_I_chain` (elementary part).
- `eqn_7_3` (🚗): `g_P_2_lo_tight`, `fact_4_1` [4_1], computer verification.
- `g_P_3_formula`: calculus, `eqn_3_4` [3_0] ($J=J_{w_0}$ on $[\frac12,1]$).
- `prop_7_1_case_III_mono`: $J''<0$ and $J'(x_0)=0$ (`iteratedDeriv_two_J`, `deriv_J_x₀` [6_1],
  or `Jw_spec` [3_0]); `lemma_5_8` [5_3] (with $\beta_0<\log_2\frac32$).
- `g_P_3_lo_tight`: `lemma_5_8` [5_3], `prop_7_1_case_III_mono`, `absDJ_enclosure` [6_1],
  `eqn_3_4` [3_0].
- `eqn_7_4` (🚗): `g_P_3_lo_tight`, `fact_4_1` [4_1], computer verification.

### 4. Proof dependencies per file

These are the files needed to **prove** all claims of the file, beyond the files it imports for its
statements. Transitive imports are omitted.

| File | Statement imports | Additional proof dependencies |
|---|---|---|
| 4_1_Dyadic_Partitioning | Mathlib | none |
| 4_2_Interval_Arithmetic | Mathlib | none |
| 4_3_Source_Code | Mathlib | none (no claims) |
| 5_1_Small_Exponents_Large_Exponents | Thm_1_1 | none |
| 5_2_Two_Point_Inequalities | 2_0_Envelope_Functions | none |
| 5_3_Properties_L_Q | 2_0_Envelope_Functions | none (`Q_spec` comes from 2_0, which is already imported) |
| 5_4_Lower_Bounds_Gaussian_Isoperimetric_Profile | 3_0_Variants_Bobkov_Inequality, 4_1_Dyadic_Partitioning | **5_3_Properties_L_Q** (`eqn_5_3`), **6_1_Case_J** (`eqn_6_2`, `J_monotoneOn_antitoneOn`; forward); plus computer verification for (5.11) and literature ([Jam06], asymptotics of $I$) |
| 7_0_Proof_Poincare_Inequality | Thm_1_10, 3_0_Variants_Bobkov_Inequality, 4_1_Dyadic_Partitioning | **5_3_Properties_L_Q** (`lemma_5_8`, `eqn_5_2`), **5_4_Lower_Bounds_Gaussian_Isoperimetric_Profile** (`cor_5_12`), **6_1_Case_J** (`J_monotoneOn_antitoneOn`, `deriv_J_x₀`, `iteratedDeriv_two_J`, `absDJ_enclosure`); plus computer verification for (7.3), (7.4) |

### 5. Other files that use these claims (for information; not part of this audit)

- `Thm_1_1.eqn_1_1_mono` (§1) uses Lemma 5.1 `lemma_5_1` [5_1] (forward).
- `Thm_1_7.eqn_1_6_improves` and `2_2_Proofs_Theorems_1_1_1_5_1_7` ((2.9)) use
  Lemma 5.13 `lemma_5_13` [5_4] (forward).
- `Thm_1_10.thm_1_10` is proved in §7 from `eqn_7_1`, `grad_norm_ge`, `prop_7_1` [7_0] (forward;
  this is the paper's structure).
- §6 files use Lemmas 5.2, 5.4, 5.6, 5.8, 5.9 and (6.2) (backward, fine).

## Part C: [DIR] §6

Based on the paper's arguments (not on Lean imports). Global order: `automation/tmp/paper_order.txt`;
§6 files are `6_1` < `6_2` < … < `6_6` (all in `Isoperim/DIR/6_Proof_Two_Point_Inequality/`).
"Forward" = a claim stated before one of its prerequisites (later in the same file or in a later
file). No §6 claim depends on a *later file*; all forward instances are within one file
(statement-then-proof structure). (Outside these files: Theorem 2.2, `Auto.DIR.thm_2_2` in
`2_0`, is proved by all of §6, i.e. depends on the later files 6_1–6_6; not audited here.)

### Forward instances

| Lean name (file) | Paper location | Later prerequisite(s) (paper ref — Lean name, file) | Explanation |
|---|---|---|---|
| `prop_6_1` (6_1) | Prop. 6.1 | monotonicity in β — `caseJ_G₁_mono_β`; §6.1.1 — `caseJ_I_region_subset`, `caseJ_I`; §6.1.2 — `caseJ_II_suffices`, `caseJ_II` (all 6_1, later) | Proposition stated at the start of §6.1, proved by Cases I/II afterwards. |
| `caseJ_I` (6_1) | §6.1.1 | §6.1.1 bound — `caseJ_I_G₁_ge_g_J_1`; (6.3) — `eqn_6_3` (6_1, later) | Region claim stated before the estimate and the computer check that prove it. |
| `caseJ_II_iff_g_J_2` (6_1) | §6.1.2 | $2J(\frac{x+y}2)-J(x)\ge0$ — `caseJ_II_nonneg` (6_1, next) | Squaring equivalence needs the nonnegativity asserted in the next sentence. |
| `caseJ_II_nonneg` (6_1) | §6.1.2 | monotonicity in $y$, $x$ — `caseJ_II_antitone_y`, `caseJ_II_antitone_x` (6_1, later) | Paper asserts "$\ge0$" (no proof); the natural proof is via the monotonicity proved after it plus the value at $(\frac9{16},1)$. |
| `prop_6_2` (6_2) | Prop. 6.2 | `caseQ_I`, `caseQ_reduction`, (6.6) — `eqn_6_6` (6_2, later) | Proposition at the start of §6.2. |
| `eqn_6_6` (6_2) | (6.6) | §6.2.1 — `caseQ_II`, `caseQ_II_y_ge`; §6.2.2 — `caseQ_III_iff_G_Q`, `caseQ_III_min`, `caseQ_III_G_Q_quarter`, `caseQ_III_G_Q_diag`, `caseQ_III_iff_f_QIII`, `f_QIII_nonneg` (6_2, later) | Goal of §6.2 stated before both subcases. |
| `caseQ_II_g_Q_1_pos` (6_2) | §6.2.1 "if $\beta>\frac12$ then $g_{Q,1,\beta}>0$" | (6.7) — `eqn_6_7` (6_2, later) | For $\beta=\beta_0$ proved by the later computer check; for general $\beta>\frac12$ no proof in the paper. |
| `caseQ_II_g_Q_1_half_zero` (6_2) | §6.2.1 "$g_{Q,1,\frac12}(0,\frac12)=0$" | formula — `caseQ_II_g_Q_1_half_eq`; limit — `caseQ_II_claim_1_limit` (6_2, later) | Value follows from the formula displayed afterwards. |
| `caseQ_II_claim_1` (6_2) | §6.2.1 claim (1) | `caseQ_II_claim_1_limit`, `_iff`, `_poly`, `_subst`, `_mono` (6_2, later, section `Proof_Claim_1`) | Claim then proof. |
| `caseQ_II_claim_2` (6_2) | §6.2.1 claim (2) | (6.8) — `eqn_6_8`; `caseQ_II_claim_2_lo` (6_2, later) | Claim then proof. |
| `lemma_6_4` (6_2) | Lemma 6.4 | proof of Lemma 6.4 — `lemma_6_4_deriv`, `lemma_6_4_denom_pos`, `eqn_6_11`, `lemma_6_4_poly`, `eqn_6_11_eq_p_Q`, `lemma_6_4_of_strictAntiOn`, `g_Q_2_eq`, `g_Q_2_lo_tight`, (6.12) `eqn_6_12` (6_2, later) | Proof explicitly postponed to the end of §6.2. Second claim ($\partial_hG(\frac14,y)>0$) has no proof at all. |
| `deriv_f_QIII_nonpos` (6_2) | §6.2.2 "we claim $f'_\beta\le0$" | `deriv_f_QIII`, `deriv_f_QIII_nonpos_iff`, `f_QIII_deriv_eq_sub`, `caseQ_III_suffices_f_QIII_0`, (6.9) `eqn_6_9`, (6.10) `eqn_6_10`, `deriv_f_QIII_0_neg`, `deriv_f_QIII_0_neg_Icc_eighth` (6_2, later) | Claim then proof (and the proof needs the interval $[\frac18,\frac12]$). |
| `prop_6_6` (6_3) | Prop. 6.6 | Lemma 6.7 — `lemma_6_7`; `prop_6_6_reduction`; claims (1)–(3) — `caseLJQ_claim_1/2/3` (6_3, later) | Proposition then lemma and claims. |
| `lemma_6_7` (6_3) | Lemma 6.7 | `lemma_6_7_deriv2`, (6.14) `eqn_6_14`, `lemma_6_7_mono`, `Q_deriv2_monotone_β`, `lemma_6_7_eval` (6_3, later) | Lemma then proof. |
| `caseLJQ_claim_1` (6_3) | §6.3.2 claim (1) | `f_LJQ_1_eq`, `f_LJQ_1_ge_min`, `f_LJQ_1_one_nonneg`, `f_LJQ_1_half_nonneg` and their prerequisites (6.15), (6.16), `f_LJQ_1_half_deriv_half` (6_3, later) | Claim then proof. |
| `caseLJQ_claim_2` (6_3) | §6.3.2 claim (2) | `g_LJQ_2_lo_tight`, (6.17) `eqn_6_17` (6_3, later) | Claim then proof. |
| `caseLJQ_claim_3` (6_3) | §6.3.2 claim (3) | `f_LJQ_3_eq`, `f_LJQ_3_monotoneOn_β`, `f_LJQ_3_half_concaveOn`, `f_LJQ_3_half_one`, (6.18) `eqn_6_18` (6_3, later) | Claim then proof. |
| `prop_6_8` (6_4) | Prop. 6.8 | `prop_6_8_monotoneOn_beta`, `g_LJ_eq`, `g_LJ_nonneg` (6_4, later) | Proposition then proof. |
| `g_LJ_deriv2_nonpos` (6_4) | proof of Prop. 6.8, "we claim $\partial_x^2g_{LJ}\le0$" | `g_LJ_deriv2_eq`, `L_half_deriv2_monotoneOn_neg`, (6.19), `J_inv_le_two`, `g_LJ_deriv2_nonpos_of_le`, `g_LJ_deriv2_nonpos_of_deriv3`, (6.20), `J_inv_monotoneOn_Ico_x₀`, `g_LJ_deriv2_quarter_nonpos`, `g_LJ_deriv3_nonneg` (6_4, later) | Claim then argument. |
| `r_LJ_antitoneOn` (6_4) | proof of Prop. 6.8, "we claim $r$ decreasing" | `r_LJ_deriv`, `r_LJ_deriv_nonpos_of`, `h_LJ_deriv`, `h_LJ_antitoneOn`, `h_LJ_le_h_LJ_t`, `h_LJ_nonpos`, `two_h_LJ_le` (6_4, later) | Claim then argument. |
| `prop_6_9` (6_5) | Prop. 6.9 | `prop_6_9_of_endpoints`, `G_QJQ_ge_G_QJQ_half`, `G_QJQ_y_half_eq`, `G_QJQ_y_half_nonneg` (6_5, later) | Proposition then proof. |
| `rem_6_10` (6_5) | Remark 6.10 | (no proof in paper) natural proof via `G_QJQ_y_half_eq`, `G_QJQ_y_half_factor`, `p_QJQ` at $x=\frac14$ (6_5, later) | Failure occurs at $(\frac14,\frac12)$: $G=\frac1{32}p_\beta(\frac14)<0$. |
| `G_QJQ_monotone_or_antitone` (6_5) | §6.5 after Rem. 6.10 | positivity of $2Q_\beta(\frac{x+y}2)-Q_\beta(x)$ — `two_Q_sub_Q_pos_mono`/`two_Q_sub_Q_ge` (6_5, later); (5.9) `eqn_5_9` (5_3) | $\partial_\beta G_{QJQ}=-2A_\beta\,2^\beta k(x,y)$; sign constant needs $A_\beta>0$, shown later. |
| `G_QJQ_ge_G_QJQ_half` (6_5) | §6.5 "reducing to $y=\frac12$" | (6.25) — `eqn_6_25` (6_5, later) | Reduction stated before the computer check. |
| `J_mul_deriv_J_antitoneOn` (6_5) | §6.5 item 1 | `J_mul_deriv_J_deriv`, `deriv_J_sq_convexOn`, `deriv_J_sq_sub_two_endpoints`, `deriv_J_sq_sub_two_lt` (6_5, later) | Item then proof. |
| `two_Q_sub_Q_pos_mono` (6_5) | §6.5 item 2 | `two_Q_sub_Q_ge`, `deriv_Q_pos`, `two_Q_sub_Q_deriv_x` (6_5, later) | Item then proof. |
| `G_QJQ_y_half_nonneg` (6_5) | §6.5 final claim | `G_QJQ_y_half_factor`, `p_QJQ_coeffs_pos`, `p_QJQ_monotoneOn`, `p_QJQ_quarter` (6_5, later) | Claim then computation. |
| `prop_6_11` (6_6) | Prop. 6.11 | `prop_6_11_mono_beta`, `G₁_nonneg_iff_g_QJ_nonneg`, `g_QJ_nonneg_of_half`, `g_QJ_half_nonneg_iff`, `G₁_J_half_nonneg` (6_6, later); Prop. 6.1 `prop_6_1` (6_1, earlier) | Proposition then proof. |
| `g_QJ_deriv_x_nonpos` (6_6) | §6.6.1 "we claim $\partial_xg_{QJ}\le0$" | `g_QJ_deriv_x`, `g_QJ_deriv_x_nonpos_of_pos`, `g_QJ_1_tightLowerBound`, (6.26) `eqn_6_26` (6_6, later) | Claim then argument. |
| `prop_6_12` (6_6) | Prop. 6.12 / (6.27) | `g_QJ_2_tightLowerBound` (6_6, later, section `Proof_Proposition_6_12`); Fact 4.1 `fact_4_1_if` (4_1) | Proposition then proof. |

Claims with no proof in the paper (not forward, but unsupported): `rem_6_3` (Remark 6.3, all
$\beta\in[\frac12,1]$), `caseLJQ_I_all_β` (§6.3.1, all $\beta\in[\frac12,1]$),
`f_LJQ_1_one_nonneg` (§6.3.2 "$\beta=1$ very similar"), `caseQ_II_g_Q_1_pos` for
$\beta\ne\beta_0$, second claim of `lemma_6_4`, `rem_6_10`, `caseQ_G₁_L` (cited, [BIM23, Lemma 2.2]).

### Proof dependencies per file (beyond the statement imports)

Statement imports (current): 6_1 ← 3_0, 4_1, 5_3; 6_2 ← 4_1, 5_3; 6_3 ← 6_1; 6_4 ← 3_0;
6_5 ← 3_0, 4_1; 6_6 ← 3_0, 4_1 (changed from 6_1 in this audit). "Computations" means the
interval-arithmetic machinery/code of §4.2–4.3 (`4_2_Interval_Arithmetic`, `4_3_Source_Code`),
needed for every (🚗) claim and for the numerical evaluations (6.9), (6.10), (6.15)–(6.22).

- **6_1** needs: `1_Introduction/Thm_1_7` (`J`, `IsJ`, `existsUnique_J`: smoothness, $JJ''=-2$,
  boundary values), `1_Introduction/Thm_1_1` (`β₀`), `2_0` (`G₁`, `c₀`), `3_0` (`eqn_3_4`,
  `Jw_spec`, `w₀_mem`, `x₀`, `eqn_3_6`, `rem_3_6`, properties of `I`), `4_1` (`fact_4_1_if`,
  tight lower bounds), `4_2`/`4_3` (computations for (6.3), (6.5)), `5_2` (`lemma_5_4`).
- **6_2** needs: `2_0` (`G₁`, `L`, `Q`, `Q_spec`), `1_Introduction/Thm_1_1` (`β₀`), `5_2`
  (`lemma_5_2`, `lemma_5_4`), `5_3` (`lemma_5_8`, `lemma_5_9`, `eqn_5_5`–`eqn_5_8`, `α₁_pos_iff`,
  `α₀`, `α₁`), `4_1` (`fact_4_1_if`), `4_2`/`4_3` ((6.7), (6.8), (6.9), (6.10), (6.12));
  literature: [BIM23, Lemma 2.2] for `caseQ_G₁_L`.
- **6_3** needs: `6_1` (`eqn_6_1`, `eqn_6_2`, `iteratedDeriv_two_J`, `J_monotoneOn_antitoneOn`,
  `deriv_J_x₀`), `1_Introduction/Thm_1_7` (`J`), `2_0` (`G`, `b`, `L`, `Q`, `Q_spec`), `3_0`
  (`eqn_3_4`: one-sided values at $\frac12$, e.g. `f_LJQ_1_half_deriv_half`), `5_3` (`lemma_5_6`,
  `rem_5_7`, `eqn_5_7`, `eqn_5_9`, `lemma_5_8`, `α₁_pos_iff`), `4_1` (`fact_4_1_if`), `4_2`/`4_3`
  ((6.13), (6.15)–(6.18)).
- **6_4** needs: `6_1` (`iteratedDeriv_two_J`, `J_monotoneOn_antitoneOn`, `deriv_J_x₀`),
  `1_Introduction/Thm_1_7` (`J`), `2_0` (`L`), `3_0` (`eqn_3_4`, `w₀_mem`, `x₀`), `5_3`
  (`lemma_5_6`), `4_2`/`4_3` (evaluations (6.19)–(6.22), $f'(\frac34)>0$).
- **6_5** needs: `6_1` ($JJ''=-2$: `iteratedDeriv_two_J`; value $J'(\frac12^+)$), `1_Introduction/
  Thm_1_7` (`J`, $J(\frac12)=\frac12$), `2_0` (`Q`), `3_0` (`lemma_3_2`, `eqn_3_4`, `Jw_spec`),
  `5_3` (`lemma_5_8`, `eqn_5_6`, `eqn_5_7`, `eqn_5_9`), `4_1` (`fact_4_1_if`), `4_2`/`4_3` ((6.25),
  $p_\beta(\frac14)$, endpoint values of $(J')^2-2$).
- **6_6** needs: `6_1` (`prop_6_1` for `G₁_J_half_nonneg`; `J_monotoneOn_antitoneOn`,
  `deriv_J_x₀`, and the enclosure lemmas `eqn_6_2`/`absDJ_enclosure`, whose $J_{w_0}$-analogues are
  needed for `g_QJ_1_tightLowerBound`, `g_QJ_2_tightLowerBound`), `1_Introduction/Thm_1_1`, `Thm_1_7`,
  `2_0` (`G₁`, `b`, `Q`, `c₀`), `3_0` (`eqn_3_4`, `Jw_spec`, monotonicity of $J_{w_0}$ on
  $[1-w_0,1]$, `w₀_mem`, `x₀`), `5_3` (`lemma_5_8`, `eqn_5_9`), `4_1` (`fact_4_1_if`), `4_2`/`4_3`
  ((6.26), (6.27)).

## Part D: [DIRX]

Scope: all 15 files `Isoperim/DIRX/**/*.lean`. The analysis is of the paper's arguments (which
results each proof uses), not of Lean proofs (all claims are `sorry`). Global order =
`automation/tmp/paper_order.txt` (all [DIR] files, then the [DIRX] files in paper order); within a
file, declaration order. Citations of [DIR] are backward by construction; the [DIR] files needed
are listed in Part B.

Abbreviations for files: `X/Thm_1_1` = `Isoperim/DIRX/1_Introduction/Thm_1_1.lean`,
`X/2_1` = `Isoperim/DIRX/2_Preliminaries/2_1_Reduction_Two_Point_Inequality.lean`, `X/3_k` =
`Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_k_*.lean`, `X/4_0`, `X/5_0` analogously;
`D/...` likewise for `Isoperim/DIR/...`. All Lean names are in namespace `Auto.DIRX` unless
prefixed `DIR.` (= `Auto.DIR.`).

### A. Forward instances (a claim appears before one of its prerequisites)

#### A.1 Prerequisite in a later file

| # | Claim (Lean, file) | Paper location | Prerequisite (paper ref, Lean, file) | Explanation |
|---|---|---|---|---|
| 1 | `thm_1_1`, X/Thm_1_1 | Thm 1.1 | Kahn–Park reduction (§2.1, `kahn_park`), $B_w\ge L$ (§2.1, `BX_ge_LX`), reduction (§2.1, `thm_1_1_of_eqn_2_4`), all X/2_1 | Thm 1.1 is proved in §2.1 from (2.4) via the Kahn–Park induction |
| 2 | `thm_1_1`, X/Thm_1_1 | Thm 1.1 | (2.4) `eqn_2_4` (X/2_1), proved by §3.1–3.6: `caseJ` (X/3_1), `caseQ` (X/3_2), `caseLJQ` (X/3_3), `caseLJ` (X/3_4), `caseQJQ` (X/3_5), `caseQJ` (X/3_6) | the two-point inequality is the core of the proof |
| 3 | `thm_1_3`, X/Thm_1_3 | Thm 1.3 | §4: `thm_1_3_of_eqn_4_1`, (4.1) `eqn_4_1`, `norms_indicator`, `bool_eq_indicator` (X/4_0) | Thm 1.3 is proved in §4 |
| 4 | `thm_1_3`, X/Thm_1_3 | Thm 1.3 | (2.5) `eqn_2_5` (X/2_1) | "does not follow directly from Theorem 1.1, but from (2.5)"; used in `thm_1_3_of_eqn_4_1` |
| 5 | `eqn_1_4`, X/Thm_1_3 | (1.4) | `bool_eq_indicator` (§4, X/4_0) | writing a Boolean $f$ as $\mathbf 1_A$ (trivial, but stated only in §4) |
| 6 | `poincareConstBool_one`, X/Thm_1_3 | §1 after Thm 1.3 | `thm_1_3` (earlier, same file) | direct prerequisite is backward; transitively forward via #3, #4 |
| 7 | `eqn_2_4`, X/2_1 | (2.4) | `caseJ`, `caseQ`, `caseLJQ`, `caseLJ`, `caseQJQ`, `caseQJ` (§3.1–3.6, X/3_1…X/3_6) | (2.4) is proved in §3 by the six cases |
| 8 | `eqn_2_5`, X/2_1 | (2.5) | `eqn_2_4` (earlier in file) | direct prerequisite backward; transitively §3 (#7) |
| 9 | `rem_2_1`, X/2_1 | Remark 2.1 | the whole §3 argument (X/3_1…X/3_6), redone uniformly for $w$ in an interval | no proof in the paper; §3 only treats $w=w_1$ |
| 10 | `rem_2_2_near_one`, X/2_1 | Remark 2.2 | value of $I(\frac1{2w_1})$ (equivalently $\gamma$), `γX_mem` (§2.2, X/2_2) | leading constant $\sqrt{2\gamma}\approx1.972<2\cdot0.997$ of $\mathrm{J}(1-t)/(t\sqrt{2\log(1/t)})$; could alternatively be a direct single-point evaluation |
| 11 | `rem_2_2_stronger`, X/2_1 | Remark 2.2 | properties of $\mathrm{J}$ from §2.2 (`JX_mul_deriv2`, `JX_mono`, `γX_mem`, X/2_2) | no proof in the paper; any comparison of $J_{w_0}$ with $\mathrm{J}$ on $(\frac12,1)$ needs the ODE/monotonicity facts of §2.2 |
| 12 | `caseJ_I_convex`, X/3_1 | §3.1 Case I | convexity of $(\mathrm J')^2$: the paper cites [DIR, Lemma 3.2] (`DIR.lemma_3_2`, D/3_0, backward); the [DIRX]-normalized statement `deriv_JX_sq_convex` is in X/3_5 | forward only if one uses the Lean statement of X/3_5 instead of instantiating `DIR.lemma_3_2` |

#### A.2 Prerequisite later in the same file (headline claim before its proof steps)

| # | Claim (Lean, file) | Paper location | Prerequisites (later in same file) |
|---|---|---|---|
| 13 | `thm_1_2`, X/Thm_1_2 | Thm 1.2 | `thm_1_2_chain` (derivation after the theorem) |
| 14 | `eqn_1_4`, X/Thm_1_3 | (1.4) | `sensitivity_indicator`, `hA_mul_hA_compl`, `sqrt_sensitivity_indicator`, `eqn_1_4_of_thm_1_1` |
| 15 | `JX_mul_deriv2`, X/2_2 | §2.2 | `JX_contDiff` (smoothness of $\mathrm J$, needed to differentiate) |
| 16 | `eqn_2_6`, X/2_2 | (2.6) | `I_lower`, `eqn_2_6_step`, `εX_monotone`, `eqn_2_6_eval` |
| 17 | `JX_mono`, X/2_2 | §2.2 | `deriv_JX` ($\mathrm J'(x_1)=0$, $\mathrm J''<0$) |
| 18 | `caseJ`, X/3_1 | §3.1 | `caseJ_G₁_eq`, `eqn_3_1` |
| 19 | `eqn_3_1`, X/3_1 | (3.1) | `caseJ_cu`, `caseJ_rhs_nonneg`, `caseJ_sq_iff`, `FX_nonneg` |
| 20 | `caseJ_cu`, X/3_1 | §3.1 | `caseJ_rhs_nonneg`, `caseJ_sq_iff`, `FX_nonneg` |
| 21 | `eqn_3_2`, X/3_1 | (3.2) | `caseJ_I`, `caseJ_II`, `caseJ_II_eval` (and `γX_le_two`) |
| 22 | `caseQ`, X/3_2 | §3.2 | `caseQ_G₁_max`, `BX_eq_max` |
| 23 | `caseLJQ`, X/3_3 | §3.3 | `eqn_3_3`, `G₂_BX_eq_G_LJQ`, `caseLJQ_II` |
| 24 | `caseLJQ_II`, X/3_3 | §3.3 Case II | `G_LJQ_strictConcave`, `eqn_3_4`, `caseLJQ_II_of_boundary`, `fX_nonneg`, `eqn_3_7`, `G_LJQ_diag_nonneg` |
| 25 | `G_LJQ_strictConcave`, X/3_3 | §3.3 | `eqn_3_4` (3.4) |
| 26 | `caseLJ`, X/3_4 | §3.4 | `G₂_BX_eq_h_LJ`, `h_LJ_nonneg` |
| 27 | `h_LJ_nonneg`, X/3_4 | §3.4 | `h_LJ_deriv2`, `h_LJ_concave`, `eqn_3_8`, `h_LJ_eq_gX`, `gX_nonneg` |
| 28 | `gX_nonneg`, X/3_4 | §3.4 Case II | `gX_half`, `gX_deriv`, `deriv_LX_JX_anti`, `gX_deriv_ge` (and `gX_deriv_ge_1/2/3`) |
| 29 | `caseQJQ`, X/3_5 | §3.5 | `eqn_3_9`, `caseQJQ_of_eqn_3_9` |
| 30 | `eqn_3_9`, X/3_5 | (3.9) | `eqn_3_9_low`, `eqn_3_12` |
| 31 | `QJQ_monotone`, X/3_5 | §3.5 | `deriv_QX_pos` ($Q'>0$ on $[0,\frac{33}{64}]$; needed because $\frac{x+y}2$ reaches $\frac{65}{128}>\frac12$) |
| 32 | `JX_mul_deriv_anti`, X/3_5 | §3.5 | `JX_mul_deriv_deriv`, `deriv_JX_sq_convex`, `deriv_JX_sq_sub_γX` |
| 33 | `caseQJ`, X/3_6 | §3.6 | `caseQJ_near`, `G₁_BX_eq_h_QJ₂`, `eqn_3_14` |
| 34 | `caseQJ_near`, X/3_6 | §3.6.1 | `G₁_of_g_QJ`, `g_QJ_half`, `g_QJ_nonneg` |
| 35 | `g_QJ_nonneg`, X/3_6 | §3.6.1 | `g_QJ_deriv`, `eqn_3_13` |
| 36 | `eqn_3_14`, X/3_6 | (3.14) | `h_QJ₂_lo_tight` (the tight lower bound is displayed after the claim) |
| 37 | `eqn_4_1`, X/4_0 | (4.1) | `G_PX_symm`, `G_PX_eq_I`, `G_PX_I_lower`, `g_P₁X_antitone_eval`, `G_PX_I`, `eqn_4_2`, `G_PX_III` |
| 38 | `G_PX_III`, X/4_0 | §4 Case III | `G_PX_half`, `G_PX_III_anti`, `h_P₂_eq`, `deriv_JX_one_sub_mono`, `eqn_4_3` |

No forward instances in X/2_3, X/2_4, X/5_0 (in X/5_0 every step uses only earlier steps and the
definitions of X/Thm_1_3), and none in X/Thm_1_1 other than #1–#2 (`eqn_1_2`, `eqn_1_1_rpow`
use `thm_1_1`, which is earlier in the file; the other claims there are cited from the literature
or are direct computations).

Totals: 12 cross-file instances (A.1, of which #6 and #8 are only transitive and #12 is
conditional) and 26 same-file instances (A.2).

### B. Proof dependencies per [DIRX] file

"Direct" = files whose results are invoked in the paper's proofs of the claims of the file;
"beyond imports" = those not already (transitively) imported by the file for its statements.
Literature results stated as cited claims (Talagrand, Harper, [KP20], [BIM23], [BELP08],
[ILvHV], [BG99]) are not proved from other files.

| [DIRX] file | Direct proof dependencies (reason) | Beyond imports |
|---|---|---|
| X/Thm_1_1 | X/2_1 (`kahn_park`, `BX_ge_LX`, `thm_1_1_of_eqn_2_4`, `eqn_2_4`); via (2.4): X/3_1–X/3_6 and their deps (X/2_2, X/2_3, D/4_1, D/5_3, D/6_2, D/6_3, D/6_5, D/5_4); D/5_1 (`DIR.lemma_5_1`, Hölder, for `eqn_1_1_rpow`; or `DIR.eqn_1_1_mono` in D/Thm_1_1); D/Thm_1_5 (`DIR.bobkov_goetze`, `DIR.no_dimension_free_bound`); D/2_0 (`DIR.prop_2_1`, Kahn–Park) | X/2_1, X/2_2, X/2_3, X/3_1–X/3_6, D/Thm_1_5, D/2_0, D/3_0, D/4_1, D/5_1, D/5_3, D/5_4, D/6_2, D/6_3, D/6_5 |
| X/Thm_1_2 | X/Thm_1_1 (`thm_1_1` for $B\cup W$), hence all of the X/Thm_1_1 row | X/Thm_1_1 and its row |
| X/Thm_1_3 | X/4_0 (proof of Thm 1.3), X/2_1 (`eqn_2_5`), X/Thm_1_1 (`thm_1_1` for (1.4)); transitively §3 and its deps | X/Thm_1_1, X/2_1, X/2_2, X/2_3, X/3_1–X/3_6, X/4_0, D/2_0, D/3_0, D/4_1, D/5_3, D/5_4, D/6_2, D/6_3, D/6_5 |
| X/2_1 | D/2_0 (`DIR.prop_2_1`), D/3_0 (`DIR.I_characterization`), D/5_3 (`DIR.lemma_5_9`), D/5_4 (`DIR.prop_5_11`, `DIR.lemma_5_13`, asymptotics of $I$, Remark 2.2), D/2_2 (`DIR.eqn_2_9`, Remark 2.2), D/Thm_1_7 (`DIR.J`, `DIR.thm_1_7`); X/2_2 (`γX_mem`, $\mathrm J$ properties, Remark 2.2); X/3_1–X/3_6 (`eqn_2_4`, `rem_2_1`) | D/2_2, D/5_3, D/5_4, X/2_2, X/2_3, X/3_1–X/3_6, D/4_1, D/6_2, D/6_3, D/6_5 |
| X/2_2 | D/3_0 (`DIR.I_characterization`, smoothness and symmetry of $I$), D/5_4 (`DIR.prop_5_11` for `I_lower`) | D/5_4 |
| X/2_3 | D/5_3 (`DIR.lemma_5_6`, `DIR.lemma_5_8` at $\beta=\frac12$) | D/5_3 |
| X/2_4 | none (no claims) | none |
| X/3_1 | X/2_1 (`JXw_half_one`), X/2_2 (`JX_concave`, `JX_mono`, `deriv_JX`, `JX_mul_deriv2`, `JX_contDiff`, `γX_mem`), D/3_0 (`DIR.lemma_3_2`) | none (optionally X/3_5 `deriv_JX_sq_convex`, see #12) |
| X/3_2 | D/6_2 (`DIR.prop_6_2` at $\beta=\frac12$), D/5_3 (`DIR.lemma_5_9`) | D/5_3, D/6_2 |
| X/3_3 | X/2_1, X/2_2 (`eqn_2_7`, `JX_mul_deriv2`, `JX_contDiff`), X/2_3 (`lemma_2_3`, `lemma_2_4`), D/6_3 (`DIR.lemma_6_7` for (3.4)), D/4_1 (`DIR.fact_4_1`) | X/2_3, D/6_3 |
| X/3_4 | X/2_1, X/2_2 (`eqn_2_7`, `JX_mul_deriv2`, `deriv_JX`), X/2_3 (`lemma_2_3`), D/4_1 | X/2_3 |
| X/3_5 | X/2_1, X/2_2 (`eqn_2_7`, `JX_mul_deriv2`), X/2_3 (`lemma_2_4`), D/3_0 (`DIR.lemma_3_2`), D/6_5 (`DIR.two_Q_sub_Q_pos_mono`, `DIR.G_QJQ_y_half_nonneg`), D/4_1 | X/2_3, D/6_5 |
| X/3_6 | X/2_1, X/2_2 (`eqn_2_7`, `JX_mono`, `deriv_JX`, `absDJX_encl`), X/2_3 (`lemma_2_4`), X/3_1 (`eqn_3_1` for `g_QJ_half`), D/4_1 | X/2_3, X/3_1 |
| X/4_0 | X/2_1 (`eqn_2_5`, `JXw_half_one`, `QX_spec`), X/2_2 (`eqn_2_6`, `JX_mono`, `deriv_JX`, `x₁_eq`), X/2_3 (`lemma_2_4`), X/Thm_1_3 (`sensitivity_indicator`, `hA_mul_hA_compl` for `norms_indicator`), D/Thm_1_10 (defs), D/4_1; via `eqn_2_5`: X/3_1–X/3_6 and their deps | X/Thm_1_3, X/2_3, X/3_1–X/3_6, D/5_3, D/5_4, D/6_2, D/6_3, D/6_5 |
| X/5_0 | none beyond its own earlier steps (X/Thm_1_3 only for the definitions `probZ`, `s_{f}`) | none |

Note on mutual dependencies at file level: X/Thm_1_3 needs X/4_0 (proof of Thm 1.3) and X/4_0
needs X/Thm_1_3 (`sensitivity_indicator`, `hA_mul_hA_compl`); there is no cycle at the level of
declarations. Similarly X/2_1 (`eqn_2_4`) needs §3 while §3 imports X/2_1 for definitions.
