

numeros = []
while True:
    n = int(input("Escribe un número (0 para terminar): "))
    if n == 0:
        break
    numeros.append(n)
buscar = int(input("¿Qué número quieres buscar?: "))
posiciones = [i for i, num in enumerate(numeros) if num == buscar]
if posiciones:
    print(f"El número {buscar} aparece en las posiciones: {posiciones}")
else:
    print(f"El número {buscar} no aparece en la lista.")
