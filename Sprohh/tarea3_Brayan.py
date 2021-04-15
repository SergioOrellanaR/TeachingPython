def trianguloEquilatero(lado1,lado2,lado3):
    return lado1 == lado2 == lado3

def trianguloIsosceles(lado1,lado2,lado3):
    return (lado1==lado3) and (lado1!=lado2) and (lado3!=lado2)

def trianguloEscaleno(lado1,lado2,lado3):
    return (lado1!=lado2) and (lado1!=lado3) and (lado2!=lado3)

def perimetro(lado1,lado2,lado3):
    return lado1+lado2+lado3

def main():
    print('Ingrese el lado A del triangulo')
    lado1 = int(input())
    print('Ingrese el lado B del triangulo')
    lado2 = int(input())
    print('Ingrese el lado C del triangulo')
    lado3 = int(input())

    print('El perimetro del triangulo es: '+str(perimetro(lado1,lado2,lado3)))
    if(trianguloEquilatero(lado1,lado2,lado3)):
        print('El trignaulo es Equilatero')
    elif(trianguloIsosceles(lado1,lado2,lado3)):
        print('El triangulo es Isoscele')
    elif(trianguloEscaleno(lado1,lado2,lado3)):
        print('El triangulo es Escaleno')
    else:
        print('El tringualo no es Equilatero ni Isosceles ni Escaleno')

main()