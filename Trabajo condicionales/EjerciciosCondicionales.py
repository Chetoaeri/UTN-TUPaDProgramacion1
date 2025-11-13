#Ejercicio 1
#Definimos edad como un input de categoria entero para preguntar la edad al usuario
edad = int(input("Decime tu edad: "))

#Genero un condicional. Si la edad es menor a 18...
if edad < 18 :
    #Entonces imprime es menor de edad
    print("Es menor de edad")
    #Caso contrario imprime que es mayor
else:
    print("Es mayor de edad")

#Ejercicio 2
#Definimos nota como un input de categoria entero para preguntar la nota al usuario
nota = int(input("Decime tu nota: "))

#Genero un condicional. Si la nota es menor a 6...
if nota < 6 :
    #Entonces imprime Desaprobado
    print("Desaprobado")
    #Caso contrario imprime Aprobado
else:
    print("Aprobado")

#Ejercicio 3
#Defino a nume como un input entero para que el usuario elija un numero
nume = int(input ("Decime un numero par: "))

#Defino comprobacion como el resto entre nume y 2
comprobacion = nume % 2

#Si comprobacion es igual a 0 eso indica que el numero es par
if comprobacion == 0 :
    #Entonces imprimiria que es par
    print("Ha ingresado un número par")
    #Caso contrario imprime que es impar
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
#Defino edad como entero para que el usuario coloque su edad
edad = int(input("¿Cuantos años tenes?: "))

#Si la edad es menor a 12 años imprime "Perteneces a categoria niño"
if edad < 12:
    print("Perteneces a categoria niño")
#Si la edad es mayor o igual que 12 y menor que 18 entonces imprime "Perteneces a categoria adolescente"
elif edad >= 12 and edad < 18 :
    print("Perteneces a categoria adolescente")
#Si la edad es mayor o igual que 18 y menor que 30 entonces imprime "Perteneces a categoria adulto/a joven"
elif edad >= 18 and edad < 30 :
    print("Perteneces a categoria adulto/a joven")
#En cualquier otro caso imprime "Perteneces a categoria adulto/a"
else:
    print("Perteneces a categoria adulto/a")

#Ejercicio 5
#Defino contra para que el usuario ponga una contraseña
contra = input("Elegi una contraseña: ")
#Defino longitud para saber la cantidad de caracteres que tiene la misma
longitud = len(contra)
#Si la longitud en menor a 8 o mayor a 14...
if longitud < 8 or longitud > 14:
    #Imprime el siguiente texto
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else:
    #Caso contrario imprime lo siguiente
    print("Ha ingresado una contraseña correcta")

#Ejercicio 6
import random
from statistics import mode, median, mean

#Definimos numeros_aleatorios en el que se van a elegir 50 numero aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1,100) for i in range (50)]

print("##########################################")
#Imprimo los numeros aleatorios generados
print(numeros_aleatorios)
print("##########################################")

#Calculo la moda y la imprimo
moda = mode(numeros_aleatorios)
print("La moda es: ", moda)

#Calculo la mediana y la imprimo
mediana = median (numeros_aleatorios)
print("La mediana es: ", mediana)

#Calculo la media y la imprimo
media = mean (numeros_aleatorios)
print("La media es: ", media)

#Si la media es mayor a la mediana y la mediana es mayor a la moda...
if media > mediana and mediana > moda: 
    #Se imprime lo siguiente
    print("Hay sesgo positivo")
#Si la media es menor a la mediana y la mediana es menor a la moda...
elif media < mediana and mediana < moda:
    #Se imprime lo siguiente
    print("Hay sesgo negativo")
#Si la media es igual a la mediana y la mediana es igual a la moda...
elif media == mediana and mediana == moda:
    #Se imprime lo siguiente
    print("No hay sesgo")

#Ejercicio 7
#Definimos palabra como input para que el usuario elija una palabra
palabra = input("Decime una palabra: ")
#Definimos letra como la ultima letra de palabra
letra = palabra[-1]

