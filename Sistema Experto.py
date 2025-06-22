import os
import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox

# Ramirez Hernandez Ismael
# Alvaro Castillo Jesús Angel
# Campa Quintanar Carlos

# Base de Conocimiento y Hechos
base_conocimiento = {
    "coche": {
        "hechos": {
            "motor_no_enciende": False,
            "bateria_descargada": False,
            "luces_apagan": False,
            "frenos_suenan": False,
            "aire_acondicionado_no_enfria": False,
            "ruido_suspension": False,
            "sobrecalentamiento_motor": False,
        },
        "reglas": [
            {"condiciones": ["motor_no_enciende", "bateria_descargada"], "diagnostico": "La batería del coche necesita ser reemplazada."},
            {"condiciones": ["luces_apagan"], "diagnostico": "El alternador del coche está dañado."},
            {"condiciones": ["frenos_suenan"], "diagnostico": "Los frenos del coche podrían estar desgastados o tener un problema con las pastillas."},
            {"condiciones": ["aire_acondicionado_no_enfria"], "diagnostico": "El aire acondicionado del coche podría estar sin refrigerante o tener un problema con el compresor."},
            {"condiciones": ["ruido_suspension"], "diagnostico": "Problema con la suspensión del coche (amortiguadores, bujes, etc.)."},
            {"condiciones": ["sobrecalentamiento_motor"], "diagnostico": "El motor del coche se está sobrecalentando. Revisa el sistema de enfriamiento."},
        ]
    },
    "moto": {
        "hechos": {
            "motor_no_arranca": False,
            "bateria_baja": False,
            "luces_fallan": False,
            "cadena_suena_extraño": False,
            "frenos_chirrian": False,
            "problema_cambio_marchas": False,
        },
        "reglas": [
            {"condiciones": ["motor_no_arranca", "bateria_baja"], "diagnostico": "La batería de la moto está baja o muerta."},
            {"condiciones": ["luces_fallan"], "diagnostico": "Problema eléctrico en la moto, posiblemente el regulador de voltaje."},
            {"condiciones": ["cadena_suena_extraño"], "diagnostico": "La cadena de la moto necesita ajuste, lubricación o reemplazo."},
            {"condiciones": ["frenos_chirrian"], "diagnostico": "Las pastillas de freno de la moto están desgastadas o necesitan limpieza."},
            {"condiciones": ["problema_cambio_marchas"], "diagnostico": "Problema con el embrague o la transmisión de la moto."},
        ]
    }
}

# Motor de Inferencia
def motor_inferencia(hechos, reglas):
    diagnosticos = []
    for regla in reglas:
        if all(hechos[condicion] for condicion in regla["condiciones"]):
            diagnosticos.append(regla["diagnostico"])
    if not diagnosticos:
        diagnosticos.append("El problema podría estar en otro componente no cubierto por la base de conocimientos.")
    return diagnosticos

