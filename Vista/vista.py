import tkinter as tk
from tkinter import ttk


class Vista:
    def __init__(self, root):
        # Variables booleanas para controlar los estados de los Checkbuttons
        self.boolAll = tk.BooleanVar()
        self.boolAlk = tk.BooleanVar()
        self.boolVir = tk.BooleanVar()
        self.boolTuLl = tk.BooleanVar()
        self.boolHom = tk.BooleanVar()
        self.boolEas = tk.BooleanVar()
        self.boolJum = tk.BooleanVar() 
        self.boolMet = tk.BooleanVar() 
        self.boolGrupIn = tk.BooleanVar()
        self.boolLasLl = tk.BooleanVar() 

        # Variable de control para el Radiobutton de rendimiento
        self.d = tk.IntVar(value=6)

        # Configuración básica de la ventana principal
        self.root = root
        self.root.title("ImllaScraping")
        self.root.option_add("*tearOff", False) # This is always a good idea

        # Configuración de la apariencia y tema de la ventana principal
        self.root.columnconfigure(index=0, weight=1)
        self.root.columnconfigure(index=1, weight=1)
        self.root.rowconfigure(index=0, weight=1)
        self.root.rowconfigure(index=1, weight=1)
        self.root.tk.call("source", "Vista/Forest-ttk-theme-master/forest-dark.tcl")
        self.style = ttk.Style(self.root)
        self.style.theme_use("forest-dark")

        # Creación del marco para las páginas
        self.pages_frame = ttk.LabelFrame(root, text="Páginas", padding=(20, 10))
        self.pages_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

        self.checkbuttonAll = ttk.Checkbutton(self.pages_frame, text="Todas", variable=self.boolAll,)
        self.checkbuttonAll.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.checkbuttonAlk = ttk.Checkbutton(self.pages_frame, text="Alkosto", variable=self.boolAlk)
        self.checkbuttonAlk.grid(row=1,column=0, sticky="nsew",padx=20)

        self.checkbuttonVir = ttk.Checkbutton(self.pages_frame, text="Virtual Llantas", variable=self.boolVir)
        self.checkbuttonVir.grid(row=5,column=0, sticky="nsew",padx=20)

        self.checkbuttonTuLl = ttk.Checkbutton(self.pages_frame, text="Tu llanta", variable=self.boolTuLl)
        self.checkbuttonTuLl.grid(row=6,column=0, sticky="nsew",padx=20)

        self.checkbuttonHom = ttk.Checkbutton(self.pages_frame, text="Homcenter", variable=self.boolHom)
        self.checkbuttonHom.grid(row=7,column=0, sticky="nsew",padx=20)

        self.checkbuttonEas = ttk.Checkbutton(self.pages_frame, text="Easy", variable=self.boolEas)
        self.checkbuttonEas.grid(row=8,column=0, sticky="nsew",padx=20)

        self.checkbuttonJum = ttk.Checkbutton(self.pages_frame, text="Jumbo", variable=self.boolJum)
        self.checkbuttonJum.grid(row=9,column=0, sticky="nsew",padx=20)

        self.checkbuttonMet = ttk.Checkbutton(self.pages_frame, text="Metro", variable=self.boolMet)
        self.checkbuttonMet.grid(row=10,column=0, sticky="nsew",padx=20)

        self.checkbuttonGrupIn = ttk.Checkbutton(self.pages_frame, text="InterLlantas", variable=self.boolGrupIn)
        self.checkbuttonGrupIn.grid(row=11,column=0, sticky="nsew",padx=20)

        self.checkbuttonLasLl = ttk.Checkbutton(self.pages_frame, text="Las llantas", variable=self.boolLasLl)
        self.checkbuttonLasLl.grid(row=12,column=0, sticky="nsew",padx=20)


        # Separador entre secciones
        self.separator = ttk.Separator(root)
        self.separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

        # Creación del marco para seleccionar el rendimiento
        self.efficiency_frame = ttk.LabelFrame(root, text="Redimiento", padding=(20, 10))
        self.efficiency_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")
        self.radio_efficienceL = ttk.Radiobutton(self.efficiency_frame, text="Bajo", variable=self.d, value=3)
        self.radio_efficienceL.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        self.radio_efficienceM = ttk.Radiobutton(self.efficiency_frame, text="Medio", variable=self.d, value=6)
        self.radio_efficienceM.grid(row=1, column=0, padx=5, pady=10, sticky="W")
        self.radio_efficienceH = ttk.Radiobutton(self.efficiency_frame, text="Alto", variable=self.d, value=9)
        self.radio_efficienceH.grid(row=2, column=0, padx=5, pady=10, sticky="W")

        # Creación de la ventana dividida (panel)
        self.paned = ttk.PanedWindow(root)
        self.paned.grid(row=0, column=1, pady=(25, 5), sticky="nsew", rowspan=3)

        # Creacion de pestañas y widgets dentro del primer panel en un Notebook (Detalles y pestañas)
        self.pane_1 = ttk.Frame(self.paned)
        self.paned.add(self.pane_1, weight=70)
        self.notebookInf = ttk.Notebook(self.pane_1)
        self.textInfFrame= ttk.Frame(self.notebookInf)
        self.textInfText = tk.Text(self.textInfFrame, relief="solid", width=80,height=20,wrap="word")
        self.textInfText.pack(padx=0, pady=0, fill="both", expand=True)
        self.notebookInf.add(self.textInfFrame, text="Detalles")
        self.notebookInf.pack(expand=True, fill="both", padx=5, pady=5)

        # Creación de otro panel y Notebook en el segundo panel (Path, tiempo y inicio)
        self.pane_2 = ttk.Frame(self.paned)
        self.paned.add(self.pane_2, weight=30)
        self.notebook = ttk.Notebook(self.pane_2)

        self.tab_1 = ttk.Frame(self.notebook)
        self.tab_1.columnconfigure(index=0, weight=95)
        self.tab_1.columnconfigure(index=1, weight=5)
        self.tab_1.rowconfigure(index=0, weight=1)
        self.tab_1.rowconfigure(index=1, weight=1)

        self.notebook.add(self.tab_1, text="Inicio")
        self.entry = ttk.Entry(self.tab_1)
        self.entry.grid(row=0, column=0, pady=20, sticky="ew")

        self.buttonPath = ttk.Button(self.tab_1, text="Guardar en:")
        self.buttonPath.grid(row=0, column=1, pady=20, sticky="nsew",padx=10)

        self.tiempo_aproximado=0
        self.tiempo_extra=0
        self.labeltiempo = ttk.Label(self.tab_1, text="", justify="center")
        self.labeltiempo.grid(row=1, column=0, pady=(10,10) )

        self.button = ttk.Button(self.tab_1, text="Iniciar")
        self.button.grid(row=1, column=1, padx=(10,10), pady=(10,10), sticky="nsew")

        self.notebook.pack(expand=True, fill="both", padx=5, pady=5)

        # Ajustes finales de tamaño y posición de la ventana principal
        self.sizegrip = ttk.Sizegrip(self.root)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.x_cordinate = int((self.root.winfo_screenwidth()/2) - (self.root.winfo_width()/2))
        self.y_cordinate = int((self.root.winfo_screenheight()/2) - (self.root.winfo_height()/2))
        self.root.geometry("+{}+{}".format(self.x_cordinate, self.y_cordinate))

    # Método para crear una ventana emergente de progreso
    def ProgressBarWindow(self):
        self.VentanaProgreso = tk.Toplevel(self.root,borderwidth=5,relief="solid")
        self.VentanaProgreso.title("Descarga")
        self.VentanaProgreso.overrideredirect(True)
        #VentanaProgreso.attributes('-topmost', 1)
        self.VentanaProgreso.focus_set()  # Establecer el enfoque en la ventana top-level
        self.VentanaProgreso.grab_set()  # Capturar el enfoque en la ventana top-level
        
        self.VentanaProgreso.overrideredirect(True)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        marco = tk.Frame(self.VentanaProgreso)
        marco.grid(row=0, column=0, sticky="nsew",)

        marco.columnconfigure(0, weight=1)
        marco.columnconfigure(1, weight=1)
        marco.columnconfigure(2, weight=1)
        marco.rowconfigure(0, weight=1)
        marco.rowconfigure(1, weight=1)
        marco.rowconfigure(2, weight=1)
        marco.rowconfigure(3, weight=1)

        top_level_width = 340  # Ancho de la ventana Top Level
        top_level_height = 165  # Alto de la ventana Top Level
        x = (screen_width - top_level_width) // 2
        y = (screen_height - top_level_height) // 2

       
        etiqueta2 = tk.Label(marco, text="Descargando...",justify="center")
        etiqueta2.grid(row=0, column=0, sticky="nsew",padx=(20,20),pady=10,columnspan=3)
       
        # Establecer la posición de la ventana Top Level
        self.VentanaProgreso.geometry(f"{top_level_width}x{top_level_height}+{x}+{y}")

        
        self.v= tk.IntVar()
        self.m= tk.IntVar()
        self.m.set(100)
        self.progressbar = ttk.Progressbar(marco, variable=self.v, maximum=self.m.get(), length=250, mode="determinate")
        self.progressbar.grid(row=1, column=0, padx=10, pady=(10,0), columnspan=3, sticky="nsew")
        
        self.porcentaje = tk.Label(marco, text="0.00%")
        self.porcentaje.grid(row=2, column=0, sticky="nsew",padx=(10,60),pady=(0,10))
        self.cantidad1 = tk.Label(marco, text="n",anchor="e")
        self.cantidad1.grid(row=2, column=1, sticky="nsew",padx=(90,0),pady=(0,10))
        self.cantidad2 = tk.Label(marco, text="/n",anchor="w")
        self.cantidad2.grid(row=2, column=2, sticky="nsew",padx=(0,10),pady=(0,10))

        self.boton_cerrar = tk.Button(marco, text="Cerrar")
        self.boton_cerrar.grid(row=3, column=2, padx=(0,10),pady=10)
        
        self.VentanaProgreso.update()
        
        #self.root.wait_window(VentanaProgreso)


        

        
    
