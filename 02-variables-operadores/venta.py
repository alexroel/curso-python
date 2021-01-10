"""
Práctica 02: Calcular precio de venta

Enunciado: dado el valor de venta de 
productos, hallar el IGV (18%) y el 
precio de venta.

Análisis: para la solución de este problema,
se requiere que el usuario ingrese el valor de 
venta del producto y el sistema realice el 
cálculo respectivo para hallar el IGV y el 
precio de venta, para esto use la siguiente 
expresión.

igv = vv * 0.18

pv = vv + igv
"""
#Mensaje de la Aplicación
print("---- REALIZAR UNA VENTA --- ")

#Entrada de datos 
vv = float(input('Ingrese valor de venta: '))

#Operaciones 
igv = vv * 0.18
pv = vv + igv

#Salida de datos 
print('='*25)
print('---- FACTURA DE VENTA ---')
print('='*25)
print('Valor de Venta: ', vv)
print('IGV: ', igv)
print('Precio de Venta: ', pv)
print('='*25)