# Modulo de comunicaciones
def guardar_diagnostico(descripcion, diagnosticos, tipo_vehiculo):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_path = os.path.join(directorio_actual, "diagnosticos.txt")
    
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo_path, "a") as archivo:
        archivo.write(f"Fecha y hora: {fecha_hora}\n")
        archivo.write(f"Tipo de Vehículo: {tipo_vehiculo.capitalize()}\n")
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

    # Preguntar al usuario si es coche o moto
    tipo_vehiculo = simpledialog.askstring("Tipo de Vehículo", "¿Es un 'coche' o una 'moto'?", initialvalue="coche")
    if not tipo_vehiculo:
        messagebox.showwarning("Advertencia", "Debe seleccionar un tipo de vehículo.")
        return
    
    tipo_vehiculo = tipo_vehiculo.lower()
    if tipo_vehiculo not in base_conocimiento:
        messagebox.showwarning("Advertencia", "Tipo de vehículo no reconocido. Por favor, elija 'coche' o 'moto'.")
        return

    hechos_actuales = base_conocimiento[tipo_vehiculo]["hechos"]
    reglas_actuales = base_conocimiento[tipo_vehiculo]["reglas"]

    descripcion = simpledialog.askstring("Entrada", f"Describe el problema de la {tipo_vehiculo}:")
    if not descripcion:
        messagebox.showwarning("Advertencia", "Debe ingresar una descripción del problema.")
        return

    # Reiniciar hechos para la sesión actual (importante para que no arrastre hechos de ejecuciones anteriores)
    for key in hechos_actuales:
        hechos_actuales[key] = False

    # Detectar hechos basados en la descripción usando frases más coloquiales
    descripcion_lower = descripcion.lower()
    if tipo_vehiculo == "coche":
        hechos_actuales["motor_no_enciende"] = any(phrase in descripcion_lower for phrase in ["motor no enciende", "no arranca el motor", "el carro no prende"])
        hechos_actuales["luces_apagan"] = any(phrase in descripcion_lower for phrase in ["luces se apagan", "las luces fallan", "los focos no prenden"])
        hechos_actuales["frenos_suenan"] = any(phrase in descripcion_lower for phrase in ["frenos suenan", "los frenos chilan", "rechinan los frenos"])
        hechos_actuales["aire_acondicionado_no_enfria"] = any(phrase in descripcion_lower for phrase in ["aire acondicionado no enfria", "el clima no enfría", "no sale aire frío del aire"])
        hechos_actuales["ruido_suspension"] = any(phrase in descripcion_lower for phrase in ["ruido suspension", "ruido en la suspensión", "suena al pasar baches", "golpeteo al andar"])
        hechos_actuales["sobrecalentamiento_motor"] = any(phrase in descripcion_lower for phrase in ["sobrecalentamiento motor", "se calienta el motor", "temperatura alta del motor", "se sube la aguja de la temperatura"])
    elif tipo_vehiculo == "moto":
        hechos_actuales["motor_no_arranca"] = any(phrase in descripcion_lower for phrase in ["motor no arranca", "la moto no prende", "no enciende la moto"])
        hechos_actuales["bateria_baja"] = any(phrase in descripcion_lower for phrase in ["bateria baja", "batería sin carga", "se le acabó la batería"])
        hechos_actuales["luces_fallan"] = any(phrase in descripcion_lower for phrase in ["luces fallan", "las luces de la moto no prenden", "los faros no funcionan"])
        hechos_actuales["cadena_suena_extraño"] = any(phrase in descripcion_lower for phrase in ["cadena suena extraño", "la cadena hace ruido", "suena raro la cadena"])
        hechos_actuales["frenos_chirrian"] = any(phrase in descripcion_lower for phrase in ["frenos chirrian", "los frenos de la moto chillan", "rechinan los frenos de la moto"])
        hechos_actuales["problema_cambio_marchas"] = any(phrase in descripcion_lower for phrase in ["problema cambio marchas", "no entran las marchas", "le cuesta cambiar de velocidad", "se traba el cambio"])

    if not any(hechos_actuales.values()):
        messagebox.showinfo("Diagnóstico", f"Lo siento, no puedo identificar el problema del/la {tipo_vehiculo} basado en la descripción proporcionada.")
        return

    # Preguntas adicionales específicas del vehículo
    if tipo_vehiculo == "coche" and hechos_actuales["motor_no_enciende"]:
        respuesta = simpledialog.askstring("Pregunta", "¿La batería del coche está descargada? (si/no):")
        hechos_actuales["bateria_descargada"] = respuesta and respuesta.lower() == "si"
    elif tipo_vehiculo == "moto" and hechos_actuales["motor_no_arranca"]:
        respuesta = simpledialog.askstring("Pregunta", "¿La batería de la moto está baja? (si/no):")
        hechos_actuales["bateria_baja"] = respuesta and respuesta.lower() == "si"

    diagnosticos = motor_inferencia(hechos_actuales, reglas_actuales)
    
    if not diagnosticos:
        messagebox.showinfo("Diagnóstico", f"Lo siento, no puedo identificar el problema del/la {tipo_vehiculo} basado en la descripción proporcionada.")
        return
    
    resultado = f"Descripción del problema de la {tipo_vehiculo}: {descripcion}\nDiagnóstico(s):\n"
    for diag in diagnosticos:
        resultado += f"- {diag}\n"
    messagebox.showinfo("Diagnóstico", resultado)    

    guardar_diagnostico(descripcion, diagnosticos, tipo_vehiculo)

# Ejecutar el sistema
if __name__ == "__main__":
    interfaz_usuario()
