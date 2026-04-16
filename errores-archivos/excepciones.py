
while True:
    print("=== Programa de División ===")
    try:
        a = int(input("Ingrese un número: ")) # ValueError
        b = int(input("Ingrese otro número: "))

        resultado = a / b # ZeroDivisionError: division by zero
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"División entre {a}/{b} = {resultado}")

    ## Salir
    salir = input("¿Desea salir? (s/n): ")
    if salir.lower() == 's':
        break

