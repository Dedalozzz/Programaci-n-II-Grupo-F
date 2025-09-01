# Importación de librerías 
import tkinter as tk
from tkinter import ttk, messagebox
# Crear ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Libro de Pacientes y Doctores")
ventanaPrincipal.geometry("890x600")
# Crear contenedor NoteBook (pestañas)
pestañas = ttk.Notebook(ventanaPrincipal)
# Crear frames 
framePacientes = ttk.Frame(pestañas)
frameDoctores = ttk.Frame(pestañas)
# Agregar pestañas al NoteBook
pestañas.add(framePacientes, text="Pacientes")
pestañas.add(frameDoctores, text="Doctores")
# Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")
# Nombre
labelNombre = tk.Label(framePacientes, text=" Nombre Completo:")
labelNombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nombreP = tk.Entry(framePacientes)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="w")
# Fecha de nacimiento
labelFechaN = tk.Label(framePacientes, text=" Fecha de Nacimiento:")
labelFechaN.grid(row=1, column=0, padx=5, pady=5, sticky="w")
fechaN = tk.Entry(framePacientes)
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="w")
# Edad (readonly)
labelEdad = tk.Label(framePacientes, text=" Edad:")
labelEdad.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadP = tk.Entry(framePacientes, state="readonly")
edadP.grid(row=2, column=1, padx=5, pady=5, sticky="w")
# Género
labelGenero = tk.Label(framePacientes, text=" Género:")
labelGenero.grid(row=3, column=0, padx=5, pady=5, sticky="w")
genero = tk.StringVar()
genero.set("Masculino") # Valor por defecto
radioMasculino = ttk.Radiobutton(framePacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, padx=5, sticky="w")
radioFemenino = ttk.Radiobutton(framePacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, padx=5, sticky="w")
# Grupo sanguíneo
albelGrupoS = tk.Label(framePacientes, text=" Grupo Sanguíneo:")
albelGrupoS.grid(row=5, column=0, padx=5, pady=5, sticky="w")
entryGrupoS = tk.Entry(framePacientes)
entryGrupoS.grid(row=5, column=1, padx=5, pady=5, sticky="w")
# Tipo de seguro
labelTipoS = tk.Label(framePacientes, text=" Tipo de Seguro:")
labelTipoS.grid(row=6, column=0, padx=5, pady=5, sticky="w")
tipoSeguro = tk.StringVar()
tipoSeguro.set("Público") # Valor por defecto
comboTipoS = ttk.Combobox(framePacientes, values=["Público", "Privado","Ninguno"], textvariable=tipoSeguro)
comboTipoS.grid(row=6, column=1, padx=5, pady=5, sticky="w")
# Tipo de centro médico
labelCentroM = tk.Label(framePacientes, text=" Centro Médico:")
labelCentroM.grid(row=7, column=0, padx=5, pady=5, sticky="w")
centroM = tk.StringVar()
centroM.set("Hospital Central") # Valor por defecto
comboCentroM = ttk.Combobox(framePacientes, values=["Hospital Central", "Clínica Norte","Centro Salud Sur"], textvariable=centroM)
comboCentroM.grid(row=7, column=1, padx=5, pady=5, sticky="w")
# Frame para los botones
btnFrame = tk.Frame(framePacientes)
btnFrame.grid(row=8, column=1, columnspan=2, pady=5, sticky="w")
# Botón registrar 
btnRegistrar = tk.Button(btnFrame, text="Registrar",bg="green", fg="white", command="")
btnRegistrar.grid(row=0, column=0, padx=5)
# Botón Eliminar
btnEliminar = tk.Button(btnFrame, text="Eliminar", bg="red", fg="White", command="")
btnEliminar.grid(row=0, column=1, padx=5)
# Crera Treeview para mostrar los pacientes
treeview = ttk.Treeview(framePacientes, columns=("Nombre","FechaN","Edad", "Género", "GrupoS", "TipoS", "CentroM"), show="headings")
# Definir encabezados
treeview.heading("Nombre", text="Nombre")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Género", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo de Seguro")
treeview.heading("CentroM", text="Centro Médico")
#definir ancho de columnas
treeview.column("Nombre", width=200)    
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50)
treeview.column("Género", width=100)
treeview.column("GrupoS", width=100)
treeview.column("TipoS", width=100)
treeview.column("CentroM", width=150)
#ubicar el treeview en la cuadricula
treeview.grid(row=9, column=0, columnspan=4, padx=5, pady=5)
#Escrolbar vertical
scrollbar = ttk.Scrollbar(framePacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.grid(row=9, column=4, sticky="ns")
# Nombre
labelNombreD = tk.Label(frameDoctores, text="Nombre:")
labelNombreD.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entryNombreD = tk.Entry(frameDoctores)
entryNombreD.grid(row=0, column=1, padx=5, pady=5, sticky="w")
# Especialidad
labelEspecialidadD = tk.Label(frameDoctores, text="Especialidad:")
labelEspecialidadD.grid(row=1, column=0, padx=5, pady=5, sticky="w")
especialidadD = tk.StringVar()
comboEspecialidadD = ttk.Combobox(frameDoctores, values=["Cardiología", "Dermatología", "Neurología", "Pediatría", "Ginecología", "Ortopedia"], textvariable=especialidadD, state="readonly")
comboEspecialidadD.grid(row=1, column=1, padx=5, pady=5, sticky="w")
# Edad
labelEdadD = tk.Label(frameDoctores, text="Edad:")
labelEdadD.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entryEdadD = tk.Spinbox(frameDoctores,from_=0,to=100, width=5)
entryEdadD.grid(row=2, column=1, padx=5, pady=5, sticky="w")
# Teléfono
labelTelefonoD = tk.Label(frameDoctores, text="Teléfono:")
labelTelefonoD.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entryTelefonoD = tk.Entry(frameDoctores)
entryTelefonoD.grid(row=3, column=1, padx=5, pady=5, sticky="w")
# Frame para botones
btnFrameD = tk.Frame(frameDoctores)
btnFrameD.grid(row=4, column=1, columnspan=2, pady=5, sticky="w")

btnRegistrarD = tk.Button(btnFrameD, text="Registrar", bg="green", fg="white")
btnRegistrarD.grid(row=0, column=0, padx=5)
btnEliminarD = tk.Button(btnFrameD, text="Eliminar", bg="red", fg="white")
btnEliminarD.grid(row=0, column=1, padx=5)
# Treeview para mostrar doctores
treeviewD = ttk.Treeview(frameDoctores, columns=("Nombre", "Especialidad", "Edad", "Teléfono"), show="headings")
treeviewD.heading("Nombre", text="Nombre")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Edad", text="Edad")
treeviewD.heading("Teléfono", text="Teléfono")
treeviewD.column("Nombre", width=180)
treeviewD.column("Especialidad", width=140)
treeviewD.column("Edad", width=60)
treeviewD.column("Teléfono", width=120)
treeviewD.grid(row=5, column=0, columnspan=4, padx=5, pady=5)
# Scrollbar vertical para treeview doctores
scrollbarD = ttk.Scrollbar(frameDoctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscroll=scrollbarD.set)
scrollbarD.grid(row=5, column=4, sticky="ns")

ventanaPrincipal.mainloop()