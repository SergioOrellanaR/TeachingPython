'''
op1: Suma de los 4 números.
op2: Suma de los 2 primeros menos los 2 últimos. 
op3: Suma de los 3 primeros y el resto de 5.
op4: La suma de los 2 primeros numeros x la suma de los 2 ultimos numeros dividido en 10 
op5: Resta del resultado de la op1 y op2

'''

def op1 (num1,num2,num3,num4):
    return (num1+num2+num3+num4)

def op2 (num1,num2,num3,num4):
    return ((num1+num2)-(num3+num4))

def op3 (num1,num2,num3):
    return (((num1+num2+num3)%5))

def op4 (num1,num2,num3,num4):
    return ((((num1+num2)*(num3+num4)/10)))

def op5 (num1,num2):
    return num1-num2

def datos () :
    print('Usuario ingrese un número desde el 1 al 3')
    num1=int(input())
    print('Usuario ingrese un número desde el 4 al 6')
    num2=int(input())
    print('Usuario ingrese un número desde el 7 al 9')
    num3=int(input())
    print('Usuario ingrese un número desde el 10 al 12')
    num4=int(input())
    primeraOp=op1(num1, num2, num3, num4)
    segundaOp=op2(num1, num2, num3, num4)
    print('La suma de los 4 numeros es '+str(primeraOp))
    print('La suma de los 2 primeros menos los 2 últimos es: '+str(segundaOp))
    print('La suma de los 3 primeros y el resto de 5 es: '+str(op3(num1, num2, num3)))
    print('La suma de los 2 primeros numeros x la suma de los 2 ultimos numeros dividido en 10 es: '+str(op4(num1, num2, num3, num4)))
    print('La resta del resultado de la op1 y op2 es:'+str(op5(primeraOp, segundaOp)))


datos ()



