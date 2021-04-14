#+ para suma
#- para resta
#* para multiplicación
#/ para división
#% para módulo (El resto)
def suma(val1, val2):
    return val1+val2

def resta(val1, val2):
    return val1-val2

def multiplicacion(val1, val2):
    return val1*val2

def division(val1, val2):
    return val1/val2



'''
TIPOS DE DATO
Int: 4 (int)
Float: 4.0 (float)
String: "Esto es una palabra" (str)
Boolean: True (1) or False(0) (bool)
'''

def main():
    print('Por favor usuario chan, ingrese un número')
    dato=int(input())
    print('Por favor usuario chan, ingrese otro número')
    dato2=int(input())
    print('La suma es: '+str(suma(dato,dato2)))
    print('La resta es: '+str(resta(dato,dato2)))
    print('La multiplicacion es: '+str(multiplicacion(dato,dato2)))
    print('La division es: '+str(division(dato,dato2)))

main()


''' 
TAREA
Realizar programa que solicite al usuario el ingreso de 4 números diferentes, y realizar (En lo posible separado en métodos) las siguientes operaciones:

Suma de los 4 números.
Suma de los 2 primeros menos los 2 últimos. ((dato1+dato2)-(dato3+dato4))
Suma de los 3 primeros y el resto de 5 (resultadoDeSuma%5)
La sgte operación: Dato1+Dato2*(Dato3+Dato4)/10


Bonus: En matemáticas las operaciones se resuelven en este orden:

Lo que va dentro de Paréntesis
Multiplicación
División
Suma y Resta


Torpedo:

def sumaDe4Numeros(dato1,dato2,dato3,dato4):
    return (dato1+dato2+dato3+dato4)
'''