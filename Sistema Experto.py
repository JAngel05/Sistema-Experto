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
            "aceite_bajo": False,
            "escape_humoso": False,
            "vibracion_volante": False,
        },
        "reglas": [
            {"condiciones": ["motor_no_enciende", "bateria_descargada"], "diagnostico": "El sistema de arranque no recibe suficiente energía. Se recomienda verificar el estado de la batería y el sistema de carga (alternador)."},
            {"condiciones": ["luces_apagan"], "diagnostico": "La disminución de intensidad o el apagado de las luces indican una posible falla en el alternador o un problema con el regulador de voltaje. Inspeccione el sistema eléctrico."},
            {"condiciones": ["frenos_suenan"], "diagnostico": "Ruido al frenar sugiere desgaste avanzado de las pastillas de freno, discos deformados o la presencia de contaminantes. Es crucial una inspección profesional del sistema de frenado."},
            {"condiciones": ["aire_acondicionado_no_enfria"], "diagnostico": "La falta de enfriamiento del aire acondicionado puede deberse a una fuga de refrigerante, un compresor defectuoso o un problema en el sistema de climatización. Se aconseja una revisión especializada."},
            {"condiciones": ["ruido_suspension"], "diagnostico": "Ruidos inusuales en la suspensión (golpeteos, crujidos) a menudo indican componentes desgastados como amortiguadores, bujes, rótulas o terminales de dirección. Un diagnóstico detallado es necesario para identificar el origen exacto."},
            {"condiciones": ["sobrecalentamiento_motor"], "diagnostico": "El sobrecalentamiento del motor es crítico. Puede ser causado por un nivel bajo de refrigerante, un termostato defectuoso, una bomba de agua averiada o un radiador obstruido. Detenga el vehículo de inmediato y revise el sistema de enfriamiento."},
            {"condiciones": ["aceite_bajo"], "diagnostico": "Un nivel bajo de aceite del motor puede provocar un desgaste excesivo de los componentes internos. Verifique inmediatamente el nivel y rellene con el tipo de aceite recomendado. Si el consumo es recurrente, investigue posibles fugas o problemas internos."},
            {"condiciones": ["escape_humoso"], "diagnostico": "El color del humo del escape es indicativo: humo azulado sugiere quema de aceite, humo blanco persistente puede ser refrigerante, y humo negro indica una combustión rica. Esto requiere una evaluación del motor y el sistema de escape."},
            {"condiciones": ["vibracion_volante"], "diagnostico": "La vibración en el volante, especialmente a ciertas velocidades, comúnmente indica un desequilibrio en las ruedas, problemas de alineación o, en casos más graves, componentes de la dirección o suspensión dañados."},
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
            "pata_apoyo_no_funciona": False,
            "consumo_excesivo": False,
            "falla_encendido": False,
        },
        "reglas": [
            {"condiciones": ["motor_no_arranca", "bateria_baja"], "diagnostico": "El motor no arranca debido a una batería con carga insuficiente o defectuosa. Revise las conexiones de la batería y su voltaje, y considere la recarga o reemplazo."},
            {"condiciones": ["luces_fallan"], "diagnostico": "La intermitencia o inoperatividad de las luces sugiere una falla en el sistema eléctrico, posiblemente el regulador/rectificador, el estator o conexiones sueltas. Es necesaria una inspección del circuito eléctrico."},
            {"condiciones": ["cadena_suena_extraño"], "diagnostico": "Un ruido anómalo en la cadena (golpeteo, chirrido) indica una tensión incorrecta, falta de lubricación, desgaste excesivo de la cadena o los piñones. Requiere ajuste, limpieza y lubricación, o posible reemplazo del kit de arrastre."},
            {"condiciones": ["frenos_chirrian"], "diagnostico": "El chirrido de los frenos de la moto puede ser causado por pastillas de freno desgastadas, discos sucios o cristalizados, o un desajuste. Se recomienda una revisión y limpieza del sistema de frenado."},
            {"condiciones": ["problema_cambio_marchas"], "diagnostico": "Dificultad al cambiar marchas o marchas que se saltan pueden indicar un problema con el embrague (ajuste, desgaste) o componentes internos de la transmisión. Es aconsejable una evaluación del sistema de embrague y caja de cambios."},
            {"condiciones": ["pata_apoyo_no_funciona"], "diagnostico": "Si la pata de apoyo no se despliega o no se mantiene correctamente, podría ser un problema con el mecanismo, el resorte o un sensor de seguridad que impide el arranque. Verifique el mecanismo y cualquier sensor asociado."},
            {"condiciones": ["consumo_excesivo"], "diagnostico": "Un consumo de combustible inusualmente alto puede ser síntoma de un carburador desajustado, inyectores sucios, filtro de aire obstruido o problemas en el sistema de encendido. Se sugiere una revisión del sistema de alimentación."},
            {"condiciones": ["falla_encendido"], "diagnostico": "Dificultad para encender la moto indica posibles fallos en las bujías, el sistema de encendido (bobina, CDI) o el suministro de combustible. Revise estos componentes para asegurar una chispa y mezcla adecuadas."},
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
        diagnosticos.append("El problema podría estar en otro componente no cubierto por la base de conocimientos o requiere una evaluación más profunda por un especialista.")
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

# Interfaz de Usuario (actualizada con detección de nuevos problemas)
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

    # Reiniciar hechos para la sesión actual
    for key in hechos_actuales:
        hechos_actuales[key] = False

    # Detectar hechos basados en la descripción
    descripcion_lower = descripcion.lower()
    if tipo_vehiculo == "coche":
        hechos_actuales["motor_no_enciende"] = any(phrase in descripcion_lower for phrase in ["motor no enciende", "no arranca el motor", "el carro no prende"])
        hechos_actuales["luces_apagan"] = any(phrase in descripcion_lower for phrase in ["luces se apagan", "las luces fallan", "los focos no prenden"])
        hechos_actuales["frenos_suenan"] = any(phrase in descripcion_lower for phrase in ["frenos suenan", "los frenos chilan", "rechinan los frenos"])
        hechos_actuales["aire_acondicionado_no_enfria"] = any(phrase in descripcion_lower for phrase in ["aire acondicionado no enfria", "el clima no enfría", "no sale aire frío del aire"])
        hechos_actuales["ruido_suspension"] = any(phrase in descripcion_lower for phrase in ["ruido suspension", "ruido en la suspensión", "suena al pasar baches", "golpeteo al andar"])
        hechos_actuales["sobrecalentamiento_motor"] = any(phrase in descripcion_lower for phrase in ["sobrecalentamiento motor", "se calienta el motor", "temperatura alta del motor", "se sube la aguja de la temperatura"])
        hechos_actuales["aceite_bajo"] = any(phrase in descripcion_lower for phrase in ["aceite bajo", "nivel de aceite bajo", "poco aceite", "luce de aceite encendida"])
        hechos_actuales["escape_humoso"] = any(phrase in descripcion_lower for phrase in ["escape humoso", "humo del escape", "sale humo del tubo", "escape echa humo"])
        hechos_actuales["vibracion_volante"] = any(phrase in descripcion_lower for phrase in ["vibracion volante", "vibra el volante", "steering wheel shakes", "vibra al conducir"])
        
    elif tipo_vehiculo == "moto":
        hechos_actuales["motor_no_arranca"] = any(phrase in descripcion_lower for phrase in ["motor no arranca", "la moto no prende", "no enciende la moto"])
        hechos_actuales["bateria_baja"] = any(phrase in descripcion_lower for phrase in ["bateria baja", "batería sin carga", "se le acabó la batería"])
        hechos_actuales["luces_fallan"] = any(phrase in descripcion_lower for phrase in ["luces fallan", "las luces de la moto no prenden", "los faros no funcionan"])
        hechos_actuales["cadena_suena_extraño"] = any(phrase in descripcion_lower for phrase in ["cadena suena extraño", "la cadena hace ruido", "suena raro la cadena"])
        hechos_actuales["frenos_chirrian"] = any(phrase in descripcion_lower for phrase in ["frenos chirrian", "los frenos de la moto chillan", "rechinan los frenos de la moto"])
        hechos_actuales["problema_cambio_marchas"] = any(phrase in descripcion_lower for phrase in ["problema cambio marchas", "no entran las marchas", "le cuesta cambiar de velocidad", "se traba el cambio"])
        hechos_actuales["pata_apoyo_no_funciona"] = any(phrase in descripcion_lower for phrase in ["pata apoyo no funciona", "no funciona la pata", "problema con el caballete", "sensor de pata falla"])
        hechos_actuales["consumo_excesivo"] = any(phrase in descripcion_lower for phrase in ["consumo excesivo", "gasta mucha gasolina", "alto consumo combustible", "rendimiento bajo"])
        hechos_actuales["falla_encendido"] = any(phrase in descripcion_lower for phrase in ["falla encendido", "problema al encender", "no prende bien", "tarda en arrancar"])

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