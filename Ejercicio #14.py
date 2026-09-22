"""
Clase RegistroNotas que: (1) tenga método registrar(estudiante, nota) que guarde en un diccionario;
(2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; 
(3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.
"""

class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        estudiantes = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                estudiantes.append(estudiante)

        return estudiantes

    def mejor_estudiante(self):
        mayor = 0
        mejor = ""

        for estudiante, nota in self.notas.items():
            if nota > mayor:
                mayor = nota
                mejor = estudiante 

        return mayor, mejor


registro = RegistroNotas()

registro.registrar("Juan", 8.5)
registro.registrar("María", 9.2)
registro.registrar("Pedro", 6.8)
registro.registrar("Ana", 7.5)

print(registro.estudiantes_aprobados(7))
print(registro.mejor_estudiante())


"PRUEBA"
"""
Ejercicio: RegistroVentas
Crea una clase llamada RegistroVentas que:
1. Método registrar(producto, cantidad)
Debe guardar en un diccionario el producto y la cantidad vendida.
2. Método productos_mas_vendidos(cantidad_minima) Debe retornar una lista con los productos
cuya cantidad vendida sea mayor o igual a la cantidad mínima.
3. Método producto_mas_vendido() Debe retornar el nombre del producto y la cantidad del producto 
que tenga más ventas.
"""

class RegistroVentas:
    def __init__(self):
        self.ventas = {}

    def registrar(self, producto, cantidad):
        self.ventas[producto] = cantidad 

    def productos_mas_vendidos(self, cantidad_minima):
        productos = []

        for producto, cantidad in self.ventas.items():

            if cantidad >= cantidad_minima:
                productos.append(producto)
        return productos
    
    def producto_mas_vendido(self):
        mayor_v = 0
        nombre = ""

        for producto, cantidad in self.ventas.items():
            if cantidad > mayor_v :
                mayor_v = cantidad
                nombre = producto

        return mayor_v, nombre  

registro = RegistroVentas()

registro.registrar("Mouse", 15)
registro.registrar("Teclado", 9)
registro.registrar("Plasma", 10)
registro.registrar("CPU", 5)

print(registro.productos_mas_vendidos(8))
print(registro.producto_mas_vendido())      