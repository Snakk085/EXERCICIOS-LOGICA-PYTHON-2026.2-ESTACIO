print("--- ANÁLISE LINGUÍSTICA DE UMA FRASE ---")

# Recebendo a frase do usuário
frase_input = input("Digite uma frase qualquer: ")

# Tratando adequadamente espaços extras (início, fim e múltiplos espaços internos)
palavras = frase_input.split()
frase_tratada = " ".join(palavras)

# 1. Quantidade total de caracteres (da frase original, incluindo espaços)
total_caracteres = len(frase_input)

# 2. Quantidade de palavras
qtd_palavras = len(palavras)

# 3. Primeira e última palavra
if qtd_palavras > 0:
    primeira_palavra = palavras[0]
    ultima_palavra = palavras[-1]
else:
    primeira_palavra = "Nenhuma palavra digitada"
    ultima_palavra = "Nenhuma palavra digitada"

# 4. Quantidade de ocorrências de uma letra escolhida pelo usuário
while True:
    letra_busca = input("Escolha uma letra para contar na frase: ").strip()
    if len(letra_busca) == 1 and letra_busca.isalpha():
        break
    print("Erro: Por favor, digite apenas uma única letra.")

# Contando a letra (convertendo para minúsculo para ser case-insensitive)
qtd_letra = frase_tratada.lower().count(letra_busca.lower())

# 5. Frase em maiúsculas e minúsculas
frase_maiuscula = frase_tratada.upper()
frase_minuscula = frase_tratada.lower()

# Exibição do relatório analítico
print("\n" + "="*50)
print("             RELATÓRIO LINGUÍSTICO             ")
print("="*50)
print(f"Frase formatada      : {frase_tratada}")
print(f"Total de caracteres  : {total_caracteres}")
print(f"Quantidade de palavras: {qtd_palavras}")
print(f"Primeira palavra     : {primeira_palavra}")
print(f"Última palavra       : {ultima_palavra}")
print(f"A letra '{letra_busca}' aparece : {qtd_letra} vez(es)")
print(f"Em maiúsculas        : {frase_maiuscula}")
print(f"Em minúsculas        : {frase_minuscula}")
print("="*50)