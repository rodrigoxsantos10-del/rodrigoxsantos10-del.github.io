"""Páginas extras do site MS Luz Solar: serviços, guias e Sobre (SEO + respostas para IAs)."""
import html, json

DIST = {"GO": ("Equatorial Goiás", "a distribuidora de energia de Goiás"), "DF": ("Neoenergia Brasília", "a distribuidora de energia do Distrito Federal")}

# Conteúdo local único por cidade (evita páginas duplicadas)
LOCAL = {
 "luziania": {"bairros": "Centro, Setor Aeroporto, Parque Estrela Dalva, Mingone, Setor Norte, Jardim Ingá, Parque Nápolis e zona rural",
   "perfil": "Luziânia combina bairros residenciais em crescimento, comércio forte no Centro e uma grande área rural. Isso abre espaço para três tipos de projeto: telhado residencial, telhado comercial e usina em solo em chácaras e fazendas.",
   "faq": [("Vocês são de Luziânia mesmo?", "Sim. A MS Luz Solar é a linha de energia solar da MS Manutenção, empresa de Luziânia-GO com responsável técnico registrado no CRT. A visita técnica e o pós-venda são feitos por quem está na cidade."),
           ("Atendem a zona rural de Luziânia?", "Sim. Fazemos projetos para chácaras, fazendas e granjas, inclusive com instalação em solo e uso dos créditos em outro imóvel do mesmo titular.")]},
 "brasilia-df": {"bairros": "Plano Piloto, Lago Sul, Lago Norte, Park Way, Jardim Botânico, Gama, Santa Maria, Samambaia, Taguatinga, Ceilândia, Águas Claras e Sobradinho",
   "perfil": "No DF, muitas casas térreas e sobrados com bom espaço de telhado e alto uso de ar-condicionado tornam a energia solar especialmente vantajosa. Em condomínios horizontais, verificamos também as regras internas antes do projeto.",
   "faq": [("Moro em condomínio no DF. Posso instalar?", "Na maioria dos condomínios horizontais, sim. Verificamos as regras do condomínio e o projeto é apresentado à administração quando necessário."),
           ("Qual distribuidora aprova o sistema no DF?", "No Distrito Federal a homologação é feita junto à Neoenergia Brasília. Nós cuidamos de todo o processo.")]},
 "valparaiso-de-goias": {"bairros": "Jardim Céu Azul, Parque Esplanada, Valparaíso I e II, Etapas A, B e C, Morada Nobre e região",
   "perfil": "Valparaíso de Goiás tem muitas casas de família e comércios de bairro que sentem o peso da conta de luz. Sistemas residenciais de pequeno e médio porte costumam ter ótimo custo-benefício na cidade.",
   "faq": [("Atendem todos os bairros de Valparaíso?", "Sim, atendemos toda a cidade. A simulação é feita pelo WhatsApp e a visita técnica é agendada no endereço."),
           ("Quanto tempo leva para ligar o sistema?", "Depende do prazo de análise da distribuidora e da entrega dos equipamentos. Informamos o cronograma estimado na proposta.")]},
 "cidade-ocidental": {"bairros": "Centro, Jardim ABC, Parque Nova Friburgo, Mansões Recreio Mossoró e região",
   "perfil": "Em Cidade Ocidental, a combinação de casas com quintal e chácaras próximas ao Jardim ABC permite projetos tanto no telhado quanto em solo, conforme o espaço disponível.",
   "faq": [("Atendem o Jardim ABC?", "Sim. Atendemos Cidade Ocidental, o Jardim ABC e as chácaras da região."),
           ("Meu telhado é pequeno. Tem solução?", "Avaliamos alternativas como estrutura em solo, garagem ou uso de créditos gerados em outro imóvel do mesmo titular (autoconsumo remoto).")]},
 "jardim-inga-luziania": {"bairros": "Jardim Ingá, Parque Nápolis, Pedregal, Mandu, Parque Estrela Dalva e região",
   "perfil": "O Jardim Ingá é um dos polos que mais crescem em Luziânia, com muitas casas novas e comércios. Instalar energia solar logo após a construção ou reforma facilita o projeto e começa a gerar economia desde cedo.",
   "faq": [("Estou construindo no Jardim Ingá. Quando instalar?", "O ideal é planejar junto com a obra: assim já deixamos o quadro e a passagem dos cabos preparados, e o sistema pode ser ligado assim que a unidade consumidora estiver ativa."),
           ("Vocês vão até o Jardim Ingá para a visita?", "Sim, estamos na mesma região. A visita técnica é agendada pelo WhatsApp.")]},
 "cristalina": {"bairros": "Centro, setores residenciais e toda a região agrícola de Cristalina",
   "perfil": "Cristalina é um dos maiores polos de agricultura irrigada do país. Pivôs, bombas e armazéns consomem muita energia — e o terreno amplo permite usinas em solo bem orientadas para o sol.",
   "faq": [("Fazem projeto para pivô e irrigação?", "Fazemos o estudo de consumo da propriedade e dimensionamos o sistema para abater a energia usada na irrigação e no bombeamento, inclusive com usina em solo."),
           ("A energia gerada na fazenda pode abater a conta da cidade?", "Sim, pelo autoconsumo remoto, desde que os imóveis estejam no mesmo CPF/CNPJ e na área da mesma distribuidora.")]},
}

