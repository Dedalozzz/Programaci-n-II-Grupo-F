# Importación de librerías
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
#funcion para registrar doctor
def registrar_doctor():
    doctor = {
        "Nombre": entryNombreD.get(),
        "Especialidad": especialidadD.get(),
        "Edad": entryEdadD.get(),
        "Teléfono": entryTelefonoD.get()
    }
    doctores_data.append(doctor)
    guardar_doctores_en_archivo()
    treeviewD.insert("", "end", values=(doctor["Nombre"], doctor["Especialidad"], doctor["Edad"], doctor["Teléfono"]))
#funcion para eliminar paciente
def eliminar_paciente():
    seleccionado = treeview.selection()
    if seleccionado:
        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar el paciente seleccionado?")#pregunta si esta seguro de la eleccion
        if respuesta:
            idx = int(seleccionado[0])
            del pacientes_data[idx]
            messagebox.showinfo("Eliminar Paciente","Paciente eliminado correctamente")
            guardar_en_archivo()#Guarda los cambios en el archivo
            cargar_treeview()
    else:
        messagebox.showwarning("Eliminar", "Selecciona un paciente para eliminar.")#opcion default si no hay nada seleccionado
#funcion para guardar doctores
def guardar_doctores_en_archivo():
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(
                f"{doctor['Nombre']}|"
                f"{doctor['Especialidad']}|"
                f"{doctor['Edad']}|"
                f"{doctor['Teléfono']}\n"
            )

def cargar_doctores_desde_archivo():
    doctores_data.clear()
    try:
        with open("doctores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:
                    doctor = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Edad": datos[2],
                        "Teléfono": datos[3]
                    }
                    doctores_data.append(doctor)
        treeviewD.delete(*treeviewD.get_children())
        for doctor in doctores_data:
            treeviewD.insert("", "end", values=(doctor["Nombre"], doctor["Especialidad"], doctor["Edad"], doctor["Teléfono"]))
    except FileNotFoundError:
        open("doctores.txt", "w", encoding="utf-8").close()
#funcion para eliminar doctor
def eliminar_doctor():
    seleccionado = treeviewD.selection()
    if seleccionado:
        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar el doctor seleccionado?")
        if respuesta:
            idx = treeviewD.index(seleccionado[0])
            del doctores_data[idx]
            guardar_doctores_en_archivo()
            treeviewD.delete(seleccionado[0])
    else:
        messagebox.showwarning("Eliminar", "Selecciona un doctor para eliminar.")
#funcion para enmascarar fecha
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=""
 
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
 
    if fechaN.get() !=formato_final:
        fechaN.delete(0, tk.END)
        fechaN.insert(0, formato_final)
 
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year - fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
def guardar_en_archivo():
    with open("pacientes.txt", "w" , encoding="utf-8") as archivo:
        for paciente in pacientes_data:
            archivo.write(f"{paciente['Nombre']}|{paciente['Fecha de nacimiento']}|{paciente['Edad']}|"
             f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|"
             f"{paciente['Tipo de Seguro']}|{paciente['Centro Medico']}\n")            
#lista de pacientes
pacientes_data=[]
def cargar_treeview():
    #limpiar treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #insertar cada pacientes 
    for i, item in enumerate(pacientes_data):
        treeview.insert(
        "","end",id=str(i),
           values=(
            item["Nombre"],
            item["Fecha de nacimiento"],
            item["Edad"],
            item["Genero"],
            item["Grupo Sanguineo"],
            item["Tipo de Seguro"],
            item["Centro Medico"]
            ) 
         )
#cargar desde archivo pacientes
def cargar_desde_archivo_pacientes():
    try:
        with open("pacientes.txt", "r", encoding="utf-8") as archivo:
            pacientes_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 7:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de nacimiento": datos[1],
                        "Edad": datos[2],
                        "Genero": datos[3],
                        "Grupo Sanguineo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Medico": datos[6]
                    }
                    pacientes_data.append(paciente)
            cargar_treeview()
    except FileNotFoundError:    
        open("pacientes.txt", "w", encoding="utf-8").close()
#cargar datos al iniciar
def registrar_paciente():
    #crea un diccionario con los datos del paciente
    paciente={
        "Nombre": nombreP.get(),
        "Fecha de nacimiento": fechaN.get(),
        "Edad": edadVar.get(),
        "Genero": genero.get(),
        "Grupo Sanguineo": entryGrupoS.get(),
        "Tipo de Seguro": tipoSeguro.get(), 
        "Centro Medico": centroM.get()
    }
    #agregar paciente a la lista
    pacientes_data.append(paciente)
    #llamar a guardar en archivo
    guardar_en_archivo()
    #Cargar treeview para mostrar los datos guardados
    cargar_treeview()

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
validacion_fecha=ventanaPrincipal.register(enmascarar_fecha)
fechaN = ttk.Entry(framePacientes, validate="key", validatecommand=(validacion_fecha, '%P'))
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="w")
# Edad (readonly)
labelEdad = tk.Label(framePacientes, text=" Edad:")
labelEdad.grid(row=2, column=0, padx=5, pady=5, sticky="w")
edadVar=tk.StringVar()
edadP = tk.Entry(framePacientes, textvariable=edadVar, state="readonly")
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
labelGrupoS = tk.Label(framePacientes, text=" Grupo Sanguíneo:")
labelGrupoS.grid(row=5, column=0, padx=5, pady=5, sticky="w")
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
btnRegistrar = tk.Button(btnFrame, text="Registrar", bg="green", fg="white", command=registrar_paciente)
btnRegistrar.grid(row=0, column=0, padx=5)
# Botón Eliminar
btnEliminar = tk.Button(btnFrame, text="Eliminar", bg="red", fg="White", command=eliminar_paciente)
btnEliminar.grid(row=0, column=1, padx=5)
# Crear Treeview para mostrar los pacientes
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

btnRegistrarD = tk.Button(btnFrameD, text="Registrar", bg="green", fg="white", command=registrar_doctor)
btnRegistrarD.grid(row=0, column=0, padx=5)
btnEliminarD = tk.Button(btnFrameD, text="Eliminar", bg="red", fg="white", command=eliminar_doctor)
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
doctores_data = []
scrollbarD = ttk.Scrollbar(frameDoctores, orient="vertical", command=treeviewD.yview)
treeviewD.configure(yscroll=scrollbarD.set)
scrollbarD.grid(row=5, column=4, sticky="ns")
cargar_desde_archivo_pacientes()#guarda los datos en un txt
cargar_doctores_desde_archivo()#muestra los doctores guardados en el treeview
# Iniciar el bucle principal de la interfaz
ventanaPrincipal.mainloop()