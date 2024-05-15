
def menu():
    print('')
    print('1 - O que é matemática financeira e para que serve.')
    print('2 - Porcentagem.')
    print('3 - Lucro e Prejuízo')

    print('4 - Juros Simples, Juros Compostos e Formula do Montante ')
    print('5 - Desconto e Acrescimo')
    print('6 - Retorno sobre Investimento (ROI)')
    
    print('7 - Valor Presente Líquido (VPL)')
    print('8 - Taxa Interna de Retorno (TIR)')
    print('0 - Sair')
    print('')



def calcular_roi(ganho_investimento, custo_investimento):
    roi = (ganho_investimento - custo_investimento) / custo_investimento * 100
    return roi


def porcentagem(valor, porcentagem):
    return (valor * porcentagem) / 100

def lucro(L, C, V):
    V = L + C
    L = V - C
    percentual = (L / C) * 100 
    return L, percentual

def prejuizo(L, C, V):
    V = L + C
    P = C - L
    percentual = (P / C) * 100 
    return P, percentual

def calcular_vpl(taxa, fluxo_de_caixa, investimento_inicial):
    vpl = -investimento_inicial 

    for i, fluxo in enumerate(fluxo_de_caixa):
        vpl += fluxo / (1 + taxa) ** (i + 1)

    return vpl

def calcular_tir(vpl, pv1, pv2, i1, i2):
    try:
        tir = i1 + (vpl / (pv2 - pv1)) * (i2 - i1)
        return tir
    except ZeroDivisionError:
        print("Divisão por zero. Impossível calcular a TIR.")
        return None

def calcular_montante(capital, taxa_juros, tempo):
 
    montante = capital * (1 + taxa_juros) ** tempo
    return montante

def juros_simples(valor_principal, taxa_juros, tempo):

    juros = valor_principal * (taxa_juros / 100) * tempo
    montante = valor_principal + juros
    return montante

def juros_compostos(valor_principal, taxa_juros, tempo):
 
    montante = valor_principal * ((1 + taxa_juros / 100) ** tempo)
    return montante


def calcular_desconto(preco_inicial, taxa_desconto):
   
    desconto = preco_inicial * (taxa_desconto/100)
    preco_novo = preco_inicial - desconto
    return desconto, preco_novo

def calcular_acrescimo(preco_inicial, taxa_acrescimo):
   
    acrescimo = preco_inicial * (taxa_acrescimo/100)
    preco_novo = preco_inicial + acrescimo
    return acrescimo, preco_novo

