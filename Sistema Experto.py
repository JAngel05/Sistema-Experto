import os
import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

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
            "pierde_potencia": False,
            "consumo_combustible_alto": False,
            "testigo_encendido": False,
        },
        "reglas": [
            {"condiciones": ["motor_no_enciende", "bateria_descargada"], "diagnostico": "Diagnóstico: **Fallo en el sistema de arranque por descarga de batería.** Se recomienda verificar la salud de la batería, las conexiones de los terminales y el alternador para asegurar una carga adecuada. Considera una prueba de carga de la batería."},
            {"condiciones": ["motor_no_enciende"], "diagnostico": "Diagnóstico: **Anomalía en el sistema de encendido o suministro de combustible.** Podría deberse a problemas con el motor de arranque, fallas en las bujías/bobinas, obstrucción en el sistema de combustible (bomba, filtro), o un sensor de cigüeñal/árbol de levas defectuoso. Se requiere una revisión del sistema de encendido y combustible."},
            {"condiciones": ["luces_apagan"], "diagnostico": "Diagnóstico: **Deficiencia en el sistema de carga del vehículo.** Esto suele indicar un alternador defectuoso, una correa de accesorios dañada, o un problema con el regulador de voltaje. Es crucial inspeccionar el alternador y el cableado eléctrico."},
            {"condiciones": ["frenos_suenan"], "diagnostico": "Diagnóstico: **Desgaste avanzado o irregularidad en el sistema de frenado.** El chirrido o rechinido puede ser causado por pastillas de freno desgastadas, discos de freno deformados o contaminados, o pinzas de freno con problemas. Es imperativo una inspección detallada de todo el conjunto de frenos."},
            {"condiciones": ["aire_acondicionado_no_enfria"], "diagnostico": "Diagnóstico: **Disminución de eficiencia en el sistema de climatización.** Las causas comunes incluyen bajo nivel de refrigerante (por fuga), un compresor de A/C inoperativo, un condensador obstruido, o un problema en el sistema de control climático. Se debe realizar una prueba de fugas y verificar la presión del sistema."},
            {"condiciones": ["ruido_suspension"], "diagnostico": "Diagnóstico: **Deterioro o holgura en los componentes de la suspensión.** Ruido al pasar baches o irregularidades sugiere problemas con amortiguadores/struts, bujes de horquilla, rótulas o barras estabilizadoras. Una inspección visual y funcional de los componentes de la suspensión es necesaria."},
            {"condiciones": ["sobrecalentamiento_motor"], "diagnostico": "Diagnóstico: **Ineficiencia térmica del motor.** Esto indica un problema crítico en el sistema de enfriamiento, como un termostato defectuoso, una bomba de agua averiada, un radiador obstruido, un ventilador inoperativo o un bajo nivel de refrigerante. Se debe investigar la causa del sobrecalentamiento inmediatamente para evitar daños mayores."},
            {"condiciones": ["aceite_bajo"], "diagnostico": "Diagnóstico: **Nivel insuficiente de lubricante en el motor.** Es vital verificar el nivel de aceite y rellenar. Si persiste, podría indicar una fuga de aceite (sellos, empaques) o un consumo excesivo de aceite por parte del motor, lo que requeriría una investigación más profunda."},
            {"condiciones": ["escape_humoso"], "diagnostico": "Diagnóstico: **Combustión incompleta o problemas internos del motor/sistema de escape.** El color del humo es indicativo: humo azul sugiere quema de aceite; humo blanco persistente, refrigerante; humo negro, mezcla rica de combustible. Se recomienda un diagnóstico del motor y el sistema de escape."},
            {"condiciones": ["vibracion_volante"], "diagnostico": "Diagnóstico: **Desequilibrio o desalineación en el sistema de dirección/ruedas.** La vibración a ciertas velocidades generalmente se debe a un balanceo deficiente de los neumáticos, problemas de alineación de la dirección, o componentes de la suspensión/dirección desgastados como rótulas o terminales de dirección."},
            {"condiciones": ["pierde_potencia"], "diagnostico": "Diagnóstico: **Restricción en el rendimiento del motor.** Esto puede ser causado por problemas en el suministro de combustible (bomba, inyectores, filtro), sistema de encendido, filtro de aire obstruido, convertidor catalítico tapado, o sensores del motor defectuosos (MAF, O2)."},
            {"condiciones": ["consumo_combustible_alto"], "diagnostico": "Diagnóstico: **Eficiencia de combustible comprometida.** Las causas pueden incluir inyectores sucios/defectuosos, bujías desgastadas, filtro de aire sucio, sensor de oxígeno defectuoso, presión incorrecta de los neumáticos, o hábitos de conducción agresivos. Se sugiere una revisión de los sistemas de inyección y encendido."},
            {"condiciones": ["testigo_encendido"], "diagnostico": "Diagnóstico: **Activación del sistema de diagnóstico a bordo (OBD-II).** Un testigo en el tablero (ej. Check Engine) indica un código de error específico. Es fundamental realizar un escaneo de códigos de diagnóstico (DTCs) para identificar la causa raíz precisa del problema."},
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
            "ruido_motor_extraño": False,
            "fuga_liquido": False,
            "amortiguacion_mala": False,
        },
        "reglas": [
            {"condiciones": ["motor_no_arranca", "bateria_baja"], "diagnostico": "Diagnóstico: **Insuficiencia energética para el encendido.** La batería de la moto está baja o muerta. Se debe verificar la carga de la batería, el estado de los terminales y el funcionamiento del sistema de carga (estator, regulador/rectificador)."},
            {"condiciones": ["motor_no_arranca"], "diagnostico": "Diagnóstico: **Disfunción en el sistema de ignición o alimentación.** Posibles causas incluyen bujía defectuosa, problemas en el sistema de combustible (carburador/inyección, filtro), interruptor de encendido o sensor del caballete lateral. Es necesaria una revisión del circuito de arranque y encendido."},
            {"condiciones": ["luces_fallan"], "diagnostico": "Diagnóstico: **Anomalía en el circuito eléctrico de iluminación.** Esto puede ser indicativo de un regulador de voltaje defectuoso, un estator con problemas, fusibles quemados o cableado deteriorado. Se recomienda una revisión eléctrica exhaustiva."},
            {"condiciones": ["cadena_suena_extraño"], "diagnostico": "Diagnóstico: **Desgaste, falta de mantenimiento o tensión incorrecta en la transmisión final.** La cadena de la moto necesita ajuste, lubricación o reemplazo si está muy estirada o con eslabones rígidos. También se deben inspeccionar los piñones de arrastre y corona."},
            {"condiciones": ["frenos_chirrian"], "diagnostico": "Diagnóstico: **Desgaste de componentes de fricción o contaminación en el sistema de frenado.** Las pastillas de freno pueden estar desgastadas al límite, sucias, o los discos pueden presentar irregularidades. Se requiere una inspección y posiblemente limpieza/reemplazo de las pastillas y discos."},
            {"condiciones": ["problema_cambio_marchas"], "diagnostico": "Diagnóstico: **Deficiencia en el mecanismo de transmisión o embrague.** Podría haber un problema con el embrague (cable, líquido, discos), la palanca de cambios doblada, el selector de marchas o incluso la propia transmisión interna. Se necesita una evaluación del sistema de cambio."},
            {"condiciones": ["pata_apoyo_no_funciona"], "diagnostico": "Diagnóstico: **Fallo en el sistema de seguridad del caballete lateral.** La pata de apoyo puede tener un sensor defectuoso que impide el arranque o un mecanismo atascado. Se debe revisar el sensor de seguridad y el pivote del caballete."},
            {"condiciones": ["consumo_excesivo"], "diagnostico": "Diagnóstico: **Optimización deficiente del consumo de combustible.** Las causas pueden ser un carburador desajustado, inyectores sucios, filtro de aire obstruido, bujía incorrecta o desgastada, o un sensor de oxígeno defectuoso. Se recomienda un ajuste o limpieza del sistema de alimentación."},
            {"condiciones": ["falla_encendido"], "diagnostico": "Diagnóstico: **Irregularidad en el proceso de combustión inicial.** Esto puede deberse a bujías en mal estado, bobinas de encendido defectuosas, problemas en el cableado de alta tensión o una mezcla aire-combustible inadecuada. Se requiere una revisión del sistema de encendido y combustible."},
            {"condiciones": ["ruido_motor_extraño"], "diagnostico": "Diagnóstico: **Anomalía mecánica interna del motor.** Ruidos inusuales (golpeteo, tintineo) pueden indicar problemas graves como válvulas desajustadas, cojinetes de biela/cigüeñal desgastados, tensor de cadena de distribución defectuoso, o daños en los pistones. Es imprescindible un diagnóstico profesional y urgente."},
            {"condiciones": ["fuga_liquido"], "diagnostico": "Diagnóstico: **Compromiso en la integridad de los sistemas de fluidos.** La fuga de líquido puede ser de aceite de motor/transmisión, refrigerante, líquido de frenos o hidráulico. Es crucial identificar la fuente y el tipo de líquido para determinar la reparación necesaria (empaques, mangueras, sellos)."},
            {"condiciones": ["amortiguacion_mala"], "diagnostico": "Diagnóstico: **Degradación del rendimiento del sistema de suspensión.** La sensación de rebote excesivo, falta de estabilidad o ruidos al absorber impactos indica amortiguadores/horquillas desgastadas, fugas de aceite en las barras, o ajustes incorrectos. Se recomienda una revisión y posible mantenimiento/reemplazo de los componentes de la suspensión."},
        ]
    }
}

