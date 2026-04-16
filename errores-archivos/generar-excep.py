class ColorNoValido(Exception):
    def __init__(self, color):
        super().__init__(f"El color {color} no se encuentra en la lista.")


def colores(color):
    lista_colores = ["azul", "verde", "rojo"]

    if color not in lista_colores:
        raise ColorNoValido(color=color)
    

while True:
    print("Buscar un color en la lista de colores")
    color = input("Ingrese un color: ")

    try:
        colores(color)
    except ColorNoValido as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"El color {color} se encuentra en la lista.")

    # Salir
    salir = input("¿Desea salir? (s/n): ")
    if salir.lower() == "s":
        break