#!/usr/bin/env python3
"""Gera o site estático da MS Luz Solar (msluzsolar.com.br).

PREVIEW=True  -> publica em rodrigoxsantos10-del.github.io/msluzsolar/ com noindex (evita conteúdo duplicado)
PREVIEW=False -> versão final para o domínio próprio (index liberado, caminhos na raiz)
Uso: python3 build.py [--final]
"""
import json, os, sys, html

FINAL = "--final" in sys.argv
DOMAIN = "https://msluzsolar.com.br"
BASE = "/" if FINAL else "/msluzsolar/"
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WA_NUM = "5561981214135"
PHONE = "(61) 98121-4135"
IG = "https://www.instagram.com/msluzsolar/"
FB = "https://www.facebook.com/439498825905526"

def wa(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WA_NUM}?text={quote(msg)}"

CIDADES = [
    {"slug": "luziania", "nome": "Luziânia", "uf": "GO", "texto": "Somos de Luziânia e atendemos todos os setores da cidade — Centro, Jardim Ingá, Parque Estrela Dalva, Mingone, Setor Norte e região rural. Com sol forte praticamente o ano todo, Luziânia tem ótimo potencial de geração solar para casas, comércios e propriedades rurais."},
    {"slug": "brasilia-df", "nome": "Brasília", "uf": "DF", "texto": "Atendemos residências, comércios e empresas no Distrito Federal: Plano Piloto, Gama, Santa Maria, Samambaia, Taguatinga, Ceilândia, Águas Claras, Park Way, Jardim Botânico e demais regiões administrativas. O DF tem uma das melhores irradiações solares do país."},
    {"slug": "valparaiso-de-goias", "nome": "Valparaíso de Goiás", "uf": "GO", "texto": "Levamos energia solar para casas e comércios de Valparaíso de Goiás, com projeto personalizado, homologação na distribuidora e instalação feita por equipe qualificada."},
    {"slug": "cidade-ocidental", "nome": "Cidade Ocidental", "uf": "GO", "texto": "Em Cidade Ocidental, no Jardim ABC e região, ajudamos famílias e empresas a reduzir a conta de luz com sistemas fotovoltaicos dimensionados pelo consumo real de cada imóvel."},
    {"slug": "jardim-inga-luziania", "nome": "Jardim Ingá", "uf": "GO", "texto": "Atendemos o Jardim Ingá e bairros vizinhos em Luziânia — Parque Nápolis, Pedregal, Mandu e região — com simulação gratuita, projeto personalizado, homologação na distribuidora e instalação por equipe qualificada, aqui pertinho de você."},
    {"slug": "cristalina", "nome": "Cristalina", "uf": "GO", "texto": "Em Cristalina, além de residências e comércios, atendemos propriedades rurais: irrigação, bombeamento, granjas e armazéns, com opção de instalação em solo."},
]

FAQ = [
    ("Quanto custa um sistema de energia solar?", "Depende do seu consumo. Por isso fazemos uma simulação gratuita a partir da sua conta de luz: você recebe o tamanho do sistema, o investimento, a economia estimada e o tempo de retorno."),
    ("Em quanto tempo o sistema se paga?", "Na maioria dos projetos residenciais e comerciais, o retorno acontece em poucos anos, só com a economia na conta. Depois disso, a economia segue por décadas — as placas têm garantia de performance de até 25 anos."),
    ("A conta de luz zera?", "Não totalmente. Continuam a taxa mínima (custo de disponibilidade), a iluminação pública e parte dos encargos de uso da rede previstos na Lei 14.300. Mesmo assim, a redução é grande."),
    ("Preciso de bateria?", "Não. No sistema conectado à rede (on-grid), a energia que sobra durante o dia vira crédito na distribuidora e é usada à noite ou nos meses seguintes, com validade de até 60 meses."),
    ("Funciona em dia nublado ou chuvoso?", "Sim, com geração menor. O sistema é dimensionado pela média do ano inteiro, então os dias de muito sol compensam os nublados."),
    ("Quem cuida da aprovação na distribuidora?", "Nós. O projeto, a documentação técnica e a homologação junto à distribuidora fazem parte do serviço."),
    ("Dá para financiar?", "Sim. Existem linhas de financiamento específicas para energia solar, e em muitos casos a parcela fica próxima do valor que você já paga de luz. Simulamos as opções para você."),
    ("Posso usar a energia em outro imóvel?", "Sim, pelo autoconsumo remoto: os créditos podem abater a conta de outro imóvel no mesmo CPF/CNPJ e na área da mesma distribuidora."),
]

