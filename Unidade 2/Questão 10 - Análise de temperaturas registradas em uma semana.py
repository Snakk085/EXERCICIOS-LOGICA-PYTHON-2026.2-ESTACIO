print("--- ANÁLISE DE TEMPERATURAS SEMANAIS ---")

temperaturas = []

# Coletando as temperaturas de 7 dias e armazenando na lista
for i in range(1, 8):
    while True:
        try:
            temp = float(input(f"Informe a temperatura do {i}º dia (°C): "))
            temperaturas.append(temp)
            break
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número (ex: 25.5).")

# Cálculos utilizando as funções nativas do Python
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)
media_temp = sum(temperaturas) / len(temperaturas)

# Contando quantos dias a temperatura ficou acima da média
dias_acima_media = 0
for t in temperaturas:
    if t > media_temp:
        dias_acima_media += 1

# Exibição do relatório
print("\n" + "="*45)
print("           RELATÓRIO METEOROLÓGICO           ")
print("="*45)
print(f"Temperaturas registradas: {temperaturas}")
print(f"Maior temperatura       : {maior_temp:.2f} °C")
print(f"Menor temperatura       : {menor_temp:.2f} °C")
print(f"Temperatura média       : {media_temp:.2f} °C")
print(f"Dias acima da média     : {dias_acima_media} dia(s)")
print("="*45)