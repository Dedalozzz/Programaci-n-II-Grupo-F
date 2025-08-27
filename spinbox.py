#spinbox de numeros del 1 al 10 para edad
import tkinter as tk
from tkinter import messagebox
def mostrarEdad():
    tk.Messagebox.showinfo("Edad", f"La edad es: {spin.get()}")
def mostrarGenero():
    tk.Messagebox.showinfo("Género", f"El género es: {genero.get()}")
Ventana = tk.Tk()
Ventana.geometry("350x300")
label_edad = tk.Label(Ventana, text="Edad")
label_edad.grid(row=0, column=0, padx=5, pady=5, sticky="W")
spin = tk.Spinbox(from_=1, to=10)
spin.grid(row=0, column=1, padx=10, pady=10)
boton = tk.Button(text="Obtener valor", command=mostrarEdad)
boton.grid(row=1, column=0, padx=10, pady=10)
#genero
labelgenero = tk.Label(Ventana, text="Género")
labelgenero.grid(row=2, column=0, padx=5, pady=5, sticky="W")
#spinbox de genero
genero = tk.Spinbox(Ventana, values=("Masculino", "Femenino"))
genero.grid(row=2, column=1, padx=10, pady=10)
botongenero = tk.Button(text="Obtener género", command=mostrarGenero)
botongenero.grid(row=3, column=0, padx=10, pady=10)

Ventana.mainloop()