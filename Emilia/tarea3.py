#Solicite ingresar al usuario la medida de 3 lados de un tríangulo, el sistema debe mostrar:

#1.- Perímetro del triangulo
#2.- Tipo de triangulo (Equilátero, isósceles o escaleno).

def perimetro(l1, l2, l3):
    return l1 + l2 + l3

def esIsosceles(l1, l2, l3):
    return l1 == l2 or l1 == l3 or l2 == l3

def esEquilatero(l1, l2, l3):
    return l1 == l2 and l1 == l3

def solicitaNumero():
    return int(input())

def main():
    print("Ingresa las 3 medidas de un triangulo")
    lado1 = solicitaNumero()
    lado2 = solicitaNumero()
    lado3 = solicitaNumero()
    if(esEquilatero(lado1, lado2, lado3)):
        print("Este es un tipo de triangulo Equilatero")
    elif(esIsosceles(lado1, lado2, lado3)):
        print("Este es un tipo de triangulo Isosceles")
    else:
        print("Este es un tipo de triangulo Escaleno")
    print("El perimetro del triangulo es de " + str(perimetro(lado1, lado2, lado3)))

main()