ICONS = {
 "home": '<path d="M3 11.5 12 4l9 7.5"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>',
 "store": '<path d="M4 9h16l-1-5H5z"/><path d="M5 9v11h14V9"/><path d="M9 20v-6h6v6"/>',
 "farm": '<path d="M3 21h18"/><path d="M5 21V11l7-5 7 5v10"/><path d="M9 21v-6h6v6"/><path d="M12 6V3"/>',
 "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 "shield": '<path d="M12 3 5 6v6c0 4.5 3 7.5 7 9 4-1.5 7-4.5 7-9V6z"/><path d="m9 12 2 2 4-4"/>',
 "chart": '<path d="M4 20V10"/><path d="M10 20V4"/><path d="M16 20v-7"/><path d="M22 20H2"/>',
 "leaf": '<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19 13 11"/>',
 "doc": '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5"/><path d="M9 13h7M9 17h5"/>',
 "tool": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
 "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "wallet": '<path d="M3 7h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M3 7V6a2 2 0 0 1 2-2h11"/><circle cx="16.5" cy="13.5" r="1.2"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
}
def ic(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.8.9 3.8.8a3.3 3.3 0 0 0 2.2-1.5 2.7 2.7 0 0 0 .2-1.5c-.1-.2-.3-.3-.6-.4z"/></svg>'

LOGO = '''<svg class="logo-mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="11" fill="#0A2342"/><circle cx="20" cy="17" r="6" fill="#FFB703"/><g stroke="#FFB703" stroke-width="2.4" stroke-linecap="round"><path d="M20 5v3M20 26v3M8 17h3M29 17h3M11.5 8.5l2 2M26.5 23.5l2 2M11.5 25.5l2-2M26.5 10.5l2-2"/></g><path d="M9 33h22" stroke="#CFE3F7" stroke-width="2.4" stroke-linecap="round"/></svg>'''

HERO_SVG = '''<svg class="hero-art" viewBox="0 0 560 460" role="img" aria-label="Casa com placas de energia solar no telhado">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE8B0"/><stop offset="1" stop-color="#FFF8E7"/></linearGradient>
<linearGradient id="pv" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1B4B8F"/><stop offset="1" stop-color="#0A2342"/></linearGradient>
<clipPath id="hc"><rect width="560" height="460" rx="32"/></clipPath><radialGradient id="sunG"><stop offset="0" stop-color="#FFD166"/><stop offset="1" stop-color="#FFB703"/></radialGradient></defs>
<g clip-path="url(#hc)"><rect x="0" y="0" width="560" height="460" fill="url(#sky)"/>
<g class="sun-rays" transform="translate(440 92)"><circle r="44" fill="url(#sunG)"/>
<g stroke="#FFB703" stroke-width="7" stroke-linecap="round"><path d="M0-66v-16M0 66v16M-66 0h-16M66 0h16M-47-47l-11-11M47 47l11 11M-47 47l-11 11M47-47l11-11"/></g></g>
<path d="M0 380 Q140 340 280 372 T560 360 V460 H0Z" fill="#CDE7C4"/>
<rect x="108" y="236" width="300" height="164" fill="#FFFFFF"/>
<path d="M88 244 L258 132 L428 244Z" fill="#0A2342"/>
<g transform="translate(150 158) skewX(-33) scale(1 .82)">
<g fill="url(#pv)" stroke="#9CC3EA" stroke-width="2">
<rect x="40" y="10" width="52" height="34" rx="3"/><rect x="96" y="10" width="52" height="34" rx="3"/><rect x="152" y="10" width="52" height="34" rx="3"/>
<rect x="40" y="48" width="52" height="34" rx="3"/><rect x="96" y="48" width="52" height="34" rx="3"/><rect x="152" y="48" width="52" height="34" rx="3"/></g></g>
<rect x="232" y="306" width="54" height="94" rx="4" fill="#FB8500"/>
<rect x="140" y="276" width="60" height="50" rx="4" fill="#CFE3F7"/><rect x="322" y="276" width="60" height="50" rx="4" fill="#CFE3F7"/>
</g><g class="spark"><path d="M470 300l-26 38h20l-8 30 28-42h-20z" fill="#FFB703"/></g>
<rect x="24" y="24" width="190" height="64" rx="16" fill="#fff" opacity=".95"/>
<text x="44" y="52" font-family="Inter,Arial" font-size="15" fill="#5B6B82">Economia na conta</text>
<text x="44" y="76" font-family="Inter,Arial" font-weight="800" font-size="22" fill="#0A2342">até 90%</text>
</svg>'''

CSS = r"""
:root{--navy:#0A2342;--navy2:#12345E;--sun:#FFB703;--orange:#FB8500;--sky:#CFE3F7;--ink:#0F1B2D;--muted:#5B6B82;--bg:#FFFFFF;--soft:#F4F7FB;--line:#E3E9F2;--green:#1FA855;--r:20px}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased}
img,svg{display:block;max-width:100%}
a{color:inherit}
.wrap{width:min(1160px,100% - 32px);margin-inline:auto}
.ic{width:26px;height:26px}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:16px;background:#fff;padding:8px 12px;z-index:99}
/* header */
.top{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.92);backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;height:68px;gap:16px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:900;font-size:19px;letter-spacing:-.3px;color:var(--navy)}
.brand span{color:var(--orange)} .logo-mark{width:38px;height:38px}
.nav{display:flex;gap:26px;font-size:15px;font-weight:600}
.nav a{text-decoration:none;color:var(--muted)} .nav a:hover{color:var(--navy)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;font-weight:800;text-decoration:none;border-radius:14px;padding:15px 24px;font-size:16px;border:0;cursor:pointer;transition:transform .15s,box-shadow .15s;font-family:inherit}
.btn:hover{transform:translateY(-2px)}
.btn svg{width:22px;height:22px}
.btn-wa{background:var(--green);color:#fff;box-shadow:0 10px 24px -10px rgba(31,168,85,.7)}
.btn-sun{background:var(--sun);color:var(--navy);box-shadow:0 10px 24px -10px rgba(251,133,0,.7)}
.btn-ghost{background:transparent;color:var(--navy);border:2px solid var(--line)}
.top .btn{padding:10px 16px;font-size:14px}
/* hero */
.hero{background:radial-gradient(900px 500px at 85% -10%,rgba(255,183,3,.22),transparent 60%),linear-gradient(180deg,#FFFDF6,#fff);padding:64px 0 72px}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center}
.pill{display:inline-flex;align-items:center;gap:8px;background:#FFF1CC;color:#8A5A00;font-weight:700;font-size:14px;border-radius:99px;padding:7px 14px}
.pill svg{width:18px;height:18px}
h1{font-size:clamp(36px,5.2vw,60px);line-height:1.05;letter-spacing:-1.8px;color:var(--navy);margin:18px 0 18px;font-weight:900}
h1 em,h2 em{font-style:normal;color:var(--orange)}
.lead{font-size:clamp(17px,1.6vw,20px);color:var(--muted);max-width:560px}
.cta-row{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.trust{display:flex;flex-wrap:wrap;gap:18px 28px;margin-top:30px;color:var(--muted);font-size:14.5px;font-weight:600}
.trust div{display:flex;align-items:center;gap:8px}.trust svg{width:20px;height:20px;color:var(--green)}
.hero-art{width:100%;height:auto;filter:drop-shadow(0 30px 50px rgba(10,35,66,.18))}
.sun-rays{animation:spin 40s linear infinite;transform-box:fill-box;transform-origin:center}
@keyframes spin{to{rotate:360deg}}
@media (prefers-reduced-motion:reduce){.sun-rays{animation:none}}
/* sections */
section{padding:84px 0}
.alt{background:var(--soft)}
.dark{background:var(--navy);color:#fff}
.eyebrow{font-size:14px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:var(--orange)}
h2{font-size:clamp(28px,3.6vw,42px);line-height:1.12;letter-spacing:-1px;color:var(--navy);margin:10px 0 14px;font-weight:900}
.dark h2{color:#fff}
.sec-lead{color:var(--muted);font-size:18px;max-width:640px}
.dark .sec-lead{color:var(--sky)}
.grid{display:grid;gap:20px;margin-top:40px}
.g3{grid-template-columns:repeat(3,1fr)} .g4{grid-template-columns:repeat(4,1fr)} .g2{grid-template-columns:repeat(2,1fr)}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px}
.card .ic-box{width:52px;height:52px;border-radius:14px;background:#FFF1CC;color:var(--orange);display:grid;place-items:center;margin-bottom:18px}
.card h3{font-size:20px;color:var(--navy);margin-bottom:8px;letter-spacing:-.3px}
.card p{color:var(--muted);font-size:15.5px}
.card ul{list-style:none;margin-top:14px;display:grid;gap:8px;color:var(--ink);font-size:15px}
.card li{padding-left:24px;position:relative}
.card li:before{content:"";position:absolute;left:0;top:7px;width:14px;height:14px;border-radius:50%;background:var(--sun)}
.card .more{display:inline-block;margin-top:16px;font-weight:800;color:var(--navy);text-decoration:none}
/* simulador */
.sim{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:40px;align-items:stretch}
.sim-box{background:#fff;color:var(--ink);border-radius:24px;padding:32px}
.sim-box label{font-weight:800;color:var(--navy);display:block;margin-bottom:10px}
.money{display:flex;align-items:center;border:2px solid var(--line);border-radius:14px;padding:0 16px;font-size:24px;font-weight:800;color:var(--navy)}
.money:focus-within{border-color:var(--sun)}
.money input{border:0;outline:0;font:inherit;width:100%;padding:14px 8px;color:inherit;background:transparent}
input[type=range]{width:100%;margin:22px 0 6px;accent-color:var(--orange)}
.range-l{display:flex;justify-content:space-between;font-size:13px;color:var(--muted)}
.seg{display:flex;gap:8px;margin-top:22px;flex-wrap:wrap}
.seg button{flex:1;min-width:90px;border:2px solid var(--line);background:#fff;border-radius:12px;padding:10px;font:inherit;font-weight:700;color:var(--muted);cursor:pointer}
.seg button[aria-pressed=true]{border-color:var(--sun);background:#FFF8E5;color:var(--navy)}
.sim-res{background:linear-gradient(160deg,#12345E,#0A2342);border:1px solid rgba(207,227,247,.2);border-radius:24px;padding:32px;display:flex;flex-direction:column}
.res-big{font-size:clamp(38px,5vw,54px);font-weight:900;color:var(--sun);letter-spacing:-1.5px;line-height:1.05}
.res-lbl{color:var(--sky);font-size:15px}
.res-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:24px 0}
.res-grid div{background:rgba(255,255,255,.06);border-radius:14px;padding:14px 16px}
.res-grid b{display:block;font-size:22px;color:#fff}
.res-grid span{font-size:13px;color:var(--sky)}
.note{font-size:12.5px;color:var(--sky);opacity:.85;margin-top:auto;padding-top:14px}
.incl{list-style:none;margin-top:26px;display:grid;gap:10px;font-size:15px;color:var(--ink)}
.incl li{padding-left:28px;position:relative}.incl li:before{content:"✓";position:absolute;left:0;top:0;width:20px;height:20px;border-radius:50%;background:#E3F6EA;color:var(--green);font-weight:900;font-size:13px;display:grid;place-items:center}
.hp{position:absolute;left:-9999px}
.lgpd{display:flex!important;gap:10px;align-items:flex-start;font-weight:500!important;color:var(--muted)!important;font-size:13.5px!important}
.lgpd input{width:18px!important;height:18px;margin-top:2px;flex:none;accent-color:var(--orange)}
.st{font-size:14.5px;color:var(--navy);font-weight:600}.st a{color:var(--green)}
.map{margin-top:22px;border-radius:18px;overflow:hidden;border:1px solid var(--line);aspect-ratio:16/10}
.map iframe{width:100%;height:100%;border:0;display:block}
.cred{display:flex;gap:16px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:22px;margin-top:28px}
.cred .ic-box{width:52px;height:52px;border-radius:14px;background:var(--navy);color:var(--sun);display:grid;place-items:center;flex:none}
/* passos */
.steps{counter-reset:s;display:grid;grid-template-columns:repeat(5,1fr);gap:18px;margin-top:40px}
.step{position:relative;padding:24px;border-radius:var(--r);background:#fff;border:1px solid var(--line)}
.step:before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:40px;height:40px;border-radius:12px;background:var(--navy);color:var(--sun);font-weight:900;margin-bottom:14px}
.step h3{font-size:17px;color:var(--navy);margin-bottom:6px}.step p{font-size:14.5px;color:var(--muted)}
/* números */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px}
.stat{border-left:4px solid var(--sun);padding:6px 0 6px 18px}
.stat b{display:block;font-size:clamp(30px,3.5vw,42px);font-weight:900;color:#fff;letter-spacing:-1px}
.stat span{color:var(--sky);font-size:15px}
/* faq */
.faq{margin-top:36px;display:grid;gap:12px;max-width:860px}
details{background:#fff;border:1px solid var(--line);border-radius:16px;padding:0 22px}
summary{cursor:pointer;list-style:none;font-weight:800;color:var(--navy);padding:20px 30px 20px 0;position:relative;font-size:17px}
summary::-webkit-details-marker{display:none}
summary:after{content:"+";position:absolute;right:0;top:14px;font-size:28px;color:var(--orange);font-weight:400}
details[open] summary:after{content:"–"}
details p{padding:0 0 20px;color:var(--muted)}
/* contato */
.contact{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:40px}
form{background:#fff;border:1px solid var(--line);border-radius:24px;padding:30px;display:grid;gap:16px}
form label{font-weight:700;font-size:14px;color:var(--navy);display:grid;gap:6px}
form input,form select,form textarea{font:inherit;border:2px solid var(--line);border-radius:12px;padding:12px 14px;color:var(--ink);background:#fff;width:100%}
form input:focus,form select:focus,form textarea:focus{outline:0;border-color:var(--sun)}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.ch{display:grid;gap:14px}
.ch a{display:flex;align-items:center;gap:16px;text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px}
.ch a:hover{border-color:var(--sun)}
.ch .ico{width:50px;height:50px;border-radius:14px;display:grid;place-items:center;flex:none}
.ch b{display:block;color:var(--navy)} .ch span{color:var(--muted);font-size:14.5px}
.cities{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.cities a{text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:99px;padding:9px 16px;font-weight:700;font-size:14.5px;color:var(--navy);display:inline-flex;gap:6px;align-items:center}
.cities a svg{width:17px;height:17px;color:var(--orange)}
.cities a:hover{border-color:var(--sun)}
/* cta final + footer */
.final{background:linear-gradient(120deg,var(--sun),var(--orange));color:var(--navy);border-radius:28px;padding:48px;display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.final h2{color:var(--navy);margin:0}
.final p{font-weight:600;margin-top:10px}
footer{background:var(--navy);color:var(--sky);padding:56px 0 100px;font-size:14.5px}
footer .wrap{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:32px}
footer b{color:#fff;display:block;margin-bottom:10px}
footer a{color:var(--sky);text-decoration:none;display:block;margin:5px 0} footer a:hover{color:#fff}
.copy{grid-column:1/-1;border-top:1px solid rgba(207,227,247,.15);padding-top:20px;font-size:13px}
.float{position:fixed;right:18px;bottom:18px;z-index:60;width:62px;height:62px;border-radius:50%;background:var(--green);color:#fff;display:grid;place-items:center;box-shadow:0 12px 30px -8px rgba(0,0,0,.35)}
.float svg{width:34px;height:34px}
.crumbs{font-size:14px;color:var(--muted);margin-bottom:6px}.crumbs a{color:var(--muted)}
/* responsivo */
@media (max-width:980px){
 .hero .wrap,.sim,.contact{grid-template-columns:1fr}
 .g3,.g4,.stats{grid-template-columns:1fr 1fr}
 .steps{grid-template-columns:1fr 1fr}
 .nav{display:none}
 footer .wrap{grid-template-columns:1fr 1fr}
}
@media (max-width:620px){
 section{padding:60px 0}
 .hero{padding:36px 0 52px}
 .g3,.g4,.g2,.steps,.row2,.res-grid{grid-template-columns:1fr}
 .stats{grid-template-columns:1fr 1fr}
 .cta-row .btn{width:100%}
 .final{padding:30px 22px}
 .final .btn{width:100%}
 footer .wrap{grid-template-columns:1fr}
 .top .btn span{display:none}
 .sim-box,.sim-res,form{padding:22px}
}
"""

JS = r"""
(function(){
 const fmt=v=>v.toLocaleString('pt-BR',{style:'currency',currency:'BRL',maximumFractionDigits:0});
 const inp=document.getElementById('conta'),rng=document.getElementById('contaR');
 if(!inp)return;
 let tipo='residencial';
 // Premissas conservadoras (estimativa): tarifa média c/ impostos ~R$ 1,00/kWh; geração média ~120 kWh/mês por kWp no DF/GO;
 // economia de 75% a 90% do valor da conta (permanecem taxa mínima, iluminação pública e encargos de rede).
 function calc(){
  let v=parseFloat(String(inp.value).replace(/\D/g,''))||0;
  const kwh=v/1.0, kwp=Math.max(kwh/120,0), placas=Math.ceil(kwp*1000/580);
  const eMin=v*.75, eMax=v*.90;
  document.getElementById('rMes').textContent=v?fmt(eMin)+' a '+fmt(eMax):'—';
  document.getElementById('rAno').textContent=v?fmt(eMin*12)+'+':'—';
  document.getElementById('r25').textContent=v?fmt(eMin*12*25)+'+':'—';
  document.getElementById('rKwp').textContent=v?kwp.toFixed(1).replace('.',',')+' kWp':'—';
  document.getElementById('rPlacas').textContent=v?('≈ '+placas+' placas'):'—';
  const msg=`Olá! Fiz a simulação no site da MS Luz Solar. Minha conta de luz é de ${fmt(v)} por mês (${tipo}). Quero uma proposta de energia solar.`;
  document.getElementById('simWa').href='https://wa.me/WA_NUM?text='+encodeURIComponent(msg);
 }
 inp.addEventListener('input',()=>{rng.value=parseFloat(inp.value.replace(/\D/g,''))||0;calc()});
 rng.addEventListener('input',()=>{inp.value=rng.value;calc()});
 document.querySelectorAll('.seg button').forEach(b=>b.addEventListener('click',()=>{
  document.querySelectorAll('.seg button').forEach(x=>x.setAttribute('aria-pressed','false'));
  b.setAttribute('aria-pressed','true');tipo=b.dataset.t;calc();}));
 calc();
 const f=document.getElementById('orc');
 const WEBHOOK='https://hook.us2.make.com/gjjw1e8e20fba1ljsn7djqrvyji3e2un';
 f&&f.addEventListener('submit',e=>{e.preventDefault();
  const st=document.getElementById('orc-st'),btn=f.querySelector('button[type=submit]');
  if(f.empresa_site.value)return;
  let tel=f.telefone.value.replace(/\D/g,'');if(tel.indexOf('55')!==0)tel='55'+tel;
  if(!f.nome.value.trim()||!f.aceite.checked||tel.length<12||tel.length>13||!f.valor.value.trim()){st.textContent='Confira nome, telefone, valor da conta e o aceite.';return;}
  const d=new FormData(f);
  const msg=`Olá! Quero uma simulação de energia solar.\nNome: ${d.get('nome')}\nCidade: ${d.get('cidade')}\nTipo de imóvel: ${d.get('tipo')}\nValor médio da conta: R$ ${d.get('valor')}${d.get('obs')?'\nObs.: '+d.get('obs'):''}`;
  const wa='https://wa.me/WA_NUM?text='+encodeURIComponent(msg);
  const p=new URLSearchParams({empresa:'MS Luz Solar',nome:f.nome.value.trim(),telefone:tel,cidade:d.get('cidade'),
   tipo_servico:'Energia solar - '+d.get('tipo'),valor_conta:d.get('valor'),obs:d.get('obs')||'',origem:location.href,
   gclid:new URLSearchParams(location.search).get('gclid')||'',data_envio:new Date().toISOString()});
  btn.disabled=true;st.textContent='Enviando...';
  const c=new AbortController(),t=setTimeout(()=>c.abort(),8000);
  fetch(WEBHOOK,{method:'POST',mode:'no-cors',body:p,signal:c.signal})
   .then(()=>{st.innerHTML='Recebemos sua solicitação! Para agilizar, <a href="'+wa+'" target="_blank" rel="noopener">continue no WhatsApp</a>.';f.reset();
     if(window.gtag)gtag('event','conversion',{'send_to':'AW-11471703423/8kKYCIWuragdEP-akd4q'});if(window.gtag)gtag('event','generate_lead',{empresa:'MS Luz Solar'});})
   .catch(()=>{st.textContent='Abrindo o WhatsApp para você...';window.open(wa,'_blank');})
   .finally(()=>{clearTimeout(t);btn.disabled=false;});});
 // conversões: cliques no WhatsApp e no telefone (mesmas ações do Google Ads da MS)
 document.addEventListener('click',e=>{const a=e.target.closest&&e.target.closest('a[href]');if(!a||typeof gtag!=='function')return;
  const h=a.getAttribute('href')||'';
  if(h.indexOf('https://wa.me/')===0)gtag('event','conversion',{'send_to':'AW-11471703423/no1fCM-0yZIdEP-akd4q'});
  else if(h.indexOf('tel:')===0)gtag('event','conversion',{'send_to':'AW-11471703423/o9v9CNK0yZIdEP-akd4q'});},true);
})();
""".replace("WA_NUM", WA_NUM)

def head(title, desc, path, extra_ld=None):
    url = DOMAIN + path
    robots = '<meta name="robots" content="index,follow,max-image-preview:large">' if FINAL else '<meta name="robots" content="noindex">'
    ld = [{
        "@context": "https://schema.org", "@type": "LocalBusiness", "@id": DOMAIN + "/#empresa",
        "name": "MS Luz Solar", "description": "Projeto, homologação e instalação de sistemas de energia solar fotovoltaica no DF e Entorno.",
        "url": DOMAIN + "/", "telephone": "+55 61 98121-4135", "image": DOMAIN + "/og.jpg", "logo": DOMAIN + "/logo.svg",
        "priceRange": "$$", "taxID": "56.964.600/0001-24", "address": {"@type": "PostalAddress", "addressLocality": "Luziânia", "addressRegion": "GO", "addressCountry": "BR"},
        "areaServed": [{"@type": "City", "name": f'{c["nome"]} - {c["uf"]}'} for c in CIDADES],
        "sameAs": [IG, FB],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "07:00", "closes": "19:00"}],
        "legalName": "MS Manutenção Residencial e Industrial", "inLanguage": "pt-BR",
        "contactPoint": {"@type": "ContactPoint", "telephone": "+55-61-98121-4135", "contactType": "customer service", "areaServed": ["BR-GO", "BR-DF"], "availableLanguage": "pt-BR"},
        "founder": {"@type": "Person", "name": "Rodrigo Xavier dos Santos", "jobTitle": "Eletrotécnico", "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "Registro profissional CREA", "identifier": "06870181616"}},
        "hasMap": "https://www.google.com/maps/search/?api=1&query=Luzi%C3%A2nia+GO",
        "geo": {"@type": "GeoCoordinates", "latitude": -16.2525, "longitude": -47.9501},
        "knowsAbout": ["Energia solar fotovoltaica", "Sistemas on-grid", "Homologação na distribuidora", "Autoconsumo remoto", "Energia solar rural"],
    }]
    if extra_ld: ld += extra_ld
    return f"""<!doctype html>
<html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{robots}
<link rel="canonical" href="{url}">
<meta name="geo.region" content="BR-GO"><meta name="geo.placename" content="Luziânia">
<meta name="keywords" content="energia solar Luziânia, energia solar Brasília, placa solar Luziânia, energia solar Valparaíso, energia solar Cidade Ocidental, energia solar Cristalina, energia solar Jardim Ingá, painel solar DF, energia solar rural, financiamento energia solar">
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-11471703423"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','AW-11471703423');gtag('config','G-Q1MKHZCG7Z');</script>
<meta name="theme-color" content="#0A2342">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="MS Luz Solar">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{DOMAIN}/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}estilo.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head><body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="top"><div class="wrap">
<a class="brand" href="{BASE}" aria-label="MS Luz Solar — início">{LOGO}MS Luz <span>Solar</span></a>
<nav class="nav" aria-label="Principal"><a href="{BASE}#beneficios">Benefícios</a><a href="{BASE}#simulador">Simulador</a><a href="{BASE}#como-funciona">Como funciona</a><a href="{BASE}#duvidas">Dúvidas</a><a href="{BASE}#contato">Contato</a></nav>
<a class="btn btn-wa" href="{wa('Olá! Vim pelo site da MS Luz Solar e quero uma simulação de energia solar.')}" target="_blank" rel="noopener">{WA_SVG}<span>Falar no WhatsApp</span></a>
</div></header>
<main id="conteudo">
"""

