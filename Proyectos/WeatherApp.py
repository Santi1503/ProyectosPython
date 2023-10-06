import requests

API_KEY = '6d9f4373192bf101d734806809581067'

def obtener_pronostico(ciudad):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            clima = data["weather"][0]["description"]
            temperatura = data["main"]["temp"]
            humedad = data["main"]["humidity"]
            viento = data["wind"]["speed"]

            print(f"Pronostico del tiempo en {ciudad}")
            print(f"Descripción: {clima}")
            print(f"Temperatura: {temperatura} °C")
            print(f"Humedad: {humedad}")
            print(f"Viento: {viento}")
        else:
            print("No se pudo encontrar la ciudad") 
    except Exception as e:
        print(f"Se produjo un error: {str(e)}")

ciudad = input("Ingresa el nombre de la ciudad: ")
obtener_pronostico(ciudad)

