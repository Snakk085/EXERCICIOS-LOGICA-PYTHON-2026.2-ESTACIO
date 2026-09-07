print("--- SISTEMA INTERATIVO DE GERENCIAMENTO DE NÚMEROS ---")

numeros = []

while True:
    print("\n===============================")
    print("  GERENCIAMENTO DE NÚMEROS     ")
    print("===============================")
    print("1 - Cadastrar número")
    print("2 - Listar números")
    print("3 - Exibir maior número")
    print("4 - Exibir menor número")
    print("5 - Calcular média")
    print("0 - Encerrar programa")
    print("===============================")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        while True:
            try:
                num = float(input("Digite o número que deseja cadastrar: "))
                numeros.append(num)
                print("Número cadastrado com sucesso!")
                break
            except ValueError:
                print("Erro: Digite um valor numérico válido.")
                
    elif opcao == '2':
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            print(f"Números cadastrados: {numeros}")
            
    elif opcao == '3':
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            print(f"O maior número é: {max(numeros)}")
            
    elif opcao == '4':
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            print(f"O menor número é: {min(numeros)}")
            
    elif opcao == '5':
        if len(numeros) == 0:
            print("Nenhum número cadastrado[cite: 1].")
        else:
            media = sum(numeros) / len(numeros)
            print(f"A média dos números é: {media:.2f}")
            
    elif opcao == '0':
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 0 e 5.")