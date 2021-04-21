'''
    1.- Escriba un programa que pida al usuario ingresar una cantidad, esa cantidad será el número de veces que el usuario deberá ingresar números positivos, a continuación pida números hasta que se haya escrito la cantidad de números positivos indicada.
    
    Por ejemplo: El usuario inserta '4'.
    El programa le pedirá ingresar números hasta que haya ingresado 4 números positivos.
    
    2.- Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
    
    3.-Escriba un programa que guarde en un diccionario los precios del valor por kilo de cada fruta (Plátano = 800, Manzana = 500, Pera = 1200 y Naranja= 1000), pregunte al usuario por una fruta, número de kilos a comprar y muestre por pantalla el precio a gastar. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
'''



class Auto:

    def __init__(self, marca, km, color):
        self.marca = marca
        self.kilometraje = km
        self.color = color


def main():
    
    lista = [
    Auto("Mercedes",2000, "Blanco"), 
    Auto("Audi",10000, "Negro"), 
    Auto("Chevrolet",50000,"Azul"), 
    Auto("Ferrari",0, "Rojo"), 
    Auto("Toyota",3000,"Blanco"), 
    Auto("Subaru",20000,"Verde")
    ]

    diccionario = {
        "Pera" : 1000,
        "Manzana" : 2000,
        "Naranja" : 1500
    }

    for i in diccionario:
        print(i)
        print(diccionario[i])
        print("---------------------")

'''    
    for i in diccionario.keys:
        print(i.marca)
        print(i.color)
        print("---------------------")
'''        


'''
    while index < 10:
        index += 1
        if index == 5:
            continue
        print(index)
    else:
        print("El ciclo dejó de ejecutarse porque el índice fue mayor a 10")
'''    


main()