#Ejercicio 1
numero = 0
while numero != 101:
    print(numero)
    numero = numero + 1

#Ejercicio 2
usuario = int(input("Decime un numero: "))
contador = 0

while usuario > 1:
    usuario = usuario / 10
    contador += 1

print(f"El numero entregado tiene ",contador, " digitos")

#Ejercicio 3
numero1 = int(input("Decime un numero: "))
numero2 = int(input("Decime otro numero: "))
suma = numero1
suma2 = 0
while suma != (numero2 - 1):

    suma = suma + 1 
    suma2 = suma + suma2
    
    print (f"1 = " , suma)
    print (f"2 = " , suma2)

#Ejercicio 4
contador = 1
equis = 0
while contador != 0:
    contador = int(input("Decime un numero: "))
    resultado = contador + equis
    equis = resultado
print(equis)

#Ejercicio 5
import random
aleatorio = random.randint(0 , 9)
elegir = 10
intentos = 0
while elegir != aleatorio:
    elegir = int(input("Elegi un numero del 0 al 9: "))
    intentos = intentos + 1
print(f"LLevo " , intentos , " intentos")

#Ejercicio 6
resto = 0
for i in range (0 , 101):
    resto = i % 2
    if resto == 0:
        print(i)

#Ejercicio 7
suma = 0
suma2 = 0
usuario = int(input("Elegi un numero: "))
for i in range (0 , (usuario + 1)):
    suma = suma + 1 
    suma2 = suma + suma2
    print (suma2)

#Ejercicio 8
negativos = 0
positivos = 0
pares = 0
impares = 0
for i in range (0,100):
    usuario = int(input("Elegi un numero: "))
    if usuario > 0:
        positivos = positivos + 1
    if usuario < 0:
        negativos = negativos + 1
    if usuario % 2 == 0:
        pares = pares + 1
    if usuario % 2 != 0:
        impares = impares + 1
print (f"Hay " , pares, " numeros pares")
print (f"Hay " , impares, " numeros impares")
print (f"Hay " , positivos, " numeros positivos")
print (f"Hay " , negativos, " numeros negativos")

#Ejercicio 9
suma = 0


for i in range (0 , 100):
    usuario = int(input("Decime un numero: "))
    suma = suma + usuario
media = suma / 100
print(f"La media de los numeros sumados es de " , media)

#Ejercicio 10
usuario = 2
numero = int(input("Decime un numero: "))
invertido = 0
while numero != 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10
print(f"El numero invertido es: " , invertido)