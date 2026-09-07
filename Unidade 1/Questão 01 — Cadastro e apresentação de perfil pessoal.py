print("--- CADASTRO DE PERFIL PESSOAL ---")

 # Coleta de dados em texto
nome_completo = input("Informe seu nome completo: ")
cidade = input("Informe a cidade onde reside: ")

# Validação da Idade (Inteiro e não negativo)
while True:
    try:
        idade = int(input("Informe sua idade (em anos): "))
        if idade >= 0:
            break
        else:
            print("Erro: A idade não pode ser um valor negativo. Tente novamente.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# Validação da Altura (Decimal e positivo)
while True:
    try:
        altura = float(input("Informe sua altura em metros (ex: 1.75): "))
        if altura > 0:
            break
        else:
            print("Erro: A altura deve ser um valor positivo. Tente novamente.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número válido.")

# Exibição dos dados simulando um cartão
print("\n" + "="*35)
print("      CARTÃO DE IDENTIFICAÇÃO      ")
print("="*35)
print(f"Nome   : {nome_completo.title()}")
print(f"Idade  : {idade} anos")
print(f"Altura : {altura:.2f} m")
print(f"Cidade : {cidade.title()}")
print("="*35)