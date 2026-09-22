"""
Clase AgrupadorEdades que: (1) tenga método clasificar_edad(edad) que retorne 
la categoría ("niño", "adolescente", "adulto", "mayor"); (2) tenga método 
agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; 
(3) tenga método edad_promedio_categoria(categoria).
"""

class AgrupadorEdades:

    def __init__(self):
        self.edades = {}

    def  clasificar_edad(self, edad):
        if edad <= 12:
            return "Niño"
        elif edad <= 17:
            return "Adolescente" 
        elif edad <= 64:
            return "Adulto"
        else:
            return "Adulto mayor"

    def agrupar_por_categoria(self, *edades):
        resultado = {}

        for edad in edades:
            categoria = self.clasificar_edad(edad)

            if categoria not in resultado:
                resultado[categoria] = []

            resultado[categoria].append(edad)

        self.edades = resultado
        return resultado

    def edad_promedio_categoria(self, categoria):

        edades = self.edades[categoria]

        promedio = sum(edades) / len(edades)
        return promedio
        

agrupador = AgrupadorEdades()

print(agrupador.agrupar_por_categoria(
    5, 8, 13, 16, 20, 30, 40, 70, 80
))

print(agrupador.edad_promedio_categoria("Niño"))
print(agrupador.edad_promedio_categoria("Adulto"))


"PRUEBA"
"""
Crea una clase llamada AgrupadorNotas que: 1. clasificar_nota(nota) Reciba una nota y 
retorne una categoría: 0 a 5.9 → "Reprobado "6 a 7.9 → "Regular" 8 a 8.9 → "Bueno" 
9 a 10 → "Excelente" 2. agrupar_por_categoria(*notas) Debe recibir varias notas y retornar 
un diccionario 3.promedio_categoria(categoria) Debe recibir una categoría y calcular 
el promedio de las notas que están dentro de ella.
"""

class AgrupadorNotas:

    def __init__(self):
        self.notas = {}

    def clasificar_nota(self, nota):
        if nota <= 5.9:
            return "Reprobado"
        elif nota <= 7.9:
            return "Regular"
        elif nota <= 8.9:
            return "Bueno"
        else:
            return "Exelente"

    def agrupar_por_categoria(self, *notas):
        resultado = {}

        for nota in notas:
            clasificacion = self.clasificar_nota(nota)

            if clasificacion not in resultado:
                resultado[clasificacion] = []

            resultado[clasificacion].append(nota)

        self.notas = resultado
        return resultado

    def promedio_categoria(self, clasificacion):
        respuesta = self.notas[clasificacion]

        promedio = sum(respuesta) / len(respuesta)

        return promedio


agrupa = AgrupadorNotas()

print(agrupa.agrupar_por_categoria(
    5, 4.5, 6, 7, 8, 8.5, 9, 10
))
print(agrupa.promedio_categoria("Reprobado"))
print(agrupa.promedio_categoria("Regular"))
print(agrupa.promedio_categoria("Bueno"))
print(agrupa.promedio_categoria("Excelente"))