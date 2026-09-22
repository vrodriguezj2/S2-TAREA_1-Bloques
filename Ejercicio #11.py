"""
Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) que guarde 
en un diccionario contando repeticiones; (2) tenga método elemento_mas_frecuente() 
que retorne el elemento con mayor frecuencia; (3) tenga método frecuencia_elemento(elemento)
que retorne cuántas veces aparece.
"""

class ContadorFrecuencia:

    def __init__(self):
        self.repeticiones = {} 

    def agregar_elemento(self, elemento):
        if elemento in self.repeticiones:
            self.repeticiones[elemento] += 1
        else:
            self.repeticiones[elemento] = 1

    def elemento_mas_frecuente(self):
        mayor = 0
        elemento_mayor = ""

        for elemento, frecuencia in self.repeticiones.items():
            if frecuencia > mayor:
                mayor = frecuencia
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.repeticiones:
            return self.repeticiones[elemento]
        else:
            return 0 


contador = ContadorFrecuencia()

contador.agregar_elemento("Python")
contador.agregar_elemento("Java")
contador.agregar_elemento("Python")
contador.agregar_elemento("C++")
contador.agregar_elemento("Python")
contador.agregar_elemento("Java")

print(contador.repeticiones)
print(contador.elemento_mas_frecuente())
print(contador.frecuencia_elemento("Python")) 



"PRUEBA"
"""
Crea una clase llamada RegistroBusquedas para contar términos buscados.
Debe indicar el término más repetido y la frecuencia de cualquier término solicitado.
"""

class RegistroBusquedas:
    def __init__(self):
        self.frecuencias = {}

    def agregar_busqueda(self, termino):
        if termino in self.frecuencias:
            self.frecuencias[termino] += 1
        else:
            self.frecuencias[termino] = 1

    def termino_mas_buscado(self):
        if len(self.frecuencias) == 0:
            return None

        termino_mayor = None
        frecuencia_mayor = -1
        for termino, frecuencia in self.frecuencias.items():
            if frecuencia > frecuencia_mayor:
                termino_mayor = termino
                frecuencia_mayor = frecuencia
        return termino_mayor

    def frecuencia_de(self, termino):
        if termino in self.frecuencias:
            return self.frecuencias[termino]
        return 0


registro = RegistroBusquedas()
registro.agregar_busqueda("Python")
registro.agregar_busqueda("Excel")
registro.agregar_busqueda("Python")
print(registro.termino_mas_buscado())
print(registro.frecuencia_de("Python"))