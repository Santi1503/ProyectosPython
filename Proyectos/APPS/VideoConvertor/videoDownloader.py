from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox

print(os.getcwd())

def accionMP3():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.filter(only_audio=True).first()
    # Obtener el título del video y eliminar caracteres no deseados del nombre del archivo
    titulo = video.title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
    # Descargar el archivo con el nombre del título y la extensión .mp3
    descarga.download(output_path="C:/Users/gomez/OneDrive/Escritorio/DescargasPrograma", filename=f"{titulo}.mp3")

def accionMP4():
    enlace=videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download(output_path="C:/Users/gomez/OneDrive/Escritorio/DescargasPrograma")
    
def popup():
    MessageBox.showinfo("Sobre el programa","El programa esta diseñado para permitir a creadores de contenido poder descargar videos y audios de YouTube")
    
root = Tk()
root.config(bd=15)
root.title("Descarga videos de Youtube")

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Más información", menu=helpmenu)
helpmenu.add_command(label="Más información del programa", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

instrucciones = Label(root, text="Programa realizado con Python para descargar mp3 y mp4 de YouTube\n")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar mp3", command=accionMP3)
boton.grid(row=2, column=1)

boton = Button(root, text="Descargar mp4", command=accionMP4)
boton.grid(row=2, column=2)

root.mainloop()