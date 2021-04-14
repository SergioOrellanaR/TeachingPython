def mensaje(nombreDato):
    return "Ingrese el "+nombreDato+" numero"

def solicitaNumero():
    return int(input())

def sumaDosNumeros(val1,val2):
    return val1 + val2

def sumaCuatroNumeros(val1,val2,val3,val4):
    return val1+val2+val3+val4

def operacionDos(val1,val2,val3,val4):
    return sumaDosNumeros(val1,val2) - sumaDosNumeros(val3,val4)

def operacionTres(val1,val2,val3,val4):
    return ((val1+val2+val3)%5)

def operacionCuatro(val1,val2,val3,val4):
    return (sumaDosNumeros(val1,val2)*sumaDosNumeros(val3,val4)/10)

def operacionCinco(val1,val2):
    return val1 - val2

def realizarOperaciones(val1,val2,val3,val4):
    resultadoUno = sumaCuatroNumeros(val1,val2,val3,val4)
    resultadoDos = operacionDos(val1,val2,val3,val4)
    print("Suma de 4 números: ")
    print(str(resultadoUno))
    print("Suma de 2 primeros menos 2 últimos: ")
    print(str(resultadoDos))
    print("Suma de 3 primeros y resto de 5: ")
    print(operacionTres(val1,val2,val3,val4))
    print("Cuarta operación: ")
    print(operacionCuatro(val1,val2,val3,val4))
    print("Operación 1 - Operación 2: ")
    print(operacionCinco(resultadoUno, resultadoDos))

def main():
    print(mensaje("primer"))
    val1=solicitaNumero()
    print(mensaje("segundo"))
    val2=solicitaNumero()
    print(mensaje("tercer"))
    val3=solicitaNumero()
    print(mensaje("cuarto"))
    val4=solicitaNumero()
    print("---------------------------------------")
    print("RESULTADOS: ")
    print("---------------------------------------")
    realizarOperaciones(val1,val2,val3,val4)

main()