def foot():
    cid = "".join(f'<a href="{BASE}energia-solar-{c["slug"]}/">Energia solar em {c["nome"]}</a>' for c in CIDADES)
    return f"""</main>
<footer><div class="wrap">
<div><a class="brand" href="{BASE}" style="color:#fff">{LOGO}MS Luz <span>Solar</span></a>
<p style="margin-top:14px;max-width:360px">Energia solar fotovoltaica para casas, empresas e propriedades rurais no DF e Entorno. Projeto, homologação e instalação.</p></div>
<div><b>Atendimento</b><a href="{wa('Olá! Vim pelo site da MS Luz Solar.')}" target="_blank" rel="noopener">WhatsApp {PHONE}</a><a href="tel:+5561981214135">Ligar: {PHONE}</a><a href="{IG}" target="_blank" rel="noopener">Instagram @msluzsolar</a><a href="{FB}" target="_blank" rel="noopener">Facebook</a><span style="display:block;margin-top:5px">Seg a sáb, 7h às 19h</span></div>
<div><b>Cidades atendidas</b>{cid}</div>
<div class="copy">© 2026 MS Luz Solar · CNPJ 56.964.600/0001-24 · Responsável técnico: Rodrigo Xavier dos Santos, Eletrotécnico — CREA 06870181616 · Luziânia-GO · <a style="display:inline" href="{BASE}privacidade.html">Política de Privacidade</a> · <a style="display:inline" href="{BASE}termos.html">Termos de Uso</a> · Estimativas do simulador são aproximadas e não substituem a proposta técnica.</div>
</div></footer>
<a class="float" href="{wa('Olá! Vim pelo site da MS Luz Solar e quero uma simulação de energia solar.')}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{WA_SVG}</a>
<script src="{BASE}app.js" defer></script>
</body></html>"""

