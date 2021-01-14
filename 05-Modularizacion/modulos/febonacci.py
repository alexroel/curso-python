# Módulo de números de Fibonacci
def fibo(n):
    a, b = 0, 1
    while a < n: 
        print(a, end=' ')
        a, b = b, a + b 
        
    print()

def fibo2(n):
    resultado = []
    a, b = 0, 1
    while a < n: 
        resultado.append(a)
        a, b = b, a + b 
    
    return resultado

