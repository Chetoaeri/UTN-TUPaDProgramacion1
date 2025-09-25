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