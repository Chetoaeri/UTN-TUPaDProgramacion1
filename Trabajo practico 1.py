
#Ejercicio 1#
print ("Hola Mundo!.")

#Ejercicio 2#

nombre1 = input("¿Cual es tu nombre?: ")

print (f"¡Hola {nombre1}!, ¿Como estas?")

#Ejercicio 3#

nombre3 = input("Decime tu nombre: ")
apellido3 = input("Decime tu apellido: ")
edad3 = input("¿Cuantos años tenes?: ")
residencia3 = input("Decime tu residencia: ")

print (f"Asi que sos {nombre3} {apellido3}, tenes {edad3} años, y vivis en {residencia3} ¿verdad?...")

#Ejercicio 4#

a4 = float(input("Decime un radio: "))
b4 = 3.14
c4 = (float(b4 * a4)) ** 2
d4 = 2 * (float(b4 * a4))

print (f"El area del circulo es de: {c4} y el perimetro es de: {d4}")

#Ejercicio 5#

segundos5 = int(input("Decime una cantidad de segundos: "))
minutos5 = segundos5 / 60
horas5 = minutos5 / 60

print(f"{segundos5} segundos equivalen a {horas5} horas.")

#Ejercicio 6#

numero6 = input("Decime un numero: ")
numeros6 = int(numero6)

print(f"1 * {numero6} = " , (numeros6 * 1))
print(f"2 * {numero6} = " , (numeros6 * 2))
print(f"3 * {numero6} = " , (numeros6 * 3))
print(f"4 * {numero6} = " , (numeros6 * 4))
print(f"5 * {numero6} = " , (numeros6 * 5))
print(f"6 * {numero6} = " , (numeros6 * 6))
print(f"7 * {numero6} = " , (numeros6 * 7))
print(f"8 * {numero6} = " , (numeros6 * 8))
print(f"9 * {numero6} = " , (numeros6 * 9))
print(f"10 * {numero6} = " , (numeros6 * 10))

#Ejercicio 7#

numero71 = int(input("Elegi un numero: "))
numero72 = int(input("Elegi otro numero: "))
suma7 = numero71 + numero72
resta7 = numero71 - numero72
multi7 = numero71 * numero72
divi7 = numero71 / numero72
print ("Los resultados son: ")
print (f"Suma = {suma7}")
print (f"Resta = {resta7}")
print (f"Multiplicacion = {multi7}")
print (f"Division = {divi7}")

#Ejercicio 8#
peso8 = int(input("Decime tu peso: "))
altura8 = int(input("Decime tu altura: "))
alturac8 = altura8 ** 2

imc8 = peso8 / alturac8

print("Tu indice de masa corporal es de: " , imc8)

#Ejercicio 9#

tempC9 = int(input("Decime una temperatura en Cº: "))
tempF9 = ((9/5)*tempC9 + 32)
print(tempC9 ," Cº son " , tempF9 , " Fº")

#Ejercicio 10#

numero101 = int(input ("Decime el primer numero: "))
numero102 = int(input ("Decime el segundo numero: "))
numero103 = int(input ("Decime el tercer numero: "))

promedio10 = (numero101 + numero102 + numero103) / 3

print("El promedio es de: " , promedio10)