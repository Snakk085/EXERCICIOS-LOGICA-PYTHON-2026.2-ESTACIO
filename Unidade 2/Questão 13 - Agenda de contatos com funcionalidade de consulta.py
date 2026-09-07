print("--- AGENDA ELETRÔNICA DE CONTATOS ---")

agenda = []

# Requisito obrigatório: cadastrar pelo menos 5 contatos utilizando lista de dicionários
for i in range(1, 6):
    print(f"\n--- Cadastro do {i}º Contato ---")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Endereço de e-mail: ").strip()
    
    # Criando o dicionário do contato
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    agenda.append(contato)

# Consulta de contato na agenda
print("\n" + "="*40)
print("          CONSULTA NA AGENDA          ")
print("="*40)

busca = input("Digite o nome da pessoa para consulta: ").strip()
encontrado = False

# Percorrendo a lista de dicionários para buscar o contato
for contato in agenda:
    # Usamos .lower() para tornar a busca sensível ou não a letras maiúsculas/minúsculas
    if contato["nome"].lower() == busca.lower():
        print("\n[CONTATO LOCALIZADO]")
        print(f"Nome     : {contato['nome']}")
        print(f"Telefone : {contato['telefone']}")
        print(f"E-mail   : {contato['email']}")
        encontrado = True
        break

# Se o contato não for encontrado após percorrer a lista
if not encontrado:
    print("\nContato não encontrado.")

print("="*40)