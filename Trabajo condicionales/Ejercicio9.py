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