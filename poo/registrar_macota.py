from mascota import Mascota

class RegistroMascotas:
    def __init__(self):
        self.mascotas = []
    
    def agregar_mascota(self, mascota: Mascota):
        self.mascotas.append(mascota)
    
    def listar_mascotas(self):
        if self.mascotas:
            for i, mascota in enumerate(self.mascotas, start=1):
                print(f"{i}. {mascota}")
        else:
            print("No hay mascotas registradas.")

    def editar_mascota(self, indice: int, nueva_mascota: Mascota):
        if 0 <= indice < len(self.mascotas): # indice >= 0 y indice < len(self.mascotas)
            self.mascotas[indice] = nueva_mascota
        else:
            print("Índice fuera de rango.")

    def eliminar_mascota(self, indice: int):
        if 0 <= indice < len(self.mascotas):
            del self.mascotas[indice]
            print("Mascota eliminada.")
        else:
            print("Índice fuera de rango.")