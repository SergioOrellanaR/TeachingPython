'''
Tarea 5:

Tarea: Cree la clase campeón con las propiedades Nombre, Rol y Género.

Cree 2 equipos, cada uno con 5 campeones respectivamente.

Equipo 1:
Jax
Sejuani
Ahri
Vayne
Bardo

Equipo 2:
Yone
Rengar
Annie
Yasuo
Malphite

El usuario debera ingresar un rol y el sistema mostrará los campeones en dicho rol. (Por ej, si ingresa jg, mostrará en pantalla 'Equipo 1: Sejuani, Equipo 2: Rengar')
'''

class Campeon():
    equipoUno = {}
    equipoDos = {}

    def __init__(self, nombre, rol, genero):
        self.nombre = nombre
        self.rol = rol
        self.genero = genero

    def agregarCampeonEquipoUno(self, Campeon):
        equipoUno[self.rol] = self.nombre    

    def agregarCampeonEquipoDos(self, Campeon):
        equipoDos[self.rol] = self.nombre        
        
def main():
    #Equipo 1
    campeon = Campeon('Jax', 'Top', 'Hombre')
    campeon.agregarCampeonEquipoUno(campeon)
    campeon = Campeon('Sejuani', 'Jg', 'Mujer')
    campeon.agregarCampeonEquipoUno(campeon)
    campeon = Campeon('Ahri', 'Mid', 'Mujer')
    campeon.agregarCampeonEquipoUno(campeon)
    campeon = Campeon('Vayne', 'ADC', 'Mujer')
    campeon.agregarCampeonEquipoUno(campeon)
    campeon = Campeon('Bardo', 'Supp', 'Hombre')
    equipoUno = campeon.agregarCampeonEquipoUno(campeon)

    #Equipo 2
    campeon = Campeon('Yone', 'Top', 'Hombre')
    campeon.agregarCampeonEquipoDos(campeon)
    campeon = Campeon('Rengar', 'Jg', 'Hombre')
    campeon.agregarCampeonEquipoDos(campeon)
    campeon = Campeon('Annie', 'Mid', 'Mujer')
    campeon.agregarCampeonEquipoDos(campeon)
    campeon = Campeon('Yasuo', 'ADC', 'Hombre')
    campeon.agregarCampeonEquipoDos(campeon)
    campeon = Campeon('Malphite', 'Supp', 'Hombre')
    equipoDos = campeon.agregarCampeonEquipoDos(campeon)

    print('Ingrese un rol')
    rol = input()

main()