def submenu_porcentagem():
    print('''
    1 - Exibir informações sobre sobre Porcentagem.
    2 - Função original de cálculo de Porcentagem.
    0 - Voltar Menu Inicial
    ''')
    opcao = int(input("Escolha uma opção do submenu: "))
    if opcao == 1:
        print("############################################################")
        print("#                           Porcentagem                                     #")
        print("############################################################\n")
        
        print("O que é Porcentagem?")
        print("Porcentagem é uma medida utilizada para expressar uma parte de")
        print("um todo como uma fração de 100. Ela é comumente utilizada em")
        print("situações que envolvem comparação, crescimento, desconto, lucro,")
        print("e muitas outras áreas.\n")
        
        print("Como Calcular Porcentagem?")
        print("A fórmula básica para calcular a porcentagem de um valor em relação")
        print("a outro é:")
        print("Porcentagem = (Parte / Total) * 100\n")
        
        print("Exemplo:")
        print("Se você tem 30 maçãs e quer calcular quanto isso representa em relação")
        print("a um total de 100 maçãs:")
        print("Porcentagem = (30 / 100) * 100 = 30%\n")
        
        print("Porcentagem de Acréscimo ou Desconto:")
        print("Quando se trata de acréscimo ou desconto, a fórmula muda um pouco:")
        print("Porcentagem de Acréscimo = (Valor Final - Valor Inicial) / Valor Inicial * 100")
        print("Porcentagem de Desconto = (Valor Inicial - Valor Final) / Valor Inicial * 100\n")
        
        print("Exemplo de Acréscimo:")
        print("Se você comprou um produto por R$ 100 e vendeu por R$ 120:")
        print("Porcentagem de Acréscimo = (120 - 100) / 100 * 100 = 20%\n")
        
        print("Exemplo de Desconto:")
        print("Se um produto custava R$ 150 e está sendo vendido por R$ 120:")
        print("Porcentagem de Desconto = (150 - 120) / 150 * 100 = 20%\n")
        
        print("Porcentagem de Variação:")
        print("Quando se quer calcular a variação percentual entre dois valores:")
        print("Porcentagem de Variação = ((Valor Final - Valor Inicial) / Valor Inicial) * 100\n")
        
        print("Exemplo de Variação:")
        print("Se o preço de um produto aumentou de R$ 100 para R$ 120:")
        print("Porcentagem de Variação = ((120 - 100) / 100) * 100 = 20%\n")
        
        print("Porcentagem do Valor Total:")
        print("Quando se quer calcular a parte de um valor em relação ao todo:")
        print("Porcentagem do Valor Total = (Valor da Parte / Valor Total) * 100\n")
        
        print("Exemplo de Parte do Valor Total:")
        print("Se você tem R$ 50 e quer saber quanto isso representa de R$ 200:")
        print("Porcentagem do Valor Total = (50 / 200) * 100 = 25%\n")
        
        print("Conclusão")
        print("A porcentagem é uma ferramenta fundamental em diversas áreas da")
        print("vida cotidiana e das finanças. Saber calcular e interpretar")
        print("porcentagens é essencial para tomar decisões informadas em")
        print("diversas situações.\n")
    elif opcao == 2:
        valor = float(input("Digite o valor: "))
        percentual = float(input("Digite a porcentagem: "))
        resultado = porcentagem(valor, percentual)
        print(f"{percentual}% de {valor} é {resultado}.")
    elif opcao == 0:
        menu()
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")


def submenu_lucro_prejuizo():
    print('''
    1 - Exibir informações sobre sobre Lucro e Prejuízo.
    2 - Cálculo de lucro.
    3 - Cálculo de prejuízo.
    0 - Voltar Menu Inicial
    ''')
    opcao = int(input("Escolha uma opção do submenu: "))
    if opcao == 1:
        print("############################################################")
        print("#                       Lucro e Prejuízo                                    #")
        print("############################################################\n")
        
        print("O que é Lucro e Prejuízo?")
        print("Lucro é o ganho financeiro obtido quando o valor de venda de um produto")
        print("ou serviço é maior do que o seu custo de produção ou aquisição. Por outro")
        print("lado, prejuízo ocorre quando o valor de venda é menor que o custo.\n")
        
        print("Como Calcular Lucro e Prejuízo?")
        print("Para calcular o lucro, a fórmula básica é:")
        print("Lucro = Valor de Venda - Custo\n")
        
        print("E para calcular o prejuízo:")
        print("Prejuízo = Custo - Valor de Venda\n")
        
        print("Exemplo de Lucro:")
        print("Se você compra um produto por R$ 50 e o vende por R$ 80:")
        print("Lucro = 80 - 50 = R$ 30\n")
        
        print("Exemplo de Prejuízo:")
        print("Se você compra um produto por R$ 80 e o vende por R$ 50:")
        print("Prejuízo = 80 - 50 = R$ 30\n")
        
        print("Margem de Lucro e Prejuízo:")
        print("A margem de lucro é a porcentagem do lucro em relação ao preço de venda.")
        print("A margem de prejuízo é a porcentagem do prejuízo em relação ao custo.\n")
        
        print("Para calcular a margem de lucro:")
        print("Margem de Lucro (%) = (Lucro / Valor de Venda) * 100\n")
        
        print("E para calcular a margem de prejuízo:")
        print("Margem de Prejuízo (%) = (Prejuízo / Custo) * 100\n")
        
        print("Exemplo de Margem de Lucro:")
        print("Se você tem um lucro de R$ 20 em uma venda de R$ 100:")
        print("Margem de Lucro (%) = (20 / 100) * 100 = 20%\n")
        
        print("Exemplo de Margem de Prejuízo:")
        print("Se você tem um prejuízo de R$ 20 em um custo de R$ 80:")
        print("Margem de Prejuízo (%) = (20 / 80) * 100 = 25%\n")
        
        print("Conclusão")
        print("Entender lucro e prejuízo é essencial para a gestão financeira de")
        print("qualquer negócio. Saber calcular e interpretar essas métricas ajuda")
        print("a tomar decisões informadas sobre preços, investimentos e estratégias\n")
    elif opcao == 2:
        lucro_total = float(input("Digite o lucro total: "))
        custo = float(input("Digite o custo: "))
        valor_venda = float(input("Digite o valor da venda: "))
        lucro_calculado, percentual_lucro = lucro(lucro_total, custo, valor_venda)
        print(f"Lucro: {lucro_calculado}")
        print(f"Percentual de lucro: {percentual_lucro}%")
    elif opcao == 3:
        prejuizo_total = float(input("Digite o prejuízo total: "))
        custo = float(input("Digite o custo: "))
        valor_venda = float(input("Digite o valor da venda: "))
        prejuizo_calculado, percentual_prejuizo = prejuizo(prejuizo_total, custo, valor_venda)
        print(f"Prejuízo: {prejuizo_calculado}")
        print(f"Percentual de prejuízo: {percentual_prejuizo}%")
    elif opcao == 0:
        menu()
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

