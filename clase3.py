import tkinter as tk
from tkinter import messagebox
def nuevoPaciente():
    VentanaRegistro = tk.Toplevel(ventanaPrincipal)
    VentanaRegistro.title("Registro de Paciente")
    VentanaRegistro.geometry("400x350")
    VentanaRegistro.configure(bg="#123B69")
    nombreLabel = tk.Label(VentanaRegistro, text="Nombre:",bg="#123B69", fg="white", font=("times new roman", 12))
    nombreLabel.grid(row=0, column=0, padx=10, pady=5,sticky="w")
    entryNombre = tk.Entry(VentanaRegistro)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    direccionLabel = tk.Label(VentanaRegistro, text="Dirección:", bg="#123B69", fg="white", font=("times new roman", 12))
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entryDireccion = tk.Entry(VentanaRegistro)
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    telefonoLabel = tk.Label(VentanaRegistro, text="Teléfono:", bg="#123B69", fg="white", font=("times new roman", 12))
    telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entryTelefono = tk.Entry(VentanaRegistro)
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    sexoLabel = tk.Label(VentanaRegistro, text="Sexo:", bg="#123B69", fg="white", font=("times new roman", 12))
    sexoLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    sexo= tk.StringVar(value='Masculino')
    rbMasculino = tk.Radiobutton(VentanaRegistro, text="Masculino", variable=sexo, value='Masculino', bg="#123B69", fg="white")
    rbMasculino.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    rbFemenino = tk.Radiobutton(VentanaRegistro, text="Femenino", variable=sexo, value='Femenino', bg="#123B69", fg="white")
    rbFemenino.grid(row=3, column=2, padx=10, pady=5, sticky="w")
    
    def registarDatos():
        messagebox.showinfo("Datos Registrados")
        VentanaRegistro.destroy()
        info=(
        f'Nombre: {entryNombre.get()}\n'
        f'Dirección: {entryDireccion.get()}\n'
        f'Teléfono: {entryTelefono.get()}\n'
        f'Sexo: {sexo.get()}'
        )

    btnRegistrar = tk.Button(VentanaRegistro, text="Registrar Datos", command=registarDatos)
    btnRegistrar.grid(row=9, column=1, padx=10, pady=15, columnspan=2, )
def eliminarPaciente():
    messagebox.showinfo("Eliminar Paciente", "Eliminar un paciente existente")
def buscarPaciente():
    messagebox.showinfo("Buscar Paciente", "Buscar un paciente por ID o nombre")

#venntana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Sistetema de Registro de Pacientes")
ventanaPrincipal.geometry("700x500")
ventanaPrincipal.configure(bg="#123B69")
#barra de menu
barraMenu = tk.Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=barraMenu)
#menu de pacientes
menuPacientes = tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Pacientes", menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente", command=nuevoPaciente)
menuPacientes.add_command(label="Eliminar Paciente", command=eliminarPaciente)
menuPacientes.add_command(label="Buscar Paciente", command=buscarPaciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir", command=ventanaPrincipal.quit)
#menu de doctores
menuDoctores = tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=lambda:print("Nuevo Doctor"))
menuDoctores.add_command(label="Buscar Doctor", command=lambda:print("Buscar Doctor"))
menuDoctores.add_command(label="Eliminar Doctor", command=lambda:print("Eliminar Doctor"))
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal.quit)
#menu ayuda
menuAyuda = tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda:messagebox.showinfo("Acerca de","Sistema de el ala de Ing biomedica v1.0\nDev: Dedalozzz"))

ventanaPrincipal.mainloop()