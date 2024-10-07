import tkinter as tk
from tkinter import messagebox

# Función para añadir una tarea
def add_task(event=None):
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "No puedes añadir una tarea vacía.")

# Función para marcar una tarea como completada
def mark_completed(event=None):
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"[Completada] {task}")
        task_listbox.itemconfig(selected_task_index, {'fg': 'gray'})  # Cambia el color para tareas completadas
    except IndexError:
        messagebox.showwarning("Ninguna tarea seleccionada", "Por favor selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task(event=None):
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Ninguna tarea seleccionada", "Por favor selecciona una tarea para eliminar.")

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Campo de entrada para añadir tareas
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Botón para añadir tareas
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar como completada
complete_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)
complete_button.grid(row=2, column=0, padx=10, pady=10)

# Botón para eliminar tarea
delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# Asociar atajos de teclado
root.bind('<Return>', add_task)  # Enter para añadir tarea
root.bind('<c>', mark_completed)  # 'C' para marcar como completada
root.bind('<d>', delete_task)  # 'D' para eliminar tarea
root.bind('<Delete>', delete_task)  # Tecla Delete para eliminar tarea
root.bind('<Escape>', close_app)  # Escape para cerrar la aplicación

# Iniciar el bucle principal de la ventana
root.mainloop()

# JONATHAN TANDAZO 