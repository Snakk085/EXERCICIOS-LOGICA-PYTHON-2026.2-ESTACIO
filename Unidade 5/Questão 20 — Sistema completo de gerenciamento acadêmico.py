def calcular_media(n1, n2, n3):
    """Calcula a média aritmética de três notas."""
    return (n1 + n2 + n3) / 3

def determinar_situacao(media):
    """Determina a situação acadêmica com base na média."""
    if media >= 7.0:
        return "Aprovado"
    elif 5.0 <= media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastrar_estudante(turma):
    """Cadastra um novo estudante no sistema."""
    print("\n--- CADASTRAR ESTUDANTE ---")
    nome = input("Nome completo: ").strip()
    
    # Validação da idade (inteiro positivo)
    while True:
        try:
            idade = int(input("Idade (positivo): "))
            if idade > 0:
                break
            print("Erro: A idade deve ser um valor inteiro positivo.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")
            
    curso = input("Curso: ").strip()
    
    # Coleta e validação das 3 notas
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Informe a {i}ª nota (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                print("Erro: A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Erro: Digite um valor numérico válido.")
                
    media = calcular_media(notas[0], notas[1], notas[2])
    situacao = determinar_situacao(media)
    
    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }
    
    turma.append(estudante)
    print(f"\nEstudante '{nome}' cadastrado com sucesso!")

def listar_estudantes(turma):
    """Exibe todos os estudantes cadastrados."""
    print("\n--- LISTA DE ESTUDANTES ---")
    if not turma:
        print("Nenhum estudante cadastrado no sistema.")
        return
        
    for idx, est in enumerate(turma, start=1):
        print(f"\n[{idx}] Nome: {est['nome']}")
        print(f"    Idade: {est['idade']} | Curso: {est['curso']}")
        print(f"    Notas: {est['notas'][0]:.1f}, {est['notas'][1]:.1f}, {est['notas'][2]:.1f}")
        print(f"    Média Final: {est['media']:.2f} | Situação: {est['situacao']}")

def consultar_estudante(turma):
    """Busca um estudante pelo nome e exibe seus dados completos."""
    print("\n--- CONSULTAR ESTUDANTE ---")
    if not turma:
        print("Nenhum estudante cadastrado no sistema.")
        return
        
    busca = input("Digite o nome do estudante para consulta: ").strip().lower()
    encontrado = False
    
    for est in turma:
        if est['nome'].lower() == busca:
            print(f"\n[ESTUDANTE ENCONTRADO]")
            print(f"Nome     : {est['nome']}")
            print(f"Idade    : {est['idade']}")
            print(f"Curso    : {est['curso']}")
            print(f"Notas    : {est['notas'][0]:.1f}, {est['notas'][1]:.1f}, {est['notas'][2]:.1f}")
            print(f"Média    : {est['media']:.2f}")
            print(f"Situação : {est['situacao']}")
            encontrado = True
            break
            
    if not encontrado:
        print("Estudante não encontrado.")

def alterar_dados(turma):
    """Permite a edição de qualquer campo de um estudante existente."""
    print("\n--- ALTERAR DADOS DO ESTUDANTE ---")
    if not turma:
        print("Nenhum estudante cadastrado no sistema.")
        return
        
    busca = input("Digite o nome do estudante que deseja alterar: ").strip().lower()
    for est in turma:
        if est['nome'].lower() == busca:
            print(f"\nEstudante encontrado: {est['nome']}")
            print("O que você deseja alterar?")
            print("1 - Nome")
            print("2 - Idade")
            print("3 - Curso")
            print("4 - Notas (recalcula média e situação)")
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '1':
                est['nome'] = input("Novo nome: ").strip()
                print("Nome alterado com sucesso!")
            elif opcao == '2':
                while True:
                    try:
                        nova_idade = int(input("Nova idade: "))
                        if nova_idade > 0:
                            est['idade'] = nova_idade
                            print("Idade alterada com sucesso!")
                            break
                        print("Erro: A idade deve ser positiva.")
                    except ValueError:
                        print("Erro: Digite um número inteiro.")
            elif opcao == '3':
                est['curso'] = input("Novo curso: ").strip()
                print("Curso alterado com sucesso!")
            elif opcao == '4':
                novas_notas = []
                for i in range(1, 4):
                    while True:
                        try:
                            n = float(input(f"Nova {i}ª nota (0 a 10): "))
                            if 0 <= n <= 10:
                                novas_notas.append(n)
                                break
                            print("Erro: A nota deve estar entre 0 e 10.")
                        except ValueError:
                            print("Erro: Digite um número válido.")
                est['notas'] = novas_notas
                est['media'] = calcular_media(novas_notas[0], novas_notas[1], novas_notas[2])
                est['situacao'] = determinar_situacao(est['media'])
                print("Notas e média recalculadas com sucesso!")
            else:
                print("Opção inválida.")
            return
            
    print("Estudante não encontrado.")

