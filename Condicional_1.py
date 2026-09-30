def calcular_mayoría_de_edad(edad):

    if edad >= 18 and edad <= 150:
        return "Eres mayor de edad."
    elif edad < 18 and edad >= 0:
        return "Eres menor de edad."
    elif edad > 150:
        return "¿Porque no estás muerto bro?."
    elif edad < 0:
        return "Bro... aún no has nacido."
    else:
        return "Edad no válida."

edad = int(input("Introduce tu edad: "))
print(calcular_mayoría_de_edad(edad))

