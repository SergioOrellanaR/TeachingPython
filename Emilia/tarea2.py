
def Ejercicio(ejercicio, dato1, dato2, dato3, dato4):
    if(ejercicio == 1):
        return dato1 + dato2 + dato3 + dato4
    elif(ejercicio == 2):
        return ((dato1+dato2)-(dato3+dato4))
    elif(ejercicio == 3):
        return (dato1+dato2+dato3)%5
    elif(ejercicio == 4):
        return dato1+dato2*(dato3+dato4)/10
    elif(ejercicio == 5):
        return Ejercicio(1, dato1, dato2, dato3, dato4) + Ejercicio(2, dato1, dato2, dato3, dato4)

def main():
    print("Ingresa 4 numeros diferentes")
    dato1 = int(input())
    dato2 = int(input())
    dato3 = int(input())
    dato4 = int(input())
    print(Ejercicio(1, dato1, dato2, dato3, dato4))
    print(Ejercicio(2, dato1, dato2, dato3, dato4))
    print(Ejercicio(3, dato1, dato2, dato3, dato4))
    print(Ejercicio(4, dato1, dato2, dato3, dato4))
    print(Ejercicio(5, dato1, dato2, dato3, dato4))

main()
