#Ejercicio 1
with open("productos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,350.0,15\n")
    archivo.write("Regla,90.0,40\n")

print("Archivo 'productos.txt' creado con productos iniciales.\n")


#Ejercicio 2
productos = []
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("\nProductos cargados correctamente.")
print("-" * 50)


#Ejercicio 3
agregar = input("¿Desea agregar un nuevo producto? (s/n): ").lower()
while agregar == "s":
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

   
    with open("productos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    agregar = input("¿Desea agregar otro producto? (s/n): ").lower()

print("\nProductos actualizados:")
for p in productos:
    print(f"{p['nombre']} - ${p['precio']} ({p['cantidad']} unidades)")
print("-" * 50)


#Ejercicio 4
buscar = input("Ingrese el nombre del producto a buscar: ").capitalize()
encontrado = False

for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nEl producto no existe en la lista.")
print("-" * 50)


#Ejercicio 5
with open("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo actualizado correctamente con los productos actuales.")
print("-" * 50)
