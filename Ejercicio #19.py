"""
Clase Inventario que: (1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
(2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
(3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.
"""

class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if cantidad < 0:
            return False

        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad
        return True

    def restar_stock(self, producto, cantidad):
        if cantidad < 0:
            return False
        if producto not in self.stock:
            return False
        if self.stock[producto] < cantidad:
            return False
        self.stock[producto] -= cantidad
        return True

    def productos_bajo_stock(self, minimo):
        productos = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                productos.append(producto)
        return productos


inventario = Inventario()
inventario.agregar_stock("pan", 50)
print(inventario.restar_stock("pan", 30))
print(inventario.productos_bajo_stock(15))


"PRUEBA"
"""
Crea una clase llamada GestorBiblioteca para controlar copias disponibles de libros.
Debe agregar copias, prestar libros y mostrar los títulos con pocas existencias.
"""
class GestorBiblioteca:
    def __init__(self):
        self.copias = {}

    def agregar_copias(self, libro, cantidad):
        if cantidad <= 0:
            return False

        if libro in self.copias:
            self.copias[libro] += cantidad
        else:
            self.copias[libro] = cantidad
        return True

    def prestar_libro(self, libro):
        if libro not in self.copias:
            return False
        if self.copias[libro] == 0:
            return False

        self.copias[libro] -= 1
        return True

    def libros_con_pocas_copias(self, minimo):
        resultado = {}
        for libro, cantidad in self.copias.items():
            if cantidad < minimo:
                resultado[libro] = cantidad
        return resultado


biblioteca = GestorBiblioteca()
biblioteca.agregar_copias("Python", 3)
biblioteca.agregar_copias("Estadística", 1)
print(biblioteca.prestar_libro("Python"))
print(biblioteca.libros_con_pocas_copias(2))