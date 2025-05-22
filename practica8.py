class Animal:
    def hacer_sonido(self):
        # Este método lo define cada animal según su especie
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau~"

# Esta función recibe un animal y hace que emita su sonido
def reproducir_sonido(animal):
    print(animal.hacer_sonido())

# Creamos algunas mascotas
firulais = Perro()
michi = Gato()

reproducir_sonido(firulais)  # Guau guau!
reproducir_sonido(michi)     # Miau~