def submenu_juros():
            print('')
            print('1 - Exibir informações sobre Juros Simples')
            print('2 - Exibir informações sobre Juros Composto')
            print('3 - Exibir informações sobre a Formula Montante')
            print('4 - Calcular Juros Simples')
            print('5 - Calcular Juros Composto')
            print('6 - Calculo do Montante ')
            print('0 - Voltar ao menu principal')
            print('')


            opcaoSubMenu = int(input("Digite o número correspondente para selecionar uma opção do menu: "))

            if opcaoSubMenu == 1:
                print('')
                print("############################################################")
                print("#                           Juros Simples                                    #")
                print("############################################################\n")
                
                print("O que são Juros Simples?")
                print("Juros Simples são uma forma de calcular os juros sobre um valor")
                print("emprestado ou investido, onde os juros são calculados apenas sobre")
                print("o valor principal, sem considerar os juros acumulados de períodos")
                print("anteriores.\n")
                
                print("Como Calcular Juros Simples?")
                print("A fórmula básica dos juros simples é:")
                print("Juros Simples = Principal * Taxa de Juros * Tempo\n")
                
                print("Onde:")
                print("● Principal: O valor inicial emprestado ou investido.")
                print("● Taxa de Juros: A taxa de juros aplicada (em decimal).")
                print("● Tempo: O período de tempo pelo qual o dinheiro é emprestado ou investido.\n")
                
                print("Exemplo:")
                print("Você investe R$ 1.000 a uma taxa de juros simples de 5% ao ano por 3 anos.")
                print("Principal = R$ 1.000")
                print("Taxa de Juros = 5/100 = 0.05")
                print("Tempo = 3 anos")
                print("Juros Simples = 1.000 * 0.05 * 3 = R$ 150\n")
                
                print("O valor total acumulado (Principal + Juros) após 3 anos será:")
                print("Valor Total = Principal + Juros Simples")
                print("Valor Total = 1.000 + 150 = R$ 1.150\n")
                
                print("Por que Entender Juros Simples é Importante?")
                print("● Planejamento Financeiro: Ajuda a planejar empréstimos e investimentos.")
                print("● Comparação de Produtos Financeiros: Permite comparar diferentes opções de empréstimos e investimentos.")
                print("● Educação Financeira: Entender os juros simples é fundamental para tomar decisões financeiras informadas.\n")
                
                print("Conclusão")
                print("Os juros simples são uma ferramenta básica, mas essencial na matemática")
                print("financeira. Saber como calculá-los ajuda a compreender melhor como")
                print("os investimentos e empréstimos funcionam, permitindo tomar decisões")
                print("mais informadas e eficientes.\n")

            elif opcaoSubMenu == 2:
                print('')
                print("############################################################")
                print("#                          Juros Compostos                                  #")
                print("############################################################\n")
                
                print("O que são Juros Compostos?")
                print("Juros Compostos são uma forma de calcular os juros sobre um valor")
                print("emprestado ou investido, onde os juros são calculados sobre o valor")
                print("principal mais os juros acumulados de períodos anteriores. Isso resulta")
                print("em um crescimento exponencial do montante.\n")
                
                print("Como Calcular Juros Compostos?")
                print("A fórmula básica dos juros compostos é:")
                print("Montante = Principal * (1 + Taxa de Juros) ** Tempo\n")
                
                print("Onde:")
                print("● Principal: O valor inicial emprestado ou investido.")
                print("● Taxa de Juros: A taxa de juros aplicada por período (em decimal).")
                print("● Tempo: O número de períodos de tempo em que os juros são aplicados.\n")
                
                print("Exemplo:")
                print("Você investe R$ 1.000 a uma taxa de juros compostos de 5% ao ano por 3 anos.")
                print("Principal = R$ 1.000")
                print("Taxa de Juros = 5/100 = 0.05")
                print("Tempo = 3 anos")
                print("Montante = 1.000 * (1 + 0.05) ** 3")
                print("Montante = 1.000 * 1.157625 = R$ 1.157,63\n")
                
                print("O valor total acumulado após 3 anos será R$ 1.157,63, com os juros compostos")
                print("sendo R$ 157,63.\n")
                
                print("Por que Entender Juros Compostos é Importante?")
                print("● Crescimento Exponencial: Juros compostos permitem que investimentos cresçam exponencialmente ao longo do tempo.")
                print("● Planejamento Financeiro: Ajuda a planejar melhor seus investimentos entender o impacto do tempo nos retornos financeiros.")
                print("● Comparação de Produtos Financeiros: Permite comparar diferentes opções de investimentos com base em seus potenciais de crescimento.\n")
                
                print("Conclusão")
                print("Os juros compostos são uma ferramenta poderosa na matemática financeira.")
                print("Saber como calculá-los permite compreender o potencial de crescimento")
                print("dos investimentos ao longo do tempo, ajudando a tomar decisões financeiras")
                print("mais informadas e estratégicas.\n")

            elif opcaoSubMenu == 3:
                print("############################################################")
                print("#                          Fórmula do Montante                                #")
                print("############################################################\n")
                
                print("O que é a Fórmula do Montante?")
                print("A fórmula do montante é utilizada para calcular o valor total acumulado")
                print("em um investimento ou empréstimo ao final de um determinado período,")
                print("considerando os juros aplicados.\n")
                
                print("Como Calcular o Montante com Juros Compostos?")
                print("A fórmula do montante para juros compostos é:")
                print("Montante = Principal * (1 + Taxa de Juros) ** Tempo\n")
                
                print("Onde:")
                print("● Principal: O valor inicial emprestado ou investido.")
                print("● Taxa de Juros: A taxa de juros aplicada por período (em decimal).")
                print("● Tempo: O número de períodos de tempo em que os juros são aplicados.\n")
                
                print("Exemplo de Juros Compostos:")
                print("Você investe R$ 1.000 a uma taxa de juros compostos de 5% ao ano por 3 anos.")
                print("Principal = R$ 1.000")
                print("Taxa de Juros = 5/100 = 0.05")
                print("Tempo = 3 anos")
                print("Montante = 1.000 * (1 + 0.05) ** 3")
                print("Montante = 1.000 * 1.157625 = R$ 1.157,63\n")
                
                print("O valor total acumulado após 3 anos será R$ 1.157,63, com os juros compostos")
                print("sendo R$ 157,63.\n")
                
                print("Como Calcular o Montante com Juros Simples?")
                print("A fórmula do montante para juros simples é:")
                print("Montante = Principal + (Principal * Taxa de Juros * Tempo)\n")
                
                print("Exemplo de Juros Simples:")
                print("Você investe R$ 1.000 a uma taxa de juros simples de 5% ao ano por 3 anos.")
                print("Principal = R$ 1.000")
                print("Taxa de Juros = 5/100 = 0.05")
                print("Tempo = 3 anos")
                print("Montante = 1.000 + (1.000 * 0.05 * 3)")
                print("Montante = 1.000 + 150 = R$ 1.150\n")
                
                print("O valor total acumulado após 3 anos será R$ 1.150, com os juros simples")
                print("sendo R$ 150.\n")
                
                print("Por que Entender a Fórmula do Montante é Importante?")
                print("● Planejamento Financeiro: Ajuda a planejar melhor seus investimentos")
                print("  e empréstimos.")
                print("● Educação Financeira: Entender como os juros impactam o montante final")
                print("  é fundamental para tomar decisões financeiras informadas.")
                print("● Comparação de Produtos Financeiros: Permite comparar diferentes opções")
                print("  de investimentos com base em seus retornos.\n")
                
                print("Conclusão")
                print("A fórmula do montante é uma ferramenta essencial na matemática financeira.")
                print("Saber como calcular o montante acumulado permite compreender o impacto")
                print("dos juros, seja simples ou compostos, ajudando a tomar decisões financeiras")
                print("mais informadas e eficientes.\n")

            elif opcaoSubMenu == 4:
                valor_principal = float(input("Digite o valor principal: "))
                taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))
                tempo = int(input("Digite o tempo (em anos): "))
                montante = juros_simples(valor_principal, taxa_juros, tempo)
                print(f"O montante com juros simples é: {montante}")

            elif opcaoSubMenu == 5:
                valor_principal = float(input("Digite o valor principal: "))
                taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))
                tempo = int(input("Digite o tempo (em anos): "))
                montante = juros_compostos(valor_principal, taxa_juros, tempo)
                print(f"O montante com juros compostos é: {montante}")

            elif opcaoSubMenu == 6:
                capital = float(input("Digite o capital inicial: "))
                taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))
                tempo = int(input("Digite o tempo (em anos): "))
                montante = calcular_montante(capital, taxa_juros, tempo)
                print(f"O montante é: {montante}")

            elif opcaoSubMenu == 0:
                menu()

            else:
                print("Opção inválida. Por favor, selecione uma opção válida.")

