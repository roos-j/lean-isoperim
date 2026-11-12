# Error report: discrepancies between [DIR]/[DIRX] and the formalization

Timestamps: local time of the computer (UTC).

- 2026-11-11T19:00+00:00 — [DIR] §1.4, after Corollary 1.9: "Kahn and Park proved this with
  $\log_3(\frac32)\approx0.585$". $\log_3(3/2)\approx0.369$; the value $0.585$ is
  $\log_2(3/2)$. Resolved: `DIR.cor_1_9_kahn_park` uses $\log_2(3/2)$ (typo repair).
- 2026-11-11T19:00+00:00 — [DIR] §3: "$I$ is also characterized by $I(0)=I(1)=0$,
  $I\cdot I''=-1$". Without nonnegativity this fails ($-I$ satisfies the same conditions).
  Resolved: `DIR.I_characterization` adds the implicit hypothesis $g\ge0$.
- 2026-11-11T19:00+00:00 — [DIR] §6 equation numbering: the PDF has no equation (6.4) (counter
  artifact of the `\auto` tag together with `\eqref` in the caption of Figure 5). Lean names
  follow the PDF numbers. Not a mathematical discrepancy.
- 2026-11-11T19:00+00:00 — [DIR] proof of Lemma 5.4: the Taylor remainder is written
  $-\frac12\beta(1-\beta)\tilde a^2$; the Lagrange form is
  $-\frac12\beta(1-\beta)(1+\tilde a)^{\beta-2}a^2$. The paper's bound $E_1\le\frac12\beta(1-\beta)
  B^{1-2/\beta}h^{2/\beta}$ is unaffected. Resolved: `DIR.lemma_5_4_taylor` and
  `DIR.lemma_5_4_expansion` use the Lagrange form; Lemma 5.4 itself is unchanged.
- 2026-11-11T19:00+00:00 — [DIR] Remark 2.4 "Failure for smaller values of $\beta_0$ occurs at
  $x=\frac12$ and $y>\frac12$" is formalized as the existence of a failure point
  $(\frac12,y)$, $y>\frac12$, at $\beta=\frac12$ (interpretation; `DIR.rem_2_4_failure`).
- 2026-11-11T19:14+00:00 — [DIR] §6.5, item 2: "$2Q_\beta(\frac{x+y}2)-Q_\beta(x)$ is increasing in
  $y$" fails on the full rectangle $[\frac14,\frac12]\times[\frac12,\frac34]$ (needs
  $\frac{x+y}2\le\frac12$, e.g. $Q'_{1/2}(\frac58)<0$). The stated tight lower bound for $g_{QJQ,\beta}$
  and (6.25) may therefore be unjustified on the part with $x+y>1$ (irrelevant to Case $QJQ$).
  Unresolved: `DIR.two_Q_sub_Q_pos_mono` is stated for $y\in[\frac12,1-x]$;
  `DIR.g_QJQ_tightLowerBound` is stated on the full rectangle as in the paper (possibly false there).
- 2026-11-11T19:14+00:00 — [DIR] §6.6 (6.26), (6.27) and their tight lower bounds evaluate $J$ at
  points $<\frac12$; there $J$ must mean $J_{w_0}$ (3.4). Resolved: these statements assume
  `hJ : EqOn J (Jw w₀) (Icc (1 - w₀) 1)` (to be revisited in the proof phase, e.g. by restating with
  `Jw w₀`).
- 2026-11-11T19:14+00:00 — [DIR] §6.6.1: Proposition 6.11 omits $x+y\ge1$ (in the subsection
  title); added as hypothesis. The Partition₂ rectangle $[\frac14,\frac12]\times[\frac12,\frac58]$ is
  kept as written although the triangle has $x\ge\frac38$.
- 2026-11-11T19:14+00:00 — [DIR] §6.4: "$J^{-1}$ is increasing on $[\frac34,1]$" is true but the
  argument needs $J^{-1}$ increasing on $[x_0,\frac58]$; both stated. Pointwise derivative claims
  for $J$ are stated on open domains or with one-sided `derivWithin` at $\frac12$.
- 2026-11-11T19:16+00:00 — [DIR] §6.1.1: $\underline{g_{J,1,\beta,c}}$ bounds $E_6$ over a
  non-shrinking interval, so it is a lower bound but not tight in the sense of §4.1. Resolved:
  only the lower-bound property is stated (`g_J_1_lo_le`). Derivative claims on $J$ assume $x>\frac12$.
- 2026-11-11T19:16+00:00 — [DIR] §6.2.1: $g_{Q,1,1/2}(0,y)$ uses $h^{-1/\beta}$ at $h=0$; stated via
  the limit $h\to0^+$ (continuous extension). Same for $f''_{1/2}(\frac12)$ in §6.3.2.
- 2026-11-11T19:16+00:00 — [DIR] §6.2.2: $\beta yf'_\beta(y)=f_{\beta,0}(y)-f_{\beta,0}(y/2)$ needs
  $f_{\beta,0}'\le0$ on $[\frac18,\frac12]$, the paper shows it on $[\frac14,\frac12]$ (true
  numerically). Lemma 6.4's claim $\partial_hG_{Q,\beta}(\frac14,y)>0$ is not argued in the paper.
  Unresolved gaps (not errors in statements); reduction stated on $[\frac18,\frac12]$.
- 2026-11-11T19:16+00:00 — [DIR] Proposition 6.6: hypothesis $x+y\le1$ (standing assumption of Case
  $LJQ$) added. §6.3.2 proof of (1) also needs $f'_{1/2}(\frac12^+)\ge0$ (≈0.058). §6.3.1 runs
  Partition₂ only for $\beta=\frac12$ but claims (6.13) for $\beta\in\{\beta_0,\frac12\}$ (likely
  typo). $\underline{g_{LJQ,2}}$ is not termwise monotone for $\overline\beta$ near 1 (unverified).
- 2026-11-11T19:26+00:00 — [DIRX] Remark 2.2 cites "[DIR24, Thm. 1.6]": this is the numbering of [DIR] arXiv v1; in
  v2 it is Theorem 1.7 (`Auto.DIR.thm_1_7`). Noted in a comment.
