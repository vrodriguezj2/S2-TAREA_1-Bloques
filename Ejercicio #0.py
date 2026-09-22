"""
Enunciado. Crear una clase NumeroPrimo que:
Tenga un método es_primo(numero) que retorne True o False.
Tenga un método primos_en_rango(*args) que reciba múltiples números y 
retorne una lista con los que son primos, reutilizando es_primo().
Tenga un atributo historial (una lista) que guarde todos los números probados.
Tenga un método cantidad_verificados() que retorne cuántos números se han probado.
"""
class NumeroPrimo:
    primos_verficados=[]
    def __init__(self):
        self.historial=[]

    def es_primo(self,numero):
        self.historial.append(numero)
        primo=True
        if numero < 2:
            primo=False
        else:
            for i in range(2,numero):
                if numero % i == 0:
                    primo=False
                    break 
        return primo


    def primos_en_rango(self,*args):
        primos=[]
        
        for num in args:
            
            if self.es_primo(num)==True:
                primos.append(num)
                NumeroPrimo.primos_verficados.append(num)
                
      
        return primos        

    def cantidad_verificados(self):
        return len(self.historial)

    @staticmethod 
    def get_primos_verificados():
        return len(NumeroPrimo.primos_verficados)
       
primo1 = NumeroPrimo()

if primo1.es_primo(2):
    print("El número es primo")
    NumeroPrimo.primos_verficados.append(2)
else:
    print("El número 2, no es primo")

print(primo1.primos_en_rango(9,3))
print(primo1.historial)
print(primo1.cantidad_verificados())

primo2=NumeroPrimo()
if primo2.es_primo(5):
    print("El número es primo")
    NumeroPrimo.primos_verficados.append(5)
else:
    print("El número 5, no es primo")

print(primo2.historial)
print(NumeroPrimo.primos_verficados)
print(NumeroPrimo.get_primos_verificados())


"PRUEBA"
"""
1. Método es_par(numero Debe recibir un número y retornar: True si el número es par. 
False si el número es impar. 2. Método pares_en_lista(*args). 3. Método cantidad_verificados()
Debe retornar la cantidad de números almacenados en historial
"""

class AnalizadorPares:

    def __init__(self):
        self.historial = []

    def es_par(self, numero):
        self.historial.append(numero)

        if numero % 2 == 0:
            return True
        else:
            return False

    def pares_en_lista(self, *args):
        pares = []

        for numero in args:
            if self.es_par(numero):
                pares.append(numero)

        return pares

    def cantidad_verificados(self):
        return len(self.historial)


analizador = AnalizadorPares()

print(analizador.es_par(8))

print(analizador.pares_en_lista(
    3, 8, 11, 20, 7, 14
))

print(analizador.historial)

print(analizador.cantidad_verificados())