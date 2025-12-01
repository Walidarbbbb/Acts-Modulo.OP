import random
import time

# Juego 1: Pieda Papel o Tijera 
def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    print("\n--- Piedra, Paple o Tijera ---")  
    elec = input("Elige (piedra/papel/tijera): ").lower()
    while elec not in opciones:
        elec = input("Entrada invalida. Pon piedra, papel o tijera: ").lower()

    maquina = random.choice(opciones)
    print("La maquina ha elegido:", maquina)  

    if elec == maquina:
        print("Empate!")
    elif elec == "piedra" and maquina == "tijera":
        print("Has ganado :)")
    elif elec == "papel" and maquina == "piedra":
        print("Has ganado :)")
    elif elec == "tijera" and maquina == "papel":
        print("Has ganado :)")
    else:
        print("Uy... creo que has perdido. :(")


# Juego 2: Adivina el numero
def adivina_numero():
    print("\n--- Adivina el numero ---") 
    print("Dificultad:")
    print("1) Facil (1-20)")
    print("2) Normal (1-50)")
    print("3) Dificil (1-100)")

    while True:
        try:
            dif = int(input("Elige dificultad (1/2/3): "))
            if dif in (1,2,3):
                break
        except:
            pass
        print("Opcion invalida, intenta otra vez.")

    limites = {1:20, 2:50, 3:100}
    limite = limites[dif]
    secreto = random.randint(1, limite)

   
    intentos = 4
    print(f"Adivina un numero entre 1 y {limite}. Tienes 4 intentos.")  

    inicio = time.time()
    while intentos > 0:
        try:
            guess = int(input("Tu intento: "))
        except:
            print("Eso no es un numero valido.")
            continue

        if guess == secreto:
            tiempo = round(time.time() - inicio, 2)
            print(f"Enorabuena! Lo acertaste en {tiempo} segundos y te han sobrado {intentos} intentos.")
            return
        elif guess < secreto:
            print("Mas alto ↑")
        else:
            print("Mas bajo ↓")

        intentos -= 1
        print("Intentos restantes:", intentos)

    print("Se acabó! El numero era:", secreto)


# Juego 3: Calculo mental 
def calculo_mental():
    print("\n--- Calculo Mental ---")
    print("Tienes 20 segundos para responder (o eso dice el cartel)...") 

    aciertos = 0
    inicio = time.time()

    limite_tiempo = 15
    while time.time() - inicio < limite_tiempo:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        oper = random.choice(["+", "-"])
        correcto = a + b if oper == "+" else a - b

        try:
            resp = int(input(f"{a} {oper} {b} = "))
            if resp == correcto:
                aciertos += 1
                print("Bien!")
            else:
                print("No, ese no es.")
        except:
            print("Entrada no valida, siguiente...")

    print("Se acabó el tiempo! Has conseguido:", aciertos, "aciertos.")


# Juego 4: Eco loco 
def eco_loco():
    print("\n--- Eco Loco ---")
    texto = input("Escribe algo y te devuelvo cosas chulas: ")

    invertida = texto[::-1]
    caracteres = len(texto)
    
    vocales = sum(1 for c in texto.lower() if c in "aeiou")
    print("Cadena invertida ->", invertida)
    print("Numero de caracters:", caracteres)  
    print("Numero de vocales (sin tildes):", vocales)


# MENU PRINCIPAL 
def main():
    while True:
        print("\n==============================")
        print("     MINI ARCADE - PRINCIPIANTE")
        print("==============================")
        print("1. Piedra, Papel o Tijera")
        print("2. Adivina el numero")
        print("3. Calculo mental")
        print("4. Eco loco")
        print("0. Salir")
        print("==============================")

        try:
            opcion = int(input("Elige una opcion: "))
        except:
            print("Pon un numero por favor.")
            continue

        if opcion == 1:
            piedra_papel_tijera()
        elif opcion == 2:
            adivina_numero()
        elif opcion == 3:
            calculo_mental()
        elif opcion == 4:
            eco_loco()
        elif opcion == 0:
            print("Saliendo... hasta luego!")
            break
        else:
            print("Opcion no valida, prueba otra vez.")


if __name__ == "__main__":
    main()