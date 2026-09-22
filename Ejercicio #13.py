"""
Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne una lista 
alternando elementos de ambas; (2) tenga método intercalar_multiples(*listas) que reutilice 
para varias listas.
"""

class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        longitud = max(len(lista1), len(lista2))
        for indice in range(longitud):
            if indice < len(lista1):
                resultado.append(lista1[indice])
            if indice < len(lista2):
                resultado.append(lista2[indice])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []
        resultado = list(listas[0])
        for indice in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[indice])
        return resultado


combinador = CombinadorListas()
print(combinador.intercalar([1, 2], [3, 4],))
print(combinador.intercalar_multiples([1, 2], [3, 4]))


"PRACTICA"
"""
Crea una clase llamada MezcladorRutas que combine paradas de dos rutas alternadamente.
También debe permitir combinar más de dos listas de paradas.
"""


class MezcladorRutas:
    def mezclar(self, ruta1, ruta2):
        resultado = []
        longitud = max(len(ruta1), len(ruta2))

        for indice in range(longitud):
            if indice < len(ruta1):
                resultado.append(ruta1[indice])
            if indice < len(ruta2):
                resultado.append(ruta2[indice])
        return resultado

    def mezclar_varias(self, *rutas):
        if len(rutas) == 0:
            return []

        resultado = list(rutas[0])
        for indice in range(1, len(rutas)):
            resultado = self.mezclar(resultado, rutas[indice])
        return resultado


mezclador = MezcladorRutas()
print(mezclador.mezclar(["A", "B"], ["C", "D"]))
print(mezclador.mezclar_varias(["A", "B"], ["C", "D"], ["E"]))