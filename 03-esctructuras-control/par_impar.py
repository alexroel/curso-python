
n = int(input('Ingrese un número entero: '))

if n != 0:
    if n > 0:
        if n % 2 == 0:  # True
            print(f'El número {n} es PAR POSITIVO')
        else:
            print(f'El número {n} es IMPAR POSITIVO')
    else:
        if n % 2 == 0:  # True
            print(f'El número {n} es PAR NEGATIVO')
        else:
            print(f'El número {n} es IMPAR NEGATIVO')
else:
    print(f'El número {n} es NEUTRO')


