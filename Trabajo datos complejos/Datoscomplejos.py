

#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}


precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("1) Diccionario con nuevas frutas:")
print(precios_frutas)
print("-" * 50)

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("2) Diccionario actualizado con nuevos precios:")
print(precios_frutas)
print("-" * 50)

#Ejercicio 3
lista_frutas = list(precios_frutas.keys())
print("3) Lista de frutas sin precios:")
print(lista_frutas)
print("-" * 50)

#Ejercicio 4
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input("Ingrese el número telefónico: ")
    agenda[nombre] = telefono

consulta = input("\nIngrese el nombre del contacto a buscar: ")
if consulta in agenda:
    print(f"Número de {consulta}: {agenda[consulta]}")
else:
    print("Contacto no encontrado.")
print("-" * 50)

#Ejercicio 5
frase = input("Ingrese una frase: ").lower()
palabras = frase.split()

palabras_unicas = set(palabras)
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("\nPalabras únicas:", palabras_unicas)
print("Cantidad de repeticiones por palabra:")
for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")
print("-" * 50)

#Ejercicio 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
print("-" * 50)

#Ejercicio 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("7) Resultados de parciales:")
print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)
print("-" * 50)

#Ejercicio 8
stock = {
    "Lapicera": 50,
    "Cuaderno": 20,
    "Regla": 30
}

producto = input("Ingrese el nombre del producto a consultar: ")
if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = input("¿Desea agregar unidades? (s/n): ").lower()
    if agregar == "s":
        unidades = int(input("Cantidad a agregar: "))
        stock[producto] += unidades
else:
    print("Producto no encontrado. Será agregado al stock.")
    nuevo_stock = int(input("Ingrese cantidad inicial: "))
    stock[producto] = nuevo_stock

print("\nStock actualizado:")
for prod, cant in stock.items():
    print(f"{prod}: {cant}")
print("-" * 50)

#Ejercicio 9
agenda_eventos = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "15:00"): "Clase de Python",
    ("Jueves", "09:30"): "Examen parcial"
}

dia = input("Ingrese el día a consultar: ").capitalize()
hora = input("Ingrese la hora (HH:MM): ")

evento = agenda_eventos.get((dia, hora))
if evento:
    print(f"Evento agendado: {evento}")
else:
    print("No hay eventos en ese día y hora.")
print("-" * 50)

#Ejercicio 10
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Perú": "Lima"
}

capitales = {capital: pais for pais, capital in paises.items()}
print("10) Diccionario invertido (capitales como claves):")
print(capitales)
print("-" * 50)
