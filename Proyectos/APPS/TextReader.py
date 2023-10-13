import tkinter as tk
import pyttsx3

def readText():
    textIn = in_Text.get("1.0", "end-1c")
    engine = pyttsx3.init()

    engine.setProperty("engine", "sapi5")

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    engine.say(textIn)
    engine.runAndWait()

window = tk.Tk()
window.title("Lector de texto")

tag = tk.Label(window, text="Ingresa el texto: ")
tag.pack()
in_Text = tk.Text(window, height=10, width=40)
in_Text.pack()

buttonRead = tk.Button(window, text="Leer texto", command=readText)
buttonRead.pack()

window.mainloop()