- 2026-11-11T19:26+00:00 — [DIRX] §3.3 Case II and §3.6.1: hypotheses $x+y\le1$ resp. $x+y\ge1$ (standing
  assumptions of the cases, needed for $B_w(\frac{x+y}2)$ to be the stated piece) added.
- 2026-11-11T19:26+00:00 — [DIRX] §5: the $O(np)$ error in $\sqrt{1-(T_\rho f)^2}=2\sqrt{p(1-p)}\sqrt{s_f}+O(np)$
  needs $p\lesssim n^{-2}$ (otherwise the error is $O(n^2p^{3/2})$); stated for
  $p\in(0,1/(2n^2)]$ with an absolute constant. Irrelevant to the limit $p\to0^+$ at fixed $n$.
- 2026-11-11T19:26+00:00 — [DIRX] §1: the Bobkov–Götze bound is not given explicitly; formalized as
  $\mathbf{E}\sqrt{h_A}\ge\sqrt3|A|(1-|A|)$ (from [DIR] §1.2). The Hellinger conjecture is
  stated only for balanced $f$ as in §5; Courtade–Kumar in its standard mutual-information form.

## Audit round 2 (2026-11-11, after user request of 22:51 UTC)

Entries above remain as historical record; where an audit-2 entry revises an earlier one, the later entry controls (e.g. the [DIRX] §5 $O(np)$ range entry is withdrawn, see [DIRX] below). Every entry below also has a `**Discrepancy with the paper.**` paragraph (or a Lean-fix note) at the named declaration.

### [DIR] §1–§3

Files: `Isoperim/DIR/1_Introduction/*.lean`, `Isoperim/DIR/2_Envelope_Functions/*.lean`,
`Isoperim/DIR/3_Variants_Bobkov_Inequality/3_0_Variants_Bobkov_Inequality.lean`.
Each item has a `**Discrepancy with the paper.**` paragraph in the docstring of the named
declaration.

#### Existing entries (re-checked; Discrepancy paragraph added/rewritten at the place)

- 2026-11-11 — [DIR] §1.4, after Corollary 1.9: "Kahn and Park proved this with
  $\log_3(\frac32)\approx0.585$". $\log_3(\frac32)\approx0.369$ (an exponent $<\frac12$ would even
  contradict the conjectured optimality of $0.5$); $0.585\approx\log_2(\frac32)$, as in the
  abstract and §1.1. Resolved: `Auto.DIR.cor_1_9_kahn_park` uses $\log_2(\frac32)$ (typo repair).
- 2026-11-11 — [DIR] §3: "$I$ is also characterized by $I(0)=I(1)=0$, $I\cdot I''=-1$". False
  without a sign condition ($-I$ satisfies both). Resolved: `Auto.DIR.I_characterization` assumes
  $g\ge0$ (plus continuity on $[0,1]$, $C^2$ on $(0,1)$) for the competitor $g$.
- 2026-11-11 — [DIR] Remark 2.4: "Failure for smaller values of $\beta_0$ occurs at $x=\frac12$ and
  $y>\frac12$" is informal (which $\beta<\beta_0$? all failure points?); read literally ("for every
  $\beta<\beta_0$") it is not established ($\beta_0$ is only where the computer proof succeeds).
  Interpretation: `Auto.DIR.rem_2_4_failure` = there is $y\in(\frac12,1]$ with
  $G_{1/2}[b_{1/2}](\frac12,y)<0$ (numerically true: $y\approx0.585$, $G^1\approx-3.1\cdot10^{-5}$,
  $G^2\approx-0.22$).

#### New entries

- 2026-11-11 — [DIR] Lemma 3.1: the paper allows any $B:\mathcal I\to\mathbb R$. **False for
  sign-changing $B$**: $\mathcal I=[0,1]$, $S=\{0.1,0.2,0.6,0.9,0.45\}$, $B=0$ on
  $S\setminus\{0.45\}$, $B(0.45)=1$, $B=-2$ off $S$; no two distinct points of $S$ have midpoint in
  $S$, so the $n=1$ case holds, but $f=(0.1,0.2,0.6,0.9)$ on $\{0,1\}^2$ gives
  $B(\mathbf E f)=1>\mathbf E Mf\approx0.34$. The induction ([Bob97, Lemma 1], [BG99, Lemma 2.1])
  needs $B\ge0$; all applications ($L_{1/2}$, $J$) are non-negative. Resolved:
  `Auto.DIR.lemma_3_1` adds `hB : ∀ t ∈ 𝓘, 0 ≤ B t`.
- 2026-11-11 — [DIR] (3.2): for $n=1$ the right side of (3.1) is
  $\frac12\sqrt{(y-x)^2+B(y)^2}+\frac12|B(x)|$, so "(3.1) may be written as (3.2)" needs
  $B(x)\ge0$. Resolved: `Auto.DIR.eqn_3_2` adds `hB : 0 ≤ B (min (f 0) (f 1))` (previously the
  Lean iff was false for $B(x)<0$).
- 2026-11-11 — [DIR] §1.3, (1.5): asserted for all $\beta\in[\beta_0,1]$, but for $|A|>\frac12$
  only proved for $\beta=\beta_0$ (via (1.6)); for $\beta\in(\beta_0,1]$ it rests on Remark 1.8
  (details omitted); Lemma 5.1 does not suffice. Unresolved gap; `Auto.DIR.eqn_1_5` kept as in the
  paper.
- 2026-11-11 — [DIR] Theorem 1.10: (1.7) is claimed for all $p\ge2\beta_0$, but §7 only proves
  $p=2\beta_0$ (from (2.6) at $\beta_0$ and Proposition 7.1, which is for $p/2\in[\frac12,\beta_0]$),
  plus the $p=1$ bound with $0.997$. $p\in(2\beta_0,2]$ would need the omitted Remarks 2.3, 7.2; for
  $p>2$ nothing is said; neither Hölder (Lemma 5.1) nor $h^{p/2}\ge h^{\beta_0}$ reduces it to
  $p=2\beta_0$. Unresolved gap; `Auto.DIR.thm_1_10` kept as in the paper (same for the new
  `Auto.DIR.poincareConstBool_bounds`, "$C_{B,p}=1$ for $p\ge2\beta_0$").
