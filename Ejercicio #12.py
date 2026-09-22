"""
Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una tupla 
con números en ese rango; (2) tenga método elementos_en_multiples_rangos(*rangos) 
que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados 
usando un conjunto.
"""

class SelectorRango:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin+1))

    def elementos_en_multiples_rangos(self, *rangos):
        resultado = set()
        for rango in rangos:
            inicio, fin = rango

            elementos = self.crear_rango(inicio, fin)

            for numero in elementos:
                resultado.add(numero)

        return list(resultado)


selector = SelectorRango()

print(selector. crear_rango(1, 10))

print(selector. elementos_en_multiples_rangos(
    (1, 5),
    (4, 8),
    (7, 10)
))




"Practica"
"""
Crea una clase llamada SelectorPares que:

Tenga un método crear_pares(inicio, fin) que retorne una tupla con todos los números pares dentro de ese rango.
Tenga un método pares_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio, fin) y 
retorne una lista con todos los números pares de esos rangos, sin duplicados, 
utilizando un conjunto (set).
"""

class SelectorRangoPares:

    def rango_pares(self, inicio, fin):
        if inicio % 2 == 0:
            par = inicio
        else:
            par = inicio + 1

        return tuple(range(par, fin + 1, 2))

    def multiples_rangos_pares(self, *rangos):
        conjunto = set()

        for rango in rangos:
            inicio, fin = rango 

            numeros = self.rango_pares(inicio,fin)

            for numero in numeros:
                conjunto.add(numero)

        return list(conjunto)   


selector = SelectorRangoPares()

print(selector.rango_pares(1, 10))

print(selector.multiples_rangos_pares(
    (1, 5),
    (4, 8),
    (7, 10)
))