
def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    return suma, kwargs

suma_total, datos = sumar(10,20,3, 100, nombre = 'Alex', edad = 25)
print('La suma total es: ', suma_total)
print(datos)