- 2026-11-11 — [DIR] §2.1, after Definition 2.7: "Proposition 2.1 implies
  $\mathcal B_\beta\ge\mathfrak B_\beta$", but Proposition 2.1 assumes (2.2) for all real
  $x\le y$, while $\mathfrak B_\beta$ only satisfies it on $\mathcal Q$ (it is $+\infty$ off
  $\mathcal Q$). Needs the dyadic version of Proposition 2.1 (same induction). Resolved: new
  `Auto.DIR.prop_2_1_dyadic` (cited, KP20); discrepancy noted at
  `Auto.DIR.isoProfile_ge_envelope`.

#### Pure Lean fixes (no paper discrepancy)

- `Auto.DIR.Q_spec`: the uniqueness was taken over polynomials satisfying the conditions *and*
  $p=Q_\beta$ (trivial). Now: unique cubic interpolant exists, and every such interpolant equals
  $Q_\beta$.
- `Auto.DIR.expect_hA_rpow_compl_ne`: moved inside the sentence it formalizes (paper order).
- Docstrings: `Auto.DIR.dens` notation `｜A｜`; `Auto.DIR.no_dimension_free_bound` marked as cited
  from [BIM23, §3]; `Auto.DIR.rem_1_2` marked as cited from [DIRX26, Thm 1.1].
