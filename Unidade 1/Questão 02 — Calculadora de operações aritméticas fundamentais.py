print("--- CALCULADORA DE OPERAÇÕES BÁSICAS ---")

try:
    # Recebendo os dois números reais
    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))
    
    print("\n" + "="*35)
    print("            RESULTADOS           ")
    print("="*35)
    
    # Operações que sempre são executadas
    print(f"Adição           : {n1} + {n2} = {n1 + n2}")
    print(f"Subtração        : {n1} - {n2} = {n1 - n2}")
    print(f"Multiplicação    : {n1} * {n2} = {n1 * n2}")
    print(f"Potenciação      : {n1} ** {n2} = {n1 ** n2}")
    
    # Validação para as operações de divisão
    if n2 == 0:
        mensagem_erro = "Divisão por zero não permitida"
        print(f"Divisão          : {mensagem_erro}")
        print(f"Divisão inteira  : {mensagem_erro}")
        print(f"Resto da divisão : {mensagem_erro}")
    else:
        print(f"Divisão          : {n1} / {n2} = {n1 / n2:.2f}")
        print(f"Divisão inteira  : {n1} // {n2} = {n1 // n2}")
        print(f"Resto da divisão : {n1} % {n2} = {n1 % n2}")
        
    print("="*35)

except ValueError:
    print("Erro: Por favor, insira números válidos.")