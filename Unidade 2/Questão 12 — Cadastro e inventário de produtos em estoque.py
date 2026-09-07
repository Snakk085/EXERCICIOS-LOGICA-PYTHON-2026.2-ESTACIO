print("--- SISTEMA DE CONTROLE DE ESTOQUE ---")

# Lista que vai guardar todos os produtos
estoque = []

# Requisito: cadastrar pelo menos 5 produtos
for i in range(1, 6):
    print(f"\n--- Cadastro do {i}º Produto ---")
    nome = input("Nome do produto: ")
    
    # Validação do preço (aceita decimais e não pode ser negativo)
    while True:
        try:
            preco = float(input("Preço unitário (R$): "))
            if preco >= 0:
                break
            else:
                print("Erro: O preço não pode ser negativo.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número válido.")
            
    # Validação da quantidade (deve ser número inteiro)
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade >= 0:
                break
            else:
                print("Erro: A quantidade não pode ser negativa.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")
            
    # Criando o dicionário do produto e adicionando à lista
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    estoque.append(produto)

# Inicializando variáveis para os cálculos
valor_total_estoque = 0
# Assumimos temporariamente que o primeiro produto cadastrado é o mais caro
produto_mais_caro = estoque[0] 

print("\n" + "="*50)
print("             INVENTÁRIO DE PRODUTOS             ")
print("="*50)

# 1. Exibir todos os produtos cadastrados
for p in estoque:
    # Exibição individual acessando as chaves do dicionário
    print(f"Produto: {p['nome']} | Preço: R${p['preco']:.2f} | Qtd: {p['quantidade']}")
    
    # 2. Calcular o valor total do estoque (preço * quantidade)
    valor_total_estoque += (p['preco'] * p['quantidade'])
    
    # 3. Identificar o produto com o maior preço unitário
    if p['preco'] > produto_mais_caro['preco']:
        produto_mais_caro = p

print("-" * 50)
print(f"Valor total acumulado no estoque: R$ {valor_total_estoque:.2f}")
print(f"Produto mais caro: {produto_mais_caro['nome']} custando R$ {produto_mais_caro['preco']:.2f}")
print("="*50)