def submenu_desconto_acrescimo():
    print('')
    print('1 - Exibir mais informações sobre Desconto e Acrescimo ')
    print('2 - Calcular Desconto')
    print('3 - Calcular Acrescimo')
    print('0 - Voltar ao menu principal')
    print('')
      
    opcaoSubMenu = int(input("Digite o número correspondente para selecionar uma opção do menu: "))

    if opcaoSubMenu == 1:
        print()
        print("############################################################")
        print("#                           Desconto e Acréscimo                               #")
        print("############################################################\n")
        
        print("O que é Desconto?")
        print("Desconto é uma redução no preço original de um produto ou serviço.")
        print("Ele é geralmente oferecido para incentivar compras ou liquidar estoques.")
        print("O valor do desconto é normalmente calculado como uma porcentagem")
        print("do preço original.\n")
        
        print("Como Calcular o Desconto?")
        print("A fórmula básica do desconto é:")
        print("Preço com Desconto = Preço Original - (Preço Original * Percentual de Desconto)\n")
        
        print("Exemplo:")
        print("Você quer comprar um produto que custa R$ 100 com um desconto de 20%.")
        print("Preço com Desconto = 100 - (100 * 0.20) = 100 - 20 = R$ 80\n")
        
        print("O que é Acréscimo?")
        print("Acréscimo é um aumento no preço original de um produto ou serviço.")
        print("Ele é aplicado por diversas razões, como aumento de custos ou aumento")
        print("de demanda. O valor do acréscimo também é geralmente calculado como")
        print("uma porcentagem do preço original.\n")
        
        print("Como Calcular o Acréscimo?")
        print("A fórmula básica do acréscimo é:")
        print("Preço com Acréscimo = Preço Original + (Preço Original * Percentual de Acréscimo)\n")
        
        print("Exemplo:")
        print("Você quer comprar um produto que custa R$ 100 com um acréscimo de 20%.")
        print("Preço com Acréscimo = 100 + (100 * 0.20) = 100 + 20 = R$ 120\n")
        
        print("Por que Entender Desconto e Acréscimo é Importante?")
        print("● Economia: Conhecer como funcionam descontos pode ajudar a economizar dinheiro em compras.")
        print("● Planejamento Financeiro: Saber calcular acréscimos e descontos é útil para planejar orçamentos e gastos.")
        print("● Negociação: Entender essas métricas ajuda a negociar melhores preços em diversas situações.\n")
        
        print("Conclusão")
        print("Descontos e acréscimos são fundamentais na vida financeira cotidiana.")
        print("Saber como calculá-los permite tomar decisões mais informadas e")
        print("aproveitar oportunidades de economia e investimento de forma mais eficiente.\n")
        print("")

    elif opcaoSubMenu == 2:
        preco_inicial = float(input("Digite o preço inicial: "))
        taxa_desconto = float(input("Digite a taxa de desconto (em porcentagem): "))
        desconto, preco_novo = calcular_desconto(preco_inicial, taxa_desconto)
        print(f"O desconto é: {desconto}")
        print(f"O preço com desconto é: {preco_novo}")

    elif opcaoSubMenu == 3:
        preco_inicial = float(input("Digite o preço inicial: "))
        taxa_acrescimo = float(input("Digite a taxa de acréscimo (em porcentagem): "))
        acrescimo, preco_novo = calcular_acrescimo(preco_inicial, taxa_acrescimo)
        print(f"O acréscimo é: {acrescimo}")
        print(f"O preço com acréscimo é: {preco_novo}")

    elif opcaoSubMenu == 0:
        menu()

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
      

