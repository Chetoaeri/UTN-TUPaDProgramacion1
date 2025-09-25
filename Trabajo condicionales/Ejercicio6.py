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