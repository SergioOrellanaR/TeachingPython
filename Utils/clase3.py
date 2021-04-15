'''
> = mayor que
< = menor que
>= = mayor o igual
<= = menor o igual
== = igual
!= = Distinto a

and = Y 
or = O
'''

def numeroEsDiez(value):
    return value == 10 

def numeroEsVeinte(value):
    return value == 20 

def main():
    print("Ingrese un número: ")
    value = int(input())
    if(numeroEsDiez(value)):
        print("El número es 10")
    elif(numeroEsVeinte(value)):
        print("El número es 20")
    else:
        print("El número no es ni 10 ni 20")

main()