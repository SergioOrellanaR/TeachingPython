def sumaDosValores(val1,val2):
    return val1+val2

def sumaTresValores(val1,val2,val3):
    return val1+val2+val3

def sumaCuatroValores(val1,val2,val3,val4):
    return val1+val2+val3+val4

def main():
    print('Por favor ingrese un numero')
    dato1 = int(input())
    print('Por favor ingrese otro numero')
    dato2 = int(input())
    print('Por favor ingrese otro numero')
    dato3 = int(input())
    print('Por favor ingrese otro numero')
    dato4 = int(input())
    print('La suma de los 4 numeros es : '+str(sumaCuatroValores(dato1,dato2,dato3,dato4)))
    print('La suma de los 2 primeros menos los dos ultimos es : '+str(sumaDosValores(dato1,dato2)-sumaDosValores(dato3,dato4)))
    print('La suma de los tres primeros y el resto de 5 es : '+str((sumaTresValores(dato1,dato2,dato3))%5))
    print('El resultaado de la operacion es : '+str(sumaDosValores(dato1,dato2)*(sumaDosValores(dato3,dato4))/10))
    print('Operacion 1 - Operacion 2 es : '+str((sumaCuatroValores(dato1,dato2,dato3,dato4))-(sumaDosValores(dato1,dato2)-sumaDosValores(dato3,dato4))))


main()