# Motor de Inferencia
def motor_inferencia(hechos, reglas):
    diagnosticos = []
    
    # Priorizar reglas con más condiciones coincidentes para diagnósticos más específicos
    reglas_coincidentes = []
    for regla in reglas:
        condiciones_cumplidas = [hechos.get(condicion, False) for condicion in regla["condiciones"]]
        if all(condiciones_cumplidas):
            reglas_coincidentes.append((len(regla["condiciones"]), regla["diagnostico"]))
    
    # Ordenar por número de condiciones (más condiciones = más específico)
    reglas_coincidentes.sort(key=lambda x: x[0], reverse=True)

    # Añadir los diagnósticos únicos
    diagnosticos_añadidos = set()
    for _, diag in reglas_coincidentes:
        if diag not in diagnosticos_añadidos:
            diagnosticos.append(diag)
            diagnosticos_añadidos.add(diag)
    
    if not diagnosticos:
        diagnosticos.append("Diagnóstico: **No se encontraron correspondencias directas en la base de conocimientos.** El problema descrito no coincide con las reglas predefinidas o puede ser una combinación inusual de síntomas. Se recomienda una inspección visual y un diagnóstico manual por un técnico calificado.")
    
    return diagnosticos

# Modulo de comunicaciones
def guardar_diagnostico(descripcion, diagnosticos, tipo_vehiculo):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_path = os.path.join(directorio_actual, "diagnosticos.txt")
    
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo_path, "a") as archivo:
        archivo.write(f"Fecha y hora: {fecha_hora}\n")
        archivo.write(f"Tipo de Vehículo: {tipo_vehiculo.capitalize()}\n")
        archivo.write(f"Problema Reportado: {descripcion}\n")
        archivo.write("Resultados del Diagnóstico:\n")
        for diag in diagnosticos:
            archivo.write(f"- {diag}\n")
        archivo.write("\n" + "="*50 + "\n\n") # Separador para mejor lectura
    messagebox.showinfo("Registro Guardado", f"El diagnóstico se ha guardado en el archivo {archivo_path}.")

