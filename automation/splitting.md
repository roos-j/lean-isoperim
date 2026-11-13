# Splitting of the proof work into Tasks 1–5

Proposal (2026-11-12, revised and audited). Computed from the declaration-level dependency graph
(`automation/proof_dependencies.txt`: statement dependencies from Lean plus the paper-proof
dependencies of every claim), so the following properties are *verified*, not estimated:

- Every one of the 444 theorems belongs to exactly one task.
- **Task 1** depends on nothing outside Task 1.
- **Tasks 2, 3, 4** are logically disjoint: no declaration of one of them depends on a
  declaration of another; each depends only on Task 1 and on itself.
- No declaration of Tasks 1–4 depends on Task 5; **Task 5** depends on Tasks 1–4.

Order: Task 1 → (Tasks 2, 3, 4 in parallel) → Task 5; the Kahn–Park reduction (Task 4)
depends only on definitions and can start at once. Within a task, follow the module order of
`Isoperim.lean` and the declaration order in each file (strict forward order is guaranteed).
Proof-stage rules: see `AGENTS.md` (a proof may start only when all its dependencies are
proved; long proofs and new lemmas go into `*_aux.lean` files).

## Prompts for the task agents

Give the agent of Task *k* the following prompt (replace *k*):

> You are the coding agent for **Task *k*** of the Lean formalization in this repository (papers
> [DIR] arXiv:2407.12674 and [DIRX] arXiv:2602.20462, TeX sources on arXiv). Read `AGENTS.md`
> (proof-stage rules), `CLAUDE.md` (commit rules) and the section "Task *k*" of `automation/splitting.md`.
> Your job: replace the `sorry` of every theorem listed for Task *k* by a complete proof, following
> the paper's argument (the docstrings give the claim and its location). Rules:
> 1. Work only on the declarations of Task *k*; never change any statement, definition or
>    another task's declaration. If a statement looks wrong or unprovable, stop working on it and
>    report it (with a precise reason) instead of changing it. Only exception: remove hypotheses
>    your proof does not use and note this in the docstring (`AGENTS.md`, rule 7).
> 2. Start a proof only when all its dependencies in `automation/proof_dependencies.txt` are
>    completely proved (no transitive `sorry`); otherwise work on another ready declaration.
>    Work in the module order of `Isoperim.lean` and the declaration order within each file.
> 3. Proofs longer than 100 lines and any additional lemmas go into the `_aux.lean` file of the
>    same folder (see `AGENTS.md`). Facts the paper uses but the scaffold does not state
>    (`automation/forward_reasoning.md` §4) are added there as needed.
>    Follow the papers' arguments; for the 🚗 claims use the paper's tight lower bound, its
>    partition (`partitions.py`) and the tools of [DIR] §4 (`AGENTS.md`, rule 8).
> 4. A proof is complete only if `#print axioms` shows nothing beyond `propext`,
>    `Classical.choice`, `Quot.sound` (no `native_decide`, no other axioms; also for 🚗 claims).
> 5. Keep `lake build` green; commit small, verified steps following `CLAUDE.md`, and record
>    progress in `automation/Status.md`.
>
> Report at the end: the declarations completed, those blocked (and by what), and any problems
> found in statements.

Task-specific notes:

- **Task 1** (preparation): Tasks 2–4 wait for your results; prioritise the declarations that
  other tasks depend on (see `automation/proof_dependencies.txt`).
- **Task 2**, **Task 3**, **Task 4**: independent of each other; they depend only on Task 1. Task 3
  starts with [DIR] Case $Q$ (§6.2). Task 4 can start the Kahn–Park reduction immediately (it depends only on definitions).
  The computer-verified (🚗) claims are proved as in the paper (tight lower bound, partition from
  `partitions.py`, [DIR] §4 tools, certified numerics of `4_3_Source_Code_aux.lean`).
- **Task 5** (wrap-up): starts when the declarations it depends on are proved; it only assembles
  results of Tasks 1–4.

## Overview

