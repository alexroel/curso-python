from mascota import Mascota
from registrar_macota import RegistroMascotas

registro = RegistroMascotas()

def main():
    while True:
        menu = """--- Menú de Registro de Mascotas ---
    1. Agregar Mascota
    2. Listar Mascotas
    3. Editar Mascota
    4. Eliminar Mascota
    5. Salir
    Ingrese una opción: """

        opcion = input(menu)

        if opcion == '1':
            nombre = input("Nombre de la mascota: ")
            especie = input("Especie de la mascota: ")
            edad = int(input("Edad de la mascota: "))

            mascota = Mascota(nombre=nombre, especie=especie, edad=edad)
            registro.agregar_mascota(mascota)
        
        elif opcion == '2':
            registro.listar_mascotas()
        
        elif opcion == '3':
            indice = int(input("Índice de la mascota a editar: ")) - 1
            nombre = input("Nombre de la mascota: ")
            especie = input("Especie de la mascota: ")
            edad = int(input("Edad de la mascota: "))

            nueva_mascota = Mascota(nombre=nombre, especie=especie, edad=edad)
            registro.editar_mascota(indice, nueva_mascota)

        elif opcion == '4':
            indice = int(input("Índice de la mascota a eliminar: ")) - 1
            registro.eliminar_mascota(indice)
        
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
            