def submenu_roi():
    print('')
    print('1 - Exibir mais informações sobre Retorno sobre Investimento (ROI)')
    print('2 - Calcular Retorno sobre Investimento (ROI)')
    print('0 - Voltar ao menu principal')
    print('')

    opcaoSubMenu = int(input("Digite o número correspondente para selecionar uma opção do menu: "))

    if opcaoSubMenu == 1:
        print('')
        print("############################################################")
        print("#                     Retorno sobre Investimento (ROI)                       #")
        print("############################################################\n")
        
        print("O que é Retorno sobre Investimento (ROI)?")
        print("Retorno sobre Investimento, ou ROI, é uma métrica usada para")
        print("avaliar a eficiência ou lucratividade de um investimento. Ele")
        print("mede o quanto você ganha em relação ao que investiu e é")
        print("expressado como uma porcentagem.\n")
        
        print("Como Calcular o ROI?")
        print("A fórmula básica do ROI é:")
        print("ROI = ((Ganho do Investimento - Custo do Investimento) / Custo do Investimento) * 100\n")
        
        print("Exemplo:")
        print("Você comprou ações por R$ 1.000 e vendeu por R$ 1.200 após um ano.")
        print("Ganho do Investimento = R$ 1.200 - R$ 1.000 = R$ 200")
        print("ROI = (200 / 1000) * 100 = 20%\n")
        
        print("Por que o ROI é Importante?")
        print("● Comparação de Investimentos: Permite comparar diferentes investimentos independentemente do valor investido.")
        print("● Tomada de Decisões: Ajuda a decidir onde alocar recursos.")
        print("● Avaliação de Desempenho: Avalia o desempenho de investimentos passados, identificando áreas de melhoria.\n")
        
        print("Limitações do ROI")
        print("● Não Considera o Tempo: Não leva em conta o tempo necessário para obter o retorno.")
        print("● Custos Adicionais: Pode não considerar todos os custos associados ao investimento.")
        print("● Risco Não Avaliado: Não leva em conta o risco envolvido.\n")
        
        print("Melhorando o Uso do ROI")
        print("Para superar algumas limitações, use outras métricas como:")
        print("● Valor Presente Líquido (VPL): Considera o valor do dinheiro no tempo.")
        print("● Taxa Interna de Retorno (TIR): Avalia o risco do investimento.\n")
        
        print("Conclusão")
        print("O ROI é essencial para avaliar a lucratividade de um investimento.")
        print("Embora tenha limitações, quando usado corretamente, pode fornecer")
        print("insights valiosos para tomar decisões financeiras mais informadas.\n")
        print('')

    elif opcaoSubMenu == 2:
        ganho_investimento = float(input("Digite o ganho do investimento: "))
        custo_investimento = float(input("Digite o custo do investimento: "))
        roi = calcular_roi(ganho_investimento, custo_investimento)
        print(f"O Retorno sobre Investimento (ROI) é: {roi}%")

    elif opcaoSubMenu == 0:
        menu()

    else:
         print("Opção inválida. Por favor, selecione uma opção válida.")