| Task | Theorems | of which computer-verified (🚗) | Main files |
|---|---|---|---|
| 1 | 56 | 0 | `5_3_Properties_L_Q`, `3_0_Variants_Bobkov_Inequality`, `6_3_Case_LJQ`, `6_5_Case_QJQ` |
| 2 | 120 | 7 | `6_4_Case_LJ`, `6_3_Case_LJQ`, `6_1_Case_J`, `6_6_Case_QJ` |
| 3 | 157 | 10 | `6_2_Case_Q`, `3_3_Case_LJQ`, `3_1_Case_J`, `3_4_Case_LJ` |
| 4 | 89 | 5 | `5_4_Lower_Bounds_Gaussian_Isoperimetric_Profile`, `3_0_Variants_Bobkov_Inequality`, `7_0_Proof_Poincare_Inequality`, `4_0_Proof_Poincare_Inequality` |
| 5 | 22 | 0 | `2_2_Proofs_Theorems_1_1_1_5_1_7`, `Thm_1_1`, `2_0_Envelope_Functions`, `Thm_1_6` |

## Task 1 — Preparation (shared foundations)

Everything that at least two of Tasks 2–4 need, with all its prerequisites: the shared part of the calculus of $L_\beta$, $Q_\beta$ ([DIR] §5.2–§5.3), basic facts on $I$, $J_w$, $J$ ([DIR] §3: existence/uniqueness of $J$, (3.4), $w_0$, $x_0$, Lemma 3.2, $J(\frac12)=\frac12$, the convexity inequality `convex_sub_ge`), Lemma 6.7 ([DIR] §6.3) and the $y=\frac12$ part of Case $QJQ$ ([DIR] §6.5), which both [DIR] §6 and [DIRX] §3 use. Small on purpose, so that Tasks 2–4 can start early.

56 theorems (0 computer-verified):

- `Isoperim/DIR/2_Envelope_Functions/Definitions.lean` (1): `Q_spec`
- `Isoperim/DIR/3_Variants_Bobkov_Inequality/3_0_Variants_Bobkov_Inequality.lean` (13): `I_characterization`, `J_half_eq_L_half`, `Jw_spec`, `convex_sub_ge`, `eqn_3_4`, `existsUnique_J`, `existsUnique_w₀`, `lemma_3_2`, `lemma_3_2_deriv2`, `lemma_3_2_sq_deriv`, `lemma_3_2_sq_deriv2`, `rem_3_6`, `w₀_mem`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_2_Two_Point_Inequalities.lean` (3): `lemma_5_4`, `lemma_5_4_expansion`, `lemma_5_4_taylor`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_3_Properties_L_Q.lean` (26): `eqn_5_2`, `eqn_5_3`, `eqn_5_4`, `eqn_5_5`, `eqn_5_6`, `eqn_5_7`, `eqn_5_8`, `eqn_5_9`, `lemma_5_6`, `lemma_5_6_2_coeffs`, `lemma_5_6_2_concave`, `lemma_5_6_2_decreasing`, `lemma_5_6_2_log_deriv`, `lemma_5_6_2_values`, `lemma_5_6_3_steps`, `lemma_5_6_4_at_half`, `lemma_5_6_4_dbeta`, `lemma_5_6_4_deriv`, `lemma_5_6_4_formula`, `lemma_5_6_4_quadratic`, `lemma_5_8`, `lemma_5_8_2_dbeta`, `lemma_5_8_2_rewrite`, `lemma_5_8_3_dbeta`, `rem_5_7`, `α₁_pos_iff`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_3_Case_LJQ.lean` (6): `Q_deriv2_monotone_β`, `eqn_6_14`, `lemma_6_7`, `lemma_6_7_deriv2`, `lemma_6_7_eval`, `lemma_6_7_mono`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_5_Case_QJQ.lean` (5): `G_QJQ_y_half_factor`, `G_QJQ_y_half_nonneg`, `p_QJQ_coeffs_pos`, `p_QJQ_monotoneOn`, `p_QJQ_quarter`
- `Isoperim/DIRX/2_Preliminaries/2_2_Properties_J.lean` (1): `JX_contDiff`
- `Isoperim/DIRX/2_Preliminaries/Definitions.lean` (1): `JXw_half_one`

## Task 2 — [DIR] main two-point inequality, remaining cases

[DIR] §6.1 Case $J$, the rest of §6.3 Case $LJQ$, §6.4 Case $LJ$, the rest of §6.5 Case $QJQ$, §6.6 Case $QJ$: the case propositions that assemble into Theorem 2.2 (Case $Q$ is in Task 1).

120 theorems (7 computer-verified):

