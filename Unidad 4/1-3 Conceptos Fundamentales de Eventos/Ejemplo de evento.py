import tkinter as tk
from tkinter import messagebox

# Función para añadir una tarea a la lista
def add_task(event=None):
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")

# Función para marcar una tarea como completada
def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        # Añadir una marca de completado a la tarea
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, f"{task} - [Completada]")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada")

# Función para eliminar una tarea de la lista
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Campo de entrada para las tareas
entry_task = tk.Entry(root, width=35)
entry_task.pack(pady=10)
entry_task.bind("<Return>", add_task)  # Añadir tarea al presionar Enter

# Botones para añadir, marcar como completada y eliminar tareas
frame_buttons = tk.Frame(root)
frame_buttons.pack()

btn_add_task = tk.Button(frame_buttons, text="Añadir Tarea", width=15, command=add_task)
btn_add_task.pack(side=tk.LEFT, padx=5)

btn_complete_task = tk.Button(frame_buttons, text="Marcar como Completada", width=20, command=complete_task)
btn_complete_task.pack(side=tk.LEFT, padx=5)

btn_delete_task = tk.Button(frame_buttons, text="Eliminar Tarea", width=15, command=delete_task)
btn_delete_task.pack(side=tk.LEFT, padx=5)

# Lista para mostrar las tareas
listbox_tasks = tk.Listbox(root, width=60, height=10)
listbox_tasks.pack(pady=10)

# Iniciar la ventana
root.mainloop()

# JONATHAN TANDAZO
