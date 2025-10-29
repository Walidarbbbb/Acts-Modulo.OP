
nombres = input("Introduce nombres separados por comas: ")
lista_nombres = [nombre.strip() for nombre in nombres.split(",")]
lista_invertida = lista_nombres[::-1]
print("Lista invertida:", lista_invertida)