def sec_beneficios():
    items = [("wallet","Conta de luz até 90% menor","A energia gerada no seu telhado abate o consumo. Fica basicamente a taxa mínima e encargos."),
             ("chart","Proteção contra reajustes","A tarifa sobe todo ano. Quem gera a própria energia fica muito menos exposto a aumentos e bandeiras."),
             ("bolt","Investimento que se paga","Com a economia mensal, o sistema se paga em poucos anos e segue gerando por décadas."),
             ("shield","Garantia de longo prazo","Placas com garantia de performance de até 25 anos e inversores com garantia de fábrica."),
             ("home","Imóvel mais valorizado","Conta baixa é argumento forte na venda ou no aluguel do imóvel."),
             ("leaf","Energia limpa","Geração sem emissões. Economia para você e respeito ao meio ambiente.")]
    cards = "".join(f'<div class="card"><div class="ic-box">{ic(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in items)
    return f'<section id="beneficios"><div class="wrap"><div class="eyebrow">Por que energia solar</div><h2>Pare de pagar caro pela luz. <em>Gere a sua.</em></h2><p class="sec-lead">Energia solar deixou de ser luxo: hoje é a forma mais inteligente de reduzir um custo que só aumenta.</p><div class="grid g3">{cards}</div></div></section>'

def sec_simulador():
    return f'''<section id="simulador" class="dark"><div class="wrap"><div class="eyebrow">Simulador gratuito</div><h2>Quanto você pode <em>economizar</em>?</h2><p class="sec-lead">Digite o valor médio da sua conta de luz e veja uma estimativa na hora.</p>
<div class="sim"><div class="sim-box">
<label for="conta">Valor médio da conta de luz (por mês)</label>
<div class="money">R$<input id="conta" inputmode="numeric" autocomplete="off" value="450" aria-describedby="nota-sim"></div>
<input id="contaR" type="range" min="100" max="5000" step="10" value="450" aria-label="Ajustar valor da conta">
<div class="range-l"><span>R$ 100</span><span>R$ 5.000+</span></div>
<div class="seg" role="group" aria-label="Tipo de imóvel"><button type="button" data-t="residencial" aria-pressed="true">Casa</button><button type="button" data-t="comercial" aria-pressed="false">Empresa</button><button type="button" data-t="rural" aria-pressed="false">Rural</button></div>
<ul class="incl"><li>Simulação e proposta sem custo</li><li>Projeto técnico e homologação na distribuidora</li><li>Instalação por equipe qualificada</li><li>Opções de pagamento e financiamento</li></ul>
</div>
<div class="sim-res" aria-live="polite"><span class="res-lbl">Economia estimada por mês</span><div class="res-big" id="rMes">—</div>
<div class="res-grid"><div><b id="rAno">—</b><span>economia por ano</span></div><div><b id="r25">—</b><span>em 25 anos (sem reajustes)</span></div><div><b id="rKwp">—</b><span>potência aproximada</span></div><div><b id="rPlacas">—</b><span>módulos de ~580 W</span></div></div>
<a id="simWa" class="btn btn-wa" href="#" target="_blank" rel="noopener">{WA_SVG}Receber proposta exata no WhatsApp</a>
<p class="note" id="nota-sim">Estimativa aproximada (tarifa média de R$ 1,00/kWh e geração típica do DF/GO). A proposta real considera seu histórico de consumo, telhado e distribuidora.</p></div></div></div></section>'''

def sec_solucoes():
    s = [("home","Residencial","Para casas e sobrados que querem reduzir a conta da família.",["Ar-condicionado e chuveiro sem medo da conta","Instalação no telhado com fixação adequada","Acompanhamento da geração pelo app"]),
         ("store","Empresas e comércio","Para quem quer cortar custo fixo e ganhar previsibilidade.",["Comércios, oficinas, clínicas, indústrias","Consumo no horário de sol = retorno mais rápido","Imagem de empresa sustentável"]),
         ("farm","Rural e agronegócio","Para chácaras, fazendas e produtores do Entorno.",["Irrigação, bombeamento, ordenha, granjas","Instalação em solo quando o telhado não ajuda","Créditos podem abater outro imóvel do titular"])]
    cards = "".join(f'<div class="card"><div class="ic-box">{ic(i)}</div><h3>{t}</h3><p>{d}</p><ul>{"".join(f"<li>{x}</li>" for x in l)}</ul><a class="more" href="{wa(f"Olá! Tenho interesse em energia solar {t.lower()}.")}" target="_blank" rel="noopener">Quero uma simulação →</a></div>' for i,t,d,l in s)
    return f'<section id="solucoes" class="alt"><div class="wrap"><div class="eyebrow">Soluções</div><h2>Energia solar para <em>cada tipo de imóvel</em></h2><p class="sec-lead">Cada projeto é dimensionado pelo consumo real — nada de sistema “no olho”.</p><div class="grid g3">{cards}</div></div></section>'

def sec_passos():
    p = [("Envie sua conta","Uma foto da conta de luz pelo WhatsApp já basta para começar."),
         ("Simulação gratuita","Calculamos o sistema ideal, a economia e o tempo de retorno."),
         ("Proposta clara","Equipamentos, garantias, prazo e opções de pagamento ou financiamento."),
         ("Projeto e homologação","Cuidamos do projeto técnico e da aprovação na distribuidora."),
         ("Instalação e economia","Equipe qualificada instala com segurança e você acompanha a geração pelo app.")]
    steps = "".join(f'<div class="step"><h3>{t}</h3><p>{d}</p></div>' for t,d in p)
    return f'<section id="como-funciona"><div class="wrap"><div class="eyebrow">Como funciona</div><h2>Do orçamento à economia em <em>5 passos</em></h2><p class="sec-lead">Você manda a conta de luz. A gente cuida do resto.</p><div class="steps">{steps}</div><div class="cred"><div class="ic-box">{ic("shield")}</div><p><b style="color:var(--navy)">Responsabilidade técnica de verdade.</b> Projetos acompanhados por Rodrigo Xavier dos Santos, eletrotécnico registrado no CREA e responsável técnico da MS Manutenção em instalações elétricas residenciais, comerciais e industriais.</p></div></div></section>'

def sec_numeros():
    s = [("até 90%","de redução na conta de luz"),("25 anos","de garantia de performance das placas"),("60 meses","de validade dos créditos de energia"),("0","bateria necessária no sistema on-grid")]
    st = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a,b in s)
    return f'<section class="dark"><div class="wrap"><div class="eyebrow">Energia solar em números</div><h2>Um investimento para <em>décadas</em></h2><div class="stats">{st}</div></div></section>'

