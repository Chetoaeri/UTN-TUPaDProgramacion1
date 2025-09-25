#Defino dia como un input entero para que el usuario elija un dia
dia = int(input("Decime un dia: "))
#Defino mes como input para que el usuario elija un mes
mes = input("Decime un mes: ")
#Paso el mes a minusculas
mes = mes.lower()

#Si las condiciones dadas se cumplen entonces se define tanto norte como sur
if (mes == "diciembre" and dia >= 21 and dia <= 31) or (mes == "enero" and dia >= 1 and dia <= 31) or (mes == "febrero" and dia >= 1 and dia <= 28) or (mes == "marzo" and dia >= 1 and dia <= 20):
    norte = "Invierno"
    sur = "Verano"
#Si las condiciones dadas se cumplen entonces se define tanto norte como sur
elif  (mes == "marzo" and dia >= 21 and dia <= 31) or (mes == "abril" and dia >= 1 and dia <= 30) or (mes == "mayo" and dia >= 1 and dia <= 31) or (mes == "junio" and dia >= 1 and dia <= 20):
    norte = "Primavera"
    sur = "Otoño"
#Si las condiciones dadas se cumplen entonces se define tanto norte como sur
elif (mes == "junio" and dia >= 21 and dia <= 30) or (mes == "julio" and dia >= 1 and dia <= 31) or (mes == "agosto" and dia >= 1 and dia <= 31) or (mes == "septiembre" and dia >= 1 and dia <= 20):
    norte = "Verano"
    sur = "Invierno"
#Si las condiciones dadas se cumplen entonces se define tanto norte como sur
elif (mes == "septiembre" and dia >= 21 and dia <= 30) or (mes == "octubre" and dia >= 1 and dia <= 31) or (mes == "noviembre" and dia >= 1 and dia <= 30) or (mes == "diciembre" and dia >= 1 and dia <= 20):
    norte = "Otoño"
    sur = "Primavera"
#En caso contrario se imprime que no es valido
else:
    print("No es valido")

#Defino norsur como input para que el usuario elija si es del norte o si es del sur
norsur = input("¿De donde sos?: ")
#Paso norsur a minusculas
norsur = norsur.lower()
#Si norsur es definido como norte entonces se imprime el texto junto con norte
if norsur == "norte":
    print("En el norte es: " + norte)
#Si norsur es definido como sur entonces se imprime el texto junto con sur
elif norsur == "sur":
    print("En el sur es: " + sur)
#De otro modo se imprime que no es valido
else:
    print("No es valido")
