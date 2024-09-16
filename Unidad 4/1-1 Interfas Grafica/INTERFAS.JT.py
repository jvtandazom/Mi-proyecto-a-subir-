import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_informacion():
    info = entry_texto.get()  # Obtener el texto del campo de texto
    if info:  # Si el campo no está vacío
        lista_datos.insert(tk.END, info)  # Agregar a la lista
        entry_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar la lista
def limpiar_informacion():
    lista_datos.delete(0, tk.END)  # Limpiar la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Etiqueta
label_texto = tk.Label(ventana, text="Ingrese información:")
label_texto.pack(pady=5)

# Campo de texto
entry_texto = tk.Entry(ventana, width=40)
entry_texto.pack(pady=5)

# Botón para agregar información
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_informacion)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=5)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_informacion)
boton_limpiar.pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()