SERVICOS = [
 {"slug": "energia-solar-residencial", "nome": "Energia solar residencial", "h1": "Energia solar <em>para sua casa</em>",
  "desc": "Energia solar residencial em Luziânia, DF e Entorno: reduza a conta de luz da família com projeto sob medida, homologação e instalação. Simulação grátis.",
  "lead": "Ar-condicionado, chuveiro elétrico, geladeira e home office sem medo da conta de luz. Projeto dimensionado pelo consumo da sua família.",
  "blocos": [("Para quem é", "Casas e sobrados com conta de luz a partir de cerca de R$ 200 por mês já costumam ter bom retorno. Quanto maior o consumo, mais rápido o sistema se paga."),
             ("O que está incluso", "Visita técnica, projeto, homologação na distribuidora, módulos e inversor com garantia de fábrica, estrutura de fixação adequada ao seu telhado, instalação e configuração do aplicativo de monitoramento."),
             ("Tipos de telhado", "Atendemos telhado cerâmico, fibrocimento, metálico e laje. Quando o telhado não é adequado, avaliamos estrutura em solo ou em garagem."),
             ("Depois da instalação", "Você acompanha a geração pelo celular. A manutenção é simples: limpeza periódica dos módulos e verificação da instalação.")]},
 {"slug": "energia-solar-para-empresas", "nome": "Energia solar para empresas", "h1": "Energia solar <em>para empresas</em> e comércio",
  "desc": "Energia solar para empresas, comércios, clínicas, oficinas e indústrias em Luziânia, DF e Entorno. Reduza custo fixo com energia. Estudo gratuito.",
  "lead": "Energia é um dos maiores custos fixos de comércios, oficinas, clínicas, padarias e indústrias. Gerar a própria energia transforma esse custo em investimento.",
  "blocos": [("Por que faz sentido", "Empresas consomem energia principalmente durante o dia — justamente quando o sistema solar gera. Isso aumenta o aproveitamento e acelera o retorno."),
             ("Estudo de viabilidade", "Analisamos as últimas contas de energia, o tipo de ligação e o espaço disponível para entregar um estudo com investimento, economia estimada e tempo de retorno."),
             ("Previsibilidade", "Com menos dependência da tarifa, o planejamento financeiro fica mais seguro diante de reajustes e bandeiras tarifárias."),
             ("Experiência em elétrica comercial e industrial", "Como linha solar da MS Manutenção, avaliamos também o quadro, a proteção e a infraestrutura elétrica do imóvel — essencial para um sistema seguro.")]},
 {"slug": "energia-solar-rural", "nome": "Energia solar rural", "h1": "Energia solar <em>rural</em> e para o agronegócio",
  "desc": "Energia solar rural em Luziânia, Cristalina e Entorno do DF: irrigação, bombeamento, granjas e armazéns. Usina em solo e autoconsumo remoto. Estudo gratuito.",
  "lead": "Bombas, irrigação, ordenha, resfriamento e armazéns: no campo, energia é custo de produção. Com energia solar, esse custo cai e a propriedade fica mais competitiva.",
  "blocos": [("Usina em solo", "Quando há espaço, a usina em solo permite a melhor orientação para o sol, facilita a limpeza e não depende do telhado."),
             ("Autoconsumo remoto", "A energia gerada na propriedade pode abater a conta de outros imóveis do mesmo titular, na área da mesma distribuidora."),
             ("Infraestrutura elétrica rural", "Avaliamos padrão de entrada, aterramento e proteção contra surtos — itens importantes em áreas rurais sujeitas a descargas atmosféricas."),
             ("Para quem é", "Chácaras, fazendas, granjas, pivôs de irrigação, poços artesianos, laticínios e armazéns no Entorno do DF.")]},
]

