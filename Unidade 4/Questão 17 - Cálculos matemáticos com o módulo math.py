import math

print("--- CÁLCULOS MATEMÁTICOS COM O MÓDULO MATH ---")

# Coletando um número real do usuário
while True:
    try:
        numero = float(input("Informe um número real: "))
        break
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")

# 1. Valor absoluto (módulo)
absoluto = math.fabs(numero)

# 2. Arredondamentos (teto e piso)
teto = math.ceil(numero)
piso = math.floor(numero)

# 3. Raiz quadrada (só existe nos reais se o número for >= 0)
if numero >= 0:
    raiz = math.sqrt(numero)
else:
    raiz = "Não é possível calcular raiz real de número negativo"

# 4. Fatorial (exige que seja um número inteiro e não negativo)
# Verificamos se o número é inteiro (ex: 5.0 é inteiro, 5.5 não é)
if numero.is_integer() and numero >= 0:
    fatorial = math.factorial(int(numero))
else:
    fatorial = "Fatorial aplicável apenas a números inteiros não negativos"

# Exibição dos resultados
print("\n" + "="*50)
print("             RELATÓRIO DO MÓDULO MATH             ")
print("="*50)
print(f"Número informado     : {numero}")
print(f"Valor absoluto       : {absoluto}")
print(f"Arredondamento teto  : {teto}")
print(f"Arredondamento piso  : {piso}")
print(f"Raiz quadrada        : {raiz if isinstance(raiz, str) else f'{raiz:.2f}'}")
print(f"Fatorial             : {fatorial}")
print("="*50)