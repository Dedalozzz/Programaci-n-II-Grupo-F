import tkinter as tk
from tkinter import ttk, messagebox
def guardar_medicamento():
    medicamento = {
        "Nombre": entryNombre.get(),
        "Dosis": entryDosis.get(),
        "Fecha": entryFecha.get(),
        "Observaciones": entryObs.get()
    }
    with open("medicamento.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{medicamento['Nombre']}|{medicamento['Dosis']}|{medicamento['Fecha']}|{medicamento['Observaciones']}\n")
    treeviewMedicamentos.insert("", "end", values=(medicamento['Nombre'], medicamento['Dosis'], medicamento['Fecha'], medicamento['Observaciones']))


def cargar_medicamentos():
    try:
        with open("medicamento.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:
                    treeviewMedicamentos.insert("", "end", values=tuple(datos))
    except FileNotFoundError:
        open("medicamento.txt", "w", encoding="utf-8").close()


def eliminar_medicamento():
    seleccionado = treeviewMedicamentos.selection()
    if seleccionado:
        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar el medicamento seleccionado?")
        if respuesta:
            treeviewMedicamentos.delete(seleccionado[0])
            # Actualizar archivo
            medicamentos = []
            for item in treeviewMedicamentos.get_children():
                medicamentos.append(treeviewMedicamentos.item(item)["values"])
            with open("medicamento.txt", "w", encoding="utf-8") as archivo:
                for med in medicamentos:
                    archivo.write("|".join(str(campo) for campo in med) + "\n")
    else:
        messagebox.showwarning("Eliminar", "Selecciona un medicamento para eliminar.")

def enmascarar_fecha(event=None):
    texto = entryFecha.get()
    limpio = ''.join(filter(str.isdigit, texto))
    formato_final = ""
    if len(limpio) > 8:
        limpio = limpio[:8]
    if len(limpio) > 4:
        formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final = limpio
    if entryFecha.get() != formato_final:
        entryFecha.delete(0, tk.END)
        entryFecha.insert(0, formato_final)

# Interfaz
ventana = tk.Tk()
ventana.title("Registro de Medicamentos")
ventana.geometry("890x400")
ventana.configure(bg="#0E6582")

frameForm = tk.Frame(ventana, bg="#0E6582")
frameForm.pack(pady=10)

# Campos del formulario
labelNombre = tk.Label(frameForm, text="Nombre:", bg="#0E6582", fg="white")
labelNombre.grid(row=0, column=0, padx=5, pady=5)
entryNombre = tk.Entry(frameForm)
entryNombre.grid(row=0, column=1, padx=5, pady=5)

labelDosis = tk.Label(frameForm, text="Dosis:", bg="#0E6582", fg="white")
labelDosis.grid(row=1, column=0, padx=5, pady=5)
entryDosis = tk.Entry(frameForm)
entryDosis.grid(row=1, column=1, padx=5, pady=5)

labelFecha = tk.Label(frameForm, text="Fecha:", bg="#0E6582", fg="white")
labelFecha.grid(row=2, column=0, padx=5, pady=5)
entryFecha = tk.Entry(frameForm)

entryFecha.grid(row=2, column=1, padx=5, pady=5)
entryFecha.bind('<KeyRelease>', enmascarar_fecha)

labelObs = tk.Label(frameForm, text="Observaciones:", bg="#0E6582", fg="white")
labelObs.grid(row=3, column=0, padx=5, pady=5)
entryObs = tk.Entry(frameForm)
entryObs.grid(row=3, column=1, padx=5, pady=5)

# Botones
frameBotones = tk.Frame(ventana, bg="#0E6582")
frameBotones.pack(pady=10)

btnGuardar = tk.Button(frameBotones, text="Guardar", bg="#0E6582", fg="white", command=guardar_medicamento)
btnGuardar.grid(row=0, column=0, padx=10)

btnEliminar = tk.Button(frameBotones, text="Eliminar", bg="#0E6582", fg="white", command=eliminar_medicamento)
btnEliminar.grid(row=0, column=1, padx=10)

# Treeview
treeviewMedicamentos = ttk.Treeview(ventana, columns=("Nombre", "Dosis", "Fecha", "Observaciones"), show="headings")
treeviewMedicamentos.heading("Nombre", text="Nombre")
treeviewMedicamentos.heading("Dosis", text="Dosis")
treeviewMedicamentos.heading("Fecha", text="Fecha")
treeviewMedicamentos.heading("Observaciones", text="Observaciones")
treeviewMedicamentos.column("Nombre", width=200)
treeviewMedicamentos.column("Dosis", width=90)
treeviewMedicamentos.column("Fecha", width=80)
treeviewMedicamentos.column("Observaciones", width=350)
treeviewMedicamentos.pack(padx=10, pady=10, fill="x")

cargar_medicamentos()
ventana.mainloop()
