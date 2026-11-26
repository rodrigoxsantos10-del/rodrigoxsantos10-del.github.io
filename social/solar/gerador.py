#!/usr/bin/env python3
"""Gera carrosséis (1080x1350 JPG) da MSLUZSOLAR a partir de banco.json.

Uso: python3 gerador.py [id ...]   (sem ids = gera todos que ainda não têm imagens)
Cada item de banco.json:
  {"id": "S01_beneficios", "cover": {"tag": "...", "title": "texto com *destaque*", "sub": "..."},
   "slides": [{"kind": "item", "n": "01", "t": "Título", "d": "Descrição"} | {"kind": "stat", "big": "R$ 120 mil", "t": "...", "d": "..."}],
   "cta": {"title": "...", "sub": "..."}, "caption": "..."}
"""
import json, os, re, sys, html
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
PHONE = "(61) 98121-4135"
NAVY, NAVY2, SUN, ORANGE, SKY = "#0A2342", "#12345E", "#FFB703", "#FB8500", "#CFE3F7"

SUN_SVG = f'''<svg width="64" height="64" viewBox="0 0 64 64"><circle cx="32" cy="32" r="13" fill="{SUN}"/>
<g stroke="{SUN}" stroke-width="5" stroke-linecap="round">
<line x1="32" y1="3" x2="32" y2="11"/><line x1="32" y1="53" x2="32" y2="61"/><line x1="3" y1="32" x2="11" y2="32"/><line x1="53" y1="32" x2="61" y2="32"/>
<line x1="11.5" y1="11.5" x2="17.2" y2="17.2"/><line x1="46.8" y1="46.8" x2="52.5" y2="52.5"/><line x1="11.5" y1="52.5" x2="17.2" y2="46.8"/><line x1="46.8" y1="17.2" x2="52.5" y2="11.5"/></g></svg>'''

