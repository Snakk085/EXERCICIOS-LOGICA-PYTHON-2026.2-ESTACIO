print("--- SISTEMA DE GERENCIAMENTO DE NOTAS DE TURMA ---")

def calcular_media(n1, n2, n3):
    """Calcula a média aritmética de três notas."""
    return (n1 + n2 + n3) / 3

def cadastrar_estudantes():
    """Cadastra pelo menos 5 estudantes utilizando lista de dicionários."""
    turma = []
    for i in range(1, 6):
        print(f"\n--- Cadastro do {i}º Estudante ---")
        nome = input("Nome do estudante: ").strip()
        
        notas = []
        for j in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Informe a {j}ª nota (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Erro: A nota deve estar compreendida entre 0 e 10.")
                except ValueError:
                    print("Erro: Entrada inválida. Digite um número válido.")
        
        media = calcular_media(notas[0], notas[1], notas[2])
        
        estudante = {
            "nome": nome,
            "notas": notas,
            "media": media
        }
        turma.append(estudante)
    return turma

def gerar_relatorio_turma(turma):
    """Gera o relatório analítico com base nos dados da turma."""
    if not turma:
        return

    maior_media = turma[0]
    menor_media = turma[0]
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    print("\n" + "="*50)
    print("               RELATÓRIO DA TURMA               ")
    print("="*50)

    for est in turma:
        print(f"Estudante: {est['nome']} | Média Final: {est['media']:.2f}")
        
        # Identificando maior e menor média
        if est['media'] > maior_media['media']:
            maior_media = est
        if est['media'] < menor_media['media']:
            menor_media = est
            
        # Contabilizando situações acadêmicas exigidas
        if est['media'] >= 7.0:
            aprovados += 1
        elif 5.0 <= est['media'] < 7.0:
            recuperacao += 1
        else:
            reprovados += 1

    print("-" * 50)
    print(f"Estudante com a maior média: {maior_media['nome']} ({maior_media['media']:.2f})")
    print(f"Estudante com a menor média: {menor_media['nome']} ({menor_media['media']:.2f})")
    print(f"Quantidade de aprovados (média >= 7.0)          : {aprovados}")
    print(f"Quantidade em recuperação (5.0 <= média < 7.0)  : {recuperacao}")
    print(f"Quantidade reprovados (média < 5.0)             : {reprovados}")
    print("="*50)

# Execução principal do programa
turma_estudantes = cadastrar_estudantes()
gerar_relatorio_turma(turma_estudantes)