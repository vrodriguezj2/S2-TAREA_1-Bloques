"""
Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False; 
(2) tenga método separar(*numeros) que retorne un diccionario 
{'pares': [...], 'impares': [...]} reutilizando es_par; 
(3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).
"""

class AnalizadorNumeros:

    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        resultado = {
            "pares" : [],
            "impares" :[]
        }

        for numero in numeros:
            if self.es_par(numero):
                resultado["pares"].append(numero)
            else:
                resultado["impares"].append(numero)

        self.pares = resultado["pares"]
        self.impares = resultado["impares"]

        return resultado

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))

analizar = AnalizadorNumeros()

print(analizar.es_par(10))
print(analizar.separar(2,3,5,80,43,22))
print(analizar.cantidad_pares_impares())


"PRUEBA"
"""
Crea una clase llamada ClasificadorMultiplos que separe números múltiplos de 3.
Debe mostrar ambos grupos y la cantidad de elementos que contiene cada uno.
"""

class ClasificadorMultiplos:
    def __init__(self):
        self.grupos = {"multiplos_de_3": [], "otros": []}

    def es_multiplo_de_3(self, numero):
        return numero % 3 == 0

    def clasificar(self, *numeros):
        for numero in numeros:
            if self.es_multiplo_de_3(numero):
                self.grupos["multiplos_de_3"].append(numero)
            else:
                self.grupos["otros"].append(numero)
        return self.grupos

    def cantidades(self):
        resultado = {}
        for grupo, numeros in self.grupos.items():
            resultado[grupo] = len(numeros)
        return resultado


clasificador = ClasificadorMultiplos()
print(clasificador.clasificar(3, 4, 6, 8, 9))
print(clasificador.cantidades())