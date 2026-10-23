cantidad = float(input("Ingrese la cantidad de dinero: "))

while opcion in [1, 2]:
    opcion = int(input("Ingrese 1 para aplicar interés, 2 para aplicar cargo, o 0 para salir: "))
    if opcion == 1:
        cantidad += cantidad * 0.05
        print("Se ha aplicado un interés del 5%. Nuevo saldo:", cantidad)
    elif opcion == 2:
        cantidad -= cantidad * 0.02
        print("Se ha aplicado un cargo del 2%. Nuevo saldo:", cantidad)