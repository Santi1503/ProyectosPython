import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def load_image(): 
    file_path = filedialog.askopenfilename()
    if file_path:
        global imagen
        imagen = Image.open(file_path)
        imagen.thumbnail((400, 400))
        imagen_label.config(image=imagen)
        imagen_label.image = imagen

def generate_meme():
    if imagen:
        texto_superior = texto_superior_entry.get()
        texto_inferior = texto_inferior_entry.get()

        draw = ImageDraw.Draw(imagen)
        width, height = imagen.size
        font = ImageFont.truetype("arial.ttf", 20)

        text_width, text_height = draw.textsize(texto_superior, font)
        draw.text(((width - text_width) / 2, 10), texto_superior, (255, 255, 255), font=font)

        text_width, text_height = draw.textsize(texto_inferior, font)
        draw.text(((width - text_width) / 2, height - text_height - 10), texto_inferior, (255, 255, 255), font=font)

        meme_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Imagen PNG", "*.png")])
        if meme_path:
            imagen.save(meme_path)


root = tk.Tk()
root.title("Generador de Memes")

cargar_imagen_button = tk.Button(root, text="Cargar Imagen", command=load_image)
cargar_imagen_button.pack()

imagen_label = tk.Label(root)
imagen_label.pack()

texto_superior_label = tk.Label(root, text="Texto Superior:")
texto_superior_label.pack()
texto_superior_entry = tk.Entry(root)
texto_superior_entry.pack()

texto_inferior_label = tk.Label(root, text="Texto Inferior:")
texto_inferior_label.pack()
texto_inferior_entry = tk.Entry(root)
texto_inferior_entry.pack()

generar_meme_button = tk.Button(root, text="Generar Meme", command=generate_meme)
generar_meme_button.pack()

root.mainloop()