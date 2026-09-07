import random

print("--- SIMULAÇÃO DE LANÇAMENTO DE DADOS ---")

# Parte 1: Lançamento único
print("\n--- Parte 1: Lançamento Único ---")
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
soma_unico = dado1 + dado2

print(f"Resultado do primeiro dado : {dado1}")
print(f"Resultado do segundo dado  : {dado2}")
print(f"Soma dos dois valores      : {soma_unico}")

# Parte 2: Múltiplos lançamentos (10 lançamentos)
print("\n--- Parte 2: Múltiplos Lançamentos (10 rodadas) ---")
contador_soma_sete = 0

for i in range(1, 11):
    d_mult1 = random.randint(1, 6)
    d_mult2 = random.randint(1, 6)
    soma_mult = d_mult1 + d_mult2
    
    print(f"Lançamento {i:2d} -> Dado 1: {d_mult1} | Dado 2: {d_mult2} | Soma: {soma_mult}")
    
    if soma_mult == 7:
        contador_soma_sete += 1

print("\n" + "="*50)
print(f"Quantidade de vezes que a soma foi igual a 7: {contador_soma_sete}")
print("="*50)