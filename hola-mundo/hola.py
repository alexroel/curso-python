# Generador de Nombres
# ---------------------------------

# Entrada de datos
nombre_animal = input("Ingrese el nombre de un animal: ").strip().capitalize()
palabra_tech = input("Introduce una palabra tecnológica (ej. Cyber, Quantum, Neural): ").strip().capitalize()

# Generación de nombre
nombre_generado = palabra_tech + nombre_animal

# Salida del resultado
print(f"\nTu nuevo nombre generado es: {nombre_generado}")