"""
Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) 
que guarde en un diccionario; (2) tenga método personas_mayores(edad_minima) 
que retorne una lista de nombres cuya edad sea ≥; (3) tenga método edad_promedio() 
que retorne el promedio de edades.
"""

class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        lista = []

        for nombre, edad in self.personas.items():
            if edad <= edad_minima:
                lista.append(nombre)

        return lista

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)


gestor = GestorPersonas()

gestor.agregar_persona("Mateo", 22)
gestor.agregar_persona("Ash", 17)
gestor.agregar_persona("Anthony", 20)
gestor.agregar_persona("Pedro", 15)

print(gestor.personas)
print(gestor.personas_mayores(18))
print(gestor.edad_promedio())



"PRUEBA"
"""
Crea una clase llamada RegistroCiudades que relacione ciudades con su población.
Debe filtrar ciudades por una población mínima y calcular el promedio registrado.
"""

class RegistroCiudades:
    def __init__(self):
        self.ciudades = {}

    def agregar_ciudad(self, nombre, poblacion):
        self.ciudades[nombre] = poblacion

    def ciudades_desde(self, poblacion_minima):
        resultado = []
        for ciudad, poblacion in self.ciudades.items():
            if poblacion >= poblacion_minima:
                resultado.append(ciudad)
        return resultado

    def poblacion_promedio(self):
        if len(self.ciudades) == 0:
            return 0
        return sum(self.ciudades.values()) / len(self.ciudades)


registro = RegistroCiudades()
registro.agregar_ciudad("Ciudad A", 5000)
registro.agregar_ciudad("Ciudad B", 9000)
registro.agregar_ciudad("Ciudad C", 7000)
print(registro.ciudades_desde(6000))
print(f"Promedio: {registro.poblacion_promedio():.2f}")