GUIAS = [
 {"slug": "quanto-custa-energia-solar", "titulo": "Quanto custa energia solar e em quanto tempo ela se paga?",
  "desc": "Entenda o que define o preço de um sistema de energia solar, como calcular a economia e o tempo de retorno no DF e Entorno. Guia da MS Luz Solar.",
  "resumo": "O preço de um sistema de energia solar depende principalmente do seu consumo de energia (kWh por mês), que define a potência necessária (kWp). Na maioria dos projetos residenciais e comerciais, o sistema se paga em poucos anos apenas com a economia na conta de luz e continua gerando por décadas.",
  "secoes": [("O que define o preço", "<p>Quatro fatores pesam no valor final:</p><ul><li><strong>Consumo mensal (kWh):</strong> quanto mais energia você usa, maior o sistema.</li><li><strong>Equipamentos:</strong> marca e tecnologia dos módulos e do inversor.</li><li><strong>Tipo de telhado ou estrutura:</strong> cerâmico, metálico, laje ou solo.</li><li><strong>Distância e infraestrutura elétrica:</strong> cabeamento, quadro e padrão de entrada.</li></ul>"),
             ("Como estimar o tamanho do sistema", "<p>Uma regra prática para o DF e Goiás: cada 1 kWp instalado gera, em média, cerca de 120 kWh por mês. Uma casa que consome 400 kWh por mês precisaria de algo em torno de 3,3 kWp. A proposta real considera o histórico de 12 meses, a orientação do telhado e as perdas do sistema.</p>"),
             ("Como calcular a economia", "<p>A energia gerada abate o consumo da conta. Continuam a cobrança mínima (custo de disponibilidade: 30, 50 ou 100 kWh conforme a ligação seja monofásica, bifásica ou trifásica), a contribuição de iluminação pública e parte da tarifa de uso da rede prevista na Lei 14.300. Por isso falamos em redução de <strong>até 90%</strong>, e não em conta zerada.</p>"),
             ("Tempo de retorno (payback)", "<p>O payback é o investimento dividido pela economia anual. Como a tarifa de energia costuma subir com o tempo, a economia em reais tende a crescer ano a ano, o que encurta o retorno. As placas têm garantia de performance de até 25 anos — ou seja, depois do retorno vêm muitos anos de economia.</p>"),
             ("Próximo passo", "<p>A forma mais precisa de saber o valor é fazer uma simulação com a sua conta de luz. Use o <a href=\"{BASE}#simulador\">simulador do site</a> para uma estimativa rápida ou envie uma foto da conta pelo WhatsApp para receber a proposta.</p>")]},
 {"slug": "lei-14300-energia-solar", "titulo": "Lei 14.300: o que mudou na energia solar e se ainda vale a pena",
  "desc": "Entenda a Lei 14.300 (marco legal da geração distribuída): Fio B, regra de transição, créditos de 60 meses e por que energia solar continua vantajosa.",
  "resumo": "A Lei 14.300/2022 criou o marco legal da geração distribuída. Para sistemas que pediram conexão a partir de 2023, passa a ser cobrada gradualmente uma parte da tarifa de uso da rede (o chamado Fio B) sobre a energia compensada. Mesmo assim, a economia continua grande e o investimento segue vantajoso na maioria dos casos.",
  "secoes": [("O que é a Lei 14.300", "<p>É a lei que regulamenta a geração própria de energia conectada à rede (micro e minigeração distribuída), trazendo segurança jurídica para quem instala energia solar.</p>"),
             ("O que é o Fio B", "<p>É a parcela da tarifa que remunera o uso da rede de distribuição. Para quem pediu conexão a partir de 7 de janeiro de 2023, uma porcentagem crescente do Fio B passa a ser cobrada sobre a energia compensada: 15% em 2023, 30% em 2024, 45% em 2025, 60% em 2026, 75% em 2027 e 90% em 2028. A partir de 2029 valem as regras definidas pela ANEEL.</p>"),
             ("Créditos de energia", "<p>A energia excedente injetada na rede vira crédito, que pode ser usado em até <strong>60 meses</strong>, inclusive em outro imóvel do mesmo titular na área da mesma distribuidora (autoconsumo remoto).</p>"),
             ("Ainda vale a pena?", "<p>Sim, na grande maioria dos casos. O Fio B incide só sobre uma parte da tarifa, e a energia consumida no mesmo momento em que é gerada não passa pela compensação. Além disso, esperar não traz regras melhores: a cobrança só aumenta com o tempo, e a tarifa de energia continua subindo.</p>"),
             ("Próximo passo", "<p>Cada caso tem um retorno diferente. Faça uma <a href=\"{BASE}#simulador\">simulação gratuita</a> e receba a proposta já considerando as regras atuais.</p>")]},
 {"slug": "como-funciona-energia-solar", "titulo": "Como funciona a energia solar on-grid, passo a passo",
  "desc": "Como funciona a energia solar conectada à rede: módulos, inversor, medidor bidirecional e créditos de energia. Sem bateria. Guia simples da MS Luz Solar.",
  "resumo": "No sistema on-grid, os módulos solares transformam a luz do sol em eletricidade, o inversor converte essa energia para uso na casa, e o excedente vai para a rede da distribuidora, virando créditos que abatem o consumo da noite e dos meses seguintes. Não é preciso bateria.",
  "secoes": [("1. Módulos fotovoltaicos", "<p>As placas captam a luz do sol e geram energia em corrente contínua. Elas funcionam com luz — não com calor — e geram menos, mas continuam gerando, em dias nublados.</p>"),
             ("2. Inversor", "<p>Converte a energia das placas para corrente alternada, a mesma das tomadas, e monitora a produção. Pelo aplicativo você acompanha quanto o sistema gerou.</p>"),
             ("3. Consumo instantâneo", "<p>Durante o dia, a casa ou empresa consome primeiro a energia gerada no telhado.</p>"),
             ("4. Medidor bidirecional e créditos", "<p>O que sobra vai para a rede e é registrado pelo medidor bidirecional, instalado pela distribuidora após a homologação. Esses créditos abatem o consumo da noite e dos meses seguintes, com validade de até 60 meses.</p>"),
             ("5. E se faltar energia na rua?", "<p>Por segurança, o sistema on-grid desliga automaticamente quando a rede cai, para proteger quem trabalha na manutenção da rede. Quem precisa de energia nesses momentos pode avaliar sistemas híbridos com bateria.</p>"),
             ("Próximo passo", "<p>Quer saber quantas placas você precisa? Use o <a href=\"{BASE}#simulador\">simulador</a> ou fale com a gente no WhatsApp.</p>")]},
]

