# Forward reasoning and import structure

Date: 2026-11-12. This replaces the earlier audit report: the project has since been reduced to
what the introduction theorems need and restructured (user request of 2026-11-12, raw entry 4).
Method: analysis of the papers' arguments only (no Lean proofs exist; every claim is `sorry`).

## 1. Dependency data

For each of the 540 remaining declarations we use
- its *statement dependencies*: the definitions/declarations occurring in its statement (for a
  definition: in its body), extracted from Lean; and
- its *proof dependencies*: the claims that the paper's proof of it uses, determined by analysis
  of the papers (one line per theorem; computer-verified (🚗) claims, numerical evaluations,
  citations and claims without proof in the paper have none).

The introduction theorems are the roots: [DIR] Theorems 1.1, 1.5, 1.6, 1.7, 1.10 and
Corollary 1.9; [DIRX] Theorems 1.1, 1.2, 1.3. Everything not reachable from them was removed.

## 2. Import loops: outcome

**Confirmed: there are no import loops, and none are forced.** After the restructuring, the
file graph whose edges are "file A contains a declaration that uses (in its statement or in its
paper proof) a declaration of file B" is acyclic, and every file imports exactly the files
containing the direct dependencies of its declarations (so all proof prerequisites are already
imported, not only the statement prerequisites).

Moving only the introduction definitions (and [DIRX] §2's) into `Definitions.lean` files did
**not** suffice; the simulation on the dependency graph still had loops. Two kinds of further
moves were necessary, and were made:

1. *Elementary claims about the moved definitions* that later files use, whose proofs need
   nothing beyond the definitions, moved into the same `Definitions.lean`:
   `Auto.DIR.dens_mem_dyadic`, `Auto.DIR.isoProfile_two_pow_le` ([DIR] intro);
   `Auto.DIRX.sensitivity_indicator`, `Auto.DIRX.hA_mul_hA_compl`,
   `Auto.DIRX.sqrt_sensitivity_indicator` ([DIRX] intro); `Auto.DIRX.JXw_half_one` ([DIRX] §2).
2. *[DIR] §2 definitions*: §2.0 defines $G^1_\beta,G^2_\beta,G_\beta,L_\beta,Q_\beta,b_\beta,c_0$
   (used by §3, §5, §6) and also states Theorem 2.2 (proved in §6). The same treatment as for
   [DIRX] §2 was applied: `Isoperim/DIR/2_Envelope_Functions/Definitions.lean` now holds these
   definitions, $\tilde b_\beta,\tilde L$ (from §2.2), and `Auto.DIR.Q_spec`.
3. *Claims relocated to the file containing their proof ingredients*:
   `Auto.DIR.existsUnique_J` (stated in §1.3, proved via $J=J_{w_0}$ in §3) and
   `Auto.DIR.J_half_eq_L_half` (§2.2, needs $J(\frac12)=\frac12$) moved into the [DIR] §3 file.
4. *Reuse*: [DIRX] now uses [DIR]'s $L_{1/2},Q_{1/2},G^1_{1/2},G^2_{1/2},G_{1/2}$ (via
   `local notation "L" => Auto.DIR.L (1 / 2)` etc.), `Auto.DIR.Q_spec` and
   `Auto.DIR.I_characterization`; the duplicates `LX`, `QX`, `G₁X`, `G₂X`, `GX`, `QX_spec`,
   `I_characterization` (DIRX) were removed.

The resulting module order (topological, `Isoperim.lean`) is: [DIR] intro definitions → §2
definitions → §3 → §5.3, §5.2 → §6.1–§6.6 → §2.0 (Theorem 2.2, Corollary 2.5) → §5.4 → §2.2 →
§5.1 → Theorems 1.1, 1.5, 1.6, 1.7 → §7 → Theorem 1.10; then [DIRX] intro definitions → §2
definitions → §2.2, §2.3 → §3 → §2.1 ((2.4), (2.5)) → Theorems 1.1, 1.2 → §4 → Theorem 1.3.
Files no longer appear in paper order where the paper states results before proving them (e.g.
the introduction theorem files now come last).

