from googletrans import Translator

def mostrar_menu():
    print("\n--- Traductor en Python ---")
    print("Elige el idioma:")
    print("1. Español (es)")
    print("2. Inglés (en)")
    print("3. Francés (fr)")
    print("4. Alemán (de)")
    print("5. Húngaro (hu)")
    print("6. Salir")

def obtener_codigo_idioma(opcion):
    idiomas = {
        '1': 'es',
        '2': 'en',
        '3': 'fr',
        '4': 'de',
        '5': 'hu'
    }
    return idiomas.get(opcion, None)

def main():
    translator = Translator()
    while True:
        mostrar_menu()
        opcion = input("Ingresa la opción: ")
        if opcion == '6':
            print("¡Hasta luego!")
            break

        codigo_idioma = obtener_codigo_idioma(opcion)
        if not codigo_idioma:
            print("Opción inválida. Intenta de nuevo.")
            continue

        texto = input("Escribe el texto a traducir: ")
        try:
            traduccion = translator.translate(texto, dest=codigo_idioma)
            print(f"Traducción ({codigo_idioma}): {traduccion.text}")
        except Exception as e:
            print("Error al traducir:", e)

def traducir(texto, codigo_idioma):
    translator = Translator()
    try:
        traduccion = translator.translate(texto, dest=codigo_idioma)
        return traduccion.text
    except Exception as e:
        return f"Error al traducir: {e}"


