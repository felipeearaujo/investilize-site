import os

content_map = {
    "Conteudoacoes.astro": {
        "q": "Como analisar ações na B3 para iniciantes?",
        "a": "Para analisar ações na bolsa de valores, o primeiro passo é entender os fundamentos da empresa. Olhe para indicadores básicos como o P/L (Preço sobre Lucro) e o Dividend Yield. Além disso, avalie o setor de atuação e se a empresa possui lucros consistentes nos últimos 5 anos. Evite tomar decisões baseadas apenas em dicas de internet; foque na geração de caixa e no valor intrínseco do negócio."
    },
    "ConteudoComparador.astro": {
        "q": "Qual a melhor Renda Fixa hoje?",
        "a": "A melhor renda fixa depende do seu prazo e objetivo. Para liquidez diária e reserva de emergência, o Tesouro Selic ou um CDB rendendo 100% do CDI são ideais. Para prazos médios (1 a 3 anos), LCIs e LCAs podem ser vantajosas por serem isentas de imposto de renda. Já para aposentadoria e proteção contra a inflação a longo prazo, o Tesouro IPCA+ é historicamente a opção mais recomendada."
    },
    "ConteudoConversorMoedas.astro": {
        "q": "Como converter moedas com cotação em tempo real?",
        "a": "Para converter moedas com precisão, é necessário utilizar a taxa de câmbio comercial do momento (PTAX ou cotações de mercado). Nossa ferramenta puxa a paridade exata para garantir que a sua conversão de Dólar, Euro ou Libra para Real reflita o cenário real do mercado financeiro hoje, evitando as distorções das taxas de câmbio turismo cobradas em casas de câmbio."
    },
    "ConteudoIndependencia.astro": {
        "q": "Como calcular o tempo para a independência financeira?",
        "a": "O tempo para atingir a independência financeira ou o movimento FIRE (Financial Independence, Retire Early) depende de 3 variáveis fundamentais: seu patrimônio atual, o valor que você consegue poupar e investir todos os meses (taxa de poupança), e a rentabilidade real (acima da inflação) da sua carteira. Quanto maior a sua taxa de poupança, mais rápido o juro composto trabalhará a seu favor."
    },
    "ConteudoIR.astro": {
        "q": "Como calcular o Imposto de Renda sobre investimentos mensais?",
        "a": "O cálculo do imposto de renda na renda fixa no Brasil segue uma tabela regressiva. Se você sacar o dinheiro em menos de 180 dias, a alíquota é de 22,5% sobre o lucro. Esse imposto cai gradativamente até chegar à alíquota mínima de 15% para investimentos mantidos por mais de 720 dias (2 anos). Lembre-se que o imposto é cobrado apenas sobre o rendimento, e não sobre o valor principal investido."
    },
    "ConteudoPerfil.astro": {
        "q": "Como descobrir meu perfil de investidor?",
        "a": "O perfil de investidor (suitability) avalia sua tolerância a perdas e o seu horizonte de tempo. Se você não suporta ver seu saldo negativo e precisa do dinheiro a curto prazo, seu perfil é Conservador (foco em Renda Fixa). Se aceita oscilações controladas em busca de maiores ganhos, é Moderado. Já se investe para o longo prazo e lida bem com a volatilidade da bolsa, você tem um perfil Arrojado."
    },
    "ConteudoPoderCompra.astro": {
        "q": "Como calcular a perda de poder de compra pela inflação?",
        "a": "O poder de compra cai conforme a inflação acumulada avança. Se a inflação foi de 10% no ano, um produto que custava R$ 100 passa a custar R$ 110. Se o seu dinheiro estava parado na conta ou embaixo do colchão, os mesmos R$ 100 agora compram cerca de 9% a menos de bens reais. Por isso é crucial investir em ativos que paguem acima da inflação (IPCA), protegendo seu esforço de poupança."
    },
    "ConteudoPrecoJusto.astro": {
        "q": "Como calcular o preço justo de uma ação pela fórmula de Graham?",
        "a": "A fórmula de Benjamin Graham (mentor de Warren Buffett) para encontrar o preço justo ou valor intrínseco de uma ação é: Valor Intrínseco = √(22,5 x VPA x LPA). Onde VPA é o Valor Patrimonial da Ação e LPA é o Lucro por Ação. Se a ação estiver sendo negociada na bolsa por um preço menor que o resultado dessa fórmula, ela teórica e estatisticamente possui uma margem de segurança para a compra."
    },
    "ConteudoReservaEmergencia.astro": {
        "q": "Como calcular a reserva de emergência ideal?",
        "a": "A regra de ouro da reserva de emergência é acumular entre 6 e 12 meses do seu custo de vida mensal (não do seu salário). Se você é funcionário público ou tem alta estabilidade, 6 meses são suficientes. Se você é profissional liberal, autônomo, CLT ou empreendedor, mire em 12 meses. Esse dinheiro deve ficar estritamente em investimentos de alta liquidez e baixo risco, como o Tesouro Selic ou CDBs 100% do CDI."
    },
    "ConteudoTaxaReal.astro": {
        "q": "Como calcular a taxa real de juros descontando a inflação?",
        "a": "Não se calcula a taxa real apenas subtraindo a inflação do rendimento bruto (ex: 10% - 4% = 6%). A forma matematicamente correta é usar a Equação de Fisher: [(1 + Taxa Nominal) / (1 + Inflação)] - 1. Isso ocorre porque o dinheiro perde valor de forma composta ao longo do tempo. É por isso que muitos investimentos que parecem render muito, na verdade entregam pouquíssimo ganho real quando a inflação está em alta."
    },
    "ConteudoTaxometro.astro": {
        "q": "Como saber quanto pago de imposto nos investimentos?",
        "a": "Muitos investidores esquecem que a inflação e o imposto de renda (IR) corroem quase todo o lucro bruto da renda fixa. Para saber quanto você paga, basta cruzar o prazo do seu investimento com a tabela regressiva do IR (que vai de 22,5% a 15%). Além do IR, aplicações resgatadas em menos de 30 dias sofrem a mordida do IOF. Fazer simulações ajuda a entender se um CDB a 100% do CDI realmente vence um LCI isento a 90%."
    },
    "ConteudoTesouroBancao.astro": {
        "q": "Tesouro Direto ou CDB de Bancão: Qual rende mais?",
        "a": "O Tesouro Selic e os CDBs de grandes bancos (bancões) são as portas de entrada da renda fixa. Historicamente, CDBs de bancões tradicionais rendem menos (em torno de 80% a 90% do CDI), o que os faz perderem para a caderneta de poupança em certos cenários. O Tesouro Selic rende 100% da Selic. Portanto, a menos que o seu bancão ofereça um CDB de 100% do CDI com liquidez diária, o Tesouro Direto ou um banco digital será muito mais rentável."
    },
    "TextoJurosCompostos.astro": {
        "q": "Como calcular juros compostos com aportes mensais?",
        "a": "O cálculo dos juros compostos com aportes mensais vai além da fórmula tradicional (M = P(1+i)^n). O seu dinheiro inicial cresce a cada mês, e cada novo aporte mensal também gera seus próprios juros ao longo do tempo restante. A matemática é exponencial e cria o efeito 'bola de neve'. É por isso que usar uma calculadora automatizada de investimentos é a forma mais rápida de simular cenários precisos para a sua independência financeira."
    }
}

comp_dir = 'src/components/ferramentas'

for file_name, seo_data in content_map.items():
    path = os.path.join(comp_dir, file_name)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if we already injected
    if seo_data['q'] in content:
        continue
        
    seo_block = f"""
    <section class="seo-faq-section">
        <h2>{seo_data['q']}</h2>
        <p>{seo_data['a']}</p>
    </section>
"""
    
    # Try to insert before </article>
    if '</article>' in content:
        content = content.replace('</article>', seo_block + '</article>')
    # Else try to insert before <style>
    elif '<style>' in content:
        content = content.replace('<style>', seo_block + '\n<style>')
    else:
        content += seo_block
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("SEO H2 sections injected successfully into all tools content files!")
