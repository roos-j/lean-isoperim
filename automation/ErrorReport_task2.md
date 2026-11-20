# Error report — Task 2

Task 2 additions to `automation/ErrorReport.md` (kept separate so that the shared file is unchanged).

## Proof stage, Task 2 ([DIR] §6, 2026-11-13)

- [DIR] (6.25), companion code: `verification.py` bounds $J(y)J'(y)$ by its value at the midpoint
  of $[\underline y,\overline y]$; since $JJ'$ is decreasing this is an upper bound, not a lower
  bound (the paper's text, $J(\overline y)J'(\overline y)$, is correct). With the paper's lower
  bound, 54 of the 55 rectangles of `g_QJQ` fail. Resolved: `Auto.DIR.g_QJQ_lo` (the paper's
  bound where $Q'_\beta(\frac{\underline x+\overline y}2)\ge0$, in particular for $x+y\le1$; a
  concavity tangent bound otherwise) with dyadic refinements of the paper's partitions
  (`g_QJQ` 55 → 340, `g_QJQh` 181 → 1180 rectangles). (6.25) itself holds; this supersedes the
  remark on `g_QJQ_tightLowerBound` (no longer a declaration).
- [DIR] (6.26), companion code: the case of $\underline{g_{QJ,1,\beta,c}}$ is decided by
  $\overline x<x_0$ instead of the paper's $\frac{\overline x+\overline y}2<x_0$; for
  $\frac{\overline x+\overline y}2>x_0$ the code's term is not a lower bound. Resolved: the paper's
  text is followed (case decided per box), the base $2\underline J-Q_\beta(\overline x)$ is
  replaced by its positive part, and the partitions are refined slightly (439 → 445, 430 → 436).
- [DIR] (6.17): the term $-2Q_{\overline\beta}(\frac1{32}+\frac{\overline y}2)$ of
  $\underline{g_{LJQ,2}}$ is not justified (see above). Resolved: `Auto.DIR.g_LJQ_2_lo` uses
  $-2(Q_{\overline\beta}(m)+|Q'_{\overline\beta}(m)|\frac{\overline y-\underline y}4)$ ($m$ the
  midpoint), justified by monotonicity in $\beta$ and concavity; the paper's partition passes
  unchanged (supersedes the reference to `g_LJQ_2_lo_tight`).
- [DIR] (6.19): the stated bound $L''_{1/2}(\frac14)\le-2.7$ does not suffice for (6.20)
  ($-2.7+J(\frac58)^{-1}\approx-0.679>-0.7$); the proof of (6.20) uses $L''_{1/2}(\frac14)\le-2.75$
  (true value $\approx-2.776$). (6.19) is proved as stated.
- [DIR] (6.3), (6.5), (6.13), (6.27): the paper's partitions are used unchanged; (6.3) and (6.13)
  for both values of $(\beta,c)$ resp. $\beta$. For (6.3) only the lower-bound property of
  $\underline{g_{J,1,\beta,c}}$ is used (`Auto.DIR.gJ1lo_le`); at $x=\frac12$ Fact 4.1 is applied
  with $f$ replaced by $1$ (`Auto.DIR.gJ1_gt_of_tree`), the case $x=\frac12$ of Case I following by
  continuity.
