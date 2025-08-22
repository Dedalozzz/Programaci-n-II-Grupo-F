import tkinter as tk
from tkinter import messagebox

def registrarDoctor():
    nombre = entryNombre.get()
    direccion = entryDireccion.get()
    telefono = entryTelefono.get()
    especialidad = varEspecialidad.get()
    disponibilidad = []
    if varManiana.get():
        disponibilidad.append("Mañana")
    if varTarde.get():
        disponibilidad.append("Tarde")
    if varNoche.get():
        disponibilidad.append("Noche")
    disp_text = ", ".join(disponibilidad) if disponibilidad else "Ninguna"
    info = (
        f"Nombre completo: {nombre}\n"
        f"Dirección: {direccion}\n"
        f"Teléfono: {telefono}\n"
        f"Especialidad: {especialidad}\n"
        f"Disponibilidad: {disp_text}"
    )
    messagebox.showinfo("Datos del Doctor", info)
def solo_numeros(char):
    return char.isdigit()

ventana = tk.Tk()
ventana.title("Registro de Doctores")
ventana.geometry("500x600")
ventana.configure(bg="#800020")

# Nombre completo
tk.Label(ventana, text="Nombre completo:", bg="#800020", fg="white", font=("Times New Roman", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entryNombre = tk.Entry(ventana, font=("Times New Roman", 12))
entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Dirección
tk.Label(ventana, text="Dirección:", bg="#800020", fg="white", font=("Times New Roman", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entryDireccion = tk.Entry(ventana, font=("Times New Roman", 12))
entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="ew")


# Teléfono
vcmd = (ventana.register(solo_numeros), '%S')
tk.Label(ventana, text="Teléfono:", bg="#800020", fg="white", font=("Times New Roman", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entryTelefono = tk.Entry(ventana, font=("Times New Roman", 12), validate="key", validatecommand=vcmd)
entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Especialidad (Radiobutton)
tk.Label(ventana, text="Especialidad:", bg="#800020", fg="white", font=("Times New Roman", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
varEspecialidad = tk.StringVar(value="Pediatría")
rbPediatria = tk.Radiobutton(ventana, text="Pediatría", variable=varEspecialidad, value="Pediatría", bg="#800020", fg="white", font=("Times New Roman", 12), selectcolor="#800020")
rbPediatria.grid(row=3, column=1, sticky="w")
rbCardiologia = tk.Radiobutton(ventana, text="Cardiología", variable=varEspecialidad, value="Cardiología", bg="#800020", fg="white", font=("Times New Roman", 12), selectcolor="#800020")
rbCardiologia.grid(row=4, column=1, sticky="w")
rbNeurologia = tk.Radiobutton(ventana, text="Neurología", variable=varEspecialidad, value="Neurología", bg="#800020", fg="white", font=("Times New Roman", 12), selectcolor="#800020")
rbNeurologia.grid(row=5, column=1, sticky="w")

# Disponibilidad (Checkbutton)
tk.Label(ventana, text="Disponibilidad:", bg="#800020", fg="white", font=("Times New Roman", 12)).grid(row=9, column=0, padx=10, pady=5, sticky="w")
varManiana = tk.BooleanVar()
varTarde = tk.BooleanVar()
varNoche = tk.BooleanVar()
cbManiana = tk.Checkbutton(ventana, text="Mañana", variable=varManiana, bg="#800020", fg="white", font=("Times New Roman", 12), selectcolor="#800020")
cbManiana.grid(row=9, column=1, sticky="w")
cbTarde = tk.Checkbutton(ventana, text="Tarde", variable=varTarde, bg="#800020", fg="white", font=("Times New Roman", 12), selectcolor="#800020")
cbTarde.grid(row=10, column=1, sticky="w")
cbNoche = tk.Checkbutton(ventana, text="Noche", variable=varNoche, bg="#800020", fg="white", font=("Times New Roman", 12), selectcolor="#800020")
cbNoche.grid(row=11, column=1, sticky="w")

# Botón registrar
btnRegistrar = tk.Button(ventana, text="Registrar al nuevo Doctor", command=registrarDoctor, font=("Times New Roman", 12), bg="#FFFFFF", fg="black")
btnRegistrar.grid(row=12, column=0, columnspan=2, pady=10)

# Botón salir
btnSalir = tk.Button(ventana, text="Salir", command=ventana.quit, font=("Times New Roman", 12), bg="#FFFFFF", fg="black")
btnSalir.grid(row=13, column=0, columnspan=2, pady=10)

ventana.mainloop()