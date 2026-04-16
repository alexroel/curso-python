from password import password as p

# Así probamos que nuestras funciones sirven
while True:
    print("\n--- MENÚ DE SEGURIDAD ---")
    respuesta = input("¿Cuántos caracteres quieres en tu password? (Escribe 'salir' para terminar): ")
    
    if respuesta.lower() == 'salir':
        print("¡Mantente seguro! Adiós.")
        break

    mi_password = p.generar_password(int(respuesta))
    nivel_seguridad = p.evaluar_password(mi_password)

    # Imprimimos resultados
    print("-" * 30)
    print(f"Tu contraseña es: {mi_password}")
    print(f"Nivel de seguridad: {nivel_seguridad}")
    print("-" * 30)
        
    