- `Isoperim/DIR/3_Variants_Bobkov_Inequality/3_0_Variants_Bobkov_Inequality.lean` (1): `eqn_3_6`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_1_Case_J.lean` (19): `J_monotoneOn_antitoneOn`, `caseJ_G₁_mono_β`, `caseJ_I`, `caseJ_II`, `caseJ_II_iff_g_J_2`, `caseJ_II_nonneg`, `caseJ_II_suffices`, `caseJ_I_G₁_ge_g_J_1`, `caseJ_I_neardiag_bound`, `caseJ_I_region_subset`, `deriv_J_x₀`, `eqn_6_1`, `eqn_6_3`, `eqn_6_5`, `iteratedDeriv_three_J`, `iteratedDeriv_two_J`, `nine_div_sixteen_gt_x₀`, `prop_6_1`, `x₀_lt_five_div_eight`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_3_Case_LJQ.lean` (29): `caseLJQ_claim_1`, `caseLJQ_claim_2`, `caseLJQ_claim_3`, `derivs_f_LJQ_1_half`, `eqn_6_13`, `eqn_6_15`, `eqn_6_16`, `eqn_6_17`, `eqn_6_18`, `f_LJQ_1_deriv_β`, `f_LJQ_1_eq`, `f_LJQ_1_ge_min`, `f_LJQ_1_half_deriv2_half`, `f_LJQ_1_half_deriv2_zero_subsingleton`, `f_LJQ_1_half_deriv4`, `f_LJQ_1_half_deriv_half`, `f_LJQ_1_half_endpoints`, `f_LJQ_1_half_nonneg`, `f_LJQ_1_half_y₀`, `f_LJQ_1_half_y₁`, `f_LJQ_1_monotone_or_antitone`, `f_LJQ_1_one_nonneg`, `f_LJQ_3_eq`, `f_LJQ_3_half_concaveOn`, `f_LJQ_3_half_deriv2`, `f_LJQ_3_half_one`, `f_LJQ_3_monotoneOn_β`, `prop_6_6`, `prop_6_6_reduction`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_4_Case_LJ.lean` (47): `J_inv_le_two`, `J_inv_monotoneOn_Ico_x₀`, `L_half_deriv2_monotoneOn_neg`, `L_half_deriv3_nonneg`, `caseLJ_region`, `deriv_J_nonpos`, `eqn_6_19`, `eqn_6_20`, `eqn_6_21`, `eqn_6_22`, `f_LJ_deriv2`, `f_LJ_deriv2_nonpos_iff`, `f_LJ_deriv2_sign_change`, `f_LJ_deriv_monotone_antitone`, `f_LJ_deriv_three_quarters`, `f_LJ_deriv_three_quarters_pos`, `f_LJ_endpoints_nonneg`, `f_LJ_eq`, `f_LJ_ge_min_endpoints`, `f_LJ_nonneg`, `g_LJ_deriv2_eq`, `g_LJ_deriv2_nonpos`, `g_LJ_deriv2_nonpos_of_deriv3`, `g_LJ_deriv2_nonpos_of_le`, `g_LJ_deriv2_quarter_nonpos`, `g_LJ_deriv3_eq`, `g_LJ_deriv3_nonneg`, `g_LJ_diag_deriv2`, `g_LJ_diag_eq`, `g_LJ_diag_nonneg`, `g_LJ_eq`, `g_LJ_nonneg`, `g_LJ_nonneg_of_boundary`, `g_LJ_one_deriv2_nonpos`, `g_LJ_one_nonneg`, `g_LJ_zero_one`, `h_LJ_antitoneOn`, `h_LJ_deriv`, `h_LJ_le_h_LJ_t`, `h_LJ_nonpos`, `prop_6_8`, `prop_6_8_monotoneOn_beta`, `r_LJ_antitoneOn`, `r_LJ_deriv`, `r_LJ_deriv_nonpos_of`, `r_LJ_sub_antitoneOn`, `two_h_LJ_le`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_5_Case_QJQ.lean` (11): `G_QJQ_deriv_y`, `G_QJQ_ge_G_QJQ_half`, `G_QJQ_ge_min`, `G_QJQ_monotone_or_antitone`, `G_QJQ_y_half_eq`, `caseQJQ_region`, `eqn_6_25`, `prop_6_9`, `prop_6_9_of_endpoints`, `two_Q_sub_Q_ge`, `β₁_approx`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_6_Case_QJ.lean` (13): `G₁_J_half_nonneg`, `G₁_nonneg_iff_g_QJ_nonneg`, `caseQJ_G₁_monotoneOn_beta`, `eqn_6_26`, `g_QJ_deriv_x_nonpos`, `g_QJ_deriv_x_nonpos_of_pos`, `g_QJ_half_nonneg_iff`, `g_QJ_nonneg_of_half`, `prop_6_11`, `prop_6_11_mono_beta`, `prop_6_12`, `prop_6_12_stronger`, `two_J_sub_Q_pos`

## Task 3 — [DIRX] two-point inequality (with [DIR] Case $Q$)

[DIR] Case $Q$ (§6.2) with its parts of §5.2–§5.3 (Lemma 5.9 etc.): within [DIR] it is only used by Theorem 2.2 (Task 5), and [DIRX] Case $Q$ *is* [DIR] Case $Q$ at $\beta=\frac12$; then [DIRX] §2.2–§2.3 (properties of $\mathrm J=\mathrm J_{w_1}$, $\gamma$, $x_1$, Lemmas 2.3, 2.4), §3.1–§3.6 (the six cases) and their assembly (2.4), plus $B_w\ge L$ and $b_\beta=Q_\beta\ge L_\beta$ on $[\frac14,\frac12]$.

157 theorems (10 computer-verified):

- `Isoperim/DIR/2_Envelope_Functions/2_2_Proofs_Theorems_1_1_1_5_1_7.lean` (1): `b_eq_Q_ge_L`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_2_Two_Point_Inequalities.lean` (3): `G₁_diag`, `lemma_5_2`, `lemma_5_2_chain`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_3_Properties_L_Q.lean` (12): `lemma_5_9`, `lemma_5_9_1_convex`, `lemma_5_9_1_endpoint`, `lemma_5_9_1_endpoints`, `lemma_5_9_1_max`, `lemma_5_9_1_quarter`, `lemma_5_9_1_quarter_steps`, `lemma_5_9_1_unique_zero`, `lemma_5_9_2_concave`, `lemma_5_9_2_convex`, `lemma_5_9_2_half`, `lemma_5_9_2_quarter`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_2_Case_Q.lean` (57): `R_derivs_one_div_β`, `R_eq`, `caseQ_G₁_L`, `caseQ_I`, `caseQ_II`, `caseQ_III_G_Q_diag`, `caseQ_III_G_Q_quarter`, `caseQ_III_iff_G_Q`, `caseQ_III_iff_f_QIII`, `caseQ_III_min`, `caseQ_III_suffices_f_QIII_0`, `caseQ_II_claim_1`, `caseQ_II_claim_1_iff`, `caseQ_II_claim_1_limit`, `caseQ_II_claim_1_mono`, `caseQ_II_claim_1_subst`, `caseQ_II_claim_2`, `caseQ_II_g_Q_1_eq`, `caseQ_II_g_Q_1_half_concave`, `caseQ_II_g_Q_1_half_deriv2`, `caseQ_II_g_Q_1_half_eq`, `caseQ_II_neardiag_bound`, `caseQ_II_second_difference`, `caseQ_II_y_ge`, `caseQ_II_β₀`, `caseQ_reduction`, `deriv2_f_QIII_0_pos`, `deriv_f_QIII`, `deriv_f_QIII_0_neg`, `deriv_f_QIII_0_neg_Icc_eighth`, `deriv_f_QIII_nonpos`, `deriv_f_QIII_nonpos_iff`, `derivs_f_QIII_1`, `derivs_f_QIII_1_nonpos`, `derivs_f_QIII_2`, `derivs_f_QIII_2_nonpos`, `eqn_6_10`, `eqn_6_11`, `eqn_6_11_eq_p_Q`, `eqn_6_12`, `eqn_6_6`, `eqn_6_7`, `eqn_6_8`, `eqn_6_9`, `f_QIII_0_eq_mul`, `f_QIII_1_nonneg_f_QIII_2_nonpos`, `f_QIII_deriv_eq_sub`, `f_QIII_half`, `f_QIII_nonneg`, `iteratedDeriv_three_f_QIII_0`, `iteratedDeriv_three_f_QIII_0_nonneg`, `lemma_6_4`, `lemma_6_4_denom_pos`, `lemma_6_4_deriv`, `lemma_6_4_of_strictAntiOn`, `lemma_6_4_poly`, `prop_6_2`
- `Isoperim/DIRX/2_Preliminaries/2_1_Reduction_Two_Point_Inequality.lean` (2): `BX_ge_LX`, `eqn_2_4`
- `Isoperim/DIRX/2_Preliminaries/2_2_Properties_J.lean` (5): `JX_concave`, `JX_mono`, `JX_mul_deriv2`, `deriv_JX`, `γX_mem`
- `Isoperim/DIRX/2_Preliminaries/2_3_Properties_L_Q.lean` (1): `lemma_2_3`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_1_Case_J.lean` (18): `FX_deriv`, `FX_deriv2`, `FX_nonneg`, `FX_zero`, `caseJ`, `caseJ_G₁_eq`, `caseJ_I`, `caseJ_II`, `caseJ_II_eval`, `caseJ_I_convex`, `caseJ_I_lower`, `caseJ_I_sq_deriv`, `caseJ_cu`, `caseJ_rhs_nonneg`, `caseJ_sq_iff`, `eqn_3_1`, `eqn_3_2`, `γX_le_two`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_2_Case_Q.lean` (3): `BX_eq_max`, `caseQ`, `caseQ_G₁_max`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_3_Case_LJQ.lean` (23): `G_LJQ_diag_concave`, `G_LJQ_diag_deriv2`, `G_LJQ_diag_eval`, `G_LJQ_diag_nonneg`, `G_LJQ_strictConcave`, `G₂_BX_eq_G_LJQ`, `caseLJQ`, `caseLJQ_II`, `caseLJQ_II_of_boundary`, `eqn_3_3`, `eqn_3_4`, `eqn_3_5`, `eqn_3_6`, `eqn_3_7`, `fX_deriv`, `fX_deriv2_strictConcave`, `fX_deriv2_zero`, `fX_deriv4_neg`, `fX_deriv_eval`, `fX_deriv_half_pos`, `fX_deriv_zero`, `fX_nonneg`, `fX_one_half`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_4_Case_LJ.lean` (15): `G₂_BX_eq_h_LJ`, `caseLJ`, `deriv_LX_JX_anti`, `eqn_3_8`, `gX_deriv`, `gX_deriv_ge`, `gX_deriv_ge_1`, `gX_deriv_ge_2`, `gX_deriv_ge_3`, `gX_half`, `gX_nonneg`, `h_LJ_concave`, `h_LJ_deriv2`, `h_LJ_eq_gX`, `h_LJ_nonneg`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_5_Case_QJQ.lean` (8): `caseQJQ`, `caseQJQ_of_eqn_3_9`, `eqn_3_11`, `eqn_3_12`, `eqn_3_9`, `eqn_3_9_deriv`, `eqn_3_9_half`, `eqn_3_9_low`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_6_Case_QJ.lean` (9): `G₁_BX_eq_h_QJ₂`, `G₁_of_g_QJ`, `caseQJ`, `caseQJ_near`, `eqn_3_13`, `eqn_3_14`, `g_QJ_half`, `g_QJ_half_iff`, `g_QJ_nonneg`

