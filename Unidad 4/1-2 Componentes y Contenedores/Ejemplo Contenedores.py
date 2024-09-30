import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Función para agregar evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    # Validar que todos los campos estén llenos y que la fecha tenga el formato correcto
    try:
        datetime.strptime(fecha, "%Y-%m-%d")  # Validar formato de fecha
        if fecha and hora and descripcion:
            treeview.insert('', 'end', values=(fecha, hora, descripcion))
            limpiar_campos()
        else:
            raise ValueError("Campos vacíos")
    except ValueError:
        messagebox.showwarning("Error", "Por favor, ingresa una fecha válida en formato YYYY-MM-DD, además de la hora y la descripción.")

# Función para eliminar evento seleccionado
def eliminar_evento():
    selected_item = treeview.selection()
    if selected_item:
        treeview.delete(selected_item)
    else:
        messagebox.showwarning("Seleccionar evento", "Por favor, selecciona un evento para eliminar.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

# Función para confirmar la salida
def confirmar_salida():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Frame para las entradas de datos
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Campo de entrada para la fecha
label_fecha = tk.Label(frame_input, text="Fecha (YYYY-MM-DD):")
label_fecha.grid(row=0, column=0, padx=10)
entry_fecha = tk.Entry(frame_input)
entry_fecha.grid(row=0, column=1, padx=10)

# Campo de entrada para la hora
label_hora = tk.Label(frame_input, text="Hora:")
label_hora.grid(row=1, column=0, padx=10, pady=5)
entry_hora = tk.Entry(frame_input)
entry_hora.grid(row=1, column=1, padx=10, pady=5)

# Campo de entrada para la descripción
label_desc = tk.Label(frame_input, text="Descripción:")
label_desc.grid(row=2, column=0, padx=10, pady=5)
entry_desc = tk.Entry(frame_input)
entry_desc.grid(row=2, column=1, padx=10, pady=5)

# Frame para los elementos adicionales (Checkbutton y Radiobutton)
frame_extras = tk.Frame(root)
frame_extras.pack(pady=10)

# Casilla de verificación
check_var = tk.IntVar()
check_button = tk.Checkbutton(frame_extras, text="Opción de verificación", variable=check_var)
check_button.grid(row=0, column=0, padx=10, pady=5)

# Botones de opción (Radiobuttons)
radio_var = tk.StringVar()
radio_var.set("Opción 1")

label_opciones = tk.Label(frame_extras, text="Opciones:")
label_opciones.grid(row=1, column=0, padx=10, pady=5)

radio_opcion1 = tk.Radiobutton(frame_extras, text="Opción 1", variable=radio_var, value="Opción 1")
radio_opcion1.grid(row=2, column=0, padx=10)

radio_opcion2 = tk.Radiobutton(frame_extras, text="Opción 2", variable=radio_var, value="Opción 2")
radio_opcion2.grid(row=3, column=0, padx=10)

radio_opcion3 = tk.Radiobutton(frame_extras, text="Opción 3", variable=radio_var, value="Opción 3")
radio_opcion3.grid(row=4, column=0, padx=10)

# Frame para el Treeview
frame_treeview = tk.Frame(root)
frame_treeview.pack(pady=10)

# TreeView para mostrar los eventos
treeview = ttk.Treeview(frame_treeview, columns=("Fecha", "Hora", "Descripción"), show="headings", height=8)
treeview.heading("Fecha", text="Fecha")
treeview.heading("Hora", text="Hora")
treeview.heading("Descripción", text="Descripción")
treeview.pack()

# Frame para los botones de acciones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# Botones de agregar, eliminar y salir
btn_agregar = tk.Button(frame_buttons, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_buttons, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_buttons, text="Salir", command=confirmar_salida)
btn_salir.grid(row=0, column=2, padx=10)

# Iniciar el loop de la ventana principal
root.mainloop()
# JONATHAN TANDAZO