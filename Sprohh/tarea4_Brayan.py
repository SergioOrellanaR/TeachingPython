''' 
TAREA:

Cree una clase Cajero con las siguientes propiedades: Ciudad, Dinero disponible, Banco.

Con el cajero se podrá "Retirar Dinero", "Depositar dinero" y "Cambiar de Ciudad" (Esto debe hacerlo con métodos dentro de la clase).

No será posible retirar dinero si el monto retirado excede a 0, debe mostrar mensaje de error correspondiente si aquello ocurre.

'''

class Cajero():

    #Constructor
    def __init__ (self, ciudad, dineroDisponible, banco):
        self.ciudad = ciudad
        self.dineroDisponible = dineroDisponible
        self.banco = banco

    def __str__(self):
        return (f"///INFORMACION CAJERO///\nCiudad: {self.ciudad} \nDinero Disponible: {self.dineroDisponible} \nBanco: {self.banco}")
    
    def retirarDinero(self, valorRetiro):
        if(valorRetiro <= self.dineroDisponible):
            self.dineroDisponible -= valorRetiro
            print('Transaccion realizada con exito')
        else:
            print('El valor de retiro debe ser menor o igual al dinero disponible')

    def depositarDinero(self, valorDeposito):
        if(valorDeposito > 0):
            self.dineroDisponible += valorDeposito
            print('Transaccion realizada con exito')
        else:
            print('El valor del deposito debe ser mayor a 0')

    def cambiarCiudad(self, nuevaCiudad):
        if(len(nuevaCiudad) > 0):
            self.ciudad = nuevaCiudad
            print('Modificacion realizada con exito')
        else:
            print('Porfavor ingrese una ciudad')
    
def ejecutarOpcion(mensaje, metodo, cajero, esNumero = True):
    print(mensaje)
    dinero = input()
    if(esNumero):
        dinero = int(dinero())
    metodo(dinero)
    print(cajero)

def main():
    cajeroActual = Cajero('Santiago', 1000000, 'BCI')

    print('Que desea realizar? Presionar 1 : Retirar Dinero ~ 2 : Depositar Dinero ~ 3 : Cambiar Ciudad')
    opcion = int(input())
    if(opcion == 1):
        ejecutarOpcion('Cuanto dinero desea retirar?', cajeroActual.retirarDinero, cajeroActual)
    elif(opcion == 2):
        ejecutarOpcion('Cuanto dinero desea depositar?', cajeroActual.depositarDinero, cajeroActual)
    elif(opcion == 3):
        ejecutarOpcion('Cual es la nueva ciudad?', cajeroActual.cambiarCiudad, cajeroActual, esNumero = False)
    else:
        print('Debe ingresar una opcion del 1 al 3')

main()