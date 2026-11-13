from fractions import Fraction as F
from math import factorial
from mpmath import mp, mpf, sqrt, exp, erfinv, pi, findroot
mp.dps=50
def I(t): z=sqrt(2)*erfinv(2*t-1); return exp(-z*z/2)/sqrt(2*pi)
w0=findroot(lambda w: sqrt(2)*w*I(1/(2*w))-mpf(1)/2, mpf('0.8957693'))
def rat(x,d): return F(int(x*10**d),10**d)
wl=rat(w0,12)-F(5,10**12); wu=wl+F(1,10**11)
R1=F(177245385091,10**11)
def gI(N,s): return sum(F((-1)**k)*s**(2*k+1)/(factorial(k)*(2*k+1)) for k in range(N))
def eN(N,v): return sum(F((-1)**k)*v**k/factorial(k) for k in range(N))
y=F(123,128)
t=(1-mpf(y.numerator)/y.denominator)/w0
s_ex=-erfinv(2*t-1)
s=rat(s_ex,12)+F(5,10**11)   # slightly larger -> Phi(-sqrt2 s) smaller
m=10; n=11
lhs=F(1,2)-gI(2*m+2,s)/R1
assert lhs <= (1-y)/wu and lhs <= 1-(1-y)/wl, (float(lhs-(1-y)/wu))
lb=wl*eN(2*n+2,s*s)/R1
Jtrue=sqrt(2)*w0*I((1-mpf(y.numerator)/y.denominator)/w0)
print('J true',Jtrue,' lower bound',float(lb),' gap',float(Jtrue-mpf(lb.numerator)/lb.denominator))
open('nums.txt','w').write(f"{wl}\n{wu}\n{s}\n{m}\n{n}\n")
def lean_q(x): return f"({x.numerator}/{x.denominator} : ℚ)" if x.denominator!=1 else f"({x.numerator} : ℚ)"
def lean_r(x): return f"({x.numerator}/{x.denominator} : ℝ)" if x.denominator!=1 else f"({x.numerator} : ℝ)"
# M1: norm_num via J_ge_cert
M1=f"""import Isoperim
set_option maxHeartbeats 0
open Auto.DIR Set
theorem t_M1 (hw : w₀ ∈ Icc {lean_r(wl)} {lean_r(wu)}) :
    {lean_r(wl)} * expNegTaylor (2 * {n} + 2) ({lean_r(s)} ^ 2) / 1.77245385091 ≤ J (123/128) :=
  J_ge_cert {m} {n} hw (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (by norm_num [gaussIntTaylor, Finset.sum_range_succ, Nat.factorial])
    (by norm_num [gaussIntTaylor, Finset.sum_range_succ, Nat.factorial]) (by norm_num)
theorem t_M1_val : ({lb.numerator}/{lb.denominator} : ℝ) ≤ {lean_r(wl)} * expNegTaylor (2 * {n} + 2) ({lean_r(s)} ^ 2) / 1.77245385091 := by
  norm_num [expNegTaylor, Finset.sum_range_succ, Nat.factorial]
#print axioms t_M1
"""
open('/tmp/claude-0/est/M1.lean','w').write(M1)
# M2/M3: rational computation in ℚ via recursive functions
common=f"""set_option maxHeartbeats 0
set_option maxRecDepth 100000
def fact : ℕ → ℕ | 0 => 1 | k+1 => (k+1) * fact k
def gI : ℕ → ℚ → ℚ | 0, _ => 0 | k+1, s => gI k s + (-1)^k * s^(2*k+1) / ((fact k : ℚ) * (2*k+1))
def eN : ℕ → ℚ → ℚ | 0, _ => 0 | k+1, v => eN k v + (-v)^k / (fact k : ℚ)
def check1 : Bool := decide ((1/2 : ℚ) - gI (2*{m}+2) {lean_q(s)} / {lean_q(R1)} ≤ (1 - 123/128) / {lean_q(wu)})
def check2 : Bool := decide ((1/2 : ℚ) - gI (2*{m}+2) {lean_q(s)} / {lean_q(R1)} ≤ 1 - (1 - 123/128) / {lean_q(wl)})
def check3 : Bool := decide ({lean_q(lb)} ≤ {lean_q(wl)} * eN (2*{n}+2) ({lean_q(s)}^2) / {lean_q(R1)})
"""
open('/tmp/claude-0/est/M2.lean','w').write(common+"theorem t1 : check1 = true := by decide +kernel\ntheorem t2 : check2 = true := by decide +kernel\ntheorem t3 : check3 = true := by decide +kernel\n#print axioms t3\n")
open('/tmp/claude-0/est/M3.lean','w').write(common+"theorem t1 : check1 = true := by native_decide\ntheorem t2 : check2 = true := by native_decide\ntheorem t3 : check3 = true := by native_decide\n#print axioms t3\n")