- Added implicit claims: `Auto.DIR.poincareConstBool_bounds` (§1.5 sentence before Theorem 1.10),
  `Auto.DIR.prop_2_1_dyadic` (§2.1), `Auto.DIR.isoProfile_ge_btilde` (§2.2, "Theorem 1.7
  follows").

### [DIR] §4, §5, §7

Timestamp: 2026-11-11 (UTC). Each `**Discrepancy with the paper.**` paragraph is in the docstring of
the named declaration.

- [DIR] proof of Fact 4.1 ('only if'): the Heine–Borel argument has a gap. Tightness only
  controls $\underline f(\underline x,\overline x)$ on rectangles that *contain* $x$, but a cell of the
  partition induced by a finite subcover of the $\varepsilon_x/2$-neighborhoods need not contain its
  center, and $\underline f$ is not assumed monotone under inclusion. The claim is still true
  (Cousin's lemma: a $\delta$-fine tagged partition for the gauge $\varepsilon_x$, by bisection).
  Statement unchanged; discrepancy paragraph added. Lean: `Auto.DIR.fact_4_1_only_if`.
- [DIR] §4.1, after Fact 4.1: "Fact 4.1 implies that ... the procedure will always succeed ...
  provided maxDepth is large enough". Fact 4.1 only gives *some* admissible partition, not
  necessarily a dyadic one. The claim is true by a bisection/König's-lemma argument. Statement
  unchanged; discrepancy paragraph added. Lean: `Auto.DIR.partition_succeeds`.
- [DIR] Lemma 5.4: only $B\ge0$ is assumed, but the formula has $B(x+h)^{1-1/\beta}$ and
  $B(x+h)^{1-2/\beta}$ with negative exponents (and the proof divides by $B(x+h)$). Implicit
  hypothesis $B(x+h)>0$ added (it was already in the Lean statement; discrepancy paragraph added).
  Lean: `Auto.DIR.lemma_5_4`.
- [DIR] proof of Lemma 5.4 (existing ErrorReport entry, now documented in place): the remainder
  $-\frac12\beta(1-\beta)\tilde a^2$ is not the Lagrange form
  $-\frac12\beta(1-\beta)(1+\tilde a)^{\beta-2}a^2$. (The paper's literal form is nevertheless true,
  with $\tilde a'=a(1+\tilde a)^{\beta/2-1}\in[0,a]$; the bound on $E_1$ is unaffected.) Lean uses the
  Lagrange form; discrepancy paragraphs added at `Auto.DIR.lemma_5_4_taylor` and
  `Auto.DIR.lemma_5_4_expansion`.
- [DIR] proof of Lemma 5.8 (2): $Q'_\beta(x)>0$ is claimed "for $x\in[0,\frac12]$ and
  $\beta\in[\frac12,\log_2(\frac32)]$" (closed), but at $\beta=\log_2(\frac32)$, $x=\frac12$ one has
  $\alpha_1=0$ and $Q'_\beta(\frac12)=\frac23\alpha_1=0$. Resolved: the Lean statement uses the
  half-open range $[\frac12,\log_2(\frac32))$ of Lemma 5.8 (previously the closed range, i.e. a
  false statement). Lean: `Auto.DIR.lemma_5_8_2_rewrite`.
- [DIR] proof of Lemma 5.8 (2): "$6x^2-6x+1=(x-\frac12-\frac{\sqrt3}6)(x-\frac12+\frac{\sqrt3}6)$" is
  missing the factor $6$ (the right side is $x^2-x+\frac16$). Resolved: Lean states
  $6x^2-6x+1=6(x-\frac12-\frac{\sqrt3}6)(x-\frac12+\frac{\sqrt3}6)$ (previously the false identity
  was stated). Lean: `Auto.DIR.lemma_5_8_2_dbeta`.
- [DIR] proof of Lemma 5.9 (1): "a maximum since $L_\beta'-Q_\beta'$ is increasing on
  $[0,\tilde x]$ and decreasing on $[\tilde x,\frac14]$" is misworded ($L'_\beta-Q'_\beta$ is strictly
  convex and $\to+\infty$ at $0^+$, so not increasing on $[0,\tilde x]$); it is $L_\beta-Q_\beta$ that
  is increasing/decreasing there. Resolved: new declaration `Auto.DIR.lemma_5_9_1_max` states the
  corrected claim (the claim was previously only in the docstring of
  `Auto.DIR.lemma_5_9_1_unique_zero`).
- [DIR] proof of Proposition 5.11, last step: "$\sqrt{1-\varepsilon}\ge1-\varepsilon$ (since
  $\varepsilon\le1$)" also needs $\varepsilon\ge0$ (true there since $(2\pi)^{1/2}|t|>1$). Lean fix:
  hypothesis `0 ≤ ε` added (the previous statement was false for $\varepsilon<0$); noted in the
  docstring. Lean: `Auto.DIR.prop_5_11_final`.
- [DIR] §5.4, proof of Lemma 5.13: uses the upper enclosure $\overline J$ of (6.2), defined only in
  §6.1.1 (forward reference). Resolved: `Auto.DIR.g_JL_lo` writes out the formula of
  $\overline J$ (identical to `Auto.DIR.J_hi`), and the §5.4 file no longer imports the §6.1 file.
- [DIR] (5.11) and the tight lower bound for $-\partial_x^2[J(x)-L_{\beta_0}(1-x)]$ on
  $[\frac12,\frac{2047}{2048}]$: Lean junk issue, since `deriv (deriv J)` at $x=\frac12$ depends on the
  junk values of `J` left of $\frac12$. Resolved: the second derivative is taken of
  $J_{w_0}$ (`Jw w₀`), equal to $J$ on $[\frac12,1]$ by (3.4) and smooth near $\frac12$. Lean:
  `Auto.DIR.eqn_5_11`, `Auto.DIR.g_JL_lo_tight`.
- [DIR] proof of Lemma 5.13: "can have at most two roots" was formalized with `Set.ncard ≤ 2`, which
  is vacuous for infinite sets. Lean fix: `Set.encard ≤ 2`. Lean: `Auto.DIR.lemma_5_13_roots`.
- [DIR] Remark 5.14: speaks of "the zero" of $s\mapsto J(1-s)-L_{\beta_0}(s)$ that "must lie in"
  $[10^{-10^{388}},10^{-10^{387}}]$; uniqueness and absence of zeros in $(0,10^{-10^{388}})$ and
  $(10^{-10^{387}},10^{-10^{380}}]$ are not argued (back-of-the-envelope remark). The previous Lean
  statement claimed absence of zeros in $(0,\frac12)$ outside the interval (stronger than the
  paper). Resolved: Lean states only the sign change ($>0$ at $10^{-10^{387}}$, $<0$ at
  $10^{-10^{388}}$) and the existence of a zero in the interval. Lean: `Auto.DIR.rem_5_14`.
- [DIR] §7, Case II and Case III: $\underline{g_{P,2}}$ and $\underline{g_{P,3}}$ are called "a tight
  lower bound for $G_{P,\beta}$" resp. "for $g_{P,3,\beta}$", but they are lower bounds uniform in
  $\beta\in[\frac12,\beta_0]$ that are tight only for their own diagonal, not for $G_{P,\beta}$ /
  $g_{P,3,\beta}$ for any $\beta$ (e.g. $L_{1/2}$ vs. $L_\beta$, $-2x(1-x)$). Only the lower-bound
  property is needed. Lean (unchanged in substance): uniform lower bound plus
  `IsTightLowerBound₁` of the diagonal; discrepancy paragraphs added. Lean:
  `Auto.DIR.g_P_2_lo_tight`, `Auto.DIR.g_P_3_lo_tight`.
- [DIR] §7, Case III: Lean junk issues. `deriv (G_P β)` is $0$ at $x=\frac14$ (corner where $b_\beta$
  switches from $L_\beta$ to $Q_\beta$) and at $x=\frac12$ (symmetric corner), so (7.4) was false at
  both endpoints; `deriv J` at $\frac12$ (used in $J'(1-x)$, $\overline{|J'|}(1-\overline x,\cdot)$ and
  the diagonal of $\underline{g_{P,3}}$) and at $1$ is junk. Resolved: `Auto.DIR.g_P_3` is
  $-$`derivWithin (G_P β) (Icc (1/4) (1/2))` (one-sided at the endpoints); $J'$ is written
  `deriv (Jw w₀)`; $\overline{|J'|}$ is written out with it in `Auto.DIR.g_P_3_lo` (instead of
  `Auto.DIR.absDJ_hi`); the monotonicity/sign claims on $J'(1-x)$ use $x\in(0,\frac12]$ (excluding
  $J'(1)=-\infty$); `Auto.DIR.g_P_3_formula` now holds on the closed interval $[\frac14,\frac12]$.
  The §7 file now imports §3.0 and §4.1 instead of §6.1.

### [DIR] §6

Timestamps: local time of the computer (UTC). Numerical checks: Python/mpmath, $J=J_{w_0}$ via
$J(x)=\sqrt2w_0\varphi(\Phi^{-1}((1-x)/w_0))$, $w_0\approx0.895769$, $x_0\approx0.552115$.
Each item has a `**Discrepancy with the paper.**` paragraph at the named declaration.

- 2026-11-11T23:25+00:00 — [DIR] §6.1.1, $\underline{g_{J,1,\beta,c}}$ is called a *tight*
  lower bound, but the enclosure of the Taylor remainder $E_6$ uses $J^{(6)}$ on
  $[\underline x,\overline x+\overline h]$, which does not shrink with the rectangle when $h>0$;
  numerically the gap is $\approx2.4\cdot10^{-4}$ for a $10^{-8}$-rectangle at $(0.56,0.1)$. Only the
  lower-bound property holds (checked on random subrectangles for 4 pairs $(\beta,c)$). Resolved:
  `Auto.DIR.g_J_1_lo_le` states only the lower-bound property (unchanged, paragraph added).
- 2026-11-11T23:25+00:00 — [DIR] (6.3): stated on $[\frac12,\frac58]\times[0,\frac3{16}]$; at
  $x=\frac12$ the derivatives $J^{(k)}(\frac12)$ are one-sided (junk for `Auto.DIR.J`). Resolved:
  `Auto.DIR.eqn_6_3` (and `caseJ_I_G₁_ge_g_J_1`, `g_J_1_lo_le`) assume $x>\frac12$; $x=\frac12$ by
  continuity. Numerically $\min g_{J,1}\approx8.5\cdot10^{-5}$ ($\beta_0,1$), $1.7\cdot10^{-4}$
  ($\frac12,c_0$).
