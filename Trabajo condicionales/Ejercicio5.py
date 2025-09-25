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