def submenu_taxa_interna_retorno():
    print('''
    1 - Texto acadêmico sobre Taxa Interna de Retorno (TIR).
    2 - Cálculo da Taxa Interna de Retorno (TIR).
    ''')
    opcao = int(input("Escolha uma opção do submenu: "))
    if opcao == 1: 
        print("############################################################")
        print("#                    Taxa Interna de Retorno (TIR)                        #")
        print("############################################################\n")
        
        print("O que é a Taxa Interna de Retorno (TIR)?")
        print("A Taxa Interna de Retorno (TIR) é uma métrica financeira que calcula a")
        print("taxa de desconto que torna o valor presente líquido (VPL) de todos os")
        print("fluxos de caixa de um investimento igual a zero. A TIR representa a")
        print("taxa de retorno esperada de um projeto ou investimento.\n")
        
        print("Como Calcular a TIR?")
        print("A TIR é encontrada resolvendo a seguinte equação para a taxa de desconto:")
        print("0 = ∑ (Fluxo de Caixa / (1 + TIR) ** Tempo) - Investimento Inicial\n")
        
        print("Onde:")
        print("● Fluxo de Caixa: Os ganhos líquidos esperados em cada período.")
        print("● Tempo: O período em que os fluxos de caixa são recebidos.")
        print("● Investimento Inicial: O valor investido no início do projeto.\n")
        
        print("Exemplo:")
        print("Você investe R$ 1.000 em um projeto que gerará R$ 400 ao final de cada um dos próximos")
        print("3 anos. Para encontrar a TIR, precisamos resolver a seguinte equação:")
        print("0 = 400 / (1 + TIR) ** 1 + 400 / (1 + TIR) ** 2 + 400 / (1 + TIR) ** 3 - 1.000\n")
        
        print("Encontrar a TIR geralmente requer o uso de ferramentas financeiras ou")
        print("software de cálculo, já que a equação pode ser complexa de resolver manualmente.\n")
        
        print("Por que Entender a TIR é Importante?")
        print("● Avaliação de Investimentos: A TIR ajuda a determinar a viabilidade")
        print("  de um investimento comparando sua taxa de retorno esperada com a")
        print("  taxa mínima de retorno desejada.")
        print("● Comparação de Projetos: Permite comparar diferentes projetos com")
        print("  base em suas taxas de retorno esperadas.")
        print("● Tomada de Decisões: Auxilia na tomada de decisões financeiras")
        print("  informadas, escolhendo projetos com TIR mais alta.\n")
        
        print("Conclusão")
        print("A Taxa Interna de Retorno (TIR) é uma ferramenta essencial na")
        print("avaliação de investimentos e projetos. Entender e calcular a TIR")
        print("ajuda a tomar decisões financeiras mais informadas, garantindo que")
        print("os investimentos selecionados ofereçam o melhor retorno possível.\n")
    elif opcao == 2:
        vpl = float(input("Digite o VPL: "))
        pv1 = float(input("Digite o primeiro valor presente: "))
        pv2 = float(input("Digite o segundo valor presente: "))
        i1 = float(input("Digite a primeira taxa de investimento: "))
        i2 = float(input("Digite a segunda taxa de investimento: "))
        tir = calcular_tir(vpl, pv1, pv2, i1, i2)
        if tir is not None:
            print(f"A Taxa Interna de Retorno (TIR) é: {tir}")
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

