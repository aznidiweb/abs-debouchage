# Contours provinces (communes Lambert 72 -> WGS84 -> Mercator z8), fusion par annulation d'arêtes, simplification
import json, math, collections, sys
sys.path.insert(0,'/home/claude/abs-debouchage/src')
G='geo/belgium-geographic-data/dist/polygons/'
a=6378388.0; f=1/297.0; e=math.sqrt(2*f-f*f)
lat1=math.radians(51+10/60+0.00204/3600); lat2=math.radians(49+50/60+0.00204/3600); lon0=math.radians(4+22/60+2.952/3600)
x0,y0=150000.013,5400088.438
m=lambda p: math.cos(p)/math.sqrt(1-e*e*math.sin(p)**2)
t=lambda p: math.tan(math.pi/4-p/2)/((1-e*math.sin(p))/(1+e*math.sin(p)))**(e/2)
n=(math.log(m(lat1))-math.log(m(lat2)))/(math.log(t(lat1))-math.log(t(lat2)))
F=m(lat1)/(n*t(lat1)**n)
def inv(x,y):
    dx=x-x0; dy=y-y0
    r=math.hypot(dx,dy); tt=(r/(a*F))**(1/n); th=math.atan2(dx,-dy)
    lon=th/n+lon0; phi=math.pi/2-2*math.atan(tt)
    for _ in range(8): phi=math.pi/2-2*math.atan(tt*((1-e*math.sin(phi))/(1+e*math.sin(phi)))**(e/2))
    return math.degrees(lon), math.degrees(phi)
Z=8
def merc(lon,lat):
    N=256*2**Z
    return (lon+180)/360*N, (1-math.log(math.tan(math.radians(lat))+1/math.cos(math.radians(lat)))/math.pi)/2*N
PRV={'11':'an','12':'an','13':'an','21':'bxl','23':'vb','24':'vb','25':'bw','31':'wv','32':'wv','33':'wv','34':'wv','35':'wv','36':'wv','37':'wv','38':'wv',
     '41':'ov','42':'ov','43':'ov','44':'ov','45':'ov','46':'ov','51':'ha','52':'ha','53':'ha','54':'ha','55':'ha','56':'ha','57':'ha','58':'ha',
     '61':'lg','62':'lg','63':'lg','64':'lg','71':'li','72':'li','73':'li','81':'lu','82':'lu','83':'lu','84':'lu','85':'lu','91':'na','92':'na','93':'na'}
mun=json.load(open(G+'be-municip-lamberts.geo.json'))['features']
segs=collections.defaultdict(collections.Counter); allsegs=collections.Counter()
K=lambda p:(round(p[0],1),round(p[1],1))
def rings(g): return g['coordinates'] if g['type']=='Polygon' else [r for poly in g['coordinates'] for r in poly]
for ft in mun:
    pid=PRV[str(ft['properties']['NIS5'])[:2]]
    for r in rings(ft['geometry']):
        for p,q in zip(r,r[1:]):
            a_,b_=K(p),K(q)
            if a_==b_: continue
            k=(a_,b_) if a_<b_ else (b_,a_)
            segs[pid][k]+=1; allsegs[k]+=1
def chain(cnt):
    edges=[k for k,c in cnt.items() if c==1]
    adj=collections.defaultdict(list)
    for a_,b_ in edges: adj[a_].append(b_); adj[b_].append(a_)
    used=set(); out=[]
    for a_,b_ in edges:
        if (a_,b_) in used: continue
        ring=[a_,b_]; used.add((a_,b_)); used.add((b_,a_)); cur=b_; prev=a_
        while True:
            nx=[v for v in adj[cur] if (cur,v) not in used]
            if not nx: break
            v=nx[0]; used.add((cur,v)); used.add((v,cur)); ring.append(v); prev,cur=cur,v
            if v==ring[0]: break
        if len(ring)>8: out.append(ring)
    return out
def rdp(pts,eps):
    if len(pts)<3: return pts
    (x1,y1),(x2,y2)=pts[0],pts[-1]; dmax=0; idx=0
    L=math.hypot(x2-x1,y2-y1) or 1e-9
    for i in range(1,len(pts)-1):
        x,y=pts[i]; d=abs((y2-y1)*x-(x2-x1)*y+x2*y1-y2*x1)/L
        if d>dmax: dmax=d; idx=i
    if dmax>eps: return rdp(pts[:idx+1],eps)[:-1]+rdp(pts[idx:],eps)
    return [pts[0],pts[-1]]
def tomerc(ring): return [merc(*inv(x,y)) for x,y in ring]
X0,Y0=merc(2.35,51.62); X1,Y1=merc(6.55,49.42)
def path(rs,eps=.6):
    d=''
    for r in rs:
        m_=tomerc(r); h=len(m_)//2; pts=rdp(m_[:h+1],eps)[:-1]+rdp(m_[h:],eps)
        if len(pts)<4: continue
        d+='M'+' '.join(f'{x-X0:.0f},{y-Y0:.0f}' for x,y in pts)+'Z'
    return d
out={'w':round(X1-X0,1),'h':round(Y1-Y0,1),'prov':{pid:path(chain(c)) for pid,c in segs.items()},'country':''}
# contrôle : extrêmes du pays
pts=[inv(x,y) for r in chain(allsegs) for x,y in r]
print('lon',min(p[0] for p in pts),max(p[0] for p in pts),'lat',min(p[1] for p in pts),max(p[1] for p in pts))
print({k:len(v) for k,v in out['prov'].items()}, len(out['country']))
open('/home/claude/abs-debouchage/src/map_osm.py','w').write('# Généré par make_osm_overlay.py : contours des provinces belges en coordonnées carte (Mercator z8, cadre 2.35–6.55°E / 49.42–51.62°N)\nOSM_SHAPES = '+json.dumps(out)+'\n')
