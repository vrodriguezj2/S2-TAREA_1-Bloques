"""
Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne una lista 
alternando elementos de ambas; (2) tenga método intercalar_multiples(*listas) que reutilice 
para varias listas.
"""

class Combinador_Listas:

    def intercalar(self, lista1, lista2):
        resultado = []

        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []

        for i in range(len(listas[0])):

            for j in range(0, len(listas), 2):

                if j + 1 < len(listas):
                    parte = self.intercalar(
                        [listas[j][i]],
                        [listas[j + 1][i]]
                    )

                    resultado.extend(parte)

                else:
                    resultado.append(listas[j][i])

        return resultado


combinador = Combinador_Listas()

lista1 = [1, 2, 3]
lista2 = ["A", "B", "C"]
lista3 = [10, 20, 30]

print(combinador.intercalar(lista1, lista2))

print(combinador.intercalar_multiples(
    lista1,
    lista2,
    lista3
))


"PRACTICA"
"""
Ejercicio: OrganizadorNumeros
Crea una clase llamada OrganizadorNumeros que tenga:
1. Método combinar(lista1, lista2)
Debe recibir dos listas de números y alternar sus elementos.
"""

class OrganizadorNumeros:

    def combinar(self, lista1, lista2):
        resultado = []

        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def combinar_multiples(self, *listas):
        resultado = []

        for i in range(len(listas[0])):

            for j in range(0, len(listas), 2):

                if j + 1 < len(listas):
                    parte = self.combinar(
                        [listas[j][i]],
                        [listas[j + 1][i]]
                    )

                    resultado.extend(parte)

                else:
                    resultado.append(listas[j][i])

        return resultado


organizador = OrganizadorNumeros()

lista1 = [10, 20, 30]
lista2 = [1, 2, 3]
lista3 = [100, 200, 300]

print(organizador.combinar(lista1, lista2))

print(organizador.combinar_multiples(
    lista1,
    lista2,
    lista3
))