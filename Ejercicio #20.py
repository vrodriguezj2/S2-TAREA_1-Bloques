"""
Clase AnalizadorPatrones que: (1) tenga método encontrar_palabras(texto, patron) que busque 
palabras que inicien con el patrón y retorne una lista; (2) tenga método agrupar_por_longitud(texto) 
que retorne un diccionario {longitud: [palabras]}; (3) tenga método palabras_unicas() usando un conjunto.
"""

class AnalizadorPatrones:
    def __init__(self):
        self.unicas = set()

    def obtener_palabras(self, texto):
        palabras = texto.lower().split()
        for palabra in palabras:
            self.unicas.add(palabra)
        return palabras

    def encontrar_palabras(self, texto, patron):
        palabras = self.obtener_palabras(texto)
        patron = patron.lower()
        coincidencias = []

        for palabra in palabras:
            if palabra.startswith(patron):
                coincidencias.append(palabra)

        return coincidencias

    def agrupar_por_longitud(self, texto):
        grupos = {}
        palabras = self.obtener_palabras(texto)

        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in grupos:
                grupos[longitud] = []
            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self):
        return self.unicas


analizador = AnalizadorPatrones()
print(analizador.encontrar_palabras("el elefante entra al edificio", "e"))
print(analizador.agrupar_por_longitud("el gato está aquí"))
print(analizador.palabras_unicas())



"PRUEBA"
"""
# Crea una clase llamada AnalizadorMensajes para trabajar con palabras de un texto.
# Debe buscar palabras que contengan un fragmento, agruparlas por su última letra y guardar las únicas.
"""

class AnalizadorMensajes:
    def __init__(self):
        self.unicas = set()

    def obtener_palabras(self, mensaje):
        palabras = mensaje.lower().split()
        for palabra in palabras:
            self.unicas.add(palabra)
        return palabras

    def buscar_fragmento(self, mensaje, fragmento):
        coincidencias = []
        for palabra in self.obtener_palabras(mensaje):
            if fragmento.lower() in palabra:
                coincidencias.append(palabra)
        return coincidencias

    def agrupar_por_ultima_letra(self, mensaje):
        grupos = {}
        for palabra in self.obtener_palabras(mensaje):
            ultima = palabra[-1]
            if ultima not in grupos:
                grupos[ultima] = []
            grupos[ultima].append(palabra)
        return grupos

    def palabras_unicas(self):
        return self.unicas


analizador = AnalizadorMensajes()
print(analizador.buscar_fragmento("programar mejora la lógica", "gra"))
print(analizador.agrupar_por_ultima_letra("hola mundo prueba"))
print(analizador.palabras_unicas())