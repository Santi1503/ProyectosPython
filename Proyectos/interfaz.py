from tkinter import *
import tkinter
root = Tk()
# nombre en ventana
root.title('Equipo de Configuraciones')
# ventana
root.geometry("650x300")
etiqueta = tkinter.Label(root, text="Chat con Corvex", bg="SeaGreen3")
etiqueta.pack(fill=tkinter.X)

color = tkinter.Label(root, bg="SeaGreen1")
color.pack(fill=tkinter.BOTH, expand=1)

# interaccion
text = tkinter.Entry(root)
text.pack()

root.mainloop()
