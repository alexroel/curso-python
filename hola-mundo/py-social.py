# ---------------------------------------------------------
# PROYECTO: FILTRO DE TOXICIDAD PARA REDES SOCIALES
# ---------------------------------------------------------

print("🌐 BIENVENIDO A PY-SOCIAL 🌐")
print("Un espacio libre de toxicidad.\n")

lista_negra = {"tonto", "idiota", "estúpido", "imbécil", "horrible"}

while True:
    # 1. Pedimos el mensaje
    mensaje = input("Escribe tu mensaje (o 'salir' para terminar): ")

    # 2. Validamos que no esté vacío
    if not mensaje.strip():
        print("⚠️ Por favor, escribe algo para compartir.\n")
        continue

    # 3. Verificamos si quiere salir
    if mensaje.lower().strip() == "salir":
        print("Gracias por usar Py-Social. ¡Hasta luego!")
        break

    # 4. Escaneamos y censuramos
    mensaje_min = mensaje.lower()
    es_toxico = False

    for palabra in lista_negra:
        if palabra in mensaje_min:
            # Censuramos todas las variaciones (minúsculas, mayúsculas, mixtas)
            mensaje = mensaje.replace(palabra, "*****")
            mensaje = mensaje.replace(palabra.capitalize(), "*****")
            mensaje = mensaje.replace(palabra.upper(), "*****")
            es_toxico = True
    
    # 5. Mostramos el resultado
    if es_toxico:
        print("⚠️ AVISO AUTOMÁTICO: Hemos censurado parte de tu contenido.")

    print(f"🐦 Publicación: {mensaje}")
    print("-" * 40)