import random
import string

def generar_password(longitud:int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(longitud):
        caracter_aleatorio = random.choice(caracteres)
        password += caracter_aleatorio
    return password

def evaluar_password(password:str) -> str:

    longitud = len(password)

    if longitud < 8:
        return "Débil 🔴 (Fácil de hackear)"
    elif longitud >= 12:
        return "Inhackeable 🟢 (Nivel militar)"
    else:
        return "Moderada 🟡 (Podría ser mejor)"
  