import tkinter as tk
import threading
import time
import openpyxl
import os
import numpy
import traceback
import psutil

import math
from Vista.vista import Vista
from openpyxl.styles import NamedStyle
from openpyxl import Workbook
from tkinter import ttk
from tkinter import filedialog


class Controlador:
    def __init__(self, root):
        """
        Inicializa el controlador.

        Esta clase controla la lógica de la aplicación. Se encarga de crear instancias de los controladores
        específicos para cada página web, configurar la vista, gestionar la interfaz de usuario y controlar
        la ejecución de las operaciones de descarga y procesamiento de datos.

        Args:
            root (Tk): La ventana principal de la aplicación.

        Returns:
            None
        """
        # self.modelo = Modelo()
        self.vista = Vista(root)
        # self.neumatico = Neumatico()

        self.state = True

        self.vista.checkbuttonAll.config()
        # self.vista.checkbuttonAlk.config(command=self.tiempoAproximado)

        # self.vista.radio_efficienceL.config(command=self.tiempoAproximado)
        # self.vista.radio_efficienceM.config(command=self.tiempoAproximado)
        # self.vista.radio_efficienceH.config(command=self.tiempoAproximado)

        # self.vista.button.config(command=self.start_selenium_thread)
        # self.vista.buttonPath.config(command=self.seleccionar_carpeta)

        ruta_carpeta_actual = os.getcwd()
        ruta_carpeta_deseada = os.path.join(ruta_carpeta_actual, 'Downloads')
        self.pathDirectory = ruta_carpeta_deseada

    def pruebas(self):
        # "textbox"
        s = 4000000  # variable craar input
        tiempoA= 3 #1,2,3,4,6,12
        tiempoAux= 3 #1,2,3,4,6,12
        #i = 0.36/{tiempoA}  # i o j radioButtom
        U_tiempo = 12 #años 
        ie = 16^(1/2)
        print(str(ie))
        pass

    def menu(self):
        print("Seleccione la tasa de interés actual:")
        print("1. Anual")
        print("2. Semestral")
        print("3. Trimestral")
        print("4. Mensual")
        print("5. Diaria")
        from_type = int(input("Ingrese el número correspondiente: "))
        
        print("Seleccione la tasa de interés a la que desea convertir:")
        print("1. Anual")
        print("2. Semestral")
        print("3. Trimestral")
        print("4. Mensual")
        print("5. Diaria")
        to_type = int(input("Ingrese el número correspondiente: "))
        
        return from_type, to_type

    def get_periods(self,type):
        if type == 1:  # Anual
            return 1
        elif type == 2:  # Semestral
            return 2
        elif type == 3:  # Trimestral
            return 4
        elif type == 4:  # Mensual
            return 12
        elif type == 5:  # Diaria
            return 360
        else:
            raise ValueError("Tipo de tasa no válido")

    def convertir_tasa(self,tasa, from_type, to_type):
        n_from = self.get_periods(from_type)
        n_to = self.get_periods(to_type)
        
        tasa_efectiva_anual = (1 + tasa / n_from) ** n_from - 1
        tasa_convertida = (1 + tasa_efectiva_anual) ** (1 / n_to) - 1
        
        return tasa_convertida * n_to



    def iniciar(self):
        """
        Inicia el bucle principal del tkinter para mostrar la interfaz gráfica al usuario.
        Esta función llama al método `mainloop()` de la raíz de la vista (`self.vista.root`),
        lo que inicia el bucle principal de tkinter y muestra la interfaz gráfica al usuario.

        Returns:
            None
    """
        
        from_type, to_type = self.menu()
        tasa = float(input("Ingrese la tasa de interés (como decimal, por ejemplo, 0.05 para 5%): "))
        
        tasa_convertida = self.convertir_tasa(tasa, from_type, to_type)
        
        print(f"La tasa convertida es: {tasa_convertida * 100:.2f}%")
        self.pruebas()
        #self.vista.root.mainloop()
