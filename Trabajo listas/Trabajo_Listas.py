import random

#Ejercicio 1
notas = [7, 8, 9, 6, 10, 5, 4, 8, 7, 9]
print("1) Lista de notas:", notas)
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("-" * 50)

#Ejercicio 2
productos = []
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

print("\nLista ordenada alfabéticamente:")
for p in sorted(productos):
    print(p)

eliminar = input("\nIngrese el producto que desea eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
else:
    print("Ese producto no está en la lista.")
print("Lista actualizada:", productos)
print("-" * 50)

#Ejercicio 3
numeros = [random.randint(1, 100) for _ in range(15)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("3) Lista de números:", numeros)
print("Pares:", pares, "→ Cantidad:", len(pares))
print("Impares:", impares, "→ Cantidad:", len(impares))
print("-" * 50)

#Ejercicio 4
valores = [1, 2, 2, 3, 4, 4, 5, 1, 6]
sin_repetidos = list(set(valores))
print("4) Lista original:", valores)
print("Lista sin repetidos:", sin_repetidos)
print("-" * 50)

#Ejercicio 5
estudiantes = ["Ana", "Juan", "Sofía", "Lucas", "María", "Pedro", "Luz", "Tomás"]
print("5) Lista actual:", estudiantes)
accion = input("¿Desea agregar o eliminar un estudiante? (agregar/eliminar): ").lower()

if accion == "agregar":
    nuevo = input("Nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == "eliminar":
    nombre = input("Nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        estudiantes.remove(nombre)
    else:
        print("Ese estudiante no está en la lista.")
else:
    print("Opción inválida.")

print("Lista final:", estudiantes)
print("-" * 50)

#Ejercicio 6
numeros = [1, 2, 3, 4, 5, 6, 7]
rotada = [numeros[-1]] + numeros[:-1]
print("6) Lista original:", numeros)
print("Lista rotada:", rotada)
print("-" * 50)

#Ejercicio 7
temperaturas = [
    [12, 25],
    [14, 24],
    [10, 22],
    [13, 26],
    [15, 27],
    [11, 23],
    [13, 28]
]

minimas = [t[0] for t in temperaturas]
maximas = [t[1] for t in temperaturas]

prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

amplitudes = [maximas[i] - minimas[i] for i in range(7)]
dia_mayor_amp = amplitudes.index(max(amplitudes)) + 1

print(f"7) Promedio mínimas: {prom_min:.2f}")
print(f"Promedio máximas: {prom_max:.2f}")
print(f"Día con mayor amplitud térmica: Día {dia_mayor_amp}")
print("-" * 50)

#Ejercicio 8
notas = [
    [7, 8, 6],
    [5, 9, 7],
    [6, 6, 8],
    [9, 7, 8],
    [8, 9, 10]
]

print("8) Promedio por estudiante:")
for i, fila in enumerate(notas):
    prom_est = sum(fila) / len(fila)
    print(f"Estudiante {i+1}: {prom_est:.2f}")

print("\nPromedio por materia:")
for j in range(3):
    prom_mat = sum(notas[i][j] for i in range(5)) / 5
    print(f"Materia {j+1}: {prom_mat:.2f}")
print("-" * 50)

#Ejercicio 9
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(t):
    for fila in t:
        print(" ".join(fila))
    print()

turno = "X"
for _ in range(5):
    print(f"Turno del jugador {turno}")
    fila = int(input("Fila (0-2): "))
    col = int(input("Columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = turno
        mostrar_tablero(tablero)
        turno = "O" if turno == "X" else "X"
    else:
        print("Casilla ocupada, elija otra.")
print("-" * 50)

#Ejercicio 10
ventas = [
    [10, 12, 8, 9, 15, 11, 13],
    [5, 7, 6, 8, 9, 10, 12],
    [14, 13, 15, 16, 12, 11, 14],
    [8, 9, 10, 9, 11, 10, 12]
]

totales_productos = [sum(fila) for fila in ventas]
print("10) Total vendido por producto:", totales_productos)

ventas_dias = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_mayor_venta = ventas_dias.index(max(ventas_dias)) + 1
print("Día con mayores ventas totales:", dia_mayor_venta)

producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print("Producto más vendido:", producto_mas_vendido)
