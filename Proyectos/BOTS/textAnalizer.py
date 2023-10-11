import tkinter as tk
from tkinter import scrolledtext
from textblob import TextBlob
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import string

nltk.download('punkt')  
nltk.download('stopwords')  

def contar_palabras(texto):
    blob = TextBlob(texto)
    palabras = blob.words
    cantidad_palabras = len(palabras)
    return cantidad_palabras

def palabras_clave(texto, cantidad_palabras_clave=5):
    palabras = word_tokenize(texto)
    palabras = [palabra for palabra in palabras if palabra not in stopwords.words('spanish') and palabra not in string.punctuation]
    
    tfidf_vectorizer = TfidfVectorizer(max_features=cantidad_palabras_clave)
    tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(palabras)])
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    return feature_names

def resumen(texto, cantidad_oraciones=2):
    oraciones = sent_tokenize(texto)
    resumen = " ".join(oraciones[:cantidad_oraciones])
    return resumen

def idea_principal(texto):
    blob = TextBlob(texto)
    sentimiento = blob.sentiment.polarity
    if sentimiento > 0:
        return "La idea principal del texto es positiva."
    elif sentimiento < 0:
        return "La idea principal del texto es negativa."
    else:
        return "La idea principal del texto es neutral."

def analizar_texto():
    texto = entrada_texto.get("1.0", "end-1c")
    
    cantidad_palabras = contar_palabras(texto)
    palabras_clave_lista = palabras_clave(texto)
    resumen_texto = resumen(texto)
    idea_principal_texto = idea_principal(texto)
    
    resultado_texto.delete("1.0", "end")
    resultado_texto.insert("1.0", f"El texto tiene {cantidad_palabras} palabras.\n\n")
    resultado_texto.insert("end", "Palabras clave identificadas:\n")
    for palabra in palabras_clave_lista:
        resultado_texto.insert("end", palabra + "\n")
    resultado_texto.insert("end", f"\nResumen del texto:\n{resumen_texto}\n\n")
    resultado_texto.insert("end", f"{idea_principal_texto}\n")

ventana = tk.Tk()
ventana.title("Herramienta de Análisis de Texto")
ventana.geometry("700x700")

entrada_texto = scrolledtext.ScrolledText(ventana, width=60, height=20)
entrada_texto.pack()

boton_analizar = tk.Button(ventana, text="Analizar Texto", command=analizar_texto)
boton_analizar.pack()

resultado_texto = scrolledtext.ScrolledText(ventana, width=60, height=20)
resultado_texto.pack()

ventana.mainloop()