def sec_faq():
    q = "".join(f'<details><summary>{html.escape(a)}</summary><p>{html.escape(b)}</p></details>' for a,b in FAQ)
    return f'<section id="duvidas" class="alt"><div class="wrap"><div class="eyebrow">Perguntas frequentes</div><h2>Tire suas <em>dúvidas</em></h2><div class="faq">{q}</div></div></section>'

def sec_contato(cidade_default=""):
    opts = "".join(f'<option{" selected" if c["nome"]==cidade_default else ""}>{c["nome"]} - {c["uf"]}</option>' for c in CIDADES) + "<option>Outra cidade</option>"
    cities = "".join(f'<a href="{BASE}energia-solar-{c["slug"]}/">{ic("pin")}{c["nome"]}</a>' for c in CIDADES)
    return f'''<section id="contato"><div class="wrap"><div class="eyebrow">Contato</div><h2>Peça sua <em>simulação gratuita</em></h2><p class="sec-lead">Responda em 30 segundos e fale direto com um especialista no WhatsApp.</p>
<div class="contact">
<form id="orc" novalidate><input type="text" name="empresa_site" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<label>Seu nome<input name="nome" required autocomplete="name" placeholder="Como podemos te chamar?"></label>
<label>WhatsApp / telefone (com DDD)<input name="telefone" required inputmode="tel" autocomplete="tel" placeholder="(61) 9 0000-0000"></label>
<div class="row2"><label>Cidade<select name="cidade">{opts}</select></label>
<label>Tipo de imóvel<select name="tipo"><option>Casa</option><option>Empresa / comércio</option><option>Propriedade rural</option></select></label></div>
<label>Valor médio da conta de luz (R$)<input name="valor" inputmode="numeric" required placeholder="Ex.: 450"></label>
<label>Observações (opcional)<textarea name="obs" rows="3" placeholder="Ex.: quero instalar no telhado da garagem"></textarea></label>
<label class="lgpd"><input type="checkbox" name="aceite" required><span>Autorizo o uso destes dados para contato sobre a simulação, conforme a <a href="{BASE}privacidade.html">Política de Privacidade</a>.</span></label>
<button class="btn btn-sun" type="submit">Quero minha simulação gratuita</button>
<p id="orc-st" role="status" aria-live="polite" class="st"></p></form>
<div><div class="ch">
<a href="{wa('Olá! Vim pelo site da MS Luz Solar e quero uma simulação de energia solar.')}" target="_blank" rel="noopener"><div class="ico" style="background:#E3F6EA;color:var(--green)">{WA_SVG}</div><div><b>WhatsApp</b><span>{PHONE} · resposta rápida</span></div></a>
<a href="tel:+5561981214135"><div class="ico" style="background:#FFF1CC;color:var(--orange)">{ic("phone")}</div><div><b>Telefone</b><span>{PHONE}</span></div></a>
<a href="{IG}" target="_blank" rel="noopener"><div class="ico" style="background:#FDE7F1;color:#C13584">{ic("sun")}</div><div><b>Instagram</b><span>@msluzsolar · dicas todos os dias</span></div></a>
</div><p style="margin-top:22px;font-weight:800;color:var(--navy)">Atendemos DF e Entorno:</p><div class="cities">{cities}</div>
<div class="map"><iframe title="Mapa da área de atendimento da MS Luz Solar — Luziânia, Entorno e DF" src="https://www.google.com/maps?q=Luzi%C3%A2nia%20-%20GO&z=9&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div>
</div></div></section>'''

