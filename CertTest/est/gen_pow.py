import random
from fractions import Fraction as F
from math import factorial
from mpmath import mp, mpf, log, exp, atanh
mp.dps=60
random.seed(1)
b0=F(50057,100000); r1=1-1/b0   # exponent 1-1/beta0 ~ -0.9977
NL=24; NE=18
def logser(m,N):  # 2*sum u^(2k+1)/(2k+1), u=(m-1)/(m+1)
    u=(m-1)/(m+1); return 2*sum(u**(2*k+1)/(2*k+1) for k in range(N))
def expser(y,N): return sum(y**k/factorial(k) for k in range(N))
L2=logser(F(2),40)  # log 2 approx (series at u=1/3)
q=lambda x: f"({x.numerator}/{x.denominator} : ℚ)"
r=lambda x: f"({x.numerator}/{x.denominator} : ℝ)"
M2=["import Mathlib.Data.Rat.Defs","set_option maxHeartbeats 0","set_option maxRecDepth 100000",
"def fact : ℕ → ℕ | 0 => 1 | k+1 => (k+1) * fact k",
"def logS : ℕ → ℚ → ℚ | 0, _ => 0 | k+1, u => logS k u + 2 * u^(2*k+1) / (2*k+1)",
"def expS : ℕ → ℚ → ℚ | 0, _ => 0 | k+1, y => expS k y + y^k / (fact k : ℚ)",
"def rnd (x : ℚ) : ℚ := ((x.num * 10^20 / (x.den : ℤ) : ℤ) : ℚ) / 10^20",""]
M1=["import Mathlib","set_option maxHeartbeats 0",""]
for i in range(40):
    X=F(random.randint(10**19,6*10**19),10**20)   # a J bound with 20 digits in (0.1,0.6)
    # range reduce: X = 2^-e * m, m in [0.7,1.4]
    e=0; m=X
    while m<F(7,10): m*=2; e+=1
    u=(m-1)/(m+1)
    Lx=logser(m,NL)-e*L2            # log X approx
    y=r1*Lx                          # exponent
    k=round(float(y)/float(L2)); yp=y-k*L2  # exp(y)=2^k exp(yp)
    val=expser(yp,NE)*(F(2)**k)
    true=mpf(X.numerator)/X.denominator; true=exp(mpf(r1.numerator)/r1.denominator*log(true))
    c=F(int((mpf(val.numerator)/val.denominator-mpf('1e-11'))*10**20),10**20)
    up=F(u.numerator,u.denominator); u2=F(1,3)
    M2.append(f"theorem p{i} : {q(c)} ≤ expS {NE} (rnd ({q(r1)} * (logS {NL} (rnd {q(up)}) - {e} * logS 40 {q(u2)}) - {k} * logS 40 {q(u2)})) * 2^({k}:ℤ) := by decide +kernel")
    ypr=F(int(yp*10**22),10**22)
    M1.append(f"theorem p{i} : ({c.numerator}/{c.denominator} : ℝ) ≤ (∑ j ∈ Finset.range {NE}, ({ypr.numerator}/{ypr.denominator} : ℝ)^j / (j.factorial : ℝ)) * 2^({k}:ℤ) := by norm_num [Finset.sum_range_succ, Nat.factorial]")
    M1.append(f"theorem pl{i} : ({(logser(m,NL)).numerator}/{(logser(m,NL)).denominator} : ℝ) = ∑ j ∈ Finset.range {NL}, 2 * ({u.numerator}/{u.denominator} : ℝ)^(2*j+1) / (2*j+1) := by norm_num [Finset.sum_range_succ]")
open('P_M2.lean','w').write("\n".join(M2)+"\n"); open('P_M3.lean','w').write("\n".join(M2).replace("by decide +kernel","by native_decide")+"\n")
open('P_M1.lean','w').write("\n".join(M1)+"\n")
print(len(str(yp.denominator)), 'digit denominators in M1 exp argument (unrounded)')