## Task 4 — Gaussian profile, asymptotics, Poincaré propositions, Kahn–Park

[DIR] §3 (Bobkov-type inequalities: Lemma 3.1, Proposition 3.3, Corollary 3.5, the steps of the proof of Theorem 1.6), §5.1 (Hölder), §5.4 (lower bounds for $I$, Corollary 5.12, Lemma 5.13) and the §2.2 facts depending on it ((2.9), $\tilde b=\max(b,\tilde L)$, upper bound of Theorem 1.5, (1.3)), **Proposition 7.1 with its proof and the lemmas for Theorem 1.10** ((7.1), `grad_norm_ge`, `indicator_norms`, `boolean_eq_indicator`; [DIR] §7), [DIRX] (2.6), **(4.1) with its proof and the lemmas for Theorem 1.3** (`norms_indicator`, `bool_eq_indicator`; [DIRX] §4), the **Kahn–Park reduction** ([DIR] Proposition 2.1, `Auto.DIR.prop_2_1`, and its [DIRX] form `Auto.DIRX.kahn_park`; only cited from [KP20] in the papers, so a full proof by induction on $n$ is needed; depends only on definitions), and elementary facts in the `Definitions.lean` files. The derivations of Theorems 1.10 / 1.3 are in Task 5.

89 theorems (5 computer-verified):

