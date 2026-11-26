import json
H = "\n\n#energiasolar #energiasolarfotovoltaica #painelsolar #economiadeenergia #contadeluz #sustentabilidade #energialimpa #luziania #brasilia #df #goias #entornodf #msluzsolar"
W = "\n\n📲 Simulação gratuita: mande uma foto da sua conta de luz no WhatsApp (61) 98121-4135."
B = []
def add(id, tag, title, sub, slides, cap, cta=None):
    d = {"id": id, "cover": {"tag": tag, "title": title, "sub": sub}, "slides": slides, "caption": cap + W + H}
    if cta: d["cta"] = cta
    B.append(d)
it = lambda t, d: {"kind": "item", "t": t, "d": d}
st = lambda big, t, d: {"kind": "stat", "big": big, "t": t, "d": d}

add("S01_beneficios", "Energia solar", "5 *benefícios* de gerar sua própria energia", "Por que cada vez mais famílias do DF e Goiás estão saindo do aluguel de energia.",
 [it("Conta de luz lá embaixo", "A energia gerada no seu telhado abate o consumo e pode **reduzir a conta em até 90%**. Fica só a taxa mínima e encargos."),
  it("Proteção contra reajustes", "Todo ano a tarifa sobe. Quem gera a própria energia **fica muito menos exposto** às bandeiras e aumentos."),
  it("Investimento que se paga", "O sistema costuma se pagar **em poucos anos** com a própria economia — e continua gerando por décadas."),
  it("Imóvel mais valorizado", "Casa com energia solar é mais atrativa: **conta baixa é argumento de venda** e de aluguel."),
  it("Energia limpa", "Zero emissão na geração. Você economiza e ainda **ajuda o meio ambiente**.")],
 "☀️ 5 benefícios de gerar sua própria energia.\n\nEnergia solar não é mais luxo: é a forma mais inteligente de parar de pagar caro pela luz. Economia todo mês, proteção contra reajustes e um imóvel que vale mais.\n\nQual desses benefícios mais pesa pra você? Comenta aqui 👇")

add("S02_25anos", "Faça a conta", "Quanto você vai pagar de luz nos *próximos 25 anos*?", "Spoiler: dá pra comprar um carro. Ou dois.",
 [st("R$ 400", "por mês na conta de luz", "É uma conta comum numa casa com ar-condicionado, chuveiro elétrico e geladeira."),
  st("R$ 120 mil", "em 25 anos", "Isso **sem contar os reajustes**. Com a tarifa subindo todo ano, o valor real é bem maior."),
  st("25+ anos", "de vida útil das placas", "Os módulos solares têm garantia de performance de **até 25 anos**. É energia por décadas."),
  it("A pergunta certa", "Não é *“quanto custa a energia solar?”*. É **“quanto eu vou continuar pagando se não fizer nada?”**")],
 "💸 Você já parou pra calcular quanto vai gastar de energia nos próximos 25 anos?\n\nUma conta de R$ 400 por mês vira R$ 120 mil — sem contar os reajustes. Esse dinheiro pode ficar com você.\n\nQuer ver esse cálculo com a SUA conta? A gente faz pra você 👇")

add("S03_comofunciona", "Passo a passo", "Como funciona a *energia solar* na sua casa", "Simples, silenciosa e sem complicação.",
 [it("As placas captam o sol", "Os módulos fotovoltaicos transformam a luz do sol em **energia elétrica** — mesmo sem calor."),
  it("O inversor converte", "Ele transforma a energia das placas em **energia pronta para usar** nas tomadas da casa."),
  it("Você consome na hora", "Durante o dia, a casa usa **primeiro a energia do sol**. Menos energia comprada da distribuidora."),
  it("O que sobra vira crédito", "O excedente vai para a rede e vira **crédito de energia**, usado à noite ou nos meses seguintes."),
  it("Créditos valem 5 anos", "Pela regra da ANEEL, os créditos podem ser usados por **até 60 meses**.")],
 "🔆 Como a energia solar funciona na prática?\n\nPlacas captam o sol, o inversor converte, sua casa consome e o que sobra vira crédito na distribuidora. Sem bateria, sem barulho, sem complicação.\n\nSalva esse post pra mostrar pra quem ainda acha que é difícil 📌")

add("S04_mitos", "Mito ou verdade?", "4 *mitos* sobre energia solar que te fazem perder dinheiro", "Vamos esclarecer de uma vez.",
 [it("“Em dia nublado não gera”", "**Mito.** A geração diminui, mas não para. E o sistema é dimensionado pela média do ano inteiro."),
  it("“Precisa de bateria”", "**Mito.** No sistema conectado à rede (on-grid), a própria rede funciona como “bateria” através dos créditos."),
  it("“A manutenção é cara”", "**Mito.** Basicamente limpeza periódica das placas e acompanhamento da geração pelo aplicativo."),
  it("“Quando falta luz, continuo com energia”", "**Atenção:** no on-grid o sistema desliga por segurança quando a rede cai. Para isso existem soluções com bateria.")],
 "🤔 Mito ou verdade?\n\nMuita gente deixa de economizar por causa de informação errada. Arrasta pro lado e confira os 4 mitos mais comuns sobre energia solar.\n\nTinha alguma dúvida que não apareceu aqui? Deixa nos comentários que a gente responde 👇")

