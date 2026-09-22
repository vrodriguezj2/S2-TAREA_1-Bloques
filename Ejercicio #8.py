"""
Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie 
un equipo como una lista vacía en un diccionario; 
(2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo; 
(3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.
"""

class Equipos:

    def __init__ (self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = ""
        cantidad_mayor = 0

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > cantidad_mayor:
                cantidad_mayor = len(jugadores)
                mayor = equipo
            

        return mayor


equipo = Equipos()

equipo.crear_equipo("Barcelona")
equipo.crear_equipo("Chelsea")
equipo.crear_equipo("Manchester City")

equipo.agregar_jugador("Barcelona", "Mateo")
equipo.agregar_jugador("Barcelona", "Juan")
equipo.agregar_jugador("Barcelona", "Carlos")

equipo.agregar_jugador("Chelsea", "Pedro")
equipo.agregar_jugador("Chelsea", "Luis")

equipo.agregar_jugador("Manchester City", "Andrés")
equipo.agregar_jugador("Manchester City", "Diego")
equipo.agregar_jugador("Manchester City", "José")
equipo.agregar_jugador("Manchester City", "Miguel")

print(equipo.equipos)
print(equipo.equipo_mayor_integrantes())


"PRUEBA"
"""
Crea una clase llamada ListasReproduccion para organizar canciones por género.
Debe crear géneros, agregar canciones y determinar cuál tiene más canciones.
"""

class ListasReproduccion:
    def __init__(self):
        self.generos = {}

    def crear_genero(self, genero):
        if genero not in self.generos:
            self.generos[genero] = []

    def agregar_cancion(self, genero, cancion):
        if genero not in self.generos:
            return False
        self.generos[genero].append(cancion)
        return True

    def genero_con_mas_canciones(self):
        if len(self.generos) == 0:
            return None

        genero_mayor = None
        cantidad_mayor = -1
        for genero, canciones in self.generos.items():
            if len(canciones) > cantidad_mayor:
                genero_mayor = genero
                cantidad_mayor = len(canciones)
        return genero_mayor


listas = ListasReproduccion()
listas.crear_genero("Rock")
listas.crear_genero("Pop")
listas.agregar_cancion("Rock", "Canción 1")
listas.agregar_cancion("Rock", "Canción 2")
listas.agregar_cancion("Pop", "Canción 3")
print(listas.genero_con_mas_canciones())