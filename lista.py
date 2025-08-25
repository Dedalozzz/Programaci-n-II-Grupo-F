import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.title("Ejemplo de Listbox")

sintomasLabel = tk.Label(ventana, text="síntomas:")
sintomasLabel.grid(row=0, column=0, padx=5, pady=5 , sticky="w")
#crear un listbox
lista = tk.Listbox(ventana, selectmode=tk.SINGLE)
lista.insert(1, "Dolor de cabeza")
lista.insert(2, "Fiebre")
lista.insert(3, "Tos")  
lista.insert(4, "Fatiga")
lista.insert(5, "Dificultad para respirar")
lista.grid(row=0, column=1, pady=10 ,sticky="we")  
#Botón para mostrar el síntoma seleccionado
def mostrar():
    seleccionado = lista.get(lista.curselection())
    tk.Messagebox.showinfo("Síntoma seleccionado", f"Has seleccionado: {seleccionado}")
boton = tk.Button(ventana, text="Mostrar síntoma seleccionado", command=mostrar)
boton.grid(row=1, column=0, padx=10, pady=10)
ventana.mainloop()