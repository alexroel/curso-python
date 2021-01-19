divi = 0
try: 
    a = int(input('Ingrese el Dividendo: '))
    b = int(input('Ingrese el Divisor: '))

    divi = a / b
except ValueError:
    print('Error: Ingrese solo números enteros!')
except ZeroDivisionError:
    print('Error: No se Puede divir por cero!')
except Exception as error:
    print('Ha ocurrido error no previsto:', type(error).__name__)
    
print('La división es: ', divi)
