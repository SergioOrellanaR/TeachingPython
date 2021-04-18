#Tarea 4:

#Cree una clase Cajero con las siguientes propiedades: Ciudad, Dinero disponible, Banco.

#Con el cajero se podrá "Retirar Dinero", "Depositar dinero" y "Cambiar de Ciudad" (Esto debe hacerlo con métodos dentro de la clase).

#No será posible retirar dinero si el monto retirado excede a 0, debe mostrar mensaje de error correspondiente si aquello ocurre.

class Cajero:
    #Esto debiese ir en un ENUM
    accionDeposito = 1
    accionRetiro = 2
    accionCiudad = 3


    def __init__(self, ciudad, dinero, banco):
        self.ciudad = ciudad
        self.dinero = dinero
        self.banco = banco

    def retirarDinero(self, dinero):
        if(dinero > self.dinero):
            self.error()
            self.accionCajero(self.accionRetiro)
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
        if(accion == self.accionDeposito):
            print("¿Cuanto quieres depositar?")    
            trans = solicitarNumero()
            self.depositarDinero(trans)         
        elif(accion == self.accionRetiro):
            print("¿Cuanto quieres retirar?")
            trans = solicitarNumero()
            self.retirarDinero(trans)
        elif(accion == self.accionCiudad):
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
        valorRespuesta = respuesta == "si"

        if(valorRespuesta):
            print(self.realizarOperacion())
            self.solicitarAccion()

    def error(self):
        return print("Valor incorrecto, ingrese nuevamente.")

def solicitarNumero():
    return int(input())

def main():
    cajeroPlaza = Cajero("Valparaiso", 150000, "Santander")
    print(f"Bienvenido a Banco {cajeroPlaza.banco} ubicado en {cajeroPlaza.ciudad}\n"+cajeroPlaza.realizarOperacion())
    cajeroPlaza.solicitarAccion()

main()