def sec_final():
    return f'<section><div class="wrap"><div class="final"><div><h2>Cada mês esperando é uma conta cheia paga.</h2><p>Descubra hoje quanto você pode economizar — sem compromisso.</p></div><a class="btn" style="background:var(--navy);color:#fff" href="{wa("Olá! Quero começar minha simulação de energia solar.")}" target="_blank" rel="noopener">{WA_SVG}Quero economizar</a></div></div></section>'

def hero(h1, lead, pill="Energia solar no DF e Entorno"):
    trust = "".join(f'<div>{ic("shield")}{t}</div>' for t in ["Simulação gratuita","Projeto e homologação inclusos","Equipamentos certificados"])
    return f'''<section class="hero"><div class="wrap"><div>
<span class="pill">{ic("sun")}{pill}</span><h1>{h1}</h1><p class="lead">{lead}</p>
<div class="cta-row"><a class="btn btn-wa" href="{wa('Olá! Vim pelo site da MS Luz Solar e quero uma simulação gratuita de energia solar.')}" target="_blank" rel="noopener">{WA_SVG}Simulação grátis no WhatsApp</a><a class="btn btn-ghost" href="{BASE}#simulador">Calcular minha economia</a><a class="btn btn-ghost" href="tel:+5561981214135">{ic("phone")}Ligar: {PHONE}</a></div>
<div class="trust">{trust}</div></div>{HERO_SVG}</div></section>'''

