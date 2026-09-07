print("--- ANÁLISE POPULACIONAL DE CIDADES ---")

cidades = []

# Requisito: cadastrar pelo menos 5 cidades utilizando lista de dicionários
for i in range(1, 6):
    print(f"\n--- Cadastro da {i}ª Cidade ---")
    nome = input("Nome da cidade: ").strip()
    
    # Validação da sigla do estado (exigindo 2 letras)
    while True:
        estado = input("Estado (sigla com 2 letras, ex: SP, CE): ").strip().upper()
        if len(estado) == 2 and estado.isalpha():
            break
        print("Erro: Informe uma sigla de estado válida com exatamente 2 letras.")
        
    # Validação da população (número inteiro positivo)
    while True:
        try:
            populacao = int(input("População estimada (número inteiro): "))
            if populacao >= 0:
                break
            else:
                print("Erro: A população não pode ser um valor negativo.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")
            
    # Criando o dicionário da cidade e adicionando à lista
    cidade = {
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    }
    cidades.append(cidade)

# Cálculos estatísticos populacionais
populacao_total = sum(c['populacao'] for c in cidades)
media_populacao = populacao_total / len(cidades)

# Definindo pontos de partida para o maior e menor
maior_pop = cidades[0]
menor_pop = cidades[0]

for c in cidades:
    if c['populacao'] > maior_pop['populacao']:
        maior_pop = c
    if c['populacao'] < menor_pop['populacao']:
        menor_pop = c

# Exibição do relatório completo
print("\n" + "="*50)
print("             RELATÓRIO POPULACIONAL             ")
print("="*50)

print("Dados completos de todas as cidades cadastradas:")
for c in cidades:
    print(f"- {c['nome']} ({c['estado']}) : {c['populacao']:,} habitantes".replace(',', '.'))

print("-" * 50)
print(f"Cidade mais populosa : {maior_pop['nome']} ({maior_pop['estado']}) com {maior_pop['populacao']:,} hab.".replace(',', '.'))
print(f"Cidade menos populosa: {menor_pop['nome']} ({menor_pop['estado']}) com {menor_pop['populacao']:,} hab.".replace(',', '.'))
print(f"População total      : {populacao_total:,} habitantes".replace(',', '.'))
print(f"Média populacional   : {media_populacao:,.2f} habitantes".replace(',', '.').replace('.', ',', 1))
print("="*50)