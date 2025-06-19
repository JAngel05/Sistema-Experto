import os
import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox


#Ramirez Hernandez Ismael
# Base de Conocimiento y Hechos
hechos = {
    "motor_no_enciende": False,
    "bateria_descargada": False,
    "luces_apagan": False,
    "frenos_suenan": False,
    "aire_acondicionado_no_enfria": False,
}

reglas = [
    {"condiciones": ["motor_no_enciende", "bateria_descargada"], "diagnostico": "La batería necesita ser reemplazada"},
    {"condiciones": ["luces_apagan"], "diagnostico": "El alternador está dañado"},
    {"condiciones": ["frenos_suenan"], "diagnostico": "Los frenos podrían estar desgastados o tener un problema con las pastillas"},
    {"condiciones": ["aire_acondicionado_no_enfria"], "diagnostico": "El aire acondicionado podría estar sin refrigerante o tener un problema con el compresor"},
]

# Motor de Inferencia
def motor_inferencia(hechos, reglas):
    diagnosticos = []
    for regla in reglas:
        if all(hechos[condicion] for condicion in regla["condiciones"]):
            diagnosticos.append(regla["diagnostico"])
    if not diagnosticos:
        diagnosticos.append("El problema podría estar en otro componente.")
    return diagnosticos

# Modulo de comunicaciones
def guardar_diagnostico(descripcion, diagnosticos):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_path = os.path.join(directorio_actual, "diagnosticos.txt")
    
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo_path, "a") as archivo:
        archivo.write(f"Fecha y hora: {fecha_hora}\n")
        archivo.write(f"Problema: {descripcion}\n")
        archivo.write("Diagnósticos:\n")
        for diag in diagnosticos:
            archivo.write(f"- {diag}\n")
        archivo.write("\n")
    messagebox.showinfo("Guardado", f"El diagnóstico se guardó en el archivo {archivo_path}.")

# Interfaz de Usuario
def interfaz_usuario():
    ventana = tk.Tk()
    ventana.withdraw()
    descripcion = simpledialog.askstring("Entrada", "Describe el problema del automóvil:")
    if not descripcion:
        messagebox.showwarning("Advertencia", "Debe ingresar una descripción del problema.")
        return    
    hechos["motor_no_enciende"] = "motor no enciende" in descripcion.lower()
    hechos["luces_apagan"] = "luces se apagan" in descripcion.lower()
    hechos["frenos_suenan"] = "frenos suenan" in descripcion.lower()
    hechos["aire_acondicionado_no_enfria"] = "aire acondicionado no enfria" in descripcion.lower()
    
    if not any(hechos.values()):
        messagebox.showinfo("Diagnóstico", "Lo siento, no puedo identificar el problema basado en la descripción proporcionada.")
        return

    if hechos["motor_no_enciende"]:
        respuesta = simpledialog.askstring("Pregunta", "¿La batería está descargada? (si/no):")
        hechos["bateria_descargada"] = respuesta and respuesta.lower() == "si"

    diagnosticos = motor_inferencia(hechos, reglas)
    if not diagnosticos:
        messagebox.showinfo("Diagnóstico", "Lo siento, no puedo identificar el problema basado en la descripción proporcionada.")
        return    
    resultado = f"Descripción del problema: {descripcion}\nDiagnóstico(s):\n"
    for diag in diagnosticos:
        resultado += f"- {diag}\n"
    messagebox.showinfo("Diagnóstico", resultado)    

    guardar_diagnostico(descripcion, diagnosticos)
# Ejecutar el sistema
if __name__ == "__main__":
    interfaz_usuario()
