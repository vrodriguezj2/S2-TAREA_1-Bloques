"""
Clase DivisorFinder que: (1) tenga método encontrar_divisores(numero) que retorne una tupla 
con todos los divisores; (2) tenga método es_perfecto(numero) que retorne True si la suma de sus 
divisores (excepto él mismo) es igual a él; (3) tenga método 
encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.
"""

class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        
        return tuple(divisores)

    def es_perfecto(self, numero):
        suma = 0
        divisores = self.encontrar_divisores(numero)

        for divisor in divisores:
            if divisor != numero:
                suma += divisor

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        diccionario = {}

        for numero in numeros:
            divisores = self.encontrar_divisores(numero)

            diccionario[numero] = divisores
        return diccionario


divisor = DivisorFinder()

print(divisor.encontrar_divisores(12))
print(divisor.encontrar_multiples_divisores(6, 10, 12))


"PRACTICA"
"""
Ejercicio: AnalizadorNumeros
1. Crea una clase llamada AnalizadorNumeros que: Tenga un método encontrar_multiplos(numero) 
que reciba un número y retorne una tupla con todos los múltiplos de ese número entre 1 y 50.
2. Tenga un método suma_multiplos(numero) que retorne True si la suma de los múltiplos
encontrados es mayor que 100, y False en caso contrario.
3. Tenga un método encontrar_multiples_numeros(*numeros) que retorne un diccionario.
"""

class AnalizadorNumeros:

    def encontrar_multiplos(self, numero):
        multiplos = []
        for i in range(1, 51):
            if i % numero == 0:
                multiplos.append(i)

        return tuple(multiplos)

    def suma_multiplos(self, numero):
        suma = 0 
        multiplos = self.encontrar_multiplos(numero)

        for multiplo in multiplos:
            suma += multiplo

        return suma > 100

    def encontrar_multiples_numeros(self, *numeros):
        resultado = {}

        for numero in numeros:
            multiplos = self.encontrar_multiplos(numero)
            resultado[numero] = multiplos

        return resultado

analizador = AnalizadorNumeros()

print(analizador.encontrar_multiplos(5))
print(analizador.encontrar_multiplos_numeros(5,8,2))