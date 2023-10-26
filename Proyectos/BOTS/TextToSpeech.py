import pyttsx3

engine = pyttsx3.init()

engine.say("Escribe lo que quieras que diga (para salir, escribe exit)")

while True:
    text = input()
    if text.lower() == "exit":
        break

    engine.say(text)
    engine.runAndWait()

print("Saliendo del programa")