PANEL_SVG = f'''<svg class="panel" viewBox="0 0 520 300" width="520" height="300"><g transform="skewX(-18)">
{''.join(f'<rect x="{110+c*100}" y="{20+r*90}" width="92" height="82" rx="4" fill="{NAVY2}" stroke="{SKY}" stroke-opacity=".35" stroke-width="2"/>' for r in range(3) for c in range(4))}
</g><rect x="180" y="285" width="160" height="10" rx="5" fill="{SKY}" fill-opacity=".25"/></svg>'''

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:'Inter',sans-serif;color:#fff;background:{NAVY};position:relative;overflow:hidden}}
.top{{position:absolute;top:0;left:0;right:0;height:14px;background:linear-gradient(90deg,{SUN},{ORANGE})}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;right:-380px;top:-380px;background:radial-gradient(circle,rgba(255,183,3,.30),rgba(255,183,3,0) 65%)}}
.head{{position:absolute;top:62px;left:76px;right:76px;display:flex;align-items:center;justify-content:space-between}}
.brand{{display:flex;align-items:center;gap:18px}}
.brand b{{font-size:38px;font-weight:900;letter-spacing:-.5px}} .brand b span{{color:{SUN}}}
.brand small{{display:block;font-size:22px;color:{SKY};font-weight:500;margin-top:2px}}
.phone{{font-size:26px;color:{SKY};font-weight:600}}
.main{{position:absolute;left:80px;right:80px;top:250px;bottom:170px;display:flex;flex-direction:column;justify-content:center}}
.tag{{display:inline-block;align-self:flex-start;background:rgba(255,183,3,.15);color:{SUN};border:2px solid rgba(255,183,3,.5);border-radius:40px;padding:10px 26px;font-size:26px;font-weight:700;letter-spacing:1px;text-transform:uppercase;margin-bottom:36px}}
h1{{font-size:96px;line-height:1.04;font-weight:900;letter-spacing:-2.5px}}
h1 em,h2 em{{font-style:normal;color:{SUN}}}
.sub{{font-size:40px;line-height:1.3;color:{SKY};margin-top:44px;font-weight:500}}
.num{{font-size:150px;font-weight:900;color:{SUN};line-height:1;letter-spacing:-4px;opacity:.95}}
h2{{font-size:74px;line-height:1.08;font-weight:800;letter-spacing:-1.5px;margin-top:20px}}
.desc{{font-size:40px;line-height:1.38;color:#E6EEF8;margin-top:40px;font-weight:400}}
.desc strong{{color:{SUN};font-weight:700}}
.big{{font-size:150px;font-weight:900;color:{SUN};letter-spacing:-5px;line-height:1}}
.card{{background:rgba(255,255,255,.06);border:2px solid rgba(207,227,247,.18);border-radius:36px;padding:60px}}
.foot{{position:absolute;bottom:62px;left:80px;right:80px;display:flex;align-items:center;justify-content:space-between}}
.dots{{display:flex;gap:14px}} .dots i{{width:14px;height:14px;border-radius:50%;background:rgba(207,227,247,.3)}} .dots i.on{{background:{SUN};width:42px;border-radius:8px}}
.swipe{{font-size:30px;color:{SKY};font-weight:600}}
.panel{{position:absolute;right:-60px;bottom:115px;opacity:.45}}
.cta{{background:linear-gradient(160deg,{NAVY} 0%,{NAVY2} 100%)}}
.btn{{margin-top:56px;align-self:flex-start;background:{SUN};color:{NAVY};font-weight:900;font-size:44px;border-radius:24px;padding:30px 46px}}
.small{{font-size:30px;color:{SKY};margin-top:30px}}
"""

def fmt(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s.replace("\n", "<br>")

def page(inner, idx, total, extra_cls="", panel=False):
    dots = "".join(f'<i class="{"on" if i==idx else ""}"></i>' for i in range(total))
    swipe = "arrasta →" if idx < total-1 else "@msluzsolar"
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{extra_cls}"><div class="top"></div><div class="glow"></div>{PANEL_SVG if panel else ''}
<div class="head"><div class="brand">{SUN_SVG}<div><b>MS LUZ <span>SOLAR</span></b><small>Energia solar · DF e Goiás</small></div></div><div class="phone">{PHONE}</div></div>
<div class="main">{inner}</div>
<div class="foot"><div class="dots">{dots}</div><div class="swipe">{swipe}</div></div></body></html>"""

def build(item):
    pages = []
    c = item["cover"]
    total = len(item["slides"]) + 2
    pages.append(page(f'<div class="tag">{fmt(c["tag"])}</div><h1>{fmt(c["title"])}</h1><div class="sub">{fmt(c["sub"])}</div>', 0, total, panel=True))
    for i, s in enumerate(item["slides"], 1):
        if s.get("kind") == "stat":
            inner = f'<div class="card"><div class="big">{fmt(s["big"])}</div><h2>{fmt(s["t"])}</h2><div class="desc">{fmt(s["d"])}</div></div>'
        else:
            inner = f'<div class="num">{fmt(s.get("n", f"{i:02d}"))}</div><h2>{fmt(s["t"])}</h2><div class="desc">{fmt(s["d"])}</div>'
        pages.append(page(inner, i, total))
    k = item.get("cta", {})
    title = k.get("title", "Quer saber *quanto você economiza*?")
    sub = k.get("sub", "Envie uma foto da sua conta de luz e receba uma simulação gratuita e sem compromisso.")
    pages.append(page(f'<h1 style="font-size:84px">{fmt(title)}</h1><div class="sub">{fmt(sub)}</div><div class="btn">WhatsApp {PHONE}</div><div class="small">Atendemos DF e Entorno · Luziânia-GO</div>', total-1, total, "cta", panel=True))
    return pages

def render(items):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for item in items:
            for i, h in enumerate(build(item), 1):
                pg.set_content(h); pg.wait_for_timeout(150)
                out = os.path.join(BASE, f'{item["id"]}_{i:02d}.jpg')
                pg.screenshot(path=out, type="jpeg", quality=92)
                print(out)
        b.close()

if __name__ == "__main__":
    bank = json.load(open(os.path.join(BASE, "banco.json"), encoding="utf-8"))
    ids = sys.argv[1:]
    if ids:
        sel = [x for x in bank if x["id"] in ids]
    else:
        sel = [x for x in bank if not os.path.exists(os.path.join(BASE, f'{x["id"]}_01.jpg'))]
    render(sel)
