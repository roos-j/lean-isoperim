import re, ast
from fractions import Fraction as F
src=open('/tmp/claude-0/papers/dir24/anc/partitions.py').read()
blocks={}
for m in re.finditer(r'^# (\w+) \[display \(([\d.]+)\)\]\s*(with b=([\d.]+))?.*?\n# (\d+) (rectangles|intervals).*?\n(\w+) = (\[.*?\])\n\n', src, re.S|re.M):
    name,disp,_,b,cnt,kind,var,data=m.groups()
    blocks[(name,b)]=(disp,int(cnt),ast.literal_eval(data.replace('\n','')))
for k,v in blocks.items(): print(k,v[0],v[1])
def fr(s): return F(s)
def pts_gJ1(rects):
    J=set(); D=set()
    for (xm,xM),(hm,hM) in rects:
        xm,xM,hm,hM=map(fr,(xm,xM,hm,hM))
        J|={xm,xM,xm+hm,xM+hM,xM+hM/2}; D|={xm,xM,xM+hM,xM+hM/2}
    return J,D
def pts_gJ2(rects):
    J=set()
    for (xm,xM),(ym,yM) in rects:
        xm,xM,ym,yM=map(fr,(xm,xM,ym,yM)); J|={yM,(xm+ym)/2,xm}
    return J
J1a,D1a=pts_gJ1(blocks[('g_J_1','0.50057')][2]); J1b,D1b=pts_gJ1(blocks[('g_J_1','0.5')][2])
J2=pts_gJ2(blocks[('g_J_2',None)][2])
print('gJ1 beta0: J pts',len(J1a),'DJ pts',len(D1a)); print('gJ1 1/2: J pts',len(J1b),'DJ pts',len(D1b))
print('gJ1 union J',len(J1a|J1b),'DJ',len(D1a|D1b)); print('gJ2 J pts',len(J2))
allJ=J1a|J1b|J2; print('all J pts',len(allJ),'max denom',max(p.denominator for p in allJ), 'max y', float(max(allJ)))
import pickle; pickle.dump(dict(blocks=blocks,J1a=J1a,J1b=J1b,J2=J2,D=D1a|D1b),open('/tmp/claude-0/est/pts.pkl','wb'))