- `Isoperim/DIR/1_Introduction/Definitions.lean` (2): `dens_mem_dyadic`, `isoProfile_two_pow_le`
- `Isoperim/DIR/1_Introduction/Thm_1_5.lean` (1): `eqn_1_3`
- `Isoperim/DIR/1_Introduction/Thm_1_6.lean` (1): `isoProfile_half_le_sqrt`
- `Isoperim/DIR/2_Envelope_Functions/2_0_Envelope_Functions.lean` (1): `prop_2_1`
- `Isoperim/DIR/2_Envelope_Functions/2_2_Proofs_Theorems_1_1_1_5_1_7.lean` (5): `Ltilde_twopt`, `b_half_two_pow`, `btilde_eq_max`, `eqn_2_9`, `thm_1_5_upper`
- `Isoperim/DIR/3_Variants_Bobkov_Inequality/3_0_Variants_Bobkov_Inequality.lean` (18): `J_eqn_3_2`, `L_half_eqn_3_1`, `L_half_eqn_3_2`, `M_indicator`, `cor_3_5`, `eqn_3_2`, `eqn_3_2_iff_G₁`, `lemma_3_1`, `proof_thm_1_6_chain`, `prop_3_3`, `prop_3_3_Gc_deriv`, `prop_3_3_Gc_deriv2`, `prop_3_3_Gc_deriv2_ge`, `prop_3_3_Gc_nonneg`, `prop_3_3_reduction`, `prop_3_3_sq_deriv_nonneg`, `prop_3_3_sq_diff`, `prop_3_3_squared`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_1_Small_Exponents_Large_Exponents.lean` (2): `lemma_5_1`, `lemma_5_1_holder`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_4_Lower_Bounds_Gaussian_Isoperimetric_Profile.lean` (24): `J_one_sub`, `cor_5_12`, `eqn_5_10`, `eqn_5_11`, `eqn_5_12`, `eqn_5_12_small`, `lemma_5_13`, `lemma_5_13_case_1`, `lemma_5_13_case_2`, `lemma_5_13_frac_poly_bound`, `lemma_5_13_roots`, `lemma_5_13_u_range`, `lemma_5_13_used`, `prop_5_11`, `prop_5_11_Phi_le`, `prop_5_11_apply_I`, `prop_5_11_eps`, `prop_5_11_eps_small`, `prop_5_11_final`, `prop_5_11_ibp`, `prop_5_11_log_bound`, `prop_5_11_t_bounds`, `prop_5_11_t_formula`, `two_one_sub_εJ`
- `Isoperim/DIR/7_Proof_Poincare_Inequality/7_0_Proof_Poincare_Inequality.lean` (13): `G_P_symm`, `boolean_eq_indicator`, `eqn_7_1`, `eqn_7_2`, `eqn_7_3`, `eqn_7_4`, `grad_norm_ge`, `indicator_norms`, `prop_7_1`, `prop_7_1_case_I`, `prop_7_1_case_III_eq`, `prop_7_1_case_I_chain`, `prop_7_1_case_I_eq`
- `Isoperim/DIRX/1_Introduction/Definitions.lean` (3): `hA_mul_hA_compl`, `sensitivity_indicator`, `sqrt_sensitivity_indicator`
- `Isoperim/DIRX/2_Preliminaries/2_1_Reduction_Two_Point_Inequality.lean` (1): `kahn_park`
- `Isoperim/DIRX/2_Preliminaries/2_2_Properties_J.lean` (5): `I_lower`, `eqn_2_6`, `eqn_2_6_eval`, `eqn_2_6_step`, `εX_monotone`
- `Isoperim/DIRX/4_Proof_Poincare_Inequality/4_0_Proof_Poincare_Inequality.lean` (13): `G_PX_I`, `G_PX_III`, `G_PX_III_anti`, `G_PX_I_lower`, `G_PX_eq_I`, `G_PX_half`, `G_PX_symm`, `bool_eq_indicator`, `eqn_4_1`, `eqn_4_2`, `eqn_4_3`, `g_P₁X_antitone_eval`, `norms_indicator`