#Si letra es igual a una vocal entonces se imprime palabra mas un !
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    
    print(palabra + "!")

#Por el contrario se imprime la palabra
else:
    print(palabra)

#Ejercicio 8
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

#Ejercicio 9
#Defino magnitud como un entero el cual el usuario puede elegir
magnitud = int(input("Decime la magnitud del terremoto: "))

#Si magnitud es menor que 3 entonces se define terremoto
if magnitud < 3:
    terremoto = "Muy leve (imperceptible)."
#Si magnitud es mayor igual a 3 y magnitud es menor que 5 se define terremoto
elif magnitud >= 3 and magnitud < 5:
    terremoto = "Moderado (sentido por personas, pero generalmente no causa daños)."
#Si magnitud es mayor igual a 5 y magnitud es menor que 6 se define terremoto
elif magnitud >= 5 and magnitud < 6:
    terremoto = "Fuerte (puede causar daños en estructuras débiles)."
#Si magnitud es mayor igual a 6 y magnitud es menor que 7 se define terremoto
elif magnitud >= 6 and magnitud < 7:
    terremoto = "Muy Fuerte (puede causar daños significativos)."
#Si magnitud es mayor a 7 se define terremoto
else:
    terremoto = "Extremo (puede causar graves daños a gran escala)."

#Imprimimos el resultado
print("La magnitud del terremoto es: " + terremoto)

#Ejercicio 10
#Defino dia como un input entero para que el usuario elija un dia
dia = int(input("Decime un dia: "))
#Defino mes como input para que el usuario elija un mes
mes = input("Decime un mes: ")
#Paso el mes a minusculas
mes = mes.lower()

#Si las condiciones dadas se cumplen entonces se define tanto norte como sur
if (mes == "diciembre" and dia >= 21 and dia <= 31) or (mes == "enero" and dia >= 1 and dia <= 31) or (mes == "febrero" and dia >= 1 and dia <= 28) or (mes == "marzo" and dia >= 1 and dia <= 20):
    norte = "Invierno"
    sur = "Verano"
#Si las condiciones dadas se cumplen entonces se define tanto norte como sur
elif  (mes == "marzo" and dia >= 21 and dia <= 31) or (mes == "abril" and dia >= 1 and dia <= 30) or (mes == "mayo" and dia >= 1 and dia <= 31) or (mes == "junio" and dia >= 1 and dia <= 20):
    norte = "Primavera"
    sur = "Otoño"
#Si las condiciones dadas se cumplen entonces se define tanto norte como sur
elif (mes == "junio" and dia >= 21 and dia <= 30) or (mes == "julio" and dia >= 1 and dia <= 31) or (mes == "agosto" and dia >= 1 and dia <= 31) or (mes == "septiembre" and dia >= 1 and dia <= 20):
    norte = "Verano"
    sur = "Invierno"
#Si las condiciones dadas se cumplen entonces se define tanto norte como sur
elif (mes == "septiembre" and dia >= 21 and dia <= 30) or (mes == "octubre" and dia >= 1 and dia <= 31) or (mes == "noviembre" and dia >= 1 and dia <= 30) or (mes == "diciembre" and dia >= 1 and dia <= 20):
    norte = "Otoño"
    sur = "Primavera"
#En caso contrario se imprime que no es valido
else:
    print("No es valido")

#Defino norsur como input para que el usuario elija si es del norte o si es del sur
norsur = input("¿De donde sos?: ")
#Paso norsur a minusculas
norsur = norsur.lower()
#Si norsur es definido como norte entonces se imprime el texto junto con norte
if norsur == "norte":
    print("En el norte es: " + norte)
#Si norsur es definido como sur entonces se imprime el texto junto con sur
elif norsur == "sur":
    print("En el sur es: " + sur)
#De otro modo se imprime que no es valido
else:
    print("No es valido")
