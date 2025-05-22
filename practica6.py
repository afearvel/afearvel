from abc import ABC, abstractmethod

class FormaGeometrica(ABC):  # Clase base abstracta
    @abstractmethod
    def calcular_area(self):
        pass  # Método que debe implementarse en las subclases

class RectanguloCuadrado(FormaGeometrica):
    def __init__(self, medida):
        self.lado = medida

    def calcular_area(self):
        return self.lado * self.lado

class Rueda(FormaGeometrica):
    def __init__(self, tamano):
        self.radio = tamano

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

# Ejecución del programa
figura1 = RectanguloCuadrado(5)
figura2 = Rueda(3)

print(f"El área del rectángulo cuadrado es: {figura1.calcular_area()}")  # 25
print(f"El área de la rueda es: {figura2.calcular_area()}")  # 28.2744
