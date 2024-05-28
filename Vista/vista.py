import tkinter as tk
from tkinter import ttk


class Vista:
    def __init__(self, root):
        # Variables booleanas para controlar los estados de los Checkbuttons
        self.boolMen = tk.BooleanVar()
        self.boolB = tk.BooleanVar()
        self.boolTri = tk.BooleanVar()
        self.boolCua = tk.BooleanVar()
        self.boolSe = tk.BooleanVar()
        self.boolAn = tk.BooleanVar()
        self.boolJum = tk.BooleanVar() 
        self.boolMet = tk.BooleanVar() 
        self.boolGrupIn = tk.BooleanVar()
        self.boolLasLl = tk.BooleanVar() 
        

        # Variable de control para el Radiobutton de rendimiento
        self.d = tk.IntVar(value=0)
        self.a = tk.IntVar(value=0)
        # Configuración básica de la ventana principal
        self.root = root
        self.root.title("Ingenieria economica")
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
        self.pages_frame = ttk.LabelFrame(root, text="Cambio de tasas", padding=(20, 10))
        self.pages_frame.grid(row=0, column=0, padx=(5, 10), pady=(20, 10), sticky="nsew")

        self.checkbuttonMen = ttk.Radiobutton(self.pages_frame, text="Mensual", variable=self.a, value=0)
        self.checkbuttonMen.grid(row=0, column=0, padx=5, sticky="nsew")

        self.checkbuttonB = ttk.Radiobutton(self.pages_frame, text="Bimestral", variable=self.a, value=1)
        self.checkbuttonB.grid(row=1,column=0, sticky="nsew",padx=5)

        self.checkbuttonTri = ttk.Radiobutton(self.pages_frame, text="Trimestral", variable=self.a, value=2)
        self.checkbuttonTri.grid(row=2,column=0, sticky="nsew",padx=5)

        self.checkbuttonCua = ttk.Radiobutton(self.pages_frame, text="Cuatrimestral", variable=self.a, value=3)
        self.checkbuttonCua.grid(row=3,column=0, sticky="nsew",padx=5)

        self.checkbuttonSe = ttk.Radiobutton(self.pages_frame, text="Semestral", variable=self.a, value=4)
        self.checkbuttonSe.grid(row=4,column=0, sticky="nsew",padx=5)

        self.checkbuttonAn = ttk.Radiobutton(self.pages_frame, text="Anual", variable=self.a, value=5)
        self.checkbuttonAn.grid(row=5,column=0, sticky="nsew",padx=5)

        self.radio_i = ttk.Radiobutton(self.pages_frame, text="efectiva", variable=self.d, value=0)
        self.radio_i.grid(row=0, column=1, padx=0, pady=0, sticky="W")
        self.radio_j = ttk.Radiobutton(self.pages_frame, text="nominal", variable=self.d, value=1)
        self.radio_j.grid(row=0, column=2, padx=5, pady=0, sticky="W")
        
        self.TextI = ttk.Entry(self.pages_frame, width=20)
        self.TextI.grid(row=2, column=1, columnspan=2)
        
        self.TextF = ttk.Entry(self.pages_frame, width=20, state='disabled')
        self.TextF.grid(row=4, column=1, columnspan=2)
    
        self.buttonCambioTasa = ttk.Button(self.pages_frame, text="Calcular")
        self.buttonCambioTasa.grid(row=6, column=2, padx=(10,10), pady=(10,10), sticky="nsew")
        # Separador entre secciones
        self.separator = ttk.Separator(root)
        self.separator.grid(row=5, column=0, padx=(20, 10), pady=10, sticky="ew")

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


        

        
    