- 2026-11-11T23:25+00:00 — [DIR] §6.1, "When $x<x_0$ this estimate fails for $\beta=\frac12$" was
  not formalized. Resolved: new `Auto.DIR.caseJ_G₁_half_fails` (numerically true, e.g.
  $G^1_{1/2}[J](0.5,0.5+0.1702\cdot0.5)\approx-3.1\cdot10^{-5}$).
- 2026-11-11T23:25+00:00 — [DIR] §6.2.1: $g_{Q,1,\frac12}(0,y)$, $g_{Q,1,\frac12}(0,\frac12)=0$
  use $h^{-1/\beta}$ at $h=0$ (continuous extension meant); Lean's `g_Q_1 (1/2) 0 y`
  $=\frac12Q_{1/2}(y)^{-1}$ is not the extension. Resolved: stated as limits $h\to0^+$
  (`caseQ_II_g_Q_1_half_zero`, `caseQ_II_g_Q_1_half_concave`, `caseQ_II_claim_1`); paragraph at
  `Auto.DIR.caseQ_II_g_Q_1_half_zero`. Same for $f''_{1/2}(\frac12)$ in §6.3.2
  (`Auto.DIR.f_LJQ_1_half_deriv2_half`, paragraph added).
- 2026-11-11T23:25+00:00 — [DIR] §6.2.1 "If $\beta>\frac12$, then $g_{Q,1,\beta}>0$" was stated
  only for $\beta_0$. Resolved: `Auto.DIR.caseQ_II_g_Q_1_pos` now takes $\beta\in(\frac12,1]$
  (signature change: new explicit arguments `β hβ`); numerically true for
  $\beta\in\{0.5001,\dots,1\}$; the paper proves only $\beta_0$ (via (6.7)).
- 2026-11-11T23:25+00:00 — [DIR] Lemma 6.4: the claim $\partial_hG_{Q,\beta}(\frac14,y)>0$ is not
  argued (the proof only shows $p_{y,\beta}$ strictly decreasing), but it is needed for
  `caseQ_III_min`. Numerically true ($\min\approx0.0367$ / $0.0361$ for $\beta_0$ / $\frac12$).
  Unresolved gap in the paper's proof; statement kept (`Auto.DIR.lemma_6_4`, paragraph added).
