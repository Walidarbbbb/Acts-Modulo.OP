import random
import time

print("Bienvenido al juego de Adivinar el número")
print("Estoy pensando en un número entre 1 y 100...")

numero_secreto = random.randint(1, 100)
inicio = time.time()
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Escribe tu número: "))
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo...")
    elif intento > numero_secreto:
        print("Demasiado alto...")
    else:
        adivinado = True
        print("Has acertado!")

    time.sleep(0.5)

fin = time.time()
duracion = round(fin - inicio, 2)

print(f"\nHas tardado {duracion} segundos en adivinarlo.")
print(f"Lo lograste en {intentos} intentos.")
