import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()


while True:
    with microphone as source:
        print("Di algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print("Texto reconocido: " + text)
    except sr.UnknownValueError:
        print("No se pudo reconocer el texto")
    except sr.RequestError as e:
        print("Ocurrió un error; {0}".format(e))