## 3. Forward-reasoning order inside files: outcome

**Confirmed: no forward-reasoning issues remain.** Within each file, declarations were reordered
by a stable topological sort (a declaration moves only when one of its dependencies comes later;
`section Proof_…` blocks move as a unit), i.e. the minimal change: in the typical case a theorem
statement moved after the `section` containing its proof steps. A final check over all 540
declarations found **0 violations**: every statement dependency and every proof prerequisite is
earlier in the same file or in a (transitively) imported file.

Declarations moved within their file (minimal set: the complement of the longest
order-preserving subsequence):

- `Isoperim/DIR/1_Introduction/Thm_1_1.lean`: `cor_1_9_chain`
- `Isoperim/DIR/1_Introduction/Thm_1_6.lean`: `thm_1_6`
- `Isoperim/DIR/2_Envelope_Functions/2_2_Proofs_Theorems_1_1_1_5_1_7.lean`: `eqn_2_8`
- `Isoperim/DIR/3_Variants_Bobkov_Inequality/3_0_Variants_Bobkov_Inequality.lean`: `w₀_mem`, `lemma_3_2`, `prop_3_3`, `rem_3_6`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_1_Small_Exponents_Large_Exponents.lean`: `lemma_5_1_holder`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_2_Two_Point_Inequalities.lean`: `lemma_5_2_chain`, `lemma_5_4`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_3_Properties_L_Q.lean`: `lemma_5_6_2_log_deriv`, `lemma_5_6_4_quadratic`, `lemma_5_6`, `lemma_5_8`, `lemma_5_9_1_quarter_steps`, `lemma_5_9`
- `Isoperim/DIR/5_Auxiliary_Estimates/5_4_Lower_Bounds_Gaussian_Isoperimetric_Profile.lean`: `prop_5_11`, `cor_5_12`, `eqn_5_12`, `lemma_5_13`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_1_Case_J.lean`: `caseJ_I_neardiag_bound`, `caseJ_I_G₁_ge_g_J_1`, `caseJ_I`, `caseJ_II_nonneg`, `prop_6_1`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_2_Case_Q.lean`: `caseQ_II_claim_1`, `eqn_6_8`, `deriv_f_QIII_nonpos`, `f_QIII_nonneg`, `lemma_6_4_denom_pos`, `caseQ_III_iff_G_Q`, `lemma_6_4`, `caseQ_III_min`, `caseQ_III_G_Q_quarter`, `eqn_6_6`, `prop_6_2`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_3_Case_LJQ.lean`: `lemma_6_7`, `caseLJQ_claim_1`, `caseLJQ_claim_2`, `caseLJQ_claim_3`, `prop_6_6`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_4_Case_LJ.lean`: `g_LJ_deriv2_nonpos`, `f_LJ_deriv2_nonpos_iff`, `r_LJ_deriv_nonpos_of`, `r_LJ_antitoneOn`, `prop_6_8`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_5_Case_QJQ.lean`: `g_QJQ`, `G_QJQ_deriv_y`, `two_Q_sub_Q_ge`, `eqn_6_25`, `G_QJQ_y_half_nonneg`, `prop_6_9`
- `Isoperim/DIR/6_Proof_Two_Point_Inequality/6_6_Case_QJ.lean`: `g_QJ_deriv_x_nonpos`, `prop_6_11`
- `Isoperim/DIR/7_Proof_Poincare_Inequality/7_0_Proof_Poincare_Inequality.lean`: `prop_7_1`
- `Isoperim/DIRX/1_Introduction/Thm_1_2.lean`: `thm_1_2_chain`
- `Isoperim/DIRX/2_Preliminaries/2_2_Properties_J.lean`: `JX_contDiff`, `γX_mem`, `eqn_2_6`, `deriv_JX`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_1_Case_J.lean`: `eqn_3_2`, `FX_nonneg`, `caseJ_cu`, `eqn_3_1`, `caseJ`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_2_Case_Q.lean`: `caseQ`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_3_Case_LJQ.lean`: `eqn_3_4`, `caseLJQ_II`, `caseLJQ`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_4_Case_LJ.lean`: `gX_nonneg`, `h_LJ_nonneg`, `caseLJ`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_5_Case_QJQ.lean`: `eqn_3_9`, `caseQJQ`
- `Isoperim/DIRX/3_Proof_Two_Point_Inequality/3_6_Case_QJ.lean`: `eqn_3_13`, `caseQJ_near`, `caseQJ`
- `Isoperim/DIRX/4_Proof_Poincare_Inequality/4_0_Proof_Poincare_Inequality.lean`: `G_PX_III`, `eqn_4_1`

Total: 79 declarations moved within their file.


## 4. Facts used by the paper proofs but not stated in the scaffold

Recorded during the dependency analysis (to be added in the proof phase; see also
`automation/ErrorReport.md`):

- thm_2_2 (2.5) needs the scaling fact G_{1/2}[c B](x,y) >= c G_{1/2}[B](x,y) for 0<c<=1, B>=0 (both G^1 and G^2), to pass from the β=1/2 statements without c_0 (prop_6_2, eqn_6_13, prop_6_6, prop_6_8, prop_6_9, J_eqn_3_2) to c_0·b_{1/2}; this is implicit in the paper and not stated in the scaffold.
- thm_2_2 needs monotonicity of β ↦ G^1_β[B](x,y) (i.e. β ↦ ((y-x)^{1/β}+B(y)^{1/β})^β increasing) in general, to pass from G^1_{1/2} to G^1_{β₀} in Case J for x >= x₀ (J_eqn_3_2 / Cor 3.5) and in Case QJQ (prop_6_9 gives G^1_{1/2}[b_β] >= 0). Only region-specific versions exist (caseJ_G₁_mono_β for β₀ <= β, caseQJ_G₁_monotoneOn_beta); a general lemma is not stated. Also the conversion G_QJQ >= 0 => G^1_{1/2}[b_β] >= 0 on the QJQ region is not stated.
- existsUnique_J: the uniqueness of the solution of J''J=-2, J(1/2)=1/2, J(1)=0 is not argued in the paper and not stated anywhere; existence also needs smoothness of I (hence J_w) on (0,1), which is not stated as a claim (also used in cor_3_5, eqn_3_4).
- cor_3_5 needs J_w' <= 0 on [1-w/2,1] (I decreasing on [1/2,1]); the scaffold only has this inside rem_3_6 (whose failure part is unproved), so rem_3_6 is listed as prerequisite. Likewise prop_7_1_case_III_mono uses the sign/monotonicity of J_{w₀}' from rem_3_6 and Jw_spec.
- prop_5_11 needs that every x in (0,1/5] is of the form |t|^{-1}φ(t) for some t<0 (surjectivity/continuity of t ↦ |t|^{-1}φ(t)); not stated.
- lemma_5_13_roots relies on Descartes' rule of signs for generalized polynomials ([Jam06]), cited and not stated in the scaffold; eqn_5_12_small is only justified by "the same argument" in the paper.
- eqn_1_5 for β in (β₀,1] and |A|>1/2 depends on rem_1_8, which has no proof in the paper; thm_1_10 for p>2β₀ is not argued in the paper (see docstrings); these gaps remain.
- cor_2_5, isoProfile_ge_btilde, btilde_eq_max, b_lt_Ltilde_imp need b_β >= 0 on [0,1]; Q_β >= 0 comes from lemma_5_8 and J >= 0 from eqn_3_4 (J = J_{w₀} >= 0); the paper does not argue this explicitly.
- twopt_iSup, envelope_twopt: the paper only says "the same holds for the supremum"; no general sup version of lemma_5_2 exists in the scaffold.
- Tight-lower-bound claims in these files (g_JL_lo_tight, g_P_2_lo_tight, g_P_3_lo_tight) are given empty lists and are not used as prerequisites; the 🚗 claims eqn_5_11, eqn_7_3, eqn_7_4 (and §6 eqn_6_13, prop_6_12) have no prerequisites.
- Positivity of J (J > 0 on [1/2,1), J >= 0 on [1/2,1]) is used throughout §6 (caseJ_I_neardiag_bound via Lemma 5.4's hypothesis B(x+h)>0, iteratedDeriv_two_J (J''=-2/J), f_LJ_deriv2_nonpos_iff, r_LJ_*, h_LJ_*, J_inv_*, caseJ_II_iff_g_J_2, ...) but is stated nowhere in the scaffold (only h_LJ_nonpos states J>0 on [3/4,1)). It follows from J_monotoneOn_antitoneOn + existsUnique_J (J(1/2)=1/2, J(1)=0) only non-strictly; a lemma `J_pos : ∀ x ∈ Ico (1/2) 1, 0 < J x` (e.g. from eqn_3_4/J_one_sub and I > 0) should be added and used by these claims.
- caseJ_II_suffices needs (a) monotonicity of β ↦ G₁ β B x y between β=1/2 and β=β₀ (caseJ_G₁_mono_β only compares β₀ with β ≥ β₀) and (b) G₁ (1/2) (c•J) x y ≥ c·G₁ (1/2) J x y for 0<c≤1. Neither is stated in the scaffold. The same "monotonicity in β and c" facts are needed for prop_6_12_stronger (passing from g_QJ_2 ≥ 0, i.e. β=1/2, c=1, to β₀ and to c₀) and are behind caseJ_G₁_mono_β, caseQJ_G₁_monotoneOn_beta (both assertions without proof in the paper, hence empty lists).
- caseJ_II_nonneg (2J((x+y)/2) - J(x) ≥ 0) is asserted without proof in the paper (empty list); a proof needs concavity of J (deriv_J_x₀) and J(y) ≥ 0. Similarly two_J_sub_Q_pos is asserted without proof (needs e.g. J ≥ 1/2 on [1/2,x₀] (cf. J_inv_le_two), J decreasing after x₀, bounds on Q_β(x) ≤ 1/2).
- caseJ_I covers x = 1/2, but caseJ_I_G₁_ge_g_J_1 and eqn_6_3 require x > 1/2; the endpoint follows by continuity of J on [1/2,1] (from existsUnique_J), hence the existsUnique_J dependency.
- caseJ_I_G₁_ge_g_J_1 follows from caseJ_I_neardiag_bound by algebra alone because E_J is defined as the exact Taylor remainder; caseJ_I_taylor (Lagrange form) is then only needed to justify lower bounds (g_J_1_lo_le) and becomes unreachable, as do iteratedDeriv_five_J, iteratedDeriv_six_J, iteratedDeriv_three_five_J_sign, absDJ_enclosure, eqn_6_2 (the latter two appear only as deps of tight-lower-bound claims). Likewise g_QJ_deriv_x is not needed by g_QJ_deriv_x_nonpos because eqn_6_26 is stated directly for -β ∂ₓ g_QJ; it is only a dep of g_QJ_1_tightLowerBound.
- caseQ_II_claim_2 is listed with only eqn_6_8, but eqn_6_8 is stated for g_Q_1_lo (the lower-bound function), so caseQ_II_claim_2 also needs the lower-bound-validity claim caseQ_II_claim_2_lo (not listed per the rules). When the §4 framework is removed, eqn_6_8 should be restated directly as `∀ y ∈ Icc (1/4) (1/2), g_Q_1 (1/2) (1/4) y > 0.001` (🚗), or caseQ_II_claim_2_lo must be kept.
- lemma_6_4, second claim (∂_h G_{Q,β}(1/4,y) > 0, i.e. p_Q β y (1/4) > 0) is not argued in the paper and is not stated anywhere in the scaffold; it is needed by caseQ_III_min. A 🚗 claim `p_Q β y (1/4) > 0` for y ∈ [1/4,1/2], β ∈ {β₀,1/2} (plus eqn_6_11, eqn_6_11_eq_p_Q, lemma_6_4_denom_pos to transfer the sign) should be added.
- deriv_f_QIII_0_neg_Icc_eighth (not in paper) needs f_{β,0}''' ≥ 0 on [1/8,1/2] and f_{β,0}''(1/8) > 0, which are stated nowhere (the scaffold's iteratedDeriv_three_f_QIII_0_nonneg, deriv2_f_QIII_0_pos, derivs_f_QIII_* only cover [1/4,1/2]); those helper claims should be extended to [1/8,1/2] and an evaluation f_{β,0}''(1/8) > 0 added.
- lemma_6_7 for β ∈ [log₂(3/2), 1] ("analogous" in the paper) has no scaffold support: lemma_6_7_mono assumes β < log₂(3/2) (α₁ > 0); the case α₁ ≤ 0 needs a separate monotonicity statement.
- f_LJQ_1_one_nonneg (case β=1 of claim (1)), f_LJQ_1_half_deriv_half, caseQ_II_g_Q_1_pos (general β), f_LJQ_3_monotoneOn_β, prop_6_8_monotoneOn_beta, caseQJ_G₁_monotoneOn_beta, caseJ_G₁_mono_β have no proof in the paper (empty lists); the β-monotonicity ones need "L_β(x) increasing in β for x ≤ 1/4" and J ≥ 0, which are not stated in the scaffold.
- g_LJ_deriv2_quarter_nonpos uses J_inv_monotoneOn_Ico_x₀ (and J_inv_le_two/eqn_6_19 for (1/4+y)/2 < x₀), not the paper's J_inv_monotoneOn (which is used by no claim and becomes unreachable).
- Positivity of the Gaussian isoperimetric profile, I(x) > 0 on (0,1), is not stated anywhere in DIRX or DIR. Auto.DIR.I_characterization only gives the boundary values and I*I''=-1. It is used for J_w(1/2)=1/2 (it needs I(1/(2w)) != 0) in JXw_half_one, for B_w >= 0 on [1/2,1] with general w in thm_1_1_of_eqn_2_4 (the w1 case is covered by JX_concave in eqn_2_5), and for J >= 0 in JX_concave.
- Symmetry of I about 1/2 (I(x)=I(1-x), I'(1/2)=0) is not stated. It is used for J'(x1)=0 in deriv_JX, which then gives JX_mono.
- Smoothness of I on (0,1) is not stated anywhere. JX_contDiff therefore has no prerequisites ("implicit in the paper"). Most derivative computations depend on it.
- eqn_3_4 cites [DIR, Lemma 6.7] (Auto.DIR.lemma_6_7). That statement only gives strict concavity, of DIR's G_LJQ beta, which contains DIR's J and not DIRX's J; the x-dependence is the same. The second-derivative formula and the strict negativity in (3.4) are shown in the proof of Lemma 6.7: Auto.DIR.lemma_6_7_deriv2, Auto.DIR.eqn_6_14, Auto.DIR.lemma_6_7_mono, Auto.DIR.lemma_6_7_eval.
- The DIR citations at beta=1/2 need DIR's L beta, Q beta and G beta at beta=1/2 to match LX, QX, G1X/GX. No Lean lemma states this identification. The citations involved: lemma_5_6 -> lemma_2_3, lemma_5_8 -> lemma_2_4, lemma_5_9 -> BX_ge_LX and BX_eq_max, prop_6_2 -> caseQ_G1_max, G_QJQ_y_half_nonneg -> eqn_3_9_half, two_Q_sub_Q_pos_mono -> QJQ_monotone, prop_2_1 -> kahn_park.
- kahn_park follows from Auto.DIR.prop_2_1 (beta=1/2) only together with the definitional fact that E sqrt(h_A) >= Bellman_{1/2}(|A|). That fact is not a separate claim.
- Wherever B_w(1/4) occurs, gluing L and Q there uses L(1/4) = 2^{-3/2} = Q(1/4). The Q value comes from QX_spec and the L value is a direct computation; no separate claim states it. Gluing Q and J at 1/2 uses Q(1/2) = 1/2 = J(1/2) (QX_spec, JXw_half_one).
- thm_1_3, equality case for a half-cube: the paper gives no proof. It is a direct computation via norms_indicator (with |A| = 1/2, h_A = 1 on A and h_{A^c} = 1 on A^c); no separate claim states it.
- fX_deriv_zero also needs fX_deriv_half_pos (f'(1/2) > 0). This is the gap-fix recorded in the scaffold; it is a single evaluation and has no prerequisites.
- Some claims are used only to justify tight lower bounds or interval enclosures, so they will become unreachable from Thm 1.1-1.3. They are: QJQ_monotone, deriv_QX_pos, JX_mul_deriv_anti, JX_mul_deriv_deriv, deriv_JX_sq_convex, deriv_JX_sq_sub_γX, JX_one_sub_mono, deriv_JX_one_sub_mono, h_P₂_eq, eqn_2_7, absDJX_encl, x₁_eq, and through them Auto.DIR.two_Q_sub_Q_pos_mono.

### Additional notes from the independent re-analysis (2026-11-12)

- thm_2_2 / cor_2_5 / isoProfile_ge_btilde need J >= 0 on [1/2,1] (b_beta >= 0, and the hypothesis 0 <= B y of eqn_3_2_iff_G₁ for B = J); no Lean theorem states J >= 0 (derivable from J_monotoneOn_antitoneOn + J(1)=0, or from eqn_3_4 and I >= 0).
- thm_2_2 second part (c0 = 0.997) in cases Q, LJQ, LJ, QJQ: the paper only proves the beta=1/2 statements for b_{1/2}; passing to c0*b_{1/2} needs the scaling fact G_{1/2}[c*B] >= c*G_{1/2}[B] for 0<c<=1 (stated nowhere).
- thm_2_2 case QJQ: prop_6_9 gives G_QJQ (the beta=1/2 form of G^1) for beta=beta0; passing to G^1_{beta0}[b_{beta0}] needs the general monotonicity of ((y-x)^{1/beta}+B^{1/beta})^beta in beta (stated only for special B as caseJ_G₁_mono_β, caseQJ_G₁_monotoneOn_beta).
- b_eq_Q_ge_L, thm_2_2 (case Q, via lemma_5_9), cor_2_5/btilde_eq_max (via lemma_5_8) need beta0 < log2(3/2); this numerical fact is stated nowhere.
- prop_5_11 needs that every x in (0,1/5] is of the form |t|^{-1}phi(t) for some t<0 (surjectivity/IVT); stated nowhere.
- existsUnique_J: the paper never proves uniqueness of J (nor smoothness/continuity of I needed for existence via J_{w0}); deps listed cover existence only. eqn_3_4 likewise relies on that uniqueness.
- Lemma 5.3 ([DIR] lem:GLvsGR, G_beta = G^1 iff y-x <= B(y)) has no Lean statement in 5_2_Two_Point_Inequalities.lean (not needed by the listed proofs).
- thm_1_10: the paper's §7 argument only yields p = 2*beta0 and p = 1 (with 0.997); the range p > 2*beta0 is not argued (gap already documented in the docstring).
- thm_1_1 equality case for subcubes and isoProfile_two_pow_le are direct computations with no prerequisites.
- J >= 0 on [1/2,1] and J > 0 on [1/2,1) are used throughout (rpow manipulations, J'' = -2/J < 0, Lemma 5.4 needs B(x+h) > 0, monotonicity in beta / in c) but are stated as no Lean theorem; they are derived from J_monotoneOn_antitoneOn + J_half_eq_L_half (J(1/2)=1/2) + existsUnique_J (J(1)=0, J''J=-2 so J != 0 on (1/2,1)) + eqn_3_6 (1/2 <= x0 <= 1). That bundle is listed wherever positivity of J is needed.
- Monotonicity of beta -> ((a)^(1/beta) + (b)^(1/beta))^beta for a,b >= 0 (l^p-norm monotonicity), used for "by monotonicity in beta" in caseJ_G₁_mono_β, caseJ_II_suffices, caseQJ_G₁_monotoneOn_beta, prop_6_12_stronger, is not stated as a Lean theorem (lemma_5_1 is a different, Hoelder-type statement).
- Smoothness/continuity of J on (1/2,1) / [1/2,1] is taken from existsUnique_J (IsJ J); smoothness of J_{w0} near 1/2 and on (1-w0,1) (used for one-sided derivatives at 1/2, f_LJ_deriv_three_quarters, g_QJ, g_QJ_2) is not stated anywhere (Jw_spec only gives the ODE).
- Lemma 5.3 (GLvsGR) and Remark 5.5 (concavity of B) of the paper are not formalized; neither is needed as a direct prerequisite of a §6 theorem.
- caseJ_II_nonneg (2J((x+y)/2) - J(x) >= 0) and two_J_sub_Q_pos ("Observe 2J((x+y)/2) - Q(x) > 0") are asserted without proof in the paper; f_LJQ_1_one_nonneg ("the case beta=1 being very similar") has no proof given: listed with no prerequisites.
- lemma_6_4: only the first claim is proved in the paper (via lemma_6_4_of_strictAntiOn and eqn_6_12); the second claim d/dh G_Q(1/4,y) > 0 has no proof and no Lean prerequisite.
- deriv_f_QIII_0_neg_Icc_eighth is not in the paper; its sketched proof needs f_{beta,0}''' >= 0 on [1/8,1/4] and f_{beta,0}''(1/8) > 0, which are stated nowhere (derivs_f_QIII_1/2*, iteratedDeriv_three_f_QIII_0* and deriv2_f_QIII_0_pos are only stated on [1/4,1/2]). Because the Lean reduction caseQ_III_suffices_f_QIII_0 needs [1/8,1/2], deriv_f_QIII_nonpos uses deriv_f_QIII_0_neg_Icc_eighth rather than the paper's deriv_f_QIII_0_neg (which is then used by no §6 theorem).
- f_LJQ_1_half_deriv_half (not in the paper) is a single numerical evaluation of a one-sided limit, so it has no prerequisites; eqn_6_9, eqn_6_10, eqn_6_15, eqn_6_16, eqn_6_18, eqn_6_19, eqn_6_20, eqn_6_21, eqn_6_22, p_QJQ_quarter, p_QJQ_coeffs_pos, β₁_approx are single evaluations (no prerequisites); eqn_6_3, eqn_6_5, eqn_6_7, eqn_6_8, eqn_6_12, eqn_6_13, eqn_6_17, eqn_6_25, eqn_6_26, prop_6_12 are computer-verified (no prerequisites); caseQ_G₁_L is the [BIM23, Lemma 2.2] citation (no prerequisites).
- lemma_6_7: the paper treats only beta < log2(3/2) (lemma_6_7_mono assumes it) and says the case beta in [log2(3/2),1] is "analogous"; no Lean statement covers that case.
- Q_deriv2_monotone_β is derived from eqn_5_7 (lemma_5_8_3_dbeta only covers x <= 1/2). lemma_6_4_denom_pos and two_Q_sub_Q_ge use concavity of Q_beta outside [0,1/2] (y-h may be < 0; y up to 3/4), which Lemma 5.8 does not cover; eqn_5_7 (+ eqn_5_5, α₁_pos_iff) supplies it.
- g_LJ_deriv2_quarter_nonpos: the paper argues via "J^{-1} increasing on [3/4,1]", but the relevant argument (1/4+y)/2 lies in (1/2,5/8]; a correct proof splits at x0 using J_inv_le_two/eqn_6_19 below x0 and J_inv_monotoneOn_Ico_x₀/eqn_6_20 above.
- caseQ_I/caseQ_reduction: the paper cites Lemma 5.2; the pointwise form actually needed on a sub-triangle is lemma_5_2_chain, so both are listed.
- Lemma 2.4 ([Q] of DIRX: Q>=0, Q'>0, Q''<0 on [0,1/2]) has no Lean statement in Isoperim/DIRX; its uses (B_w>=0 in thm_1_1_of_eqn_2_4/eqn_2_5) are mapped to Auto.DIR.lemma_5_8 at beta=1/2. Its other uses (tight lower bounds of (3.11), (3.13), (4.3)) are inside computer-verified claims.
- Positivity of the Gaussian profile I on (0,1) (hence J_w>0 on [1/2,1), J_w>=0, I(1/(2w))>0) is used repeatedly (JXw_half_one, thm_1_1_of_eqn_2_4, eqn_2_6_step, JX_concave, deriv_JX, caseJ_I_sq_deriv, caseJ_II, fX_deriv4_neg, h_LJ_deriv2, FX_deriv2) but is stated nowhere in Lean (Auto.DIR.I_characterization gives only I(0)=I(1)=0 and I*I''=-1); JX_concave's second conjunct (J>=0) only covers non-strict nonnegativity on [1/2,1]. Continuity of I at 0 and 1 (needed for JX_contDiff's ContinuousOn part) is likewise not stated; smoothness on (0,1) can be bootstrapped from I_characterization.
- The tight-lower-bound justifications of the computer-verified claims rely on facts stated nowhere as separate Lean theorems: for (3.11) that 2Q((x+y)/2)-Q(x) is positive/increasing in y/decreasing in x ([DIR] §6.5; only partially Auto.DIR.two_Q_sub_Q_ge), Q'(33/64)>0, and that J*J' is decreasing on [1/2,3/4] via (J*J')'=(J')^2-gamma<-1 (convexity of (J')^2 from [DIR] Lemma 3.2 plus endpoint evaluations); for (3.3),(3.7),(3.8),(3.13),(3.14),(4.2),(4.3) the J/|J'| interval enclosures of (2.7) (from JX_mono, deriv_JX) and J(1-x) increasing for x<=1/4 (from JX_mono). Per the rules these 🚗 claims are listed with no prerequisites.
- eqn_3_4 is cited from [DIR, Lemma 6.7], but Auto.DIR.lemma_6_7 states only strict concavity, which does not give pointwise strict negativity of the second derivative; the strict inequality comes from the proof components Auto.DIR.lemma_6_7_deriv2, Auto.DIR.eqn_6_14, Auto.DIR.lemma_6_7_mono, Auto.DIR.lemma_6_7_eval (at beta=1/2), which are listed along with lemma_6_7. DIR's G_LJQ uses DIR's J, but the J term does not depend on x, so these transfer to G_LJQX.
- [DIR] Lemma 3.2 (Auto.DIR.lemma_3_2) is stated for I*I''=-1; applying it to J (J*J''=-gamma) needs the rescaling J/sqrt(gamma), which is not stated as a separate lemma. J'(x_1)=0 in deriv_JX is taken from Auto.DIR.rem_3_6 (J_w'(1-w/2)=0 for DIR's J_w = sqrt2*w*I(w^-1(1-x))) via JX = const*Auto.DIR.Jw w_1; this rescaling is not stated either.
- Single numerical evaluations are given no prerequisites, although evaluating derivatives needs the derivative formulas: eqn_3_6 and fX_deriv_half_pos/fX_deriv_eval would use fX_deriv (stated only on the open interval (1/2,1), while eqn_3_6 and fX_deriv_half_pos evaluate at y=1/2), and caseJ_II_eval / gX_deriv_ge_* constants would use JX_mul_deriv2/gX_deriv. g_P₁X_antitone_eval and εX_monotone (monotonicity asserted without proof in the paper) also have none.
- bool_eq_indicator and norms_indicator are proved in DIRX without citation; the listed Auto.DIR.boolean_eq_indicator, Auto.DIR.indicator_norms, Auto.DIR.eqn_7_1 (p=1) are the identical facts stated in DIR §7. The equality case of thm_1_3 (half-cubes) has no proof in the paper; norms_indicator is listed for it. The sensitivity inequality (1.4) is not stated as a Lean theorem, so the sensitivity facts have no downstream users.
