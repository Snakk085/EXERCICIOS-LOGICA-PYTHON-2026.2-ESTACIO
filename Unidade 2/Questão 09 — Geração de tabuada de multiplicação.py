print("--- TABUADA DE MULTIPLICAÇÃO ---")

# Validação para garantir que a entrada seja um número inteiro
while True:
    try:
        numero = int(input("Informe um número inteiro para gerar a tabuada: "))
        break
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

print("\n" + "="*30)
print(f"       TABUADA DO {numero}       ")
print("="*30)

# Requisito obrigatório: uso de estrutura de repetição
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("="*30)