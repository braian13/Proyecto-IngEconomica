import tkinter as tk
from tkinter import ttk


class Vista:
    def __init__(self, root):
        # Variables booleanas para controlar los estados de los Checkbuttons
        self.boolMen = tk.BooleanVar()
        self.boolAn = tk.BooleanVar() 
        self.boolbtnan = tk.BooleanVar()

        # Variable de control para el Radiobutton de rendimiento
        self.d = tk.IntVar(value=0)
        self.a = tk.IntVar(value=0)
        self.c = tk.IntVar(value=0) 
        self.e = tk.IntVar(value=0)
        self.b = tk.IntVar(value=0)
        self.f = tk.IntVar(value=0)
        #periodos de tiempo
        # Configuración básica de la ventana principal
        self.root = root
        self.root.title("Ingenieria economica")
        self.root.option_add("*tearOff", False) # This is always a good idea

        # Configuración de la apariencia y tema de la ventana principal
        self.root.columnconfigure(index=0, weight=1)
        self.root.columnconfigure(index=1, weight=1)
        self.root.rowconfigure(index=0, weight=1)
        self.root.rowconfigure(index=1, weight=1)
        self.root.tk.call("source", "Vista/Forest-ttk-theme-master/forest-light.tcl")
        self.style = ttk.Style(self.root)
        self.style.theme_use("forest-light")

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

        self.radio_i = ttk.Radiobutton(self.pages_frame, text="Efectiva", variable=self.d, value=0)
        self.radio_i.grid(row=0, column=1, padx=0, pady=0, sticky="W")
        self.radio_j = ttk.Radiobutton(self.pages_frame, text="Nominal", variable=self.d, value=1)
        self.radio_j.grid(row=0, column=2, padx=5, pady=0, sticky="W")
        self.checkbuttonAn = ttk.Checkbutton(self.pages_frame, text="Anticipada", variable=self.boolAn) 
        self.checkbuttonAn.grid(row=0,column=3, sticky="nsew",padx=5)
        self.checkbuttonAn = ttk.Checkbutton(self.pages_frame, text="Ya Anticipada", variable=self.boolbtnan) 
        self.checkbuttonAn.grid(row=0,column=4, sticky="nsew",padx=5)
        
        self.TextI = ttk.Entry(self.pages_frame, width=30)
        self.TextI.grid(row=2, column=1, columnspan=3)
        
        self.TextF = ttk.Entry(self.pages_frame, width=30, state='disabled')
        self.TextF.grid(row=4, column=1, columnspan=3)
    
        self.buttonCambioTasa = ttk.Button(self.pages_frame, text="Calcular")
        self.buttonCambioTasa.grid(row=6, column=2, padx=(10,10), pady=(10,10), sticky="nsew")
        # Separador entre secciones
        self.separator = ttk.Separator(root)
        self.separator.grid(row=5, column=0, padx=(20, 10), pady=10, sticky="ew")

        # Creación del marco para seleccionar el rendimiento
        self.efficiency_frame = ttk.LabelFrame(root, text="Equivalencia de Tasas", padding=(20, 10))
        self.efficiency_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")
        self.checkbuttonMena = ttk.Radiobutton(self.efficiency_frame, text="Mensual", variable=self.c, value=0)
        self.checkbuttonMena.grid(row=0, column=0, padx=5, sticky="nsew")

        self.checkbuttonBa = ttk.Radiobutton(self.efficiency_frame, text="Bimestral", variable=self.c, value=1)
        self.checkbuttonBa.grid(row=1,column=0, sticky="nsew",padx=5)

        self.checkbuttonTria = ttk.Radiobutton(self.efficiency_frame, text="Trimestral", variable=self.c, value=2)
        self.checkbuttonTria.grid(row=2,column=0, sticky="nsew",padx=5)

        self.checkbuttonCuaa = ttk.Radiobutton(self.efficiency_frame, text="Cuatrimestral", variable=self.c, value=3)
        self.checkbuttonCuaa.grid(row=3,column=0, sticky="nsew",padx=5)

        self.checkbuttonSea = ttk.Radiobutton(self.efficiency_frame, text="Semestral", variable=self.c, value=4)
        self.checkbuttonSea.grid(row=4,column=0, sticky="nsew",padx=5)

        self.checkbuttonAna = ttk.Radiobutton(self.efficiency_frame, text="Anual", variable=self.c, value=5)
        self.checkbuttonAna.grid(row=5,column=0, sticky="nsew",padx=5)
        
        self.buttonEqTasas = ttk.Button(self.efficiency_frame, text="Calcular")
        self.buttonEqTasas.grid(row=6, column=2, padx=(10,10), pady=(10,10), sticky="nsew")

        self.TextEqEn = ttk.Entry(self.efficiency_frame, width=30,state='disabled')
        self.TextEqEn.grid(row=2, column=2, columnspan=3)
        
        self.TextEqF = ttk.Entry(self.efficiency_frame, width=30, state='disabled')
        self.TextEqF.grid(row=4, column=2, columnspan=3)

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

        self.pages_framIn = ttk.LabelFrame(root, text="Interes compuesto", padding=(20, 10))
        self.pages_framIn.grid(row=0, column=3, padx=(5, 10), pady=(20, 10), sticky="nsew")
        self.checkbuttonS = ttk.Radiobutton(self.pages_framIn, text="Valor futuro", variable=self.b, value=0)
        self.checkbuttonS.grid(row=1,column=0, sticky="nsew",padx=5)
        self.checkbuttonP = ttk.Radiobutton(self.pages_framIn, text="Valor presente", variable=self.b, value=1)
        self.checkbuttonP.grid(row=1,column=1, sticky="nsew",padx=5)
        self.checkbuttonT = ttk.Radiobutton(self.pages_framIn, text="Tiempo", variable=self.b, value=2)
        self.checkbuttonT.grid(row=1,column=2, sticky="nsew",padx=5)
        self.checkbuttonTI = ttk.Radiobutton(self.pages_framIn, text="Tasa de interes", variable=self.b, value=3)
        self.checkbuttonTI.grid(row=1,column=3, sticky="nsew",padx=5)
        self.labelVf = ttk.Label(self.pages_framIn, text="Valor Futuro (S)",anchor="w")
        self.labelVf.grid(row=2, column=1,pady=5)
        self.TextVF = ttk.Entry(self.pages_framIn, width=50)
        self.TextVF.grid(row=2, column=2, columnspan=3,pady=5)
        self.labelVp = ttk.Label(self.pages_framIn, text="Valor Presente (P)",anchor="w")
        self.labelVp.grid(row=3, column=1,pady=5)
        self.TextVP = ttk.Entry(self.pages_framIn, width=50)
        self.TextVP.grid(row=3, column=2, columnspan=3,pady=5)
        self.labelVf = ttk.Label(self.pages_framIn, text="Tiempo (n)",anchor="w")
        self.labelVf.grid(row=4, column=1,pady=5)
        self.Texttie = ttk.Entry(self.pages_framIn, width=50)
        self.Texttie.grid(row=4, column=2, columnspan=3,pady=5)
        self.labeli = ttk.Label(self.pages_framIn, text="Tasa de interes (i)",anchor="w")
        self.labeli.grid(row=5, column=1,pady=5)
        self.Textint = ttk.Entry(self.pages_framIn, width=50)
        self.Textint.grid(row=5, column=2, columnspan=3,pady=5)
        self.buttonIntC = ttk.Button(self.pages_framIn, text="Calcular")
        self.buttonIntC.grid(row=6, column=2, padx=(10,10), pady=(10,10), sticky="nsew")

 
        self.pages_framAn = ttk.LabelFrame(root, text="Anualidades", padding=(20, 10))
        self.pages_framAn.grid(row=2, column=3, padx=(5, 10), pady=(20, 10), sticky="nsew")
        self.checkbuttonAF = ttk.Radiobutton(self.pages_framAn, text="AF", variable=self.e, value=0)
        self.checkbuttonAF.grid(row=1,column=0, sticky="nsew",padx=5)
        self.checkbuttonAFa = ttk.Radiobutton(self.pages_framAn, text="AFa", variable=self.e, value=1)
        self.checkbuttonAFa.grid(row=1,column=1, sticky="nsew",padx=5)
        self.checkbuttonAP = ttk.Radiobutton(self.pages_framAn, text="AP", variable=self.e, value=2)
        self.checkbuttonAP.grid(row=1,column=2, sticky="nsew",padx=5)
        self.checkbuttonAPa = ttk.Radiobutton(self.pages_framAn, text="APa", variable=self.e, value=3)
        self.checkbuttonAPa.grid(row=1,column=3, sticky="nsew",padx=5)
        self.checkbuttonAD = ttk.Radiobutton(self.pages_framAn, text="AD", variable=self.e, value=4)
        self.checkbuttonAD.grid(row=1,column=4, sticky="nsew",padx=5)
        self.checkbuttonAnual = ttk.Radiobutton(self.pages_framAn, text="Anualidades", variable=self.f, value=0)
        self.checkbuttonAnual.grid(row=2,column=0,sticky="nsew",padx=5)
        self.checkbuttonCuota = ttk.Radiobutton(self.pages_framAn, text="Cuota", variable=self.f, value=1)
        self.checkbuttonCuota.grid(row=3,column=0, sticky="nsew",padx=5)
        self.labelVf = ttk.Label(self.pages_framAn, text="Anualidad (A)",anchor="w")
        self.labelVf.grid(row=2, column=1,pady=5)
        self.TextAn = ttk.Entry(self.pages_framAn, width=50)
        self.TextAn.grid(row=2, column=2, columnspan=3,pady=5)
        self.labelVp = ttk.Label(self.pages_framAn, text="Cuota (C)",anchor="w")
        self.labelVp.grid(row=3, column=1,pady=5)
        self.TextCuo = ttk.Entry(self.pages_framAn, width=50)
        self.TextCuo.grid(row=3, column=2, columnspan=3,pady=5)
        self.labelVf = ttk.Label(self.pages_framAn, text="Tiempo (n)",anchor="w")
        self.labelVf.grid(row=4, column=1,pady=5)
        self.Texttiemp = ttk.Entry(self.pages_framAn, width=20)
        self.Texttiemp.grid(row=4, column=3,pady=5)
        self.labelVf = ttk.Label(self.pages_framAn, text="Tiempo diferido(m)",anchor="w")
        self.labelVf.grid(row=6, column=1,pady=5)
        self.Textinter = ttk.Entry(self.pages_framAn,width=20)
        self.Textinter.grid(row=5, column=3,pady=5)
        self.labeli = ttk.Label(self.pages_framAn, text="Tasa de interes (i)",anchor="w")
        self.labeli.grid(row=5, column=1,pady=5)
        self.TextMti = ttk.Entry(self.pages_framAn, width=20)
        self.TextMti.grid(row=6, column=3,pady=5)
        self.buttonAnu = ttk.Button(self.pages_framAn, text="Calcular")
        self.buttonAnu.grid(row=7, column=3, padx=(10,10), pady=(10,10), sticky="nsew")

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


        

        
    
