"""
Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, 
False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, 
las valide, agregue solo las válidas a una lista interna, y retorne esa lista; 
(3) tenga método promedio() que retorne el promedio de notas almacenadas.
"""

class Calificador:
    def __init__(self):
        self.notas=[]
        

    def validar_nota(self,nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False
        
    
    def cargar_notas(self, *args):
        
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        return sum(self.notas)/len(self.notas)


cal = Calificador()
print(cal.cargar_notas(-50,60,40,200))
print(cal.promedio())


"PRUEBA"
"""
Crea una clase llamada ControlBateria que guarde únicamente niveles entre 0 y 100.
Debe permitir cargar varios niveles, mostrar los valores aceptados y calcular su promedio.
"""

class ControlBateria:
    def __init__(self):
        self.niveles = []

    def nivel_valido(self, nivel):
        return 0 <= nivel <= 100

    def cargar_niveles(self, *niveles):
        for nivel in niveles:
            if self.nivel_valido(nivel):
                self.niveles.append(nivel)
        return self.niveles

    def promedio(self):
        if len(self.niveles) == 0:
            return 0
        return sum(self.niveles) / len(self.niveles)


control = ControlBateria()
print(control.cargar_niveles(80, 120, 45, -10, 60))
print(f"Promedio: {control.promedio():.2f}")