import tkinter as tk
import requests

CUTTLY_API_KEY = "71eb17608dd70acd342203e70c1387ee6d879"

def acortar_enlace():
    enlace = entrada_enlace.get()
    if not enlace:
        resultado.set("Por favor, ingresa un enlace")
        return

    payload = {
        "url": enlace
    }

    headers = {
        "Api-Key": CUTTLY_API_KEY
    }

    try:
        response = requests.post("https://cutt.ly/api/api.php", headers=headers, params=payload)
        data = response.json()
        
        if data["url"]["status"] == 7:
            enlace_acortado = data["url"]["shortLink"]
            resultado.set(enlace_acortado)
        else:
            resultado.set("Error al acortar el enlace")
    except Exception as e:
        resultado.set("Error al acortar el enlace")

ventana = tk.Tk()
ventana.title("Acortador de Enlaces")

etiqueta = tk.Label(ventana, text="Ingresa el enlace:")
etiqueta.pack()
entrada_enlace = tk.Entry(ventana, width=40)
entrada_enlace.pack()

boton_acortar = tk.Button(ventana, text="Acortar Enlace", command=acortar_enlace)
boton_acortar.pack()

resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack()

ventana.mainloop()
