import numpy as np

class Vector:
    def __init__(self, datos):
        self.elementos = np.array(datos)
    
    def agregar(self, valor):
        self.elementos = np.append(self.elementos, valor)
        print(f"Vector actualizado: {self.elementos}")
    
    def quitar(self, pos):
        if 0 <= pos < len(self.elementos):
            self.elementos = np.delete(self.elementos, pos)
            print(f"Vector actualizado: {self.elementos}")
        else:
            print("Posición inválida.")
    
    def actualizar(self, pos, nuevo_valor):
        self.elementos[pos] = nuevo_valor
        print(f"Vector actualizado: {self.elementos}")

class Coleccion:
    def __init__(self):
        self.datos = ['uno', 'dos', 'tres']
    
    def agregar_dato(self, valor):
        self.datos.append(valor)
        print(f"Lista actualizada: {self.datos}")
    
    def eliminar_dato(self, pos):
        if 0 <= pos < len(self.datos):
            eliminado = self.datos.pop(pos)
            print(f"Elemento '{eliminado}' eliminado. Lista actualizada: {self.datos}")
        else:
            print("Posición inválida.")
    
    def cambiar_dato(self, pos, nuevo_valor):
        self.datos[pos] = nuevo_valor
        print(f"Lista actualizada: {self.datos}")

# Uso de las clases
vector = Vector([5, 15, 25])
coleccion = Coleccion()

valor = input("Introduce un elemento para agregar: ")
coleccion.agregar_dato(valor)
vector.agregar(valor)

pos = int(input("Indica la posición que deseas eliminar: "))
coleccion.eliminar_dato(pos)
vector.quitar(pos)

nuevo = input("Introduce un nuevo valor para modificar: ")
pos = int(input("Indica la posición que deseas modificar: "))
coleccion.cambiar_dato(pos, nuevo)
vector.actualizar(pos, nuevo)
