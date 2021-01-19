from io import open
from os import path

def escribir_archivo():
    archivo = open('texto.txt','w')
    archivo.write('Hola Mundo de Python')
    archivo.close()

def leer_archivo():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r')
        #textos = archivo.read()
        textos = archivo.readlines()
        archivo.close()

        print(textos)
    else: 
        print('No existe el archivo')

def agregar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'a')
        archivo.write('\nHola Juan')
        archivo.close()

    else:
        print('No existe el archivo')

def modificar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r+')
        texto = archivo.readlines()
        print(texto)
        texto[1] = 'Hola Alex Roel\n'
        #archivo.write('\nHola Juan')
        print(texto)
        archivo.seek(0)
        archivo.writelines(texto)
        archivo.close()
        print(texto)

    else:
        print('No existe el archivo')

def eliminar_datos():
    archivo = open('texto.txt', 'w')
    archivo.close()

#escribir_archivo()
#leer_archivo()
#agregar_datos()
#modificar_datos()
eliminar_datos()
