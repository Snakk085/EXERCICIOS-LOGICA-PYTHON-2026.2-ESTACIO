print("--- ORDENAÇÃO MANUAL DE TRÊS NÚMEROS ---")

# Coleta e validação para garantir que são inteiros e distintos
while True:
    try:
        n1 = int(input("Informe o 1º número inteiro: "))
        n2 = int(input("Informe o 2º número inteiro: "))
        n3 = int(input("Informe o 3º número inteiro: "))
        
        # Verifica se são todos diferentes
        if n1 != n2 and n1 != n3 and n2 != n3:
            break
        else:
            print("Erro: Os três números informados devem ser distintos. Tente novamente.\n")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite números inteiros.\n")

# Lógica condicional aninhada para ordenação manual
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        meio = n2
        menor = n3
    else:
        meio = n3
        menor = n2

elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        meio = n1
        menor = n3
    else:
        meio = n3
        menor = n1

else:
    maior = n3
    if n1 > n2:
        meio = n1
        menor = n2
    else:
        meio = n2
        menor = n1

# Exibição dos resultados
print("\n" + "="*40)
print("          RESULTADO DA ORDENAÇÃO          ")
print("="*40)
print(f"Maior número        : {maior}")
print(f"Número intermediário: {meio}")
print(f"Menor número        : {menor}")
print("="*40)