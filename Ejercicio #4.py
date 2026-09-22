"""
Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que retorne 
la lista invertida sin usar reversed() (usa manual con bucles); 
(2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir 
varias listas y retorne un diccionario {lista_original: lista_invertida}.
"""

class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) -1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        multiples = {}

        for lista in listas:
            multiples[str(lista)] = self.invertir_lista(lista)

        return multiples

invertor = InversorSecuencia()
lista1 = [40, 60, 21]
lista2 = ["PHYTON", "JAVASCRIPT", "C++"]
lista3 = [1, 2, 3]

print(invertor.invertir_lista(lista1))
print(invertor.invertir_multiples(lista1, lista2, lista3))  


"PRUEBA"
"""
Crea una clase llamada RotadorListas que mueva el último elemento al inicio.
Debe poder rotar una lista y procesar varias listas recibidas como argumentos.
"""

class RotadorListas:
    def rotar(self, lista):
        if len(lista) == 0:
            return []

        resultado = [lista[-1]]
        for indice in range(len(lista) - 1):
            resultado.append(lista[indice])
        return resultado

    def rotar_varias(self, *listas):
        resultados = {}
        for lista in listas:
            resultados[tuple(lista)] = self.rotar(lista)
        return resultados


rotador = RotadorListas()
print(rotador.rotar([1, 2, 3]))
print(rotador.rotar_varias([1, 2, 3], ["a", "b", "c"]))