class Pais:
    
    #Constructor
    def __init__(self, nombre, continente, capital, cantidadHabitantes, esDesarrollado, pres = "No Tiene"):
        self.nombre = nombre
        self.continente = continente
        self.capital = capital
        self.cantidadHabitantes = cantidadHabitantes
        self.esDesarrollado = esDesarrollado
        self.presidente = pres

    def agregar1MillonHabitantes(self):
        self.cantidadHabitantes += 1000000 # ES LO MISMO QUE self.cantidadHabitantes = self.cantidadHabitantes + 1000000
        
    def asumeDictador(self, cantidadHabitantes, presidente = "No Tiene"):
        self.presidente = presidente
        self.cantidadHabitantes = cantidadHabitantes
        self.esDesarrollado = False

    def __str__(self):
        '''
        return ("Nombre: "+self.nombre+ "\n"
        "Continente: "+self.continente+ "\n"
        "Capital: "+self.capital)
        '''
        return ((f"Nombre: {self.nombre} \n")+
        (f"Continente: {self.continente} \n")+
        (f"Capital: {self.capital}"))


def main():
    chile = Pais("Chile", "Sudamerica", "Santiago", 18000000, False, "Piñera")
    argentina = Pais("Argentina","Sudamerica","Buenos Aires", 50000000, False)
    alemania = Pais("Alemania", "Europa", "Berlín", 30000000, True)
    print(chile)

main()


''' 
TAREA:

Cree una clase Cajero con las siguientes propiedades: Ciudad, Dinero disponible, Banco.

Con el cajero se podrá "Retirar Dinero", "Depositar dinero" y "Cambiar de Ciudad" (Esto debe hacerlo con métodos dentro de la clase).

No será posible retirar dinero si el monto retirado excede a 0, debe mostrar mensaje de error correspondiente si aquello ocurre.

'''