add("S05_porqueagora", "Por que agora?", "Esperar para instalar energia solar *custa caro*", "3 motivos para não deixar para o ano que vem.",
 [it("A tarifa não para de subir", "Cada mês esperando é **mais um boleto cheio** pago à distribuidora — dinheiro que não volta."),
  it("A regra ficou mais rígida", "Com a Lei 14.300, quem entra depois paga **uma parcela maior do uso da rede**. Esperar não melhora as condições."),
  it("Dá pra trocar conta por parcela", "Com financiamento solar, a parcela pode ficar **próxima do valor da conta de luz** — e um dia acaba.")],
 "⏳ O melhor momento para instalar energia solar foi ontem. O segundo melhor é hoje.\n\nA tarifa sobe, as regras de compensação ficam mais rígidas com o tempo e cada mês esperando é dinheiro que vai embora.\n\nVamos ver quanto você economizaria a partir do mês que vem?")

add("S06_empresas", "Para empresas", "Sua empresa paga *caro demais* de energia?", "Energia solar transforma um custo fixo em investimento.",
 [it("Menos custo fixo", "Energia é um dos maiores custos de comércios, oficinas e indústrias. Solar **reduz esse peso todo mês**."),
  it("Previsibilidade", "Menos susto com bandeira tarifária e reajuste: **planejamento financeiro mais seguro**."),
  it("Retorno rápido", "Quem consome mais durante o dia — horário de sol — **aproveita melhor a geração**."),
  it("Imagem sustentável", "Clientes valorizam empresas que usam **energia limpa**. É marketing positivo para o seu negócio.")],
 "🏢 Comércio, oficina, padaria, clínica, indústria: energia pesa no caixa.\n\nCom energia solar, sua empresa reduz custo fixo, ganha previsibilidade e ainda reforça uma imagem sustentável.\n\nQuer um estudo para o seu negócio? Mande a conta de energia da empresa 👇")

add("S07_rural", "No campo", "Energia solar na *propriedade rural*", "Para quem produz em Luziânia, Cristalina e todo o Entorno.",
 [it("Bombeamento e irrigação", "Bombas e irrigação consomem muito. Gerar no próprio terreno **derruba esse custo**."),
  it("Espaço não falta", "Dá para instalar **em solo**, sem depender do telhado, com a melhor orientação para o sol."),
  it("Ordenha, resfriamento e granja", "Equipamentos que funcionam o dia todo **aproveitam a energia em tempo real**."),
  it("Abata em outra unidade", "A energia gerada pode abater a conta de **outro imóvel do mesmo titular**, na mesma distribuidora.")],
 "🌾 Produtor rural: a energia está pesando no custo da produção?\n\nBomba, irrigação, ordenha, resfriamento… tudo isso pode ser alimentado pelo sol, com sistema instalado em solo no seu próprio terreno.\n\nAtendemos propriedades em todo o Entorno do DF. Fale com a gente 👇")

add("S08_remoto", "Você sabia?", "Dá para gerar energia em um lugar e *economizar em outro*", "É o autoconsumo remoto.",
 [it("Como funciona", "Você instala o sistema em um imóvel e **usa os créditos para abater a conta de outro**."),
  it("A regra", "Os imóveis precisam estar **no mesmo titular (CPF ou CNPJ)** e na área da **mesma distribuidora**."),
  it("Exemplo prático", "Telhado pequeno no apartamento? Gere na **chácara ou no galpão** e abata a conta de casa."),
  it("Uma usina, várias contas", "Dá para **distribuir os créditos** entre diferentes unidades consumidoras cadastradas.")],
 "💡 Você sabia que dá para gerar energia em um imóvel e usar os créditos em outro?\n\nÉ o autoconsumo remoto: ideal para quem mora em apartamento, tem chácara ou tem mais de um imóvel no mesmo nome.\n\nMarca aqui alguém que precisa saber disso 👇")

add("S09_checklist", "Antes de contratar", "5 pontos para conferir antes de *fechar sua energia solar*", "Evite dor de cabeça e prejuízo.",
 [it("Projeto e responsável técnico", "Exija projeto assinado por **profissional habilitado, com ART**."),
  it("Homologação na distribuidora", "O sistema só compensa energia depois de **aprovado pela distribuidora**. Confirme quem cuida disso."),
  it("Equipamentos certificados", "Placas e inversores com **registro no INMETRO** e marcas com assistência no Brasil."),
  it("Garantias por escrito", "Garantia dos módulos, do inversor e **da instalação** — tudo no contrato."),
  it("Dimensionamento correto", "O sistema deve ser calculado pelo **seu histórico de consumo**, não “no olho”.")],
 "✅ Vai investir em energia solar? Confira esses 5 pontos antes de assinar qualquer contrato.\n\nUm sistema bem feito dura décadas. Um mal feito vira dor de cabeça. Salve este checklist 📌")

