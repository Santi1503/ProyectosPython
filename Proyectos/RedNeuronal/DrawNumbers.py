import tkinter as tk
from tkinter import Canvas, messagebox, filedialog
from PIL import Image, ImageDraw
import numpy as np
import tensorflow as tf

ventana = tk.Tk()
ventana.title("Adivina el número")

canvas = None
model = None
x1, y1 = None, None

def dibujar(event):
    global x1, y1
    if x1 and y1:
        x2, y2 = event.x, event.y
        canvas.create_line((x1, y1, x2, y2), fill="black", width=10)
        draw.line([x1, y1, x2, y2], fill="black", width=10)
        x1, y1 = x2, y2

def empezar_dibujo(event):
    global x1, y1
    x1, y1 = event.x, event.y

def finalizar_dibujo(event):
    global x1, y1
    x1, y1 = None, None

def predecir():
    if model is None:
        messagebox.showerror("Error", "Carga un modelo antes de hacer una predicción.")
        return

    global draw
    imagen = Image.new("L", (280, 280), 0)
    draw = ImageDraw.Draw(imagen)
    canvas.postscript(file="dibujo.eps")
    imagen = Image.open("dibujo.eps").convert("L")
    imagen = imagen.resize((28, 28))
    imagen = np.array(imagen)
    imagen = imagen / 255.0
    imagen = imagen.reshape(1, 28, 28)

    prediccion = model.predict(imagen)
    numero_predicho = np.argmax(prediccion)
    messagebox.showinfo("Predicción", f"El número predicho es: {numero_predicho}")


def borrar():
    global canvas, draw
    canvas.delete("all")
    draw = ImageDraw.Draw(Image.new("L", (280, 280), 0))

def cargar_modelo():
    global model
    ruta_modelo = filedialog.askopenfilename(filetypes=[("Modelo de Red Neuronal", "*.h5")])
    if ruta_modelo:
        model = tf.keras.models.load_model(ruta_modelo)
        messagebox.showinfo("Éxito", "Modelo cargado correctamente.")

def guardar_modelo():
    if model is None:
        messagebox.showerror("Error", "No hay un modelo para guardar.")
        return

    ruta_guardar = filedialog.asksaveasfilename(defaultextension=".h5", filetypes=[("Modelo de Red Neuronal", "*.h5")])
    if ruta_guardar:
        model.save(ruta_guardar)
        messagebox.showinfo("Éxito", "Modelo guardado correctamente.")

canvas = Canvas(ventana, width=280, height=280, bg="white")
canvas.pack()

boton_predecir = tk.Button(ventana, text="Predecir", command=predecir)
boton_borrar = tk.Button(ventana, text="Borrar", command=borrar)
boton_cargar_modelo = tk.Button(ventana, text="Cargar Modelo", command=cargar_modelo)
boton_guardar_modelo = tk.Button(ventana, text="Guardar Modelo", command=guardar_modelo)

boton_predecir.pack()
boton_borrar.pack()
boton_cargar_modelo.pack()
boton_guardar_modelo.pack()

draw = ImageDraw.Draw(Image.new("L", (280, 280), 0))

canvas.bind("<Button-1>", empezar_dibujo)
canvas.bind("<B1-Motion>", dibujar)
canvas.bind("<ButtonRelease-1>", finalizar_dibujo)

ventana.mainloop()
