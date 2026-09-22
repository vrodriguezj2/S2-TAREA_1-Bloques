"""
Clase CodificadorCesar que: (1) tenga método codificar_letra(letra, desplazamiento) 
que retorne la letra desplazada en el alfabeto (usar operador %); 
(2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; 
(3) tenga un diccionario como atributo para historial de codificaciones.
"""

class CodificadorCesar:
    def __init__(self):
        self. historial = {}

    def codificar_letra(self, letra, desplazamiento):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        posicion = alfabeto.index(letra)

        nueva_posicion = (posicion + desplazamiento) % 26

        return alfabeto[nueva_posicion]

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            codificado = self.codificar_letra(letra, desplazamiento)
            resultado += codificado

        self.historial[palabra] = resultado

        return resultado


codificador = CodificadorCesar()

print(codificador.codificar_palabra("hola",5))
print(codificador.codificar_palabra("Luz",6))
print(codificador.codificar_letra("K",3))


"PRUEBA"
"""
Crea una clase llamada TransformadorTexto que:
1. Método transformar_letra(letra) Debe recibir una letra y retornar la letra convertida a mayúscula.
2. Método transformar_palabra(palabra) Debe recorrer toda la palabra y reutilizar transformar_letra() 
para transformar cada letra.
3. Atributo historial. La clase debe tener un diccionario como atributo para guardar las palabras transformadas.
"""

class TransformadorTexto:

    def __init__(self):
        self.historial = {}

    def transformar_letra(self, letra):
        return letra.upper()

    def transformar_palabra(self, palabra):
        resultado = ""

        for letra in palabra:
            mayusculas = self.transformar_letra(letra)
            resultado += mayusculas

        self.historial[palabra] = resultado

        return resultado

tranformar = TransformadorTexto()

print(tranformar. transformar_letra("z"))
print(tranformar. transformar_letra("a"))
print(tranformar.transformar_palabra("amor"))
print(tranformar.transformar_palabra("mundo"))