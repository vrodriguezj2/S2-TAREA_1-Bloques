"""
Clase AnalizadorString que: (1) tenga método solo_vocales(letra) que retorne True si es vocal; 
(2) tenga método contar_por_tipo(texto) que retorne un diccionario 
{'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
(3) tenga atributo que guarde el texto más largo analizado.
"""

class AnalizadorString:

    def __init__(self):
        self.texto_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        vocales = 0
        consonantes = 0
        digitos = 0

        for letra in texto:
            if self.solo_vocales(letra):
                vocales += 1
            elif letra.isalpha():
                consonantes += 1
            elif letra.isdigit():
                digitos += 1

        if len(texto) > len(self.texto_largo):
            self.texto_largo = texto

        return {
            "Vocales" : vocales,
            "Consonantes": consonantes,
            "Digitos": digitos
        }

analizar = AnalizadorString()

print(analizar.solo_vocales("i"))
print(analizar.contar_por_tipo("Anuel 304"))
print(analizar.contar_por_tipo("Anuel 2A"))
print(analizar.contar_por_tipo("F.C. Barcelona"))
print(analizar.texto_largo)


"PRUEBA"
"""
Crea una clase llamada AnalizadorIdentificadores que revise nombres de usuario.
Debe contar letras, números y guiones bajos, además de guardar el identificador más largo.
"""

class AnalizadorIdentificadores:
    def __init__(self):
        self.identificador_mas_largo = ""

    def analizar(self, identificador):
        conteo = {"letras": 0, "numeros": 0, "guiones_bajos": 0}

        for caracter in identificador:
            if caracter.isalpha():
                conteo["letras"] += 1
            elif caracter.isdigit():
                conteo["numeros"] += 1
            elif caracter == "_":
                conteo["guiones_bajos"] += 1

        if len(identificador) > len(self.identificador_mas_largo):
            self.identificador_mas_largo = identificador

        return conteo


analizador = AnalizadorIdentificadores()
print(analizador.analizar("user_2026"))
print(analizador.identificador_mas_largo)