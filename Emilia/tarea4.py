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
        if(dinero > self.dinero):
            error()
            self.accionCajero(2)
        else:
            self.dinero -= dinero
            self.succesfull()
            self.volverAOperar()

    def succesfull(self):
        return print(f"Transaccion exitosa, nuevo saldo disponible: {self.dinero}")

    def depositarDinero(self, dinero):
        self.dinero += dinero
        self.succesfull()
        self.volverAOperar()

    def cambiarCiudad(self, ciudad):
        print(f"Cambiaste la ciudad de {self.ciudad} a {ciudad}")
        self.ciudad = ciudad
        self.volverAOperar()

    def solicitarAccion(self):
        accion = solicitarNumero()
        self.accionCajero(accion)

    def accionCajero(self, accion):
        if(accion == 1):
            print("¿Cuanto quieres depositar?")    
            trans = solicitarNumero()
            self.depositarDinero(trans)         
        elif(accion == 2):
            print("¿Cuanto quieres retirar?")
            trans = solicitarNumero()
            self.retirarDinero(trans)
        elif(accion == 3):
            print("¿A que ciudad quieres cambiar?")
            ciudad = input()
            self.cambiarCiudad(ciudad)
        else:
            error()
            accion = solicitarNumero()
            self.accionCajero(accion)
            
    def realizarOperacion(self):
        return (f"¿Que transaccion quieres hacer? Saldo disponible: {self.dinero}\n1- Depositar\n2- Retirar\n3- Cambiar ciudad")

    def volverAOperar(self):
        print("¿Deseas realizar otra operacion? si/no")
        respuesta = input()
        if(respuesta == "si"):
            print(self.realizarOperacion())
            self.solicitarAccion()

def error():
    return print("Valor incorrecto, ingrese nuevamente.")

def solicitarNumero():
    return int(input())

def main():
    cajeroplaza = Cajero("Valparaiso", 150000, "Santander")
    print(f"Bienvenido a Banco {cajeroplaza.banco} ubicado en {cajeroplaza.ciudad}\n"+cajeroplaza.realizarOperacion())
    cajeroplaza.solicitarAccion()

main()