def remover_estudante(turma):
    """Exclui um estudante do sistema mediante confirmação."""
    print("\n--- REMOVER ESTUDANTE ---")
    if not turma:
        print("Nenhum estudante cadastrado no sistema.")
        return
        
    busca = input("Digite o nome do estudante que deseja remover: ").strip().lower()
    for est in turma:
        if est['nome'].lower() == busca:
            print(f"Estudante encontrado: {est['nome']} ({est['curso']})")
            confirma = input("Tem certeza que deseja remover este estudante? (s/n): ").strip().lower()
            if confirma == 's':
                turma.remove(est)
                print("Estudante removido com sucesso!")
            else:
                print("Operação cancelada.")
            return
            
    print("Estudante não encontrado.")

def gerar_relatorio_turma(turma):
    """Exibe o relatório consolidado da turma."""
    print("\n--- RELATÓRIO DA TURMA ---")
    if not turma:
        print("Nenhum estudante cadastrado para gerar relatório.")
        return
        
    total_estudantes = len(turma)
    soma_medias = sum(est['media'] for est in turma)
    media_geral = soma_medias / total_estudantes
    
    maior_media = turma[0]
    menor_media = turma[0]
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    
    for est in turma:
        if est['media'] > maior_media['media']:
            maior_media = est
        if est['media'] < menor_media['media']:
            menor_media = est
            
        if est['situacao'] == "Aprovado":
            aprovados += 1
        elif est['situacao'] == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1
            
    print(f"Total de estudantes cadastrados : {total_estudantes}")
    print(f"Média geral da turma            : {media_geral:.2f}")
    print(f"Maior média                     : {maior_media['nome']} ({maior_media['media']:.2f})")
    print(f"Menor média                     : {menor_media['nome']} ({menor_media['media']:.2f})")
    print(f"Total de Aprovados              : {aprovados}")
    print(f"Total em Recuperação            : {recuperacao}")
    print(f"Total Reprovados                : {reprovados}")

def main():
    """Função principal que controla o menu interativo do sistema."""
    turma = []
    
    while True:
        print("\n=======================================")
        print("         SISTEMA ACADÊMICO (ESTÁCIO)   ")
        print("=======================================")
        print("1 - Cadastrar estudante")
        print("2 - Listar estudantes")
        print("3 - Consultar estudante")
        print("4 - Alterar dados[cite: 1]")
        print("5 - Remover estudante[cite: 1]")
        print("6 - Gerar relatório da turma[cite: 1]")
        print("0 - Encerrar sistema[cite: 1]")
        print("=======================================")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            cadastrar_estudante(turma)
        elif opcao == '2':
            listar_estudantes(turma)
        elif opcao == '3':
            consultar_estudante(turma)
        elif opcao == '4':
            alterar_dados(turma)
        elif opcao == '5':
            remover_estudante(turma)
        elif opcao == '6':
            gerar_relatorio_turma(turma)
        elif opcao == '0':
            print("\nEncerrando o sistema acadêmico. Bons estudos!")
            break
        else:
            print("\nOpção inválida! Escolha uma opção entre 0 e 6.")

if __name__ == "__main__":
    main()