#Definimos nota como un input de categoria entero para preguntar la nota al usuario
nota = int(input("Decime tu nota: "))

#Genero un condicional. Si la nota es menor a 6...
if nota < 6 :
    #Entonces imprime Desaprobado
    print("Desaprobado")
    #Caso contrario imprime Aprobado
else:
    print("Aprobado")