#juego de piedra papel o tijera con el usuario 
import random
#leer la eleccion del usario 
user=input("Elige: Piedra, Papel o Tijera ")
#generar eleccion de la maquina 
aleatorio=random.randint(1,3)
if aleatorio==1:
    machine='piedra'
elif aleatorio ==2:
    machine='papel'
elif aleatorio==3:
    machine='tijera'

#comparar para saber quien gana 
print("El usuario elige ", user, "la maquina eligio ", machine)
if machine=='piedra' and 'papel':
    print("Gana el usuario ")
elif machine=='papel' and 'tijera':
    print("Gana el usuario")
elif machine=='tijera' and 'piedra':
    print("Gana el usuario ")

elif machine=='papel' and 'piedra':
    print("perdio")
elif machine=='tijera' and 'papel':
    print("perdio")
elif machine=='tijera' and 'piedra':
    print("perdio")

else:
    print("empate")

