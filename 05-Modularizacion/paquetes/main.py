
import my_paquete.aritmetica as a

def main():
    suma = a.sumar(4,4,5,8,7,9)
    resta = a.restar(10, 5)
    potencia = a.potencia(3,3)

    print('la suma es: ', suma)
    print('la resta es: ', resta)
    print('la potencia es: ', potencia)


if __name__ == '__main__':
    main()
