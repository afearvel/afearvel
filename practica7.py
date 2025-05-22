class Auto:
    def __init__(self, fabricante, version):
        self.__fabricante = fabricante  # Propiedad encapsulada
        self.__version = version        # Propiedad encapsulada

    # Accesores públicos
    def obtener_fabricante(self):
        return self.__fabricante

    def obtener_version(self):
        return self.__version

    def actualizar_version(self, nueva_version):
        self.__version = nueva_version

# Ejemplo de uso
vehiculo_personal = Auto("Honda", "Civic")
print(vehiculo_personal.obtener_fabricante())  # Acceso seguro
vehiculo_personal.actualizar_version("Accord")  # Cambio seguro
print(vehiculo_personal.obtener_version())

class Transporte:
    def __init__(self, fabricante):
        self.fabricante = fabricante

    def info(self):
        return f"Transporte fabricado por: {self.fabricante}"

class AutoModerno(Transporte):  # Herencia directa
    def __init__(self, fabricante, modelo):
        super().__init__(fabricante)
        self.modelo = modelo

    def info(self):
        return f"Auto moderno: {self.fabricante} {self.modelo}"

# Demostración
vehiculo_personal = AutoModerno("Honda", "Civic")
print(vehiculo_personal.info())  # Método sobrescrito