## Task 5 — Wrap-up (main theorems and their assembly)

Assembling the pieces:

- [DIR] Theorem 2.2 (from the case propositions of Tasks 1–3), Corollary 2.5 (§2.0), and the remaining steps of the proofs of Theorems 1.1, 1.5, 1.7 (§2.2);
- the final assembly of [DIR] Theorem 1.10 and of [DIRX] Theorem 1.3 (`thm_1_3_of_eqn_4_1`, which needs (2.5));
- [DIRX] (2.5) and the reduction of Theorem 1.1 to (2.4) (§2.1);
- the introduction theorems: [DIR] Thm 1.1, 1.5, 1.6, 1.7, Cor 1.9, Thm 1.10; [DIRX] Thm 1.1, 1.2, 1.3.

22 theorems (0 computer-verified):

- `Isoperim/DIR/1_Introduction/Thm_1_1.lean` (3): `cor_1_9`, `cor_1_9_chain`, `thm_1_1`
- `Isoperim/DIR/1_Introduction/Thm_1_5.lean` (1): `thm_1_5`
- `Isoperim/DIR/1_Introduction/Thm_1_6.lean` (2): `isoProfile_one_asymp`, `thm_1_6`
- `Isoperim/DIR/1_Introduction/Thm_1_7.lean` (1): `thm_1_7`
- `Isoperim/DIR/1_Introduction/Thm_1_10.lean` (1): `thm_1_10`
- `Isoperim/DIR/2_Envelope_Functions/2_0_Envelope_Functions.lean` (2): `cor_2_5`, `thm_2_2`
- `Isoperim/DIR/2_Envelope_Functions/2_2_Proofs_Theorems_1_1_1_5_1_7.lean` (5): `b_lt_Ltilde_imp`, `eqn_1_1_β₀`, `eqn_2_8`, `isoProfile_ge_btilde`, `thm_1_5_lower`
- `Isoperim/DIRX/1_Introduction/Thm_1_1.lean` (1): `thm_1_1`
- `Isoperim/DIRX/1_Introduction/Thm_1_2.lean` (2): `thm_1_2`, `thm_1_2_chain`
- `Isoperim/DIRX/1_Introduction/Thm_1_3.lean` (1): `thm_1_3`
- `Isoperim/DIRX/2_Preliminaries/2_1_Reduction_Two_Point_Inequality.lean` (2): `eqn_2_5`, `thm_1_1_of_eqn_2_4`
- `Isoperim/DIRX/4_Proof_Poincare_Inequality/4_0_Proof_Poincare_Inequality.lean` (1): `thm_1_3_of_eqn_4_1`

