#Tarea 4:

#Cree una clase Cajero con las siguientes propiedades: Ciudad, Dinero disponible, Banco.

#Con el cajero se podrá "Retirar Dinero", "Depositar dinero" y "Cambiar de Ciudad" (Esto debe hacerlo con métodos dentro de la clase).

#No será posible retirar dinero si el monto retirado excede a 0, debe mostrar mensaje de error correspondiente si aquello ocurre.

class Cajero:

    def __init__(self, ciudad, dinero, banco):
        self.ciudad = ciudad
        self.dinero = dinero
        self.banco = banco

        def retirarDinero(self, dinero):
            self.dinero -= dinero

        def depositarDinero(self, dinero):
            self.dinero += dinero

        def cambiarCiudad(self, ciudad):
            self.ciudad = ciudad

        def accionCajero(self, accion):
            if(accion == 1):
                print("¿Cuanto quieres depositar?")              
            elif(accion == 2):
                print("¿Cuanto quieres retirar?")
            else:
                print("Numero incorrecto, ingrese nuevamente.")


def solicitarNumero():
    return int(input())

def main():
    cajeroplaza = Cajero("Valparaiso", 150000, "Santander")
    print(f"Bienvenido a Banco {cajeroplaza.banco} ubicado en {cajeroplaza.ciudad}\n¿Que transaccion quieres hacer? Saldo disponible: {cajeroplaza.dinero}\n1- Depositar\n2- Retirar")
    accion = solicitarNumero()
    cajeroplaza.accionCajero(accion)

main()