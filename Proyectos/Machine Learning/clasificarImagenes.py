import tensorflow as tf
import tkinter as tk
import numpy as np
from tensorflow import keras
from tkinter import filedialog
from tkinter import ttk
from tkinter import Canvas, messagebox
from PIL import Image, ImageTk

model = keras.applications.MobileNetV2(weights="imagenet")

def ImageClasification():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path).resize((224, 224))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)
        predictions = model.predict(image)
        decoded_predictions = keras.applications.mobilenet.decode_predictions(predictions, top=5)[0]

        result_text.delete("1.0", "end")
        for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
            result_text.insert("end", f"{i +1}: {label} ({score * 100:2f}%)\n")


window = tk.Tk()
window.title("Clasificación de imagenes")

canvas = Canvas(window, width=224, height=224)
canvas.pack()

selectButtton = ttk.Button(window, text="Seleccionar Imagen", command=ImageClasification)
selectButtton.pack()

result_text = tk.Text(window, height=6, width=30)
result_text.pack()

window.mainloop()
                                                                                                 