print("--- ANÁLISE DE SINAL E PARIDADE ---")

# Validação da entrada do usuário
while True:
    try:
        numero = int(input("Informe um número inteiro: "))
        break
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# 1. Análise do sinal
if numero > 0:
        sinal = "positivo"
elif numero < 0:
        sinal = "negativo"
else:
        sinal = "nulo"

# 2. Análise da paridade
if numero % 2 == 0:
        paridade = "par"
else:
        paridade = "ímpar"

# Exibição do resultado em uma mensagem única e coesa
print("\n" + "="*45)
print(f"O número {numero} é {sinal} e {paridade}.")
print("="*45)