EXTRA_CSS = r"""
.bar{display:none}
@media (max-width:620px){.bar{display:grid;grid-template-columns:1fr 1fr;position:fixed;left:0;right:0;bottom:0;z-index:70;background:#fff;border-top:1px solid var(--line);padding:10px 12px calc(10px + env(safe-area-inset-bottom));gap:10px;box-shadow:0 -8px 24px -12px rgba(10,35,66,.25)}
.bar a{display:flex;align-items:center;justify-content:center;gap:8px;border-radius:12px;padding:13px;font-weight:800;text-decoration:none;font-size:15px}
.bar a svg{width:20px;height:20px}.bar .w{background:var(--green);color:#fff}.bar .t{background:var(--navy);color:#fff}
.float{display:none}footer{padding-bottom:120px}}
.cookie{position:fixed;left:16px;right:16px;bottom:16px;z-index:80;max-width:560px;margin-inline:auto;background:var(--navy);color:#fff;border-radius:16px;padding:16px 18px;display:none;gap:14px;align-items:center;font-size:13.5px;box-shadow:0 16px 40px -12px rgba(0,0,0,.4)}
.cookie a{color:var(--sun)}.cookie button{background:var(--sun);color:var(--navy);border:0;border-radius:10px;padding:10px 16px;font-weight:800;cursor:pointer;font-family:inherit;flex:none}
@media (max-width:620px){.cookie{bottom:86px}}
.art{max-width:780px}.art h2{font-size:clamp(24px,3vw,30px);margin-top:36px}.art p,.art li{color:#2B3A50;font-size:17.5px;margin-top:12px}.art ul{padding-left:22px}.art a{color:var(--orange);font-weight:700}
.tldr{background:#FFF8E5;border-left:5px solid var(--sun);border-radius:12px;padding:18px 20px;margin-top:22px;font-size:17px;color:var(--ink)}
.meta{color:var(--muted);font-size:14px;margin-top:8px}
.links{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:30px}
@media (max-width:980px){.links{grid-template-columns:1fr}}
.links a{display:block;text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px}.links a:hover{border-color:var(--sun)}
.links b{color:var(--navy);display:block;font-size:17px}.links span{color:var(--muted);font-size:14.5px}

/* topo: Instagram + WhatsApp (redesign 2026-11) */
.top-acoes{display:flex;align-items:center;gap:8px;flex:none}
.top-ig{display:inline-flex;align-items:center;gap:8px;min-height:42px;padding:0 14px 0 6px;border:1px solid var(--line);border-radius:99px;background:#fff;color:var(--navy);text-decoration:none;font-weight:800;font-size:14px;transition:transform .15s,box-shadow .15s}
.top-ig:hover{transform:translateY(-1px);box-shadow:0 8px 20px -10px rgba(193,53,132,.6)}
.ig-ico{width:30px;height:30px;border-radius:50%;background:linear-gradient(45deg,#f9ce34,#ee2a7b 50%,#6228d7);color:#fff;display:grid;place-items:center;flex:none}
.ig-ico svg{width:17px;height:17px}
@media (max-width:1180px){.nav{gap:18px;font-size:14px}}
@media (max-width:620px){.top .wrap{gap:8px}.top-ig{padding:0 10px 0 5px;font-size:13px}.brand{font-size:17px}.top .btn{padding:10px 12px}}
@media (max-width:430px){.brand{font-size:15px;gap:7px;white-space:nowrap}.logo-mark{width:32px;height:32px}.top-ig{font-size:12.5px}}
.brand{white-space:nowrap}
@media (max-width:360px){.ig-txt{display:none}.top-ig{padding:0 5px}}
.float::before{content:"";position:absolute;inset:0;border-radius:50%;animation:zap-pulso 2.4s ease-out infinite}
@keyframes zap-pulso{0%{box-shadow:0 0 0 0 rgba(31,168,85,.55)}70%{box-shadow:0 0 0 18px rgba(31,168,85,0)}100%{box-shadow:0 0 0 0 rgba(31,168,85,0)}}
.card{transition:transform .2s,box-shadow .2s}.card:hover{transform:translateY(-3px);box-shadow:0 18px 40px -20px rgba(10,35,66,.35)}
@media (prefers-reduced-motion:reduce){.float::before,.card{animation:none;transition:none}}
"""


