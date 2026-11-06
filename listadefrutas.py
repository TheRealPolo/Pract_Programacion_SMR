lista = ["apple", "banana", "pear"]

# 1. Añadir "watermelon" al final de la lista
lista.append("watermelon")
print(lista)

# 2. Insertar "strawberry" en la posición 1
lista.insert(1, "strawberry")
print(lista)

# 3. Imprimir la lista de frutas
print("Lista de frutas:")
for fruta in lista:
    print(fruta)

# 4. Imprimir el tercer elemento de la lista
print(lista[2])

# 5. Imprimir la posición de "banana" en la lista
print(lista.index("banana"))

#6. Imprimir la lista de frutas en orden alfabético
print("Lista de frutas en orden alfabético:")
for fruta in sorted(lista):
    print(fruta)

