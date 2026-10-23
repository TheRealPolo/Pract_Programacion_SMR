ancho = int(input("Introduce el ancho del rectángulo: "))
largo = int(input("Introduce el largo del rectángulo: "))

for fila in range(ancho):
    for columna in range(largo):
        print("*", end="")
    print()
