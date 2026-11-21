# Error report — Task 5

Task 5 additions to `automation/ErrorReport.md` (kept separate so that the shared file is unchanged).

## Proof stage, Task 5 ([DIR] §1, §2; [DIRX] §1, §2.1, §4; 2026-11-20)

- 2026-11-20T19:20-05:00 — [DIR] Theorem 1.10, (1.7): claimed for all $p\ge2\beta_0$. False for large
  $p$: for $n=2$, $f=\mathbf{1}_{\{0\}}$, $p=6$: $\|\nabla f\|_6^6=\frac14(\frac18+\frac2{64})\approx0.0391$,
  $\|f-\mathbf{E}f\|_6^6=\frac14(\frac34)^6+\frac34(\frac14)^6\approx0.0447$. (The introduction of [DIR]
  considers $1\le p\le2$.) The paper's proof (§7) covers $p=2\beta_0$ only (earlier entry of
  `automation/ErrorReport.md`, 2026-11-11). Resolved (user decision 2026-11-20T19:29-05:00):
  `Auto.DIR.thm_1_10` states (1.7) for $2\beta_0\le p\le2$. The proof for $2\beta_0<p\le2$ is new: it
  uses $\mathbf{E}h_A^{p/2}\ge\mathbf{E}h_A^{\beta_0}$ ($h_A$ integer valued), convexity of
  $\beta\mapsto r^{2\beta}$, Proposition 7.1 at $\beta_0$, and the new estimate
  $b_{\beta_0}(x)+b_{\beta_0}(1-x)\ge4x(1-x)$ on $[0,1]$ (`Auto.DIR.four_mul_le_b_add_b`, proved with
  chords of the concave $J$ through certified values of $J$ at
  $\frac{17}{32},\frac9{16},\frac58,\frac34,\frac{13}{16},\frac78,\frac{15}{16}$). The equality for half-cubes
  and the bound $\|\nabla f\|_1\ge0.997\|f-\mathbf{E}f\|_1$ are as in the paper.
- 2026-11-20 — [DIR] §1.2, after Theorem 1.6 ($\mathcal{B}_1(x)\sim x\log_2(1/x)$, "implied by (1.3)"):
  the upper bound $\mathcal{B}_1(x)\le x(\log_2(1/x)+2)$ follows from (1.3) and the digit-sum bound
  $2\sum_{j<k}s(j)\ge k\log_2k-2k$ (`Auto.DIR.two_fH_ge`, not in the paper); the lower bound
  $\mathcal{B}_1(x)\ge x\log_2(1/x)$ ($x\le\frac12$) is taken from Theorem 1.1 at $\beta=1$ instead of
  (1.3). Resolved (route documented at `Auto.DIR.isoProfile_one_ge`, `Auto.DIR.isoProfile_one_le`).
- 2026-11-20 — [DIR] §1.4, display after Corollary 1.9, and [DIRX] proof of Theorem 1.2: the chains
  do not use that $A$ is disjoint from $B$, $W$ or that $|A|=\frac12$ (only $|B\cup W|=\frac12$). Resolved:
  hypotheses removed from `Auto.DIR.cor_1_9_chain`, `Auto.DIRX.thm_1_2_chain` (rule 7, noted in the
  docstrings).
