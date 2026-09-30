def operaciones():
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))

    a_f = float(a)
    b_f = float(b)

    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a_f / b_f

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

    return suma, resta, multiplicacion, division

operaciones()