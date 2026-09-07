print("--- ESTATÍSTICA DESCRITIVA ---")

# Inicializando as variáveis contadoras e acumuladoras
soma = 0
qtd_positivos = 0
qtd_negativos = 0
qtd_pares = 0
qtd_impares = 0

# Requisito obrigatório: estrutura de repetição para 10 valores
for i in range(1, 11):
    while True:
        try:
            numero = int(input(f"Informe o {i}º número inteiro: "))
            break
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
            
    # Acumulando a soma
    soma += numero
    
    # Contando positivos e negativos (o 0 é nulo, então não conta em nenhum dos dois)
    if numero > 0:
        qtd_positivos += 1
    elif numero < 0:
        qtd_negativos += 1
        
    # Contando pares e ímpares
    if numero % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

# Calculando a média aritmética
media = soma / 10

# Exibição do relatório final
print("\n" + "="*45)
print("           RELATÓRIO ESTATÍSTICO           ")
print("="*45)
print(f"Soma de todos os números : {soma}")
print(f"Qtd. de números positivos: {qtd_positivos}")
print(f"Qtd. de números negativos: {qtd_negativos}")
print(f"Qtd. de números pares    : {qtd_pares}")
print(f"Qtd. de números ímpares  : {qtd_impares}")
print(f"Média aritmética         : {media:.2f}")
print("="*45)