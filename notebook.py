import tkinter as tk
from tkinter import ttk as tkk
#creacion de una ventana
ventana_principal = tk.Tk()
ventana_principal.title("Libro de pacientes y Doctores")
ventana_principal.geometry("800x600")
#Crear contenedor
Pestanas = tkk.Notebook(ventana_principal)
#crear los frames
frame_pacientes = tkk.Frame(Pestanas)
#agregar pestañas al notebook
Pestanas.add(frame_pacientes, text="Pacientes")

#mostrar pestañas
Pestanas.pack(expand=True, fill="both")
#crear segundo frame
Pestanas.add(tkk.Frame(Pestanas), text="Doctores")

#mostrar la ventana
Pestanas.pack(expand=True, fill="both")
#Nombre 
label_nombre = tkk.Label(frame_pacientes, text="Nombre Completo")
label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="W")
nombreP= tkk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, padx=5, pady=5, sticky="W")
#Fecha de nacimiento
label_fechaN = tkk.Label(frame_pacientes, text="Fecha de Nacimiento")
label_fechaN.grid(row=1, column=0, padx=5, pady=5, sticky="W")
fechaN= tkk.Entry(frame_pacientes)
fechaN.grid(row=1, column=1, padx=5, pady=5, sticky="W")
#Edad (readonly)
label_edad = tkk.Label(frame_pacientes, text="Edad")
label_edad.grid(row=2, column=0, padx=5, pady=5, sticky="W")
edadP= tkk.Entry(frame_pacientes)
edadP.grid(row=2, column=1, padx=5, pady=5, sticky="W")
#genero
label_genero = tkk.Label(frame_pacientes, text="Género")    
label_genero.grid(row=3, column=0, padx=5, pady=5, sticky="W")
genero=tk.StringVar()
genero.set("Masculino")
RadioMasculino = tkk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
RadioMasculino.grid(row=3, column=1, padx=5, pady=5, sticky="W")
RadioFemenino = tkk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
RadioFemenino.grid(row=3, column=2, padx=5, pady=5, sticky="W")
#Grupo sanguineo
label_grupoSanguineo = tkk.Label(frame_pacientes, text="Grupo Sanguíneo")
label_grupoSanguineo.grid(row=4, column=0, padx=5, pady=5, sticky="W")
entry_grupoSanguineo= tkk.Entry(frame_pacientes)
entry_grupoSanguineo.grid(row=4, column=1, padx=5, pady=5, sticky="W")
#tipo de seguro
labeltipoSeguro = tkk.Label(frame_pacientes, text="Tipo de Seguro")
labeltipoSeguro.grid(row=5, column=0, padx=5, pady=5, sticky="W")
tiposeguro=tk.StringVar()
tiposeguro.set("Público")
ComboTipoSeguro = tkk.Combobox(frame_pacientes, textvariable=tiposeguro)
ComboTipoSeguro["values"]=("Público", "Privado", "Ninguno")
ComboTipoSeguro.grid(row=5, column=1, padx=5, pady=5, sticky="W")
#Centro medico
labelcentroMedico = tkk.Label(frame_pacientes, text="Centro de salud")
labelcentroMedico.grid(row=6, column=0, padx=5, pady=5, sticky="W")
centroMedico=tk.StringVar()
centroMedico.set("Hospital Central")
comboCentroMedico = tkk.Combobox(frame_pacientes, textvariable=centroMedico)
comboCentroMedico["values"]=("Hospital Central", "Clínica Norte", "Centro Sur")
comboCentroMedico.grid(row=6, column=1, padx=5, pady=5, sticky="W")
ventana_principal.mainloop()