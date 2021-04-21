'''
    1.- Escriba un programa que pida al usuario ingresar una cantidad, 
    esa cantidad será el número de veces que el usuario deberá ingresar números positivos, 
    a continuación pida números hasta que se haya escrito la cantidad de números positivos indicada.
    
    Por ejemplo: El usuario inserta '4'.
    El programa le pedirá ingresar números hasta que haya ingresado 4 números positivos.
    
    2.- Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
    
    3.-Escriba un programa que guarde en un diccionario los precios del valor por kilo de cada 
    fruta (Plátano = 800, Manzana = 500, Pera = 1200 y Naranja= 1000), pregunte al usuario por una fruta, 
    número de kilos a comprar y muestre por pantalla el precio a gastar. 
    Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
'''


def main():
    def numerosPositivos():
        listaNumeros = []
        cantNumeros = int(input("Cuantos numeros positivos desea ingresar?: "))
        if(cantNumeros>0):
            i = 1
            posicionNum = 1
            while i <= cantNumeros:
                numero = int(input("Ingrese el numero "+str(i)+" : "))
                if (numero>0):
                    i += 1
                    listaNumeros.append(numero)                
                else:
                    print('Ingrese un numero positivo')
            else:
                for num in listaNumeros:
                    print('Numero ingresado en la posicion '+str(posicionNum)+' es : '+str(num))
                    posicionNum+=1
        else:
            print('Ingrese un numero positivo')


#2.- Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
    def numDivisores():
        numero = int(input("Escriba un numero entero mayor que cero: "))
        if(numero>0):
            print(f"Los divisores de {numero} son ", end="")
            for i in range(1, numero + 1):
                if numero % i == 0:
                    print(i, end=" ")
        else:
            print('El numero debe ser positivo')

    def productoFruta():
        frutas = {
            "Platano" : 800,
            "Manzana" : 500,
            "Pera" : 1200,
            "Naranja" : 10000
        }
        fruta = str(input("Que fruta desea comprar?: "))
        comprar = True
        while comprar == True:
            if (frutas.get(fruta) != None):
                valorFruta = frutas[fruta]
                kilos = int(input("El valor de la fruta es "+str(valorFruta)+", cuantos kilos desea llevar? : "))
                if(kilos>0):
                    valorTotal = kilos * valorFruta
                    print("El valor total de la compra es de $"+ str(valorTotal))
                    comprar = False
                else:
                    print("Porfavor ingresar un numero de kilos positivo")
            else:
                decision = str(input("La fruta ingresada no esta disponible, desea seguir comprando?: Si o No : "))
                if(decision == "Si"):
                    fruta = str(input("Que fruta desea comprar?: "))
                    comprar = True
                else:
                    comprar = False

    print('Que desea realizar? Presionar 1 : Ingresar numeros positivos ~ 2 : Numero y sus divisores ~ 3 : Diccionario valor Frutas')
    opcion = int(input())
    if(opcion == 1):
        numerosPositivos()
    elif(opcion == 2):
        numDivisores()
    elif(opcion == 3):
        productoFruta()
    else:
        print('Debe ingresar una opcion del 1 al 3')

main()
