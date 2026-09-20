"""Geometric gate: every <text> must sit inside the card/strip that contains its anchor, and texts must not overlap."""
from pathlib import Path
from playwright.sync_api import sync_playwright
HERE = Path(__file__).parent
JS = """sid => { const root=document.querySelector('#'+sid+' svg'); const o=root.getBoundingClientRect();
 const boxes=[...root.querySelectorAll('rect')].filter(r=>+r.getAttribute('width')>100&&+r.getAttribute('height')>40&&r.getAttribute('rx')).map(r=>r.getBoundingClientRect());
 const ts=[...root.querySelectorAll('text')].map(t=>({s:t.textContent,b:t.getBoundingClientRect()})); const out=[];
 for(const t of ts){ const cx=(t.b.left+t.b.right)/2, cy=(t.b.top+t.b.bottom)/2;
   const box=boxes.filter(b=>cx>b.left&&cx<b.right&&cy>b.top&&cy<b.bottom).sort((a,b)=>a.width*a.height-b.width*b.height)[0];
   const lim=box||o; const pad=box?6:10;
   if(t.b.left<lim.left+pad||t.b.right>lim.right-pad||t.b.bottom>lim.bottom-4) out.push('OVERFLOW: '+t.s); }
 for(const r of [...root.querySelectorAll('rect')].filter(r=>+r.getAttribute('height')==19)){const b=r.getBoundingClientRect(),cx=(b.left+b.right)/2,cy=(b.top+b.bottom)/2;
   const box=boxes.filter(k=>cx>k.left&&cx<k.right&&cy>k.top&&cy<k.bottom).sort((a,b)=>a.width*a.height-b.width*b.height)[0];
   if(box&&(b.right>box.right-6||b.bottom>box.bottom-6)) out.push('CHIP OUTSIDE BOX');
   for(const t of ts){const a=t.b; if(a.left<b.right&&b.left<a.right&&a.top<b.bottom-1&&b.top<a.bottom-1&&!(a.left>=b.left&&a.right<=b.right&&a.top>=b.top-2&&a.bottom<=b.bottom+2)) out.push('CHIP HITS TEXT: '+t.s);}}
 for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){const a=ts[i].b,b=ts[j].b;
   if(a.left<b.right-1&&b.left<a.right-1&&a.top<b.bottom-1.5&&b.top<a.bottom-1.5) out.push('OVERLAP: '+ts[i].s+' | '+ts[j].s);}
 return out; }"""
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1260, "height": 900})
    pg.goto((HERE / "journal_abstracts.html").as_uri()); pg.wait_for_timeout(500)
    bad = 0
    for sid in pg.evaluate("[...document.querySelectorAll('section.ja')].map(s=>s.id)"):
        res = pg.evaluate(JS, sid); bad += len(res)
        print(sid, "PASS" if not res else "FAIL"); [print("   ", r) for r in res]
    b.close()
raise SystemExit(1 if bad else 0)