def cargar_historial():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_path = os.path.join(directorio_actual, "diagnosticos.txt")
    
    if not os.path.exists(archivo_path):
        return "No hay diagnósticos previos registrados."
    
    with open(archivo_path, "r") as archivo:
        contenido = archivo.read()
    return contenido

# Interfaz de Usuario
class SistemaExpertoApp:
    def __init__(self, master):
        self.master = master
        master.title("Sistema Experto de Diagnóstico de Vehículos")
        master.geometry("750x550") # Tamaño un poco más grande
        master.resizable(False, False) # Evitar que la ventana se redimensione

        self.tipo_vehiculo_seleccionado = tk.StringVar(master)
        self.tipo_vehiculo_seleccionado.set("coche") # Valor por defecto

        self.label_bienvenida = tk.Label(master, text="Bienvenido al Sistema Experto de Diagnóstico Automotriz", font=("Helvetica", 16, "bold"))
        self.label_bienvenida.pack(pady=15)

        self.frame_tipo = tk.LabelFrame(master, text="Seleccione el Tipo de Vehículo", font=("Helvetica", 10, "bold"), padx=10, pady=5)
        self.frame_tipo.pack(pady=10, padx=20, fill="x")

        self.radio_coche = tk.Radiobutton(self.frame_tipo, text="Coche", variable=self.tipo_vehiculo_seleccionado, value="coche", font=("Helvetica", 10))
        self.radio_coche.pack(side="left", padx=20)
        self.radio_moto = tk.Radiobutton(self.frame_tipo, text="Moto", variable=self.tipo_vehiculo_seleccionado, value="moto", font=("Helvetica", 10))
        self.radio_moto.pack(side="left", padx=20)

        self.label_descripcion = tk.Label(master, text="Describa detalladamente el problema que presenta el vehículo:", font=("Helvetica", 10, "bold"))
        self.label_descripcion.pack(pady=10)

        self.descripcion_text = tk.Text(master, height=6, width=75, font=("Helvetica", 10), bd=2, relief="groove")
        self.descripcion_text.pack(pady=5)

        self.frame_botones = tk.Frame(master)
        self.frame_botones.pack(pady=10)

        self.btn_diagnosticar = tk.Button(self.frame_botones, text="Realizar Diagnóstico", command=self.realizar_diagnostico, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049")
        self.btn_diagnosticar.pack(side="left", padx=10)

        self.btn_ver_historial = tk.Button(self.frame_botones, text="Ver Historial de Diagnósticos", command=self.mostrar_historial, font=("Helvetica", 10, "bold"), bg="#008CBA", fg="white", activebackground="#007ba7")
        self.btn_ver_historial.pack(side="left", padx=10)

        self.label_resultado = tk.Label(master, text="Resultados del Diagnóstico:", font=("Helvetica", 10, "bold"))
        self.label_resultado.pack(pady=5)

        self.resultado_text_area = scrolledtext.ScrolledText(master, height=10, width=85, font=("Helvetica", 10), state='disabled', bd=2, relief="sunken")
        self.resultado_text_area.pack(pady=10)

    def actualizar_resultado(self, texto):
        self.resultado_text_area.config(state='normal')
        self.resultado_text_area.delete('1.0', tk.END)
        self.resultado_text_area.insert(tk.END, texto)
        self.resultado_text_area.config(state='disabled')

    def realizar_diagnostico(self):
        tipo_vehiculo = self.tipo_vehiculo_seleccionado.get()
        descripcion = self.descripcion_text.get("1.0", tk.END).strip()

        if not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, describa el problema del vehículo en el cuadro de texto.", parent=self.master)
            return

        hechos_actuales = base_conocimiento[tipo_vehiculo]["hechos"].copy() 
        reglas_actuales = base_conocimiento[tipo_vehiculo]["reglas"]

        # Reiniciar hechos para la sesión actual
        for key in hechos_actuales:
            hechos_actuales[key] = False

        # Detección de hechos basada en la descripción (mejorada con más frases clave)
        descripcion_lower = descripcion.lower()
        if tipo_vehiculo == "coche":
            hechos_actuales["motor_no_enciende"] = any(phrase in descripcion_lower for phrase in ["motor no enciende", "no arranca el motor", "el carro no prende", "no prende", "da marcha pero no arranca"])
            hechos_actuales["luces_apagan"] = any(phrase in descripcion_lower for phrase in ["luces se apagan", "las luces fallan", "los focos no prenden", "luces tenues", "baja intensidad luces"])
            hechos_actuales["frenos_suenan"] = any(phrase in descripcion_lower for phrase in ["frenos suenan", "los frenos chilan", "rechinan los frenos", "ruido al frenar", "chillido al frenar"])
            hechos_actuales["aire_acondicionado_no_enfria"] = any(phrase in descripcion_lower for phrase in ["aire acondicionado no enfria", "el clima no enfría", "no sale aire frío del aire", "clima no funciona", "solo echa aire caliente"])
            hechos_actuales["ruido_suspension"] = any(phrase in descripcion_lower for phrase in ["ruido suspension", "ruido en la suspensión", "suena al pasar baches", "golpeteo al andar", "amortiguadores suenan", "tronido en baches"])
            hechos_actuales["sobrecalentamiento_motor"] = any(phrase in descripcion_lower for phrase in ["sobrecalentamiento motor", "se calienta el motor", "temperatura alta del motor", "se sube la aguja de la temperatura", "humo del motor", "hierve el anticongelante"])
            hechos_actuales["aceite_bajo"] = any(phrase in descripcion_lower for phrase in ["aceite bajo", "nivel de aceite bajo", "poco aceite", "luz de aceite encendida", "presión de aceite baja"])
            hechos_actuales["escape_humoso"] = any(phrase in descripcion_lower for phrase in ["escape humoso", "humo del escape", "sale humo del tubo", "escape echa humo", "humo azul", "humo blanco", "humo negro"])
            hechos_actuales["vibracion_volante"] = any(phrase in descripcion_lower for phrase in ["vibracion volante", "vibra el volante", "steering wheel shakes", "vibra al conducir", "volante tiembla"])
            hechos_actuales["pierde_potencia"] = any(phrase in descripcion_lower for phrase in ["pierde potencia", "sin fuerza", "no acelera bien", "se siente lento", "jalonea", "falta de potencia"])
            hechos_actuales["consumo_combustible_alto"] = any(phrase in descripcion_lower for phrase in ["gasta mucha gasolina", "consumo excesivo de combustible", "alto consumo", "rinde poco la gasolina"])
            hechos_actuales["testigo_encendido"] = any(phrase in descripcion_lower for phrase in ["testigo encendido", "luz de check engine", "luz del motor", "se prendió una luz en el tablero", "luz de falla"])

            # Preguntas adicionales específicas si se detecta "motor_no_enciende"
            if hechos_actuales["motor_no_enciende"]:
                respuesta_bateria = simpledialog.askstring("Pregunta Adicional", "¿Al intentar encender, el motor gira lento o solo se escucha un clic? (si/no):", parent=self.master)
                if respuesta_bateria and respuesta_bateria.lower() == "si":
                    hechos_actuales["bateria_descargada"] = True
                
        elif tipo_vehiculo == "moto":
            hechos_actuales["motor_no_arranca"] = any(phrase in descripcion_lower for phrase in ["motor no arranca", "la moto no prende", "no enciende la moto", "no arranca", "da marcha pero no enciende"])
            hechos_actuales["bateria_baja"] = any(phrase in descripcion_lower for phrase in ["bateria baja", "batería sin carga", "se le acabó la batería", "no hay corriente"])
            hechos_actuales["luces_fallan"] = any(phrase in descripcion_lower for phrase in ["luces fallan", "las luces de la moto no prenden", "los faros no funcionan", "luces intermitentes"])
            hechos_actuales["cadena_suena_extraño"] = any(phrase in descripcion_lower for phrase in ["cadena suena extraño", "la cadena hace ruido", "suena raro la cadena", "cadena ruidosa", "rechina la cadena"])
            hechos_actuales["frenos_chirrian"] = any(phrase in descripcion_lower for phrase in ["frenos chirrian", "los frenos de la moto chillan", "rechinan los frenos de la moto", "ruido al frenar"])
            hechos_actuales["problema_cambio_marchas"] = any(phrase in descripcion_lower for phrase in ["problema cambio marchas", "no entran las marchas", "le cuesta cambiar de velocidad", "se traba el cambio", "salta la marcha"])
            hechos_actuales["pata_apoyo_no_funciona"] = any(phrase in descripcion_lower for phrase in ["pata apoyo no funciona", "no funciona la pata", "problema con el caballete", "sensor de pata falla", "no prende con la pata arriba"])
            hechos_actuales["consumo_excesivo"] = any(phrase in descripcion_lower for phrase in ["consumo excesivo", "gasta mucha gasolina", "alto consumo combustible", "rinde poco"])
            hechos_actuales["falla_encendido"] = any(phrase in descripcion_lower for phrase in ["falla encendido", "problema al encender", "no prende bien", "tarda en arrancar", "se ahoga al prender"])
            hechos_actuales["ruido_motor_extraño"] = any(phrase in descripcion_lower for phrase in ["ruido motor extraño", "el motor hace un ruido raro", "suena el motor", "golpeteo en el motor", "tintineo en el motor"])
            hechos_actuales["fuga_liquido"] = any(phrase in descripcion_lower for phrase in ["fuga de liquido", "hay un charco debajo", "gotea", "pierde liquido", "mancha de aceite"])
            hechos_actuales["amortiguacion_mala"] = any(phrase in descripcion_lower for phrase in ["amortiguacion mala", "rebotando mucho", "se siente inestable", "amortiguadores suaves", "suspensión dura", "suspensión blanda"])

            # Preguntas adicionales específicas si se detecta "motor_no_arranca"
            if hechos_actuales["motor_no_arranca"]:
                respuesta_bateria_moto = simpledialog.askstring("Pregunta Adicional", "¿La batería de la moto está completamente sin energía o el arranque es muy débil? (si/no):", parent=self.master)
                if respuesta_bateria_moto and respuesta_bateria_moto.lower() == "si":
                    hechos_actuales["bateria_baja"] = True

        diagnosticos = motor_inferencia(hechos_actuales, reglas_actuales)
        
        resultado_display = f"**Tipo de Vehículo:** {tipo_vehiculo.capitalize()}\n"
        resultado_display += f"**Problema Reportado:** {descripcion}\n\n"
        resultado_display += "**Análisis y Diagnóstico(s) Potencial(es):**\n"
        for diag in diagnosticos:
            resultado_display += f"{diag}\n\n" # Añadir doble salto de línea para más espacio
        
        self.actualizar_resultado(resultado_display)
        guardar_diagnostico(descripcion, diagnosticos, tipo_vehiculo)
        
    def mostrar_historial(self):
        historial_contenido = cargar_historial()
        
        historial_window = tk.Toplevel(self.master)
        historial_window.title("Historial de Diagnósticos Registrados")
        historial_window.geometry("700x500")
        historial_window.transient(self.master) # Hace que la ventana de historial aparezca sobre la principal
        historial_window.grab_set() # Bloquea la interacción con la ventana principal mientras está abierta

        historial_text_area = scrolledtext.ScrolledText(historial_window, wrap=tk.WORD, state='disabled', font=("Helvetica", 10), bd=2, relief="sunken")
        historial_text_area.pack(expand=True, fill='both', padx=10, pady=10)
        
        historial_text_area.config(state='normal')
        historial_text_area.insert(tk.END, historial_contenido)
        historial_text_area.config(state='disabled')

        # Botón para cerrar la ventana de historial
        btn_cerrar_historial = tk.Button(historial_window, text="Cerrar", command=historial_window.destroy, font=("Helvetica", 10, "bold"), bg="#f44336", fg="white")
        btn_cerrar_historial.pack(pady=5)


# Ejecutar el sistema
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaExpertoApp(root)
    root.mainloop()