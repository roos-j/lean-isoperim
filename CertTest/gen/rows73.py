import sys, json
from fractions import Fraction as F
from math import factorial
from mpmath import mp, mpf, sqrt, log, erfinv
mp.dps=40
P=[F(s) for s in ['1/64','47/2048','31/1024','77/2048','23/512','107/2048','61/1024','19/256','91/1024','53/512','121/1024','17/128','151/1024','83/512','181/1024','49/256','407/2048','211/1024','437/2048','113/512','467/2048','241/1024','497/2048','1/4']]
WL,WU=F(8957,10000),F(8958,10000)
R1=F(1772454,1000000); R2=F(25066285,10000000); SQ2=F(1414213,1000000)
T=F(1,2)*(1-F(114,100000)*F(6931472,10000000))
M=7
def Ilow(s): return sum(F((-1)**k)*s**(2*k+1)/(factorial(k)*(2*k+1)) for k in range(2*M+2))
def Elow(v): return sum(F((-1)**k)*v**k/factorial(k) for k in range(2*M+2))
fl=lambda x,den: F(int(x*den)-2, den) if not isinstance(x,F) else F((x*den).__floor__()-2,den)
rows=[]; worst=None
for a,b in zip(P,P[1:]):
    t=mpf(a.numerator)/a.denominator/mpf(WU.numerator)*WU.denominator
    s=F(int(-erfinv(2*t-1)*10**5)+3,10**5)
    c=fl(Ilow(s),10**7); e=fl(Elow(s*s),10**7)
    assert c<=Ilow(s) and e<=Elow(s*s)
    assert F(1,2)-c/R1 <= a/WU
    Jlo=SQ2*WL*e/R2
    m,den=a.numerator,a.denominator; K=den.bit_length()-1; assert 2**K==den
    d=10000; n=int(log(m,2)*d)-2
    while m**d > 2**n: n+=1
    ell=F(K)-F(n,d)
    r=F(int(sqrt(mpf(ell.numerator)/ell.denominator)*10**6),10**6); assert r*r<=ell
    val=T*(a*r+Jlo)-2*b*(1-a)
    assert val>F(1,10000)
    rows.append(dict(a=str(a),b=str(b),s=str(s),c=str(c),e=str(e),m=m,K=K,n=n,d=d,r=str(r),margin=float(val-F(1,10000))))
print(min(r['margin'] for r in rows))
json.dump(rows,open('CertTest/gen/rows73.json','w'),indent=0)
