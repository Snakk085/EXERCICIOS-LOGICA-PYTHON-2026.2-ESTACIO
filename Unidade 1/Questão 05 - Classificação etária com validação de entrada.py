print("--- SISTEMA DE CLASSIFICAÇÃO ETÁRIA ---")

# Laço de repetição para garantir que a idade inserida seja válida
while True:
    try:
        idade = int(input("Informe a idade da pessoa: "))
        
        # A questão exige expressamente não aceitar idades negativas
        if idade >= 0:
            break
        else:
            print("Erro: A idade não pode ser um valor negativo. Tente novamente.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# Estrutura condicional para determinar a classificação
if idade <= 12:
    classificacao = "Criança"
elif 13 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

# Exibição clara e objetiva do resultado
print("\n" + "="*40)
print("          RESULTADO DA ANÁLISE          ")
print("="*40)
print(f"A idade informada foi de {idade} anos.")
print(f"Classificação etária: {classificacao}")
print("="*40)