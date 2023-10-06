import requests

# Función para realizar la traducción
def traducir_texto(texto, idioma_origen, idioma_destino):
    endpoint = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"
    params = {
        "from": idioma_origen,
        "to": idioma_destino
    }
    headers = {
        "Ocp-Apim-Subscription-Key": "TU_CLAVE_DE_SUSCRIPCION_AZURE",
        "Content-Type": "application/json"
    }

    body = [
        {
            "text": texto
        }
    ]

    try:
        response = requests.post(endpoint, params=params, headers=headers, json=body)
        data = response.json()
        traduccion = data[0]["translations"][0]["text"]
        return traduccion
    except Exception as e:
        return str(e)

# Función principal
def main():
    print("Bienvenido al Traductor de Texto en Consola")

    # Solicitar texto al usuario
    texto = input("\nIngrese el texto que desea traducir: ")

    # Solicitar idioma de origen al usuario
    idioma_origen = input("Ingrese el idioma de origen (por ejemplo, 'en' para inglés): ")

    # Solicitar idioma de destino al usuario
    idioma_destino = input("Ingrese el idioma de destino (por ejemplo, 'es' para español): ")

    # Realizar la traducción
    resultado = traducir_texto(texto, idioma_origen, idioma_destino)

    # Mostrar resultado
    print("\nResultado de la traducción:")
    print(resultado)

if __name__ == "__main__":
    main()
