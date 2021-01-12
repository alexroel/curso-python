
def saludar(nombre):
    #global nombre
    return f'Hola, {nombre} desde la función saludar'

def sumar(a, b):
    return a + b

def restar(a=None, b=None):
    if a == None or b == None:
        print('Error: deves enviar dos números a la función')
        return
    return a - b

saludo = saludar('Roel')
print(saludo)

suma = sumar(10, 20)
print('La suma es:', suma)

#resta = restar(b = 20, a = 40)
resta = restar(b = 20, a = 40)

print('La resta es: ', resta)


#print('Hola desde fuera de la función', nombre)
