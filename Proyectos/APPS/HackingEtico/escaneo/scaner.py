import pywifi
from pywifi import const

# Función para escanear redes Wi-Fi
def scan_wifi():
    print("Escaneando redes Wi-Fi...")
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Obtener la primera interfaz Wi-Fi

    iface.scan()
    scan_results = iface.scan_results()

    # Mostrar las redes encontradas
    print("Redes encontradas:")
    for network in scan_results:
        # Filtrar perfiles de red
        if isinstance(network, pywifi.profile.Profile):
            continue
        print("SSID: {}, BSSID: {}, Canal: {}".format(network.ssid, network.bssid, network.channel))

# Llamar a la función de escaneo de redes Wi-Fi
scan_wifi()