- 2026-11-11T23:25+00:00 — [DIR] §6.2.2: $\beta yf_\beta'(y)=f_{\beta,0}(y)-f_{\beta,0}(y/2)$ needs
  $f_{\beta,0}'\le0$ on $[\frac18,\frac12]$; paper shows $[\frac14,\frac12]$. Gap closable: the
  sign argument for $f_{\beta,0}'''\ge0$ works on $[\frac18,\frac12]$ and
  $f''_{\beta,0}(\frac18)\approx1.67/1.64>0$; numerically $\max_{[1/8,1/2]}f'_{\beta,0}\approx-0.66$.
  Resolved: reduction `caseQ_III_suffices_f_QIII_0` on $[\frac18,\frac12]$ (paragraph added) and new
  `Auto.DIR.deriv_f_QIII_0_neg_Icc_eighth` (not in paper).
- 2026-11-11T23:25+00:00 — [DIR] (6.13): Partition₂ is run only for
  $\underline{g_{LJQ,1,1/2}}$ but (6.13) is claimed for $\beta\in\{\beta_0,\frac12\}$ (likely typo).
  Numerically $\min G_\beta[b_\beta]\approx2.0\cdot10^{-3}$ / $1.9\cdot10^{-3}$. Statement kept
  (`Auto.DIR.eqn_6_13`, paragraph added).
- 2026-11-11T23:25+00:00 — [DIR] Proposition 6.6 omits $x+y\le1$ (standing assumption of Case
  $LJQ$, covered by the proof). Resolved: hypothesis kept in `Auto.DIR.prop_6_6`, paragraph added.
  Numerically the printed version also holds on $x+y>1$ (min $\approx0.0055$ at $\beta=\frac12$),
  not claimed.
- 2026-11-11T23:25+00:00 — [DIR] §6.3.2 proof of (1): uniqueness of the zero $y_1$ of
  $f'_{1/2}$ also needs $f'_{1/2}(\frac12^+)\ge0$ (not evaluated; $\approx0.0571$). Resolved: new
  `Auto.DIR.f_LJQ_1_half_deriv_half` (limit $>0.05$); paragraph at `f_LJQ_1_half_y₁`.
- 2026-11-11T23:25+00:00 — [DIR] §6.3.2 proof of (2): $\underline{g_{LJQ,2}}$ is not termwise
  monotone: $Q_{\overline\beta}$ is not increasing on $[\frac9{32},\frac{13}{32}]$ for
  $\overline\beta\gtrsim0.6$ ($Q_1'(\frac{13}{32})\approx-0.22$; termwise violation up to
  $\approx8\cdot10^{-3}$), but the combined lower bound holds (no violation in random/targeted
  searches). Statement kept (`Auto.DIR.g_LJQ_2_lo_tight`, paragraph added).
- 2026-11-11T23:25+00:00 — [DIR] §6.4: "$J^{-1}$ increasing on $[\frac34,1]$" is true but the
  argument needs $J^{-1}$ increasing on $[x_0,\frac58]$ (the points $\frac{1/4+y}2$). Both stated
  (`Auto.DIR.J_inv_monotoneOn`, `J_inv_monotoneOn_Ico_x₀`), paragraph added. (Note
  $J(\frac58)\approx0.4948<\frac12$.)
- 2026-11-11T23:25+00:00 — [DIR] §6.5 item 2: "$2Q_\beta(\frac{x+y}2)-Q_\beta(x)$ increasing in
  $y$" is false where $\frac{x+y}2>0.5283$ ($\beta=\frac12$) / $0.5185$ ($\beta_1$), e.g. for
  $x=\frac12$, $\beta=\frac12$: $0.4820$ at $y=0.7$, $0.4643$ at $y=\frac34$. Resolved:
  `Auto.DIR.two_Q_sub_Q_pos_mono` states it for $y\in[\frac12,1-x]$ (paragraph added).
  Consequences: the justification of `Auto.DIR.g_QJQ_tightLowerBound` fails on the part
  $x+y>1$ (also because $Q'_\beta(\frac{x+y}2)$ can be negative), but the lower-bound property
  itself holds numerically on the full rectangle (random searches, no violation), and (6.25)
  holds numerically on the full rectangle ($\min g_{QJQ}\approx7.8\cdot10^{-3}$ / $3.0\cdot10^{-2}$
  for $\frac12$ / $\beta_1$, attained in $x+y\le1$). Both statements kept on the full rectangle
  (paragraphs at `g_QJQ_tightLowerBound`, `eqn_6_25`); this supersedes the 19:14 entry.
- 2026-11-11T23:25+00:00 — [DIR] §6.6 (6.26), (6.27) and their lower bounds evaluate $J$ below
  $\frac12$. Resolved (supersedes the 19:14 entry): the conditional hypothesis
  `hJ : EqOn J (Jw w₀) (Icc (1 - w₀) 1)` is removed; `g_QJ`, `dg_QJ`, `g_QJ_1_lo`, `g_QJ_2`,
  `g_QJ_2_lo` use `Jw w₀` at $\frac{x+y}2$ and new enclosures `Auto.DIR.Jw₀_lo`, `Jw₀_hi`,
  `absDJw₀_hi`; `g_QJ_1_tightLowerBound`, `eqn_6_26`, `prop_6_12`, `g_QJ_2_tightLowerBound` lose
  the argument `hJ` (signature change). `g_QJ_deriv_x`, `g_QJ_deriv_x_nonpos` now use $1\le x+y$
  (paper's triangle) instead of $1<x+y$. 6_6 now imports 3_0 and 4_1 instead of 6_1. Numerically:
  $\min$ of $-\beta\partial_xg_{QJ}$ on $[\frac14,\frac12]\times[\frac12,\frac58]$ $\approx0.0328$ /
  $0.0342$; $\min g_{QJ,2}\approx3.9\cdot10^{-5}$ at $(\frac12,\frac58)$; both lower bounds valid on
  random subrectangles.
- 2026-11-11T23:25+00:00 — [DIR] §6.6.1: Proposition 6.11 omits $x+y\ge1$ (triangle I);
  hypothesis kept in `Auto.DIR.prop_6_11` (paragraph added; printed version numerically also holds
  on $x+y<1$ with margins $\sim10^{-7}$, not claimed). Partition₂ rectangle
  $[\frac14,\frac12]\times[\frac12,\frac58]$ is larger than triangle I; kept as in the paper
  (paragraph at `Auto.DIR.eqn_6_26`).
- 2026-11-11T23:25+00:00 — [DIR] §6.6 "in this region $G^1_\beta[J](x,y)$ is increasing in $\beta$":
  $J(x)$ undefined for $x<\frac12$; meant is the $\beta$-dependent term. Statement true as written
  for `Auto.DIR.J` (paragraph at `Auto.DIR.caseQJ_G₁_monotoneOn_beta`).

Other numerical spot checks (all consistent with the paper): (6.5) $\min\approx5.3\cdot10^{-4}$;
(6.7) $\min\approx0.0131$; (6.8) $0.0929$, $0.00304$; (6.9) $3.244/3.229$; (6.10) $-0.660/-0.660$;
(6.12) $\min\approx0.114/0.108$; Lemma 6.7 for $\beta\in[\frac12,1]$ ($\max\partial_x^2\le-0.60$);
(6.15) $0.0599$, $-0.327$; (6.16) $0.0593$, $-0.1035$; (6.17) $\min\approx1.5\cdot10^{-3}$; (6.18)
$0.0299$; (6.19) $-2.776$; (6.20) $-0.755$; (6.21) $0.1139$; (6.22) $0.0299$; $f'(\frac34)\approx0.450$
(§6.4); Remark 6.10 (failure at $(\frac14,\frac12)$, $G\approx-6.4\cdot10^{-5}$ for
$\beta=\beta_1+\frac1{1024}$); $p_\beta$ factorization, coefficients, $p_{\beta_1}(\frac14)\approx
1.54\cdot10^{-4}$, $p_\beta(\frac14)$ decreasing on $[\frac12,\beta_1]$; Remark 6.3 for
$\beta\in\{0.6,0.75,0.9,1\}$; claim "$G_\beta[b_\beta]>0$ for all $\beta\in[\frac12,1]$" (§6.3.1).

### [DIRX]

Format: location — discrepancy — resolution — Lean name (file). Every paper-side item has a
paragraph starting with `**Discrepancy with the paper.**` at the place in the Lean file.

#### Items from the existing ErrorReport (revisited)

1. **[DIRX] Remark 2.2, "[DIR24, Thm. 1.6]"** — this is the theorem number of [DIR] arXiv v1; in
   v2 (formalized here) the bound $\mathbf{E}h_A^\beta\ge\max(J(|A|),(1-|A|)(\log_2\frac1{1-|A|})^\beta)$
   is Theorem 1.7 (`Auto.DIR.thm_1_7`); v2's Theorem 1.6 is the different bound (1.4).
   Resolution: discrepancy paragraph; the previously unformalized last claim of Remark 2.2
   ("which further improves on [DIR, (2.6)] as $|A|\to1-$") is now stated as
   $\exists\delta>0\ \forall x\in(1-\delta,1):\ (1-x)(\log_2\frac1{1-x})^{\beta_0}>b_{\beta_0}(x)$.
   Lean: `Auto.DIRX.rem_2_2_thm_1_7_improves` (new), X/2_1.
2. **[DIRX] §3.3 Case II** — the claim "if $x\in[0,\frac14]$, $y\in[\frac12,1]$ and $x\le\frac1{16}$
   or $y\ge\frac34$, then $G_{LJQ}(x,y)\ge0$" omits $x+y\le1$ (heading of §3.3); the proof
   (concavity in $x$ on $[0,1-y]$, boundary $x=1-y$) and the identity $G_{LJQ}=G_2[B_{w_1}]$ need
   it. Resolution: hypothesis `hxy : x + y ≤ 1` kept; discrepancy paragraph added.
   Lean: `Auto.DIRX.caseLJQ_II`, X/3_3.
3. **[DIRX] §3.6.1** — "for $\frac38\le x\le\frac12\le y\le\frac58$, $G_1[B_w](x,y)\ge0$" omits
   $x+y\ge1$ (heading); the proof uses $B_w(\frac{x+y}2)=\mathrm J(\frac{x+y}2)$. (Points with
   $x+y<1$ are covered by Case $QJQ$.) Resolution: hypothesis kept; discrepancy paragraph.
   Lean: `Auto.DIRX.caseQJ_near`, X/3_6. Also fixed the false parenthetical "(so $x+y\ge1$)" in
   the docstring of `Auto.DIRX.G₁_BX_eq_h_QJ₂` (counterexample $(\frac14,\frac58)$; the hypothesis
   `hxy` is needed and present).
4. **[DIRX] §5, $\sqrt{1-(T_\rho f)^2}=2\sqrt{p(1-p)}\sqrt{s_f}+O(np)$** — the earlier entry
   (2026-11-11T19:26) claiming that $O(np)$ needs $p\lesssim n^{-2}$ is **withdrawn**: with
   $a=\sqrt{1-T^2}$, $b=2\sqrt{p(1-p)s_f}$ one has $|a-b|\le\sqrt{|a^2-b^2|}$; for $p\le\frac1n$,
   $T=f(1-2ps_f)+E$, $|E|\le C_0n^2p^2$ and $ps_f\le1$ give $|a^2-b^2|\le(4+2C_0+C_0^2)n^2p^2$; for
   $p>\frac1n$, $|a-b|\le1+2\sqrt{np}\le3np$. So the paper's claim holds with an absolute constant
   for all $p\in[0,1]$. Resolution: range restored to $p\in[0,1]$ (`sqrt_noiseOp_asymp`) and
   $p\in(0,1]$ (`hellinger_imp_asymp`, was $(0,\frac1{2n^2}]$); discrepancy paragraph (the paper
   does not specify the uniformity of $O(\cdot)$) and updated module docstring. Lean:
   `Auto.DIRX.sqrt_noiseOp_asymp`, `Auto.DIRX.hellinger_imp_asymp`, X/5_0.
5. **[DIRX] §1, Bobkov–Götze** — the improved bound is not stated in the paper; the Lean
   statement uses $\mathbf{E}\sqrt{h_A}\ge\sqrt3|A|(1-|A|)$ from [DIR] §1.1. Resolution:
   discrepancy paragraph. Lean: `Auto.DIRX.bobkov_goetze`, X/Thm_1_1.
6. **[DIRX] §1/§5, Courtade–Kumar and Hellinger conjectures** — the paper does not state the
   Courtade–Kumar conjecture (standard mutual-information form of [KC13] used) and states the
   Hellinger conjecture only for balanced $f$ (only this case formalized; the implication
   Hellinger ⇒ Courtade–Kumar is not formalized). Resolution: discrepancy paragraphs.
   Lean: `Auto.DIRX.CourtadeKumarConjecture` (X/Thm_1_3), `Auto.DIRX.HellingerConjecture` (X/5_0).

#### New items

7. **[DIRX] §3.3, Case II, "$f'$ has exactly one zero $y_1$ on $(\frac12,1)$"** — gap: from
   "$f'$ increasing on $(\frac12,y_0)$, decreasing on $(y_0,1)$, $f'(\frac9{16})>0.05$,
   $f'(\frac{15}{16})<-0.08$" one cannot exclude a zero of $f'$ in $(\frac12,\frac9{16})$; one also
   needs $f'(\frac12)\ge0$. Numerically $f'(\frac12)=1+(\sqrt2-1)\mathrm J'(\frac12)-Q'(\frac14)
   \approx0.0465>0$, so the claim is true. Resolution: claim unchanged, discrepancy paragraph;
   missing step added as a new theorem. Lean: `Auto.DIRX.fX_deriv_zero`,
   `Auto.DIRX.fX_deriv_half_pos` (new), X/3_3.
8. **[DIRX] §3.5, tight lower bound $\underline{h_{QJQ,2}}$ on
   $[\frac14,\frac12]\times[\frac{33}{64},\frac34]$** — no justification is given; the
   monotonicity facts recorded for $\underline{h_{QJQ,1}}$ ("$2Q(\frac{x+y}2)-Q(x)$ increasing in
   $y$") fail here, since $Q'<0$ on $(t_*,\frac58]$, $t_*\approx0.5283$ (e.g. $Q'(\frac58)\approx
   -0.41$), i.e. where $x+y>1.0566$ (outside the Case $QJQ$ region $x+y\le1$). The tight-lower-bound
   claim nevertheless holds numerically (randomized check of $6\cdot10^4$ sub-rectangles, no
   violation; the $\mathrm J(\overline y)^2$ term compensates). Resolution: statement unchanged,
   discrepancy paragraph; a proof needs an extra argument. Lean: `Auto.DIRX.h_QJQ₂_lo_tight`, X/3_5.
   (For $\underline{h_{QJQ,1}}$ on $[\frac14,\frac12]\times[\frac12,\frac{33}{64}]$ the
   monotonicity is fine: $\frac{x+y}2\le\frac{65}{128}<\frac{33}{64}<t_*$; explanatory note added to
   `Auto.DIRX.QJQ_monotone`; note [DIR] `Auto.DIR.two_Q_sub_Q_pos_mono` only covers $x+y\le1$.)
9. **[DIRX] §3.6, enclosures of $\mathrm J$, $|\mathrm J'|$ used below $\frac12$** — in
   $\underline{h_{QJ,1}}$ (rectangle $[\frac14,\frac12]\times[\frac12,\frac58]$) the midpoint
   $c=\frac{x+y}2$ ranges over $[\frac38,\frac9{16}]$, and in $\underline{h_{QJ,2}}$ over
   $[\frac7{16},\frac34]$, while §2.2 states the monotonicity and the enclosures (2.7) only on
   $[\frac12,1]$. They remain valid on $[1-w_1,1)$ ($\mathrm J''=-\gamma/\mathrm J<0$, $\mathrm
   J'(x_1)=0$). Resolution: explanatory note at `Auto.DIRX.h_QJ₁_lo_tight` (X/3_6); statements
   unchanged (numerically verified).
10. **Lean: `QX_spec` (X/2_1)** — the formulation `∃! p, natDegree ≤ 3 ∧ … ∧ ∀ x, p.eval x = Q x`
    made uniqueness vacuous (any two polynomials equal to $Q$ pointwise coincide) and did not
    express "unique interpolating cubic". Resolution: restated as: $Q$ is a polynomial of degree
    $\le3$, $Q$ has the four prescribed values, and every polynomial of degree $\le3$ with these
    values equals $Q$. Lean: `Auto.DIRX.QX_spec`. (The analogous `Auto.DIR.Q_spec` in D/2_0 has
    the same issue; not edited, outside this agent's files.)
11. **Lean: global notation `∂A` (X/Thm_1_1)** — the global `notation "∂" A:max` clashed with
    Mathlib's scoped shadow notation `∂ 𝒜` (`open scoped FinsetFamily`) in every importing file
    (checked: `(∂ 𝒜) = Finset.shadow 𝒜` failed to elaborate). Resolution: changed to
    `local notation` (it is only used in X/Thm_1_1). The other global [DIRX] notations
    `s_{f}`, `T_{ρ}`, `R_{p}` were checked against integrals `∫ x, f x ∂μ`, `|a|`, set-builder
    notation and identifiers `s_`, `T`, `R`: no clash. Lean: `Auto.DIRX.vtxBdry`.
12. **[DIRX] §1, "no dimension-free lower bound ... for any $\beta<\frac12$"** — the hypothesis
    $0<\beta$ is implicit (for $\beta=0$ the Lean statement would be false since $h_A^0=1$ by
    `0 ^ 0 = 1`). Resolution: note in docstring. Lean: `Auto.DIRX.no_dimension_free_bound`.
13. **Lean docstring of `eqn_1_2` (X/Thm_1_1)** — said "if $|\partial A|=0$ then $A=\emptyset$";
    corrected to "as $|A|\le\frac12$, $A=\emptyset$" ($A$ = whole cube also has empty boundary).

#### Numerical spot checks (Python, float; $I=\varphi\circ\Phi^{-1}$ via `statistics.NormalDist`)

All of the following are consistent with the paper (no numerical error found):
$\gamma=1.94521\in[1.945,1.946]$; $I(\frac{16}{29})=0.395584$; (2.6) eval
$\frac{\sqrt2}{2w_1}I(\frac1{2w_1})^{-1}(1-\varepsilon(\frac1{64}))=1.0173>1$ and
$\min\mathrm J(1-x)/(x\sqrt{\log(w_1/x)})=1.71$ on $(0,\frac1{64}]$; Case J II value $0.0874\in
[0.08,0.09]$; (3.6) $f''(\frac12)=0.0454$, $f''(\frac9{16})=0.1004$, $f''(\frac45)=-0.286$;
$f'(\frac9{16})=0.0513$, $f'(\frac{15}{16})=-0.0951$, $f'(\frac12)=0.0465$; $\min_{[\frac12,1]}f=0$
(at endpoints); $G_{LJQ}(\frac14,\frac34)=0.0285$; $g'$ bounds $0.2685,\ 0.3003,\ 0.17096$
(tight against $0.26,0.3,0.17$); $(\mathrm J')^2-\gamma=-1.912,-1.256$ at $\frac12,\frac34$;
$g_{P,1}(\frac1{64})=0.2323$; $Q'(\frac{33}{64})=0.0515>0$; $\max(L''(x)-\frac12Q''(\frac{x+y}2))
=-0.60<0$ on $(0,\frac14]\times[0,1]$. Grid minima of the (🚗) claims: (3.3) $1.9\cdot10^{-3}$,
(3.7) $1.5\cdot10^{-3}$, (3.8) $0.0285$, (3.11) $6.8\cdot10^{-3}$, (3.12) $1.06\cdot10^{-3}$,
(3.13) $9.9\cdot10^{-3}$, (3.14) $5.0\cdot10^{-4}$, (4.2) $0.013$, (4.3) $0.033$ (all above the
stated thresholds); (4.1) $\min G_P=0$ (at $x=0,\frac12$). All tight lower bounds
($\underline{h_{LJQ,1}},\underline{h_{LJQ,2}},\underline{h_{LJ,1}},\underline{h_{QJQ,1}},
\underline{h_{QJQ,2}},\underline{h_{QJ,1}},\underline{h_{QJ,2}},\underline{h_{P,1}},
\underline{h_{P,2}}$) passed randomized checks of the lower-bound property (no violation).
Remark 2.2: $J_{w_0}^{[DIR]}>\mathrm J$ on $(\frac12,1)$ (min difference $\to0$ only at
$\frac12^+$), $0.997J_{w_0}^{[DIR]}>\mathrm J$ exactly for $x>0.5687$ (so near $1$, as claimed);
$w_0=0.895769$.


## Restructuring of 2026-11-12

- 2026-11-12T00:56+00:00 — Facts that the papers' proofs use but the scaffold does not state (e.g. positivity
  and smoothness of $I$ and $J$, monotonicity of $G^1_\beta$ in $\beta$, $G_{1/2}[cB]\ge cG_{1/2}[B]$
  for $0<c\le1$, the second claim of Lemma 6.4) are listed in `automation/forward_reasoning.md`,
  §4. Unresolved; to be added in the proof phase.