def run(m):
    B = m.BASE; D = m.DOMAIN
    urls = []
    org = {"@type": "Organization", "name": "MS Manutenção Residencial e Industrial", "url": "https://rodrigoxsantos10-del.github.io/msmanutencao/"}

    def bc(*items):
        return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": D + u} for i, (n, u) in enumerate(items)]}

    # Serviços
    for s in SERVICOS:
        path = f"/{s['slug']}/"
        svc = {"@context": "https://schema.org", "@type": "Service", "name": s["nome"], "serviceType": "Instalação de energia solar fotovoltaica",
               "provider": {"@id": D + "/#empresa"}, "areaServed": [f"{c['nome']} - {c['uf']}" for c in m.CIDADES], "description": s["desc"], "url": D + path}
        p = m.head(f"{s['nome']} em Luziânia, DF e Entorno | MS Luz Solar", s["desc"], path, [svc, bc(("Início", "/"), (s["nome"], path))])
        p += m.hero(s["h1"], s["lead"], pill=s["nome"])
        cards = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in s["blocos"])
        p += f'<section class="alt"><div class="wrap"><p class="crumbs"><a href="{B}">Início</a> › {s["nome"]}</p><h2>Como funciona o nosso serviço de <em>{s["nome"].lower()}</em></h2><div class="grid g2">{cards}</div></div></section>'
        p += m.sec_simulador() + m.sec_passos() + sec_guias(B) + m.sec_contato() + m.sec_final() + m.foot()
        m.write(path.strip("/") + "/index.html", p); urls.append(D + path)

    # Guias
    for g in GUIAS:
        path = f"/guia/{g['slug']}/"
        art = {"@context": "https://schema.org", "@type": "Article", "headline": g["titulo"], "description": g["desc"], "inLanguage": "pt-BR",
               "datePublished": "2026-11-26", "dateModified": "2026-11-26", "mainEntityOfPage": D + path, "image": D + "/og.jpg",
               "author": {"@type": "Person", "name": "Rodrigo Xavier dos Santos", "jobTitle": "Eletrotécnico (registro no CRT)"},
               "publisher": {"@id": D + "/#empresa"}}
        p = m.head(f"{g['titulo']} | MS Luz Solar", g["desc"], path, [art, bc(("Início", "/"), ("Guias", "/guia/"), (g["titulo"], path))])
        body = "".join(f'<h2>{t}</h2>{c.replace("{BASE}", B)}' for t, c in g["secoes"])
        p += f'''<section><div class="wrap art"><p class="crumbs"><a href="{B}">Início</a> › <a href="{B}guia/">Guias</a></p>
<h1 style="font-size:clamp(32px,4.4vw,48px)">{g["titulo"]}</h1><p class="meta">Por Rodrigo Xavier dos Santos, eletrotécnico (registro no CRT) · Atualizado em 26/11/2026</p>
<div class="tldr"><strong>Resposta rápida:</strong> {g["resumo"]}</div>{body}</div></section>'''
        p += sec_guias(B, exceto=g["slug"]) + m.sec_final() + m.foot()
        m.write(path.strip("/") + "/index.html", p); urls.append(D + path)
    # índice de guias
    p = m.head("Guias de energia solar | MS Luz Solar", "Guias práticos sobre energia solar: preço e retorno, Lei 14.300 e como funciona o sistema on-grid. Conteúdo da MS Luz Solar, Luziânia-GO.", "/guia/", [bc(("Início", "/"), ("Guias", "/guia/"))])
    p += m.hero("Guias de <em>energia solar</em>", "Respostas diretas para as dúvidas mais comuns antes de investir em energia solar.", pill="Conteúdo educativo")
    p += sec_guias(B) + m.sec_final() + m.foot()
    m.write("guia/index.html", p); urls.append(D + "/guia/")

    # Sobre
    path = "/sobre/"
    about = {"@context": "https://schema.org", "@type": "AboutPage", "url": D + path, "about": {"@id": D + "/#empresa"}}
    p = m.head("Sobre a MS Luz Solar | Energia solar em Luziânia-GO", "Conheça a MS Luz Solar: linha de energia solar da MS Manutenção (CNPJ 56.964.600/0001-24), de Luziânia-GO, com responsável técnico registrado no CRT.", path, [about, bc(("Início", "/"), ("Sobre", path))])
    p += m.hero("Sobre a <em>MS Luz Solar</em>", "Energia solar com a segurança de quem entende de instalação elétrica.", pill="Quem somos")
    p += f'''<section class="alt"><div class="wrap art">
<h2>Quem somos</h2><p>A MS Luz Solar é a linha de energia solar fotovoltaica da <a href="https://rodrigoxsantos10-del.github.io/msmanutencao/">MS Manutenção Residencial e Industrial</a> (CNPJ 56.964.600/0001-24), empresa de Luziânia-GO especializada em instalações elétricas residenciais, comerciais, industriais e rurais e em instalação de carregadores de carro elétrico (wallbox).</p>
<h2>Responsável técnico</h2><p>Os projetos são acompanhados por Rodrigo Xavier dos Santos, eletrotécnico registrado no CRT. Antes de instalar o sistema solar, avaliamos também a infraestrutura elétrica do imóvel — quadro, proteção, aterramento e padrão de entrada — para garantir uma instalação segura.</p>
<h2>O que fazemos</h2><ul><li>Simulação gratuita a partir da conta de luz</li><li>Projeto e homologação junto à Equatorial Goiás e à Neoenergia Brasília</li><li>Instalação de sistemas on-grid residenciais, comerciais e rurais, em telhado ou solo</li><li>Adequação elétrica do imóvel para receber o sistema</li></ul>
<h2>Onde atendemos</h2><p>{", ".join(f'<a href="{B}energia-solar-{c["slug"]}/">{c["nome"]}</a>' for c in m.CIDADES)} e Entorno do Distrito Federal.</p>
<h2>Contato</h2><p>WhatsApp e telefone: <a href="tel:+5561981214135">(61) 98121-4135</a> · Segunda a sábado, das 7h às 19h · Instagram <a href="{m.IG}">@msluzsolar</a>.</p></div></section>'''
    p += m.sec_contato() + m.foot()
    m.write("sobre/index.html", p); urls.append(D + path)
    return urls


