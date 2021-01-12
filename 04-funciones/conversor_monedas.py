
def convertir(valor_dolar, pais):
    cantidad_moneda = float(input(f'Ingrese cantidad de {pais}: '))

    dolares = cantidad_moneda / valor_dolar
    #10.4562 10.45
    dolares = round(dolares, 2)
    print(f'Tienes ${dolares} Dolares')

def main():
    
    while True:
        menu = """
        1-Soles Peruanos a Dolares 
        2-Pesos Mexicanos a Dolares 
        3-Pesos Colombianos a Dolares
        4-Salir
        Ingrese una Opcion: """

        opcion = input(menu)

        if opcion == '1':
            convertir(3.61, 'soles peruanos')
        elif opcion == '2':
            convertir(20, 'pesos Mexicanos')
        elif opcion == '3':
            convertir(3471.27, 'pesos Colombianos')
        elif opcion == '4':
            print("Cerrando conversor de monedas ")
            break
        else:
            print("Opcion incorrecta !!!")
            print("Vuelve a ingresar la opción correcta")
    

# Punto de inicio de la aplicación           
if __name__ == '__main__':
    main()