def faq_ld():
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": a, "acceptedAnswer": {"@type": "Answer", "text": b}} for a,b in FAQ]}

def write(path, content):
    full = os.path.join(OUT, path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

def main():
    write("estilo.css", CSS.strip()); write("app.js", JS.strip())
    write("favicon.svg", LOGO.replace('class="logo-mark" ', 'xmlns="http://www.w3.org/2000/svg" '))
    write("logo.svg", LOGO.replace('class="logo-mark" ', 'xmlns="http://www.w3.org/2000/svg" '))
    idx = head("Energia Solar em Luziânia, DF e Entorno | MS Luz Solar",
               "Reduza sua conta de luz em até 90% com energia solar. Simulação gratuita, projeto, homologação e instalação em Luziânia, Brasília e Entorno do DF. Fale no WhatsApp.",
               "/", [faq_ld()])
    idx += hero("Sua conta de luz <em>até 90% menor</em> com energia solar",
                "Projeto, homologação e instalação de energia solar para casas, empresas e propriedades rurais em Luziânia, Brasília e todo o Entorno do DF.")
    idx += sec_beneficios() + sec_simulador() + sec_solucoes() + sec_passos() + sec_numeros() + sec_faq() + sec_contato() + sec_final() + foot()
    write("index.html", idx)
    urls = [DOMAIN + "/"]
    for c in CIDADES:
        path = f"/energia-solar-{c['slug']}/"
        bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": f"Energia solar em {c['nome']}", "item": DOMAIN + path}]}
        p = head(f"Energia Solar em {c['nome']} - {c['uf']} | Simulação Grátis | MS Luz Solar",
                 f"Energia solar em {c['nome']}-{c['uf']}: reduza sua conta de luz em até 90%. Projeto, homologação e instalação para casas, empresas e área rural. Simulação gratuita no WhatsApp.",
                 path, [bc])
        p += hero(f"Energia solar em <em>{c['nome']}</em>", f"Reduza sua conta de luz em até 90%. Simulação gratuita, projeto, homologação e instalação para casas, empresas e área rural em {c['nome']} - {c['uf']}.", pill=f"Atendimento em {c['nome']} - {c['uf']}")
        p += f'<section class="alt"><div class="wrap"><p class="crumbs"><a href="{BASE}">Início</a> › Energia solar em {c["nome"]}</p><h2>Por que instalar energia solar em <em>{c["nome"]}</em>?</h2><p class="sec-lead">{c["texto"]} Fazemos a simulação gratuita com base na sua conta, cuidamos do projeto e da aprovação na distribuidora e entregamos o sistema funcionando.</p></div></section>'
        p += sec_beneficios() + sec_simulador() + sec_passos() + sec_faq() + sec_contato(c["nome"]) + sec_final() + foot()
        write(path.strip("/") + "/index.html", p)
        urls.append(DOMAIN + path)
    urls += [DOMAIN + "/privacidade.html", DOMAIN + "/termos.html"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc><lastmod>2026-11-26</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    write("404.html", head("Página não encontrada | MS Luz Solar", "Página não encontrada.", "/404.html") + hero("Página não <em>encontrada</em>", "Mas a sua economia está a um clique. Volte para o início ou fale com a gente no WhatsApp.") + foot())
    legal = lambda t, body: head(f"{t} | MS Luz Solar", f"{t} do site da MS Luz Solar.", "/" + ("privacidade" if "Priv" in t else "termos") + ".html") + f'<section><div class="wrap" style="max-width:820px"><h1 style="font-size:40px">{t}</h1>{body}</div></section>' + foot()
    write("privacidade.html", legal("Política de Privacidade", """<p class="sec-lead" style="margin-top:12px">Última atualização: 26/11/2026.</p>
<h2 style="font-size:24px;margin-top:28px">Quem somos</h2><p>MS Luz Solar é a linha de energia solar da MS Manutenção Residencial e Industrial (CNPJ 56.964.600/0001-24), Luziânia-GO. Contato: WhatsApp (61) 98121-4135.</p>
<h2 style="font-size:24px;margin-top:28px">Quais dados coletamos</h2><p>Nome, telefone, cidade, tipo de imóvel, valor médio da conta de luz e observações que você informa no formulário, além de dados de navegação coletados por ferramentas do Google (Google Analytics e Google Ads), como páginas visitadas e cliques nos botões de contato.</p>
<h2 style="font-size:24px;margin-top:28px">Para que usamos</h2><p>Exclusivamente para entrar em contato sobre a simulação e a proposta de energia solar e para medir o desempenho do site e dos anúncios. Não vendemos seus dados.</p>
<h2 style="font-size:24px;margin-top:28px">Base legal e seus direitos (LGPD)</h2><p>Tratamos os dados com base no seu consentimento (Lei 13.709/2018). Você pode pedir acesso, correção ou exclusão dos seus dados a qualquer momento pelo WhatsApp (61) 98121-4135.</p>
<h2 style="font-size:24px;margin-top:28px">Cookies</h2><p>Usamos cookies do Google para estatísticas e mensuração de anúncios. Você pode bloqueá-los nas configurações do seu navegador.</p>"""))
    write("termos.html", legal("Termos de Uso", """<p class="sec-lead" style="margin-top:12px">Última atualização: 26/11/2026.</p>
<h2 style="font-size:24px;margin-top:28px">Simulador</h2><p>Os valores exibidos no simulador são estimativas aproximadas, baseadas em médias de tarifa e geração solar na região. Não constituem proposta comercial. A proposta oficial depende da análise do seu histórico de consumo, do local de instalação e das regras da distribuidora.</p>
<h2 style="font-size:24px;margin-top:28px">Informações do site</h2><p>O conteúdo tem caráter informativo. Condições de pagamento, financiamento, prazos e garantias são definidos na proposta comercial.</p>
<h2 style="font-size:24px;margin-top:28px">Contato</h2><p>MS Manutenção Residencial e Industrial · CNPJ 56.964.600/0001-24 · Luziânia-GO · WhatsApp (61) 98121-4135.</p>"""))
    cidades_txt = ", ".join(f"{c['nome']}-{c['uf']}" for c in CIDADES)
    write("llms.txt", f"""# MS Luz Solar
> Empresa de energia solar fotovoltaica de Luziânia-GO (linha solar da MS Manutenção Residencial e Industrial, CNPJ 56.964.600/0001-24). Faz simulação gratuita, projeto, homologação na distribuidora e instalação de sistemas solares on-grid para casas, empresas e propriedades rurais.

- Cidades atendidas: {cidades_txt} e Entorno do DF
- Contato: WhatsApp e telefone (61) 98121-4135 — https://wa.me/5561981214135
- Horário: segunda a sábado, 7h às 19h
- Responsável técnico: Rodrigo Xavier dos Santos, eletrotécnico, CREA 06870181616
- Instagram: https://www.instagram.com/msluzsolar/

## Páginas
- [Início]({DOMAIN}/): benefícios, simulador de economia, soluções, perguntas frequentes e contato
""" + "".join(f"- [Energia solar em {c['nome']}]({DOMAIN}/energia-solar-{c['slug']}/)\n" for c in CIDADES))
    if FINAL: write("CNAME", "msluzsolar.com.br\n")
    print("ok", len(urls), "páginas; FINAL=", FINAL)

if __name__ == "__main__":
    main()
