
#Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número para calcular su factorial: "))
print(f"\nFactoriales del 1 al {num}:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

print("-" * 50)


#Ejercicio 2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Ingrese hasta qué posición de Fibonacci desea ver: "))
print("\nSerie de Fibonacci:")
for i in range(num):
    print(fibonacci(i), end=" ")

print("\n" + "-" * 50)


#Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"\n{base}^{exponente} = {potencia(base, exponente)}")
print("-" * 50)


#Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(num)
print(f"El número {num} en binario es: {binario if binario != '' else '0'}")
print("-" * 50)


#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower().replace(" ", "")
if es_palindromo(texto):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
print("-" * 50)


#Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

num = int(input("Ingrese un número entero positivo: "))
print(f"La suma de sus dígitos es: {suma_digitos(num)}")
print("-" * 50)


#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques en el nivel inferior: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")
print("-" * 50)


#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número: "))
dig = int(input("Ingrese el dígito que desea contar: "))
print(f"El dígito {dig} aparece {contar_digito(numero, dig)} veces en {numero}.")
print("-" * 50)
