import pickle
from fractions import Fraction as F
from math import factorial
from mpmath import mp, mpf, sqrt, exp, erfinv, pi, findroot
mp.dps=50
def I(t): z=sqrt(2)*erfinv(2*t-1); return exp(-z*z/2)/sqrt(2*pi)
w0=findroot(lambda w: sqrt(2)*w*I(1/(2*w))-mpf(1)/2, mpf('0.8957693'))
def rat(x,d): return F(int(x*10**d),10**d)
wl=rat(w0,12)-F(5,10**12); wu=wl+F(1,10**11)
R1=F(177245385091,10**11); R0=F(177245385090,10**11)
def gI(N,s): return sum(F((-1)**k)*s**(2*k+1)/(factorial(k)*(2*k+1)) for k in range(N))
def eN(N,v): return sum(F((-1)**k)*v**k/factorial(k) for k in range(N))
q=lambda x: f"({x.numerator}/{x.denominator} : ℚ)"
r=lambda x: f"({x.numerator}/{x.denominator} : ℝ)"
pts=pickle.load(open('sample.pkl','rb'))
M=10; N=11
L1=["import Isoperim","set_option maxHeartbeats 0","open Auto.DIR Set",""]
L2=["import Mathlib.Data.Rat.Defs","set_option maxHeartbeats 0","set_option maxRecDepth 100000",
 "def fact : ℕ → ℕ | 0 => 1 | k+1 => (k+1) * fact k",
 "def gI : ℕ → ℚ → ℚ | 0, _ => 0 | k+1, s => gI k s + (-1)^k * s^(2*k+1) / ((fact k : ℚ) * (2*k+1))",
 "def eN : ℕ → ℚ → ℚ | 0, _ => 0 | k+1, v => eN k v + (-v)^k / (fact k : ℚ)",""]
gaps=[]
for i,x in enumerate(pts):
    xf=mpf(x.numerator)/x.denominator
    t=(1-xf)/w0; tt=min(t,1-t)
    sl=rat(-erfinv(2*tt-1),12)+F(5,10**11)      # lower-bound witness
    su=max(rat(-erfinv(2*tt-1),12)-F(5,10**11),F(0))  # upper-bound witness
    lb=wl*eN(2*N+2,sl*sl)/R1; ub=wu*eN(2*N+1,su*su)/R0
    a=F(1,2)-gI(2*M+2,sl)/R1
    assert a<=(1-x)/wu and a<=1-(1-x)/wl, i
    bq=F(1,2)-gI(2*M+1,su)/R0
    assert (1-x)/wl<=bq or 1-(1-x)/wu<=bq, (i,float(x))
    Jt=sqrt(2)*w0*I(t); gaps.append(float(max(Jt-mpf(lb.numerator)/lb.denominator, mpf(ub.numerator)/ub.denominator-Jt)))
    L1.append(f"""theorem lo{i} (hw : w₀ ∈ Icc {r(wl)} {r(wu)}) :
    {r(wl)} * expNegTaylor (2 * {N} + 2) ({r(sl)} ^ 2) / 1.77245385091 ≤ J {r(x)} :=
  J_ge_cert {M} {N} (xl := {r(x)}) (xu := {r(x)}) hw (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (by norm_num [gaussIntTaylor, Finset.sum_range_succ, Nat.factorial])
    (by norm_num [gaussIntTaylor, Finset.sum_range_succ, Nat.factorial]) (by norm_num)
theorem up{i} (hw : w₀ ∈ Icc {r(wl)} {r(wu)}) :
    J {r(x)} ≤ {r(wu)} * expNegTaylor (2 * {N} + 1) ({r(su)} ^ 2) / 1.77245385090 :=
  J_le_cert {M} {N} (xl := {r(x)}) (xu := {r(x)}) hw (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (by {'left' if (1-x)/wl<=bq else 'right'}; norm_num [gaussIntTaylor, Finset.sum_range_succ, Nat.factorial]) (by norm_num)
theorem lov{i} : ({lb.numerator}/{lb.denominator} : ℝ) ≤ {r(wl)} * expNegTaylor (2 * {N} + 2) ({r(sl)} ^ 2) / 1.77245385091 := by
  norm_num [expNegTaylor, Finset.sum_range_succ, Nat.factorial]
""")
    L2.append(f"""theorem c{i} : ((1/2 : ℚ) - gI (2*{M}+2) {q(sl)} / {q(R1)} ≤ (1 - {q(x)}) / {q(wu)} ∧
    (1/2 : ℚ) - gI (2*{M}+2) {q(sl)} / {q(R1)} ≤ 1 - (1 - {q(x)}) / {q(wl)} ∧
    {q(lb)} ≤ {q(wl)} * eN (2*{N}+2) ({q(sl)}^2) / {q(R1)} ∧
    ((1 - {q(x)}) / {q(wl)} ≤ (1/2 : ℚ) - gI (2*{M}+1) {q(su)} / {q(R0)} ∨ 1 - (1 - {q(x)}) / {q(wu)} ≤ (1/2 : ℚ) - gI (2*{M}+1) {q(su)} / {q(R0)}) ∧
    {q(wu)} * eN (2*{N}+1) ({q(su)}^2) / {q(R0)} ≤ {q(ub)}) := by decide +kernel
""")
print('max enclosure error', max(gaps))
open('B_M1.lean','w').write("\n".join(L1)); open('B_M2.lean','w').write("\n".join(L2))
open('B_M3.lean','w').write("\n".join(L2).replace("by decide +kernel","by native_decide"))
