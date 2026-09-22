"""
Clase AnalizadorTexto que: (1) tenga método agregar_palabra(palabra) que agregue la palabra 
a un conjunto (para evitar duplicados) y a una lista (para el orden); 
(2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; 
(3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios.
"""


class AnalizadorTexto:

    def __init__(self):
        self.conjunto = set()
        self.lista = []

    def agregar_palabra(self,palabra):
        self.conjunto.add(palabra)

        if palabra not in self.lista:
            self.lista.append(palabra)

    def contar_palabras(self):
        return len(self.conjunto)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


    
analizador = AnalizadorTexto()

analizador.agregar_palabra("Mateo")
analizador.agregar_palabra("Hola")
analizador.agregar_palabra("Mundo")

analizador.agregar_multiples("Mateo", "Hi", "Contar", "Phyton")

print(analizador.lista)
print(analizador.conjunto)
print(analizador.contar_palabras())


"PRUEBA"

class RegistroCodigos:
    def __init__(self):
        self.codigos_unicos = set()
        self.orden = []

    def agregar_codigo(self, codigo):
        if codigo not in self.codigos_unicos:
            self.codigos_unicos.add(codigo)
            self.orden.append(codigo)

    def agregar_varios(self, *codigos):
        for codigo in codigos:
            self.agregar_codigo(codigo)
        return self.orden

    def cantidad(self):
        return len(self.codigos_unicos)


registro = RegistroCodigos()
print(registro.agregar_varios("A10", "B20", "A10", "C30"))
print(registro.cantidad())