def submenu_valor_presente_liquido():
    print('''
    1 - Texto acadêmico sobre Valor Presente Líquido (VPL).
    2 - Cálculo do Valor Presente Líquido (VPL).
    ''')
    opcao = int(input("Escolha uma opção do submenu: "))
    if opcao == 1:
        print("############################################################")
        print("#                     Valor Presente Líquido (VPL)                        #")
        print("############################################################\n")
        
        print("O que é o Valor Presente Líquido (VPL)?")
        print("O Valor Presente Líquido (VPL) é uma métrica financeira que")
        print("calcula o valor presente dos fluxos de caixa futuros gerados por um")
        print("investimento, descontados a uma taxa de desconto específica. O VPL")
        print("ajuda a determinar se um investimento vale a pena, considerando o")
        print("valor do dinheiro no tempo.\n")
        
        print("Como Calcular o VPL?")
        print("A fórmula básica do VPL é:")
        print("VPL = ∑ (Fluxo de Caixa / (1 + Taxa de Desconto) ** Tempo) - Investimento Inicial\n")
        
        print("Onde:")
        print("● Fluxo de Caixa: Os ganhos líquidos esperados em cada período.")
        print("● Taxa de Desconto: A taxa que reflete o custo de oportunidade do capital.")
        print("● Tempo: O período em que os fluxos de caixa são recebidos.\n")
        
        print("Exemplo:")
        print("Você investe R$ 1.000 em um projeto que gerará R$ 400 ao final de cada um dos próximos")
        print("3 anos, com uma taxa de desconto de 10% ao ano.")
        print("Investimento Inicial = R$ 1.000")
        print("Taxa de Desconto = 10/100 = 0.10")
        print("Fluxo de Caixa (Ano 1) = R$ 400 / (1 + 0.10) ** 1 = R$ 363,64")
        print("Fluxo de Caixa (Ano 2) = R$ 400 / (1 + 0.10) ** 2 = R$ 330,58")
        print("Fluxo de Caixa (Ano 3) = R$ 400 / (1 + 0.10) ** 3 = R$ 300,53")
        print("VPL = R$ 363,64 + R$ 330,58 + R$ 300,53 - R$ 1.000 = - R$ 5,25\n")
        
        print("Nesse caso, o VPL é negativo, indicando que o investimento não é viável.\n")
        
        print("Por que Entender o VPL é Importante?")
        print("● Avaliação de Investimentos: O VPL ajuda a determinar a viabilidade")
        print("  econômica de um projeto ou investimento.")
        print("● Comparação de Projetos: Permite comparar diferentes projetos com")
        print("  base em seu retorno financeiro ajustado pelo valor do dinheiro no tempo.")
        print("● Tomada de Decisões: Auxilia na tomada de decisões financeiras")
        print("  informadas, escolhendo projetos com VPL positivo e mais alto.\n")
        
        print("Conclusão")
        print("O Valor Presente Líquido (VPL) é uma ferramenta fundamental na")
        print("avaliação de investimentos e projetos. Entender e calcular o VPL")
        print("ajuda a tomar decisões financeiras mais informadas, considerando o")
        print("valor do dinheiro no tempo e maximizando o retorno dos investimentos.\n")
    elif opcao == 2:
        investimento_inicial = float(input("Digite o investimento inicial: "))
        fluxos = []
        while True:
            valor = float(input("Digite o valor do fluxo de caixa para o período (digite 0 para encerrar): "))
            if valor == 0:
                break
            fluxos.append(valor)
        taxa = float(input("Digite a taxa de desconto: "))
        vpl = calcular_vpl(taxa, fluxos, investimento_inicial)
        print(f"O Valor Presente Líquido (VPL) é: {vpl}")
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")