## Audit of this split (2026-11-12)

Checked from scratch:
- The statement dependencies were re-extracted from the compiled Lean code. The paper-proof
  dependencies were re-derived by three agents that saw only the TeX sources and the Lean
  statements, not the earlier analysis. The split was checked against the old analysis, the
  fresh one, and their union: **0 violations in each**. Every one of the 444 theorems is in
  exactly one task, and the union dependency graph is acyclic.
- The fresh analysis found two problems, both fixed by moving the item into Task 1:
  `Auto.DIR.J_half_eq_L_half` ($J(\frac12)=\frac12$, needed by Task 2) and
  `Auto.DIR.convex_sub_ge` (needed by Task 3), both previously in Task 4.
- Five forward-order problems under the new dependency edges were fixed: two by reordering
  declarations in [DIR] §6.1, three by adding imports in [DIRX] §4. The repository now satisfies
  strict forward order and has complete imports for the union of all dependencies.
- `automation/proof_dependencies.txt` lists the union of all dependencies with the task of each
  declaration.

## Notes

- Task 3 is the largest because it contains [DIR] Case $Q$, which only [DIRX] §3 (and Task 5) needs;
  keeping Task 1 small lets Tasks 2 and 4 start as early as possible.
- Facts that the paper proofs use but the scaffold does not state yet (`forward_reasoning.md` §4)
  are added (in `*_aux.lean` files) by the task that first needs them; if two tasks need the
  same missing fact, it belongs to Task 1.
- Computer-verified (🚗) claims are proved following the paper with standard axioms only (see
  `AGENTS.md`, rules 3 and 8, and the test on branch `cert-test`, `CertTest/REPORT.md`).
