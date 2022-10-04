import os
def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multi(num1, num2):
    return num1*num2

def div(num1, num2):
    if num2==0:
        num2=1
    return num1/num2
def return_values():
    num1=int(input("Ingresa un numero "))
    num2=int(input("Ingresa un segundo numero "))
    return [num1, num2] #regresa los numeros

if __name__ == '__main__':
    os.system('cls')
    message=f"Calculadora:\n  Elige la opcion\n 1=Suma\n  2=Resta\n  3=Multiplicacion\n 4=Divison\n 5=Para salir\n"
    while True:
        option=int(input(message))
        #compara cada opcion y llama a la funcion correspondiente 
        if option == 1:
            #pedir numeros al usuario 
            numeros=return_values()
            resultado_suma=suma(numeros[0], numeros[1])
            print("el resultado de la suma es ", resultado_suma)
        elif option== 2:
            #pedir numeros al usuario 
            numeros=return_values()
            resultado_resta=resta(numeros[0], numeros[1])
            print("el resultado de la resta es ", resultado_resta)
        elif option==3:
            #pedir numeros al usuario
            numeros=return_values() 
            resultado_multi=multi(numeros[0], numeros[1])
            print("el resultado de la multiplicacion es ", resultado_multi)
        elif option==4:
            #pedir numeros al usuario
            numeros=return_values() 
            resultado_div=div(numeros[0], numeros[1])
            print("el resultado de la division es ", resultado_div)
        elif option == 5:
            print("BYE")
            break
        else:
            print ("Opcion incorrecta")