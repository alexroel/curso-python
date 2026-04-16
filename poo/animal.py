class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hacer_sonido(self):
        pass

    def __str__(self) -> str:
        return f"Animal: {self.especie}, Edad: {self.edad} años"

class Perro(Animal):
    def __init__(self, nombre: str, raza: str, edad: int):
        super().__init__(especie="Perro", edad=edad)
        self.nombre = nombre
        self.raza = raza

    def hacer_sonido(self) -> str:
        return "¡Guau!"

    def __str__(self)-> str:
        return f"Perro: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años"


class Gato(Animal):
    def __init__(self, nombre: str, raza: str, edad: int):
        super().__init__(especie="Gato", edad=edad)
        self.nombre = nombre
        self.raza = raza

    def hacer_sonido(self) -> str:
        return "¡Miau!"

    def __str__(self) -> str:
        return f"Gato: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años"

