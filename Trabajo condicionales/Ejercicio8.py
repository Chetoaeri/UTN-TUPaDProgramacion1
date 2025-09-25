#Defino nombre como un input para que el usuario elija su nombre
nombre = input("Decime tu nombre: ")
#Defino numero como el entero de un input para que el usuario elija un numero entero
numero = int(input("Decime un numero (1,2,3): "))

#Si numero es 1
if numero == 1:
#Nombre va a ser nombre con todas las letras mayusculas y se imprime nombre
    nombre = nombre.upper()
    print(nombre)
#Si numero es 2
elif numero == 2:
#Nombre va a ser nombre con todas las letras en minusculas y se imprime nombre
    nombre = nombre.lower()
    print(nombre)
#Si numero es 3
elif numero == 3:
#Nombre va a ser nombre pero con la primer letra mayuscula y se imprime nombre
    nombre = nombre.title()
    print(nombre)
#Caso contrario se imprime no valido
else:
    print("No valido")

