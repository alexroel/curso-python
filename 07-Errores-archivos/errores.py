c = 0
suma = 0
while c < 3:
    try:
        n = int(input(f'Ingrese un número {c+1}: '))
        suma += n
        c += 1
    except:
        print('Error: Ingrese solo números enteros')
    else:
        print('Todo ha funcionado correctamente')
        #break
    finally:
        print('Fin de la ejecución')

print('La suma total es: ', suma)
