print("--- RELATÓRIO ANALÍTICO DE LISTA NUMÉRICA ---")

numeros = []
pares = []
impares = []

# Coletando os 10 números inteiros e armazenando na lista principal
for i in range(1, 11):
    while True:
        try:
            num = int(input(f"Informe o {i}º número inteiro: "))
            numeros.append(num)
            break
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# Percorrendo a lista original para separar pares e ímpares
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Realizando os cálculos com as funções nativas
soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

# Exibição do relatório analítico
print("\n" + "="*50)
print("               RELATÓRIO ANALÍTICO               ")
print("="*50)
print(f"Números informados: {numeros}")
print(f"Números pares     : {pares}")
print(f"Números ímpares   : {impares}")
print(f"Soma total        : {soma}")
print(f"Média dos valores : {media:.2f}")
print(f"Maior valor       : {maior}")
print(f"Menor valor       : {menor}")
print("="*50)