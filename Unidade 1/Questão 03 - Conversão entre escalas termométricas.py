print("--- CONVERSÃO DE TEMPERATURAS ---")

try:
    # Recebendo a temperatura aceitando valores decimais
    celsius = float(input("Informe a temperatura em graus Celsius (°C): "))
    
    # Aplicando as fórmulas de conversão
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    
    # Exibindo os resultados com duas casas decimais e os respectivos símbolos
    print("\n" + "="*35)
    print("      RESULTADOS DA CONVERSÃO      ")
    print("="*35)
    print(f"Celsius    : {celsius:.2f} °C")
    print(f"Fahrenheit : {fahrenheit:.2f} °F")
    print(f"Kelvin     : {kelvin:.2f} K")
    print("="*35)

except ValueError:
    print("Erro: Por favor, insira um valor numérico válido.")