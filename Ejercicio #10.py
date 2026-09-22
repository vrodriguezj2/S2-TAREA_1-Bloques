"""
Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde 
en una lista de tuplas (descripción, prioridad); (2) tenga método tareas_prioritarias()
que retorne solo las de prioridad alta; (3) tenga método eliminar_completada(descripcion) 
que borre la tarea de la lista.
"""

class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        lista = []

        for descripcion, prioridad in self.tareas:
            if prioridad == "alta":
                lista.append((descripcion, prioridad))

        return lista

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break

tareas = Tareas()

tareas.agregar_tarea("Hacer tarea de Python", "alta")
tareas.agregar_tarea("Estudiar matemáticas discretas", "media")
tareas.agregar_tarea("Hacer ejercicio", "baja")
tareas.agregar_tarea("Preparar exposición", "alta")

print(tareas.tareas)
print(tareas.tareas_prioritarias())

tareas.eliminar_completada("Estudiar matemáticas discretas")

print(tareas.tareas)



"PRUEBA"
"""
Crea una clase llamada MesaAyuda para guardar tickets con su nivel de prioridad.
Debe mostrar los tickets críticos y eliminar un ticket cuando sea resuelto.
"""

class MesaAyuda:
    def __init__(self):
        self.tickets = []

    def agregar_ticket(self, descripcion, prioridad):
        self.tickets.append((descripcion, prioridad.lower()))

    def tickets_criticos(self):
        resultado = []
        for ticket in self.tickets:
            if ticket[1] == "critica":
                resultado.append(ticket)
        return resultado

    def resolver_ticket(self, descripcion):
        for indice in range(len(self.tickets)):
            if self.tickets[indice][0] == descripcion:
                self.tickets.pop(indice)
                return True
        return False


mesa = MesaAyuda()
mesa.agregar_ticket("Sin internet", "critica")
mesa.agregar_ticket("Cambiar clave", "normal")
print(mesa.tickets_criticos())
print(mesa.resolver_ticket("Sin internet"))
print(mesa.tickets)