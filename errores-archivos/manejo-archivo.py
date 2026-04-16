try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no se encontró.")
    print("Creando un nuevo archivo...")
    with open("datos.txt", "w") as archivo:
        archivo.write("Hola mundo!")
else:
    print("Contenido del archivo:")
    print(contenido)
# finally:
#     archivo.close()


