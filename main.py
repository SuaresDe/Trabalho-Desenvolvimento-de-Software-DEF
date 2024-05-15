import funcoes as func

while True:
    func.menu()
    opcao = int(input("Digite o número correspondente para selecionar uma opção do menu: "))

    if opcao == 0:
        break

    elif opcao == 1:
        print("############################################################")
        print("#                     Matemática Financeira                                #")
        print("############################################################\n")
        
        print("O que é Matemática Financeira?")
        print("Matemática Financeira é um ramo da matemática aplicada que estuda e")
        print("aplica técnicas matemáticas para resolver problemas financeiros.")
        print("Ela envolve a análise de investimentos, financiamentos, empréstimos,")
        print("juros, amortizações e outros aspectos relacionados à gestão financeira.\n")
        
        print("Para que Serve a Matemática Financeira?")
        print("● Planejamento e Controle Financeiro:")
        print("  A Matemática Financeira ajuda indivíduos e empresas a planejar e")
        print("  controlar suas finanças, garantindo uma gestão eficiente dos recursos.")
        print("● Avaliação de Investimentos:")
        print("  Permite avaliar a viabilidade e rentabilidade de investimentos,")
        print("  ajudando a tomar decisões informadas sobre onde e quando investir.")
        print("● Gestão de Empréstimos e Financiamentos:")
        print("  Auxilia no cálculo de prestações, juros e amortizações, facilitando")
        print("  a gestão de dívidas e financiamentos.")
        print("● Comparação de Produtos Financeiros:")
        print("  Ajuda a comparar diferentes produtos financeiros, como empréstimos,")
        print("  investimentos e seguros, com base em seus custos e benefícios.")
        print("● Tomada de Decisões:")
        print("  Fornece ferramentas para tomar decisões financeiras informadas,")
        print("  considerando fatores como risco, retorno e valor do dinheiro no tempo.\n")
        
        print("Principais Conceitos da Matemática Financeira:")
        print("● Juros Simples e Compostos:")
        print("  Juros são a remuneração pelo uso do dinheiro. Juros simples são")
        print("  calculados apenas sobre o valor principal, enquanto juros compostos")
        print("  são calculados sobre o principal mais os juros acumulados.")
        print("● Valor Presente e Valor Futuro:")
        print("  Valor presente é o valor atual de um montante que será recebido")
        print("  ou pago no futuro. Valor futuro é o valor que um montante atual")
        print("  acumulará em um determinado período, considerando uma taxa de juros.")
        print("● Taxa Interna de Retorno (TIR):")
        print("  A TIR é a taxa de desconto que torna o valor presente líquido (VPL)")
        print("  de um investimento igual a zero, indicando a rentabilidade do investimento.")
        print("● Valor Presente Líquido (VPL):")
        print("  O VPL é a soma dos fluxos de caixa descontados de um investimento")
        print("  menos o investimento inicial, usado para avaliar a viabilidade de projetos.\n")
        
        print("Conclusão")
        print("A Matemática Financeira é uma ferramenta essencial para a gestão")
        print("financeira eficaz. Ela fornece as bases necessárias para entender")
        print("e gerenciar finanças pessoais e empresariais, permitindo a tomada")
        print("de decisões mais informadas e estratégicas.\n")

    elif opcao == 2:
        func.submenu_porcentagem()

    elif opcao == 3:
        func.submenu_lucro_prejuizo()

    elif opcao == 4:
        func.submenu_juros()

    elif opcao == 5:
        func.submenu_desconto_acrescimo

    elif opcao == 6:
        func.submenu_roi()

    elif opcao == 7:
        func.submenu_valor_presente_liquido()

    elif opcao == 8:
        func.submenu_taxa_interna_retorno()

  

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

        