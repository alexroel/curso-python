from animal import Animal

class Mascota(Animal):
    def __init__(self, nombre: str, especie: str, edad: int):
        super().__init__(especie=especie, edad=edad)
        self.nombre = nombre

    def __str__(self):
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Edad: {self.edad} años"
    