def sec_guias(B, exceto=None):
    items = [(f"{B}guia/{g['slug']}/", g["titulo"], g["desc"][:110] + "…") for g in GUIAS if g["slug"] != exceto]
    if len(items) < 3:
        items += [(f"{B}{s['slug']}/", s["nome"], s["desc"][:100] + "…") for s in SERVICOS][: 3 - len(items)]
    links = "".join(f'<a href="{u}"><b>{t}</b><span>{d}</span></a>' for u, t, d in items)
    return f'<section class="alt"><div class="wrap"><div class="eyebrow">Guias</div><h2>Entenda antes de <em>investir</em></h2><div class="links">{links}</div></div></section>'


def local_block(m, c):
    L = LOCAL[c["slug"]]; dist, ddesc = DIST[c["uf"]]
    faq = "".join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in L["faq"])
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in L["faq"]]}
    return (f'<section><div class="wrap"><div class="grid g2" style="margin-top:0">'
            f'<div class="card"><h3>Energia solar em {c["nome"]}: o que considerar</h3><p>{L["perfil"]}</p></div>'
            f'<div class="card"><h3>Distribuidora e homologação</h3><p>Em {c["nome"]}, a conexão do sistema é aprovada pela <strong>{dist}</strong>, {ddesc}. Cuidamos de toda a documentação, do pedido de acesso até a troca do medidor.</p></div>'
            f'<div class="card"><h3>Bairros e regiões atendidas</h3><p>{L["bairros"]}.</p></div>'
            f'<div class="card"><h3>Serviços em {c["nome"]}</h3><p><a href="{m.BASE}energia-solar-residencial/">Residencial</a> · <a href="{m.BASE}energia-solar-para-empresas/">Empresas e comércio</a> · <a href="{m.BASE}energia-solar-rural/">Rural e agronegócio</a></p></div>'
            f'</div><h2 style="margin-top:48px">Dúvidas de quem mora em <em>{c["nome"]}</em></h2><div class="faq">{faq}</div></div></section>'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')
