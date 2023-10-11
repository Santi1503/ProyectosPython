import matplotlib.pyplot as plt
from tkinter import *

def create_graph():
    graph_type = graph_type_var.get()

    if graph_type == 'Gráfico de Barras':
        values = values_entry.get().split(',')
        categories = categories_entry.get().split(',')
        values = [int(value) for value in values]
        
        plt.bar(categories, values)
        plt.title('Gráfico de Barras')
        plt.xlabel('Categorías')
        plt.ylabel('values')
    elif graph_type == 'Gráfico de Líneas':
        values = values_entry.get().split(',')
        values = [int(value) for value in values]
        
        plt.plot(values)
        plt.title('Gráfico de Líneas')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
    elif graph_type == 'Gráfico de Dispersión':
        x_values = x_values_entry.get().split(',')
        y_values = y_values_entry.get().split(',')
        x_values = [float(x) for x in x_values]
        y_values = [float(y) for y in y_values]
        
        plt.scatter(x_values, y_values)
        plt.title('Gráfico de Dispersión')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
    elif graph_type == 'Gráfico de Pastel':
        sizes = values_entry.get().split(',')
        tags = categories_entry.get().split(',')
        sizes = [float(size) for size in sizes]
        
        plt.pie(sizes, labels=tags, autopct='%1.1f%%')
        plt.title('Gráfico de Pastel')
    elif graph_type == 'Gráfico de Área':
        x_values = x_values_entry.get().split(',')
        y_values = y_values_entry.get().split(',')
        x_values = [float(x) for x in x_values]
        y_values = [float(y) for y in y_values]
        
        plt.fill_between(x_values, y_values, color='skyblue')
        plt.title('Gráfico de Área')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')

    plt.show()


window = Tk()
window.title('Generador de Gráficos')
window.geometry("400x300")

graph_type_label = Label(window, text='Elija el tipo de gráfico:')
graph_type_label.pack()

graph_type_var = StringVar()
graph_type_var.set('Gráfico de Barras')

graph_type_optionmenu = OptionMenu(window, graph_type_var, 'Gráfico de Barras', 'Gráfico de Líneas', 'Gráfico de Dispersión', 'Gráfico de Pastel', 'Gráfico de Área')
graph_type_optionmenu.pack()

values_label = Label(window, text='values (separados por comas):')
values_label.pack()

values_entry = Entry(window)
values_entry.pack()

categories_label = Label(window, text='Categorías (separadas por comas):')
categories_label.pack()

categories_entry = Entry(window)
categories_entry.pack()

x_values_label = Label(window, text='values de Eje X (separados por comas):')
x_values_label.pack()

x_values_entry = Entry(window)
x_values_entry.pack()

y_values_label = Label(window, text='values de Eje Y (separados por comas):')
y_values_label.pack()

y_values_entry = Entry(window)
y_values_entry.pack()

create_graph_button = Button(window, text='Crear Gráfico', command=create_graph)
create_graph_button.pack()

window.mainloop()