add("S10_financiar", "Financiamento", "Trocar a *conta de luz* por uma parcela que um dia acaba", "Faz sentido financiar energia solar?",
 [it("Hoje", "Você paga a conta de luz **para sempre**, e ela sobe todo ano."),
  it("Com financiamento", "A economia na conta ajuda a pagar a parcela. Em muitos casos, o valor fica **bem próximo** do que você já paga."),
  it("Depois de quitar", "A parcela acaba e **a economia fica inteira com você** por muitos anos."),
  it("Sem descapitalizar", "Você não precisa tirar todo o dinheiro do bolso de uma vez. **Fazemos a simulação** com as opções disponíveis.")],
 "🏦 Financiar energia solar vale a pena?\n\nA lógica é simples: em vez de pagar a conta de luz para sempre, você paga uma parcela que tem fim — e depois disso a economia é toda sua.\n\nQuer ver a simulação com parcela e economia lado a lado? Chama a gente 👇")

add("S11_vidautil", "Durabilidade", "Quanto tempo dura um *sistema de energia solar*?", "Investimento para décadas.",
 [st("25 anos", "garantia de performance das placas", "Os módulos geralmente garantem **cerca de 80% da potência** após 25 anos de uso."),
  st("10+ anos", "de vida útil do inversor", "É o equipamento que mais trabalha. Bons inversores têm **garantia longa de fábrica**."),
  st("Poucos anos", "para o sistema se pagar", "Depois do retorno, a economia é **lucro direto** por muitos e muitos anos.")],
 "⏱️ Energia solar é para durar.\n\nPlacas com garantia de performance de até 25 anos, inversores com longa vida útil e um sistema que se paga em poucos anos. Depois disso, é economia pura.")

add("S12_valoriza", "Patrimônio", "Energia solar *valoriza* o seu imóvel", "Além de economizar, você constrói patrimônio.",
 [it("Mais atrativo", "Quem compra ou aluga quer **conta baixa**. É um diferencial claro na hora de negociar."),
  it("Equipamento que fica", "O sistema faz parte do imóvel e **segue gerando economia** para o próximo morador."),
  it("Sustentabilidade", "Imóveis com energia limpa estão **cada vez mais valorizados** pelo mercado.")],
 "🏡 Energia solar não é gasto: é patrimônio.\n\nAlém de reduzir sua conta, o sistema deixa o imóvel mais atrativo para venda e aluguel. Economia hoje e valorização amanhã.")

add("S13_passos", "Como contratar", "Do orçamento à economia: *6 passos* com a MS Luz Solar", "A gente cuida de tudo para você.",
 [it("Envie sua conta de luz", "Uma foto da conta pelo WhatsApp já é suficiente para começar."),
  it("Simulação gratuita", "Calculamos o **sistema ideal**, a economia e o tempo de retorno."),
  it("Proposta e condições", "Você recebe a proposta com equipamentos, garantias e **opções de pagamento**."),
  it("Projeto e homologação", "Cuidamos do projeto e da **aprovação na distribuidora**."),
  it("Instalação", "Equipe técnica qualificada instala o sistema **com segurança**."),
  it("Economia começa", "Sistema ligado, você acompanha a geração pelo **aplicativo**.")],
 "📋 Ter energia solar é mais simples do que parece.\n\nVocê manda a conta de luz e a gente cuida do resto: simulação, proposta, projeto, homologação e instalação.\n\nO primeiro passo leva 1 minuto 👇")

add("S14_faq", "Perguntas frequentes", "4 *dúvidas* que todo mundo tem antes de instalar", "Respondidas sem enrolação.",
 [it("Meu telhado aguenta?", "Na visita técnica avaliamos a estrutura. Se não for ideal, há opções como **instalação em solo**."),
  it("Posso aumentar depois?", "Sim. O sistema pode ser **ampliado** se o seu consumo crescer — com novo projeto."),
  it("E se eu mudar de casa?", "O sistema pode ser **reinstalado** em outro imóvel, ou ficar e valorizar a venda."),
  it("Conta zera?", "Não totalmente: continuam a **taxa mínima** e alguns encargos. Mas a economia é grande.")],
 "❓ Tem dúvida sobre energia solar? Você não está sozinho.\n\nReunimos as 4 perguntas que mais recebemos no WhatsApp. Se a sua não está aqui, comenta que a gente responde 👇")

json.dump(B, open("banco.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(B))
