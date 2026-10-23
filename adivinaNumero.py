import random

numero = random.randint(0, 10)
intentos = 0

while True:
    respuesta = int(input("Adivina el número (entre 0 y 10): "))
    intentos += 1

    if respuesta == numero:
        break

print(f"¡Correcto! Lo has adivinado en {intentos} intentos.")