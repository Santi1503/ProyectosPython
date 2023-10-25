import time
import requests
from plyer import notification

API_KEY = '6d9f4373192bf101d734806809581067'
CITY = 'Santander, ES'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=es'

while True:
    try:
        response = requests.get(URL)
        weather_data = response.json()

        if 'weather' in weather_data and 'main' in weather_data:
            main_data = weather_data['main']
            weather_info = weather_data['weather'][0]

            temperature = main_data['temp']
            description = weather_info['description']

            notification_title = f"Clima en {CITY}"
            notification_message = f"Temperatura: {temperature}°C\nDescripción: {description}"

            notification.notify(
                title=notification_title,
                message=notification_message,
                timeout=10
            )
        else:
            print("Error al recuperar los datos del clima")

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

    time.sleep(60 * 60 * 1)