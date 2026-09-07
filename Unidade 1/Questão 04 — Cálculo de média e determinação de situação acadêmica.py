print("--- SISTEMA DE NOTAS E SITUAÇÃO ACADÊMICA ---")

notas = []

# Loop para capturar e validar as 3 notas
for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Informe a {i}ª nota (0 a 10): "))
            # Validação para garantir que a nota está no intervalo permitido
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Erro: A nota deve estar compreendida entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número válido.")

# Calculando a média aritmética
media = sum(notas) / len(notas)

# Determinando a situação acadêmica com base nos critérios
if media >= 7.0:
    situacao = "Aprovado"
elif 5.0 <= media < 7.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Exibindo os resultados formatados
print("\n" + "="*45)
print("              BOLETIM DO ESTUDANTE           ")
print("="*45)
# Exibindo as notas informadas e a média com duas casas decimais
print(f"Notas informadas : {notas[0]:.2f} | {notas[1]:.2f} | {notas[2]:.2f}")
print(f"Média calculada  : {media:.2f}")
print(f"Situação final   : {situacao}")
print("="*45)