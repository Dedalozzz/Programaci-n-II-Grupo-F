import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
#crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Combobox")
ventana.geometry("400x250")
#etiqueta
etiketa = tk.Label(ventana, text="Selecciona una especialidad:")
etiketa.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#crear un combobox
opciones = ["Cardiología", "Dermatología", "Neurología", "Pediatría", "Dermatología"]
combo = ttk.Combobox(ventana, values=opciones,state="readonly")
combo.current(0) #default value
combo.grid(row=0, column=1, padx=10, pady=10)
#función para mostrar la opción seleccionada
def mostrar():
    seleccion = combo.get()
    tk.messagebox.showinfo("Especialidad seleccionada", f"Has seleccionado: {seleccion}")
#Boton para confirmar la seleccion
boton = tk.Button(ventana, text="Confirmar", command=mostrar)
boton.grid(row=1, column=0, columnspan=2, pady=10)
ventana.mainloop()