#condicionales if elsif else
#nos permite evaluar expresiones booleanas 
#Se realiza una accion y si esta se cumple se realiza otra accion 

#evaluar si una persona es mayor de edad
#nos diga si es un niño, joven, adulto, bebe, anciano  
genero=input("Ingresa tu genero (H/M): ")
age=int(input("Tecla tu edad "))
if genero=='m':
    if age<2:
        print("Eres una bb :3")
    elif age<17:
        print("eres una niña")
    elif age>18:
        print("eres una señorita")
    elif age>50:
        print("eres una señora")
    else:
        print("Eres muy mayor ")
if genero=='h':
    if age<=2:
        print("Eres un bb :3")
    elif age<17:
        print("eres un niño")
    elif age>18:
        print("eres un joven")
    elif age>50:
        print("eres un señor")
    else:
        print("Eres muy mayor")
