#Definimos edad como un input de categoria entero para preguntar la edad al usuario
edad = int(input("Decime tu edad: "))

#Genero un condicional. Si la edad es menor a 18...
if edad < 18 :
    #Entonces imprime es menor de edad
    print("Es menor de edad")
    #Caso contrario imprime que es mayor
else:
    print("Es mayor de edad")