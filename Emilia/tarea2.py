def Ejercicio1(d1,d2,d3,d4):
    return d1 + d2 + d3 + d4

def Ejercicio2(d1,d2,d3,d4):
    return ((d1+d2)-(d3+d4))

def Ejercicio3(d1,d2,d3,d4):
    return (d1+d2+d3)%5

def Ejercicio4(d1,d2,d3,d4):
    return d1+d2*(d3+d4)/10

def Ejercicio5(d1,d2,d3,d4):
    return Ejercicio1(d1, d2, d3, d4) + Ejercicio2(d1, d2, d3, d4)

def main():
    print("Ingresa 4 numeros diferentes")
    dato1 = int(input())
    dato2 = int(input())
    dato3 = int(input())
    dato4 = int(input())
    print(Ejercicio1(dato1, dato2, dato3, dato4))
    print(Ejercicio2(dato1, dato2, dato3, dato4))
    print(Ejercicio3(dato1, dato2, dato3, dato4))
    print(Ejercicio4(dato1, dato2, dato3, dato4))
    print(Ejercicio5(dato1, dato2, dato3, dato4))

main()
