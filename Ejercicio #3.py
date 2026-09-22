"""
Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) 
que guarde en un diccionario {nombre: precio}; 
(2) tenga método total_carrito() que retorne la suma de todos los precios; 
(3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango.
"""


class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulos(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        lista = []

        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                lista.append(nombre)

        return lista


carrito = CarroCompras()

carrito.agregar_articulos("Mouse", 30)
carrito.agregar_articulos("Monitor", 120)
carrito.agregar_articulos("Parlantes", 45)

print(carrito.articulos)
print(carrito.total_carrito())
print(carrito.articulos_por_rango(30, 90))    

"PRUEBA"

"""
Crea una clase llamada TaquillaCine para registrar el valor vendido por película.
#Debe calcular la venta total y mostrar las películas cuyas ventas estén en un rango.
"""

class TaquillaCine:
    def __init__(self):
        self.ventas = {}

    def registrar_venta(self, pelicula, valor):
        self.ventas[pelicula] = valor

    def venta_total(self):
        total = 0
        for valor in self.ventas.values():
            total += valor
        return total

    def peliculas_por_rango(self, minimo, maximo):
        resultado = {}
        for pelicula, valor in self.ventas.items():
            if minimo <= valor <= maximo:
                resultado[pelicula] = valor
        return resultado


taquilla = TaquillaCine()
taquilla.registrar_venta("Aventura", 120)
taquilla.registrar_venta("Comedia", 80)
taquilla.registrar_venta("Drama", 65)
print(f"Venta total: {taquilla.venta_total():.2f}")
print(taquilla.peliculas_por_rango(70, 100))