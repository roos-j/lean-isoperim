import pickle
from mpmath import mp, mpf, sqrt, exp, erfinv, pi, findroot
from fractions import Fraction as F
mp.dps=30
vals=pickle.load(open('/tmp/claude-0/est/vals.pkl','rb'))
def I(t): z=sqrt(2)*erfinv(2*t-1); return exp(-z*z/2)/sqrt(2*pi)
def Jw(x,w): return sqrt(2)*w*I((1-x)/w)
w0=findroot(lambda w: Jw(mpf(1)/2,w)-mpf(1)/2, mpf('0.8957693'))
x0=1-w0/2
E=[mpf(0)]
def J(x): return Jw(x,w0)
def DJ(x): return sqrt(2)*sqrt(2)*erfinv(2*(1-x)/w0-1)
def Jlo(x): return J(x)-E[0]
def Jhi(x): return J(x)+E[0]
def Jm(a,b): return min(Jlo(a),Jlo(b))
def JM(a,b):
    if b<x0: return Jhi(b)
    if a>x0: return Jhi(a)
    return Jhi(x0)
def absDJm(a,b):
    if b<x0: return DJ(b)-E[0]
    if a>x0: return -DJ(a)-E[0]
    return mpf(0)
def absDJM(a,b): return max(abs(DJ(a)),abs(DJ(b)))+E[0]
def g_J_1(xm,xM,hm,hM,b,c):
    rv = b*c**(1-1/b)*JM(xm+hm, xM+hM)**(1-1/b)
    rv -= .5*b*(1-b)*c**(1-2/b)*Jm(xm+hm, xM+hM)**(1-2/b)*hM**(1/b)
    rv -= c/2*Jm(xm, xM)**(-1)*hM**(2-1/b)
    if xM < x0:
        d=DJ(xM)-E[0]; j=Jhi(xM)
        rv += c/4*d*j**(-2)*hm**(3-1/b)
        rv += c/32*d*(7+3*(DJ(xM)+E[0])**2)*j**(-4)*hm**(5-1/b)
    else:
        rv -= c/4*absDJM(xm, xM)*Jm(xm, xM)**(-2)*hM**(3-1/b)
        rv -= c/32*absDJM(xm, xM)*(7+3*absDJM(xm, xM)**2)*Jm(xm, xM)**(-4)*hM**(5-1/b)
    rv -= 7*c/48*(1+absDJM(xm, xM)**2)*Jm(xm, xM)**(-3)*hM**(4-1/b)
    rv -= c/90*(7+23*absDJM(xm, xM+hM)**2+6*absDJM(xm, xM+hM)**4)*Jm(xm, xM+hM)**(-5)*hM**(6-1/b)
    rv += c/2880*(7+23*absDJm(xm, xM+hM/2)**2+6*absDJm(xm, xM+hM/2)**4)*JM(xm, xM+hM/2)**(-5)*hm**(6-1/b)
    return rv
def g_J_2(xm,xM,ym,yM):
    return (ym-xM)**2 + Jlo(yM)**2 - (2*Jhi((xm+ym)/2)-Jlo(xm))**2
q=lambda s: mpf(F(s).numerator)/F(s).denominator
b0=mpf('0.50057'); c0=mpf('0.997')
sets0=[('g_J_1 b0',vals['g_J_1'],lambda r: g_J_1(*map(q,r[0]),*map(q,r[1]),b0,mpf(1))),
      ('g_J_1 1/2',vals['g_J_1h'],lambda r: g_J_1(*map(q,r[0]),*map(q,r[1]),mpf('0.5'),c0)),
      ('g_J_2',vals['g_J_2'],lambda r: g_J_2(*map(q,r[0]),*map(q,r[1])))]
import sys
sets=[s for s in sets0 if s[0]=='g_J_2']
for name,rects,f in sets:
    # use the 60 rects with smallest exact value
    E[0]=mpf(0); vs=sorted(((f(r),i) for i,r in enumerate(rects)))
    worst=[rects[i] for v,i in vs[:60]]
    res=[]
    for e in ['1e-8','1e-9','1e-10','1e-11','1e-12','1e-13']:
        E[0]=mpf(e); m=min(f(r) for r in worst); res.append((e,float(m)))
    print(name,'min exact',float(vs[0][0]), res); sys.stdout.flush()
