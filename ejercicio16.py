N = int(input("Introduce el tamaño de la matriz (N): "))
matriz = []

for i in range(N):
    fila = []
    for j in range(N):
        valor = int(input(f"Introduce el valor de la posición [{i},{j}]: "))
        fila.append(valor)
    matriz.append(fila)

es_identidad = True
for i in range(N):
    for j in range(N):
        if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
            es_identidad = False
            break

if es_identidad:
    print(" La matriz es una matriz identidad.")
else:
    print("La matriz NO es una matriz identidad.")
