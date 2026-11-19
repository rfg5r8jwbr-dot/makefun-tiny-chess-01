import json as J,os,urllib.request as R
P=lambda p,b:J.load(R.urlopen(os.getenv("MAKEFUN_ENV_URL")+p,J.dumps(b).encode()))
V=[0,100,320,330,500,900,0]
S=lambda s:chr(s%8+97)+str(s//16+1)
C=lambda m:S(m&127)+S(m>>7&127)+("nbrq"[(m>>14)-2] if m>>14 else "")
NS=[33,18,-14,-31,-33,-18,14,31]
BD=[15,17,-15,-17];RD=[1,-1,16,-16];KS=RD+BD
KP={4:12,0:13,7:14,116:3,112:7,119:11}
Z=((4,6,1),(4,2,2),(116,118,4),(116,114,8))
def F(f):
 b=[0]*128;p=f.split();i=112
 for c in p[0]:
  if c=="/":i-=24
  elif c.isdigit():i+=int(c)
  else:v="pnbrqk".index(c.lower())+1;b[i]=v*(1,-1)[c.islower()];i+=1
 c=sum(1<<j for j,k in enumerate("KQkq")if k in p[2])
 e=(int(p[3][1])-1)*16+ord(p[3][0])-97 if p[3]!="-" else -1
 return b,(1,-1)[p[1]=="b"],c,e
def A(b,q,y):
 for D,y2 in ((NS,2),(KS,6),((-16*y-1,-16*y+1),1)):
  for d in D:
   t=q+d
   if t&136==0 and b[t]==y*y2:return 1
 for D,T in((BD,3),(RD,4)):
  for d in D:
   t=q+d
   while t&136==0:
    v=b[t]
    if v:
     if abs(v)in(T,5)and v*y>0:return 1
     break
    t+=d
 return 0
def G(b,s,c,e):
 m=[];a=m.append
 def h(o):
  if o>>4 in (0,7):
   for r in(5,4,3,2):a(q|o<<7|r<<14)
  else:a(q|o<<7)
 for q,p in enumerate(b):
  if q&136 or p==0 or p*s<0:continue
  t=abs(p);d=16*s
  if t==1:
   for o in(q+d,q+d-1,q+d+1):
    if o&136:continue
    if o==q+d:
     if b[o]:continue
     h(o)
     if q>>4==(1,6)[s<0]:
      w=q+d*2
      if not b[w]:a(q|w<<7)
    elif b[o]*s<0:h(o)
    elif o==e:a(q|o<<7)
  elif t in (2,6):
   for d in NS if t==2 else KS:
    o=q+d
    if o&136==0 and(not b[o]or b[o]*s<0):a(q|o<<7)
  else:
   for d in(BD,RD,KS)[t-3]:
    o=q+d
    while o&136==0:
     if b[o]:
      if b[o]*s<0:a(q|o<<7)
      break
     a(q|o<<7);o+=d
 for kf,kt,bit in Z:
  if c&bit and not(b[(kf+kt)//2]|b[kt])and(kt>kf or not b[kf-3])and not any(A(b,x,-s)for x in(kf,(kf+kt)//2,kt)):a(kf|kt<<7)
 return m
def M(b,m,s,c,e):
 f=m&127;t=m>>7&127;r=m>>14;z=b[f]
 if abs(z)==1 and t==e and not b[t]:b[t-16*s]=0
 if abs(z)==6 and abs(t-f)==2:
  a,d=(t+1,t-1) if t>f else (t-2,t+1);b[d]=b[a];b[a]=0
 b[t]=r*s if r else z;b[f]=0
 return c&KP.get(f,15)&KP.get(t,15),f+16*s if abs(z)==1 and t-f==32*s else -1
def L(b,s,c,e):
 o=[]
 for m in G(b,s,c,e):
  b2=b[:];nc,ne=M(b2,m,s,c,e)
  if not A(b2,b2.index(6*s),-s):o.append(m)
 return o
def E(b):
 sc=0;wb=bb=0;qn=5 in b or-5 in b
 for q,p in enumerate(b):
  if q&136 or p==0:continue
  t=abs(p);v=V[t];r=q>>4;ce=14-abs(q%8*2-7)-abs(r*2-7)
  if t==1:v+=(r,7-r)[p<0]*5
  elif t==2:v+=ce*2
  elif t==3:v+=ce;wb+=p>0;bb+=p<0
  elif t==6:v+=ce if qn==0 else -ce
  sc+=v*p//t
 return sc+25*((wb>1)-(bb>1))
n=[0];T={};W=set();H=set()
def Q(b,s,c,e,al,be,pl):
 n[0]+=1
 if n[0]>6e4:raise Exception
 ck=A(b,b.index(6*s),-s)
 if ck:
  ms=L(b,s,c,e)
  if not ms:return -1e5+pl
  al=-1e5
 else:
  st=s*E(b)
  if st>=be:return st
  al=max(al,st)
  ms=[m for m in G(b,s,c,e) if b[m>>7&127]]
 for m in ms:
  t=m>>7&127
  if not ck and (pl>6 or st+V[abs(b[t])]+150<al):continue
  b2=b[:];nc,ne=M(b2,m,s,c,e)
  if A(b2,b2.index(6*s),-s):continue
  sc=-Q(b2,-s,nc,ne,-be,-al,pl+1)
  if sc>=be:return sc
  if sc>al:al=sc
 return al
def D(b,s,c,e,d,al,be,pl):
 if (tuple(b),s)in W:return 0
 if d==0:return Q(b,s,c,e,al,be,pl)
 ms=L(b,s,c,e)
 if not ms:return -1e5+pl if A(b,b.index(6*s),-s)else 0
 f=2;tm=0
 if d>1:
  k=(tuple(b),s,c,e);v=T.get(k)
  if v:
   tm=v[3]
   if v[0]>=d and v[1]==0:return v[2]
 ms.sort(key=lambda m:(m!=tm,s*b[m>>7&127]))
 bm=ms[0]
 for m in ms:
  b2=b[:];nc,ne=M(b2,m,s,c,e);sc=-D(b2,-s,nc,ne,d-1,-be,-al,pl+1)
  if sc>=be:
   if d>1:T[k]=(d,1,sc,m)
   return sc
  if sc>al:al=sc;bm=m;f=0
 if d>1:T[k]=(d,f,al,bm)
 return al
def B(fen):
 b,s,c,e=F(fen);n[0]=0;T.clear();bb=b
 ms=L(b,s,c,e)
 best=C(ms[0])
 for d in range(5):
  try:
   bs=-1e5;bm=best
   for m in ms:
    u=C(m);b2=b[:];nc,ne=M(b2,m,s,c,e);v=-D(b2,-s,nc,ne,d,-1e5,-bs,1)
    if v>bs:bs,bm,bb=v,u,b2
   best=bm
  except:break
 k=(tuple(bb),-s);W.add(k)if k in H else H.add(k)
 return best
while(g:=P("/game",{}))["status"]!="done":
 while g["status"]=="your_move":g=P("/move",{"game":g["game"],"move":B(g["fen"])})
