import random

pares = []
impares = []
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for n in numeros:
    numero_random = random.randint(1,100)
    resultado = n * numero_random

    if resultado % 2 == 0:
        print(f'{n} x {numero_random} = {resultado}')
        pares.append(resultado)
    else:
        print(f'{n} x {numero_random} = {resultado}')
        impares.append(resultado)

print('LISTA DE PARES: ', pares)
print('LISTA DE IMPARES: ', impares)