def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división entre cero"

while True:
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Saliendo del programa...")
        break

    if opcion in ["1", "2", "3", "4"]:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))

        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            print("Resultado:", dividir(a, b))
    else:
        print("Opción no válida")
