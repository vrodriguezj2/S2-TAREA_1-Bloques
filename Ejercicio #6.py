"""
Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista; 
(2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
(3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.
"""

class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples_temp(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)


gestor = GestorTemperatura()

gestor.registrar_temperatura(20)
gestor.registrar_temperatura(79)
gestor.registrar_temperatura(35)

gestor.registrar_multiples_temp(10, 50, 40)

print(gestor.temperaturas)
print(gestor.minima())
print(gestor.maxima())
print(gestor.promedio())


"PRUEBA"
"""
Crea una clase llamada ConsumoElectrico que registre consumos diarios en kWh.
Debe obtener el consumo mínimo, máximo y promedio de todos los registros.
"""

class ConsumoElectrico:
    def __init__(self):
        self.consumos = []

    def registrar(self, consumo):
        if consumo >= 0:
            self.consumos.append(consumo)

    def registrar_varios(self, *consumos):
        for consumo in consumos:
            self.registrar(consumo)

    def minimo(self):
        if len(self.consumos) == 0:
            return None
        return min(self.consumos)

    def maximo(self):
        if len(self.consumos) == 0:
            return None
        return max(self.consumos)

    def promedio(self):
        if len(self.consumos) == 0:
            return 0
        return sum(self.consumos) / len(self.consumos)


registro = ConsumoElectrico()
registro.registrar_varios(8, 10, 7, 11)
print(f"Mínimo: {registro.minimo()}")
print(f"Máximo: {registro.maximo()}")
print(f"Promedio: {registro.promedio():.2f}")