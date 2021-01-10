"""
Práctica 01: Calcular cociente y Residuo
Enunciado: hallar el cociente y el residuo 
(resto) de dos números enteros.
Análisis: para la solución de este problema,
 se requiere que el usuario ingrese dos 
 números enteros y el sistema realice el 
 cálculo respectivo para hallar el cociente 
 y residuo.
"""

print('Calcular cociente y residuo')

a = input('Ingrese primer número: ')
b = input('Ingrese segundo número:')

a = int(a)
b = int(b)

cociente = a // b
residuo = a % b

print('El cociente es: ', cociente)
print('El Residuo es: ', residuo)