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
class Campeon:
    def __init__(self, nombre, rol, genero):
        self.nombre = nombre
        self.rol = rol
        self.genero = genero

def main():
    equipo1 = [
        Campeon("Jax", "TOP", "Hombre"),
        Campeon("Sejuani", "JG", "Mujer"),
        Campeon("Ahri", "MID", "Mujer"),
        Campeon("Vayne", "ADC", "Mujer"),
        Campeon("Bardo", "SUPP", "Hombre")
    ]
    equipo2 = [
        Campeon("Yone", "TOP", "Hombre"),
        Campeon("Rengar", "JG", "Hombre"),
        Campeon("Annie", "MID", "Mujer"),
        Campeon("Yasuo", "ADC", "Hombre"),
        Campeon("Malphite", "SUPP", "Hombre")
    ]  

main()