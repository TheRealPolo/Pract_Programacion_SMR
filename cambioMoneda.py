def conversor_divisas():
    print("=== CONVERSOR DE DIVISAS DE 8 MONEDAS ===")
    print("Monedas disponibles: USD, EUR, GBP, JPY, CAD, CHF, MXN, COP\n")

    origen = input("Moneda de origen: ").strip().upper()     # RECORDATORIO PARA POLITO ---> .STRIP Y .UPPER LO HE UTILIZADO PARA QUE SI POR EJEMPLO PONES gB  p FUNCIONE
    destino = input("Moneda de destino: ").strip().upper()

    try:
        monto = float(input("Monto a convertir: "))
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido.")
        return

    # Paso 1
    if origen == "USD":
        monto_usd = monto
    elif origen == "EUR":
        monto_usd = monto / 0.92
    elif origen == "GBP":
        monto_usd = monto / 0.78
    elif origen == "JPY":
        monto_usd = monto / 155.0
    elif origen == "CAD":
        monto_usd = monto / 1.36
    elif origen == "CHF":
        monto_usd = monto / 0.90
    elif origen == "MXN":
        monto_usd = monto / 18.00
    elif origen == "COP":
        monto_usd = monto / 3900.0
    else:
        monto_usd = None

    # Validar si la moneda de origen es válida
    if monto_usd == None:
        print(f"Error: La moneda de origen '{origen}' no está soportada.")
        return

    # Paso 2 
    if destino == "USD":
        resultado = monto_usd * 1.0
    elif destino == "EUR":
        resultado = monto_usd * 0.92
    elif destino == "GBP":
        resultado = monto_usd * 0.78
    elif destino == "JPY":
        resultado = monto_usd * 155.0
    elif destino == "CAD":
        resultado = monto_usd * 1.36
    elif destino == "CHF":
        resultado = monto_usd * 0.90
    elif destino == "MXN":
        resultado = monto_usd * 18.00
    elif destino == "COP":
        resultado = monto_usd * 3900.0
    else:
        resultado = None

    # Validar si la moneda de destino es válida y mostrar el resultado
    if resultado == None:
        print(f"Error: La moneda de destino '{destino}' no está soportada.")
    else:
        print(f"\n---> Resultado: {monto:,.2f} {origen} = {resultado:,.2f} {destino}")

conversor_divisas()