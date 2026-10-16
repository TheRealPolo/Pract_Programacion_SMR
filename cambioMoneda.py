def conversor_divisas():
    print("=== CONVERSOR DE DIVISAS DE 4 MONEDAS ===")

    print("Monedas disponibles:")
    print("1. Dólar estadounidense (USD)")
    print("2. Euro (EUR)")
    print("3. Libra esterlina (GBP)")
    print("4. Yen japonés (JPY)")

    cantidad = float(input("Ingrese la cantidad a convertir: "))
    moneda = input("Ingrese la moneda de destino (USD, EUR, GBP, JPY): ")

    if moneda == "USD":
        resultado = cantidad * 1.0  # 1 USD = 1 USD
    elif moneda == "EUR":
        resultado = cantidad * 0.85  # 1 USD = 0.85 EUR
    elif moneda == "GBP":
        resultado = cantidad * 0.75  # 1 USD = 0.75 GBP
    elif moneda == "JPY":
        resultado = cantidad * 110.0  # 1 USD = 110 JPY
    else:
        print("¡¡¡SOLO HAY 4 MONEDAS DISPONIBLES!!!.")

    print(f"{cantidad} USD equivale a {resultado} {moneda}")
