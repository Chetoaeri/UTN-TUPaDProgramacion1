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