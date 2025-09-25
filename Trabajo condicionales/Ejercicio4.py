#Defino edad como entero para que el usuario coloque su edad
edad = int(input("¿Cuantos años tenes?: "))

#Si la edad es menor a 12 años imprime "Perteneces a categoria niño"
if edad < 12:
    print("Perteneces a categoria niño")
#Si la edad es mayor o igual que 12 y menor que 18 entonces imprime "Perteneces a categoria adolescente"
elif edad >= 12 and edad < 18 :
    print("Perteneces a categoria adolescente")
#Si la edad es mayor o igual que 18 y menor que 30 entonces imprime "Perteneces a categoria adulto/a joven"
elif edad >= 18 and edad < 30 :
    print("Perteneces a categoria adulto/a joven")
#En cualquier otro caso imprime "Perteneces a categoria adulto/a"
else:
    print("Perteneces a categoria adulto/a")
