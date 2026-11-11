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
