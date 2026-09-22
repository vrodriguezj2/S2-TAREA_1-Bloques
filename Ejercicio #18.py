"""
Clase CalculadorDistancia que: (1) tenga método distancia_euclidiana(p1, p2) que reciba dos 
tuplas (x,y) y calcule la distancia; (2) tenga método punto_mas_cercano(referencia, *puntos)
que retorne el punto más cercano a referencia; (3) tenga un atributo lista para guardar todas 
las distancias calculadas.
"""

class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        distancia = (dx ** 2 + dy ** 2) **0.5
        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        menor = float("inf")
        punto_cercano = None

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < menor:
                menor = distancia
                punto_cercano = punto

        return punto_cercano


calculador = CalculadorDistancia()

print(calculador.distancia_euclidiana((0, 0), (3, 4)))

print(calculador.punto_mas_cercano(
    (0, 0),
    (3, 4),
    (1, 1),
    (10, 2)
))

print(calculador.distancias)



"PRUEBA"
"""
1. Método clasificar_temperatura(temperatura) Debe recibir una temperatura y devolver:
Menor o igual a 10 → "Fría", Mayor a 10 y menor o igual a 20 → "Templada", Mayor a 20 y 
menor o igual a 30 → "Cálida", Mayor a 30 → "Calurosa" 2. Método agrupar_temperaturas(*temperaturas)
Debe recibir varias temperaturas usando *temperaturas. Método promedio_categoria(categoria)
"""

class AnalizadorTemperaturas:

    def __init__(self):
        self.temperaturas = {}

    def clasificar_temperatura(self, temperatura):
        if temperatura >= 10:
            return "Fria"
        elif temperatura >= 20:
            return "Templada"
        elif temperatura >= 30:
            return "Calida"
        else:
            return "Calurosa"

    def agrupar_temperaturas(self, *temperaturas):
        resultado = {}
        for temperatura in temperaturas:
            categoria = self.clasificar_temperatura(temperatura)

            if categoria not in resultado:
                resultado[categoria] = []

            resultado[categoria].append(temperatura)

        self.temperaturas = resultado
        return resultado

    def promedio_categoria(self, categoria):
        resultado = self.temperaturas[categoria]

        promedio = sum(resultado) / len(resultado)

        return promedio


analizador = AnalizadorTemperaturas()

print(analizador.clasificar_temperatura(8))

print(analizador.agrupar_temperaturas(
    8, 10, 15, 18, 25, 28, 35, 40
))

print(analizador.promedio_categoria("Cálida"))