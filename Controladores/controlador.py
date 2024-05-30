import tkinter as tk
import threading
import time
import os
import traceback
import psutil
import re

import math

from Vista.vista import Vista
from tkinter import ttk
from tkinter import filedialog


class Controlador:
    def __init__(self, root):
        # self.modelo = Modelo()
        self.vista = Vista(root)
        # self.neumatico = Neumatico()

        self.state = True

        #self.vista.checkbuttonAll.config()
        # self.vista.checkbuttonAlk.config(command=self.tiempoAproximado)

        # self.vista.radio_efficienceL.config(command=self.tiempoAproximado)
        # self.vista.radio_efficienceM.config(command=self.tiempoAproximado)
        # self.vista.radio_efficienceH.config(command=self.tiempoAproximado)

        self.vista.buttonCambioTasa.config(command=self.CambioTasas)
        #self.vista.buttonPath.config(command=self.seleccionar_carpeta)
        self.vista.buttonEqTasas.config(command=self.equi_tasas)
        self.vista.buttonIntC.config(command=self.menu_interes_compuesto)
        self.vista.buttonAnu.config(command=self.menu_Anualidades)
        self.vista.checkbuttonAD.config(command=self.Anualidad_dif)
        self.vista.checkbuttonAF.config(command=self.Anualidad_dif)
        self.vista.checkbuttonAFa.config(command=self.Anualidad_dif)
        self.vista.checkbuttonAP.config(command=self.Anualidad_dif)
        self.vista.checkbuttonAPa.config(command=self.Anualidad_dif)
    def CambioTasas(self):
        # self.vista.TextI.insert(0,"Hola mundo")
        #if not self.validaciones():
        self.validaciones()
        print(self.seleccionar_periodo(self.vista.a.get()))
        print(self.seleccionar_tipo_tasa())
        #else:
           #pass
        
    def pruebas(self):
        pass

    def menu(self):
        pass

    def get_periods(self,type):
        pass

    def validaciones(self):
        #entrada = input(self.vista.TextI.get())
        try:
            numero = float(self.vista.TextI.get())
            if 0.0 < numero <= 1:
                self.CTasas()
            else:
                print("Entrada inválida. Asegúrese de ingresar un número correcto.")
        
        except:
                print("Entrada inválida. Asegúrese de ingresar un número correcto.")
        #Validar que solo sea pueda elegir un boton en el apartado de conversion de tasas , botones anticipada y ya anticipada
        #validacion cuadros de interes i para equivalencia de tasas, solo pueden quedar en i
    def CTasas(self):
        self.vista.TextF.config(state="normal")
        self.vista.TextF.delete(0,tk.END)
        self.vista.TextF.config(state="disabled")

    #OJO________________________________________________________________
        
        choice = self.vista.d.get()
        
        if choice == 1:
            print("Convertir tasa nominal (J) a tasa efectiva (i):")
            interes = float(self.vista.TextI.get().replace(",","."))
            i = self.convertir_J_a_i(interes, self.seleccionar_periodo(self.vista.a.get()), self.seleccionar_periodo(self.vista.a.get()), self.seleccionar_tipo_tasa(),self.seleccionar_tasa())
            self.vista.TextF.config(state="normal")
            self.vista.TextF.insert(0,f"{i * 100:.2f}%")
            self.vista.TextF.config(state="disabled")
            self.vista.TextEqEn.config(state="normal")
            self.vista.TextEqEn.insert(0,f"{i * 100:.2f}%")
            self.vista.TextEqEn.config(state="disabled")

        elif choice == 0:
            print("Convertir tasa efectiva (i) a tasa nominal (J):")
            interes = float(self.vista.TextI.get().replace(",","."))
            j = self.convertir_i_a_J(interes, self.seleccionar_periodo(self.vista.a.get()), self.seleccionar_periodo(self.vista.a.get()),self.seleccionar_tipo_tasa(),self.seleccionar_tasa())
            self.vista.TextF.config(state="normal")
            self.vista.TextF.insert(0,f"{j * 100:.2f}%")
            self.vista.TextF.config(state="disabled")
            self.vista.TextEqEn.config(state="normal")
            self.vista.TextEqEn.insert(0,f"{interes * 100:.2f}%")
            self.vista.TextEqEn.config(state="disabled")
        else:
            raise ValueError("Opción no válida")
        
        
        # if conversion == 'J_to_i':
           
        #     n_J = seleccionar_periodo("nominal (J)")
        #     n_i = seleccionar_periodo("efectiva (i)")
        #     tipo_i = seleccionar_tipo_tasa()
        #     i = convertir_J_a_i(J, n_J, n_i, tipo_i)
        #     print(f"La tasa efectiva {tipo_i} {periodo_nombre(n_i)} es: {i * 100:.2f}%")
        # elif conversion == 'i_to_J':
        #     i = float(input("Ingrese la tasa efectiva (i) como decimal (por ejemplo, 0.08 para 8%): "))
        #     n_i = seleccionar_periodo("efectiva (i)")
        #     n_J = seleccionar_periodo("nominal (J)")
        #     J = convertir_i_a_J(i, n_i, n_J)
        #     print(f"La tasa nominal {periodo_nombre(n_J)} es: {J * 100:.2f}%")
        

    def seleccionar_periodo(self,n):
        periodo = n
        if periodo == 0:
            return 12  # Mensual
        elif periodo == 1:
            return 6  # Bimestral
        elif periodo == 2:
            return 4  # Trimestral
        elif periodo == 3:
            return 3  # Cuatrimestral
        elif periodo == 4:
            return 2  # Semestral
        elif periodo == 5:
            return 1  # Anual
        else:
            raise ValueError("Opción de periodo no válida")
    
    def seleccionar_tipo_tasa(self):

        tipo = self.vista.boolAn.get()
        if tipo == False:
            return 'normal'
        elif tipo == True:
            return 'anticipada'
        else:
            raise ValueError("Opción de tipo de tasa no válida")
        
    def seleccionar_tasa(self):

        tipo_2 = self.vista.boolbtnan.get()
        if tipo_2 == False:
            return 'No anticipada'
        elif tipo_2 == True:
            return 'Ya anticipada'
        else:
            raise ValueError("Opción de tipo de tasa no válida")
            
   
    def convertir_J_a_i(self, J, n_J, n_i, tipo_i,tipo_j):
        if tipo_j == 'No anticipada':  
            if tipo_i == 'normal':
                i_anual = (1 + J / n_J) ** n_J - 1
                i_convertida = (1 + i_anual) ** (1 / n_i) - 1
            elif tipo_i == 'anticipada':
                k_conver = J/(n_J)
                k_con= k_conver/(1+k_conver)
                i_Jann=k_con*n_J
                i_convertida=i_Jann
            return i_convertida
        elif tipo_j== 'Ya anticipada':
            j_an=J/(n_J)
            i_an=j_an/(1-j_an)
            return i_ann
   
    def convertir_i_a_J(self, i, n_i, n_J,tipo_i,tipo_j):
        if tipo_j == 'No anticipada':
            if tipo_i == 'normal':
                J_convertida = i*n_i
            elif tipo_i == 'anticipada':
                aux1 = i/(1+i)
                J_convertida=aux1
            return J_convertida
        elif tipo_j== 'Ya anticipada':
            i_an=i/(1-i)
            return i_an

    def equi_tasas(self):
        self.vista.TextEqEn.config(state="normal")
        self.vista.TextEqEn.delete(0,tk.END)
        self.vista.TextEqF.config(state="normal")
        self.vista.TextEqF.delete(0,tk.END)
        if self.vista.d.get() == 0:
            periodo_i = self.seleccionar_periodo(self.vista.a.get())
            periodo_i2 = self.seleccionar_periodo(self.vista.c.get())
            i = float(self.vista.TextI.get().replace("%",""))/100
            raiz=(((1+i) ** periodo_i) ** (1/periodo_i2))-1
            self.vista.TextEqF.insert(0,f"{raiz * 100:.2f}%")
            self.vista.TextEqF.config(state="disabled")
        elif self.vista.d.get() == 1:
            periodo_i = self.seleccionar_periodo(self.vista.a.get())
            periodo_i2 = self.seleccionar_periodo(self.vista.c.get())
            i = float(self.vista.TextF.get().replace("%",""))/100
            raiz=(((1+i) ** periodo_i) ** (1/periodo_i2))-1
            self.vista.TextEqF.insert(0,f"{raiz * 100:.2f}%")
            self.vista.TextEqF.config(state="disabled")

    def menu_interes_compuesto(self):
        choice = int(self.vista.b.get())
        P = self.vista.TextVP.get()
        S = self.vista.TextVF.get()
        i = self.vista.Textint.get()
        n = self.vista.Texttie.get()
        self.calcular_interes_compuesto(choice,P,S,i,n)
        
    def calcular_interes_compuesto(self,choice, P=None, S=None, i=None, n=None):
        if choice == 0:
            self.vista.TextVF.config(state="normal")
            self.vista.TextVF.delete(0,tk.END)
            if P == "" or i == "" or n == "":
                raise ValueError("Faltan datos para calcular el monto futuro (S)")
            S = float(self.vista.TextVP.get()) * (1 + float(self.vista.Textint.get())) ** float(self.vista.Texttie.get())
            self.vista.TextVF.config(state="normal")
            self.vista.TextVF.insert(0,f"{S:.2f}")
            
        elif choice == 1:
            self.vista.TextVP.config(state="normal")
            self.vista.TextVP.delete(0,tk.END)
            if S == "" or i == "" or n == "":
                raise ValueError("Faltan datos para calcular el valor presente (P)")
            P = float(self.vista.TextVF.get()) / (1 + float(self.vista.Textint.get())) ** float(self.vista.Texttie.get())
            self.vista.TextVP.config(state="normal")
            self.vista.TextVP.insert(0,f"{P:.2f}")
        elif choice == 2:
            self.vista.Texttie.config(state="normal")
            self.vista.Texttie.delete(0,tk.END)
            import math
            if S == "" or  P == "" or i == "":
                raise ValueError("Faltan datos para calcular la tasa de interés (i)")
            n = math.log(float(self.vista.TextVF.get()) / float(self.vista.TextVP.get())) / math.log(1 + float(self.vista.Textint.get()))
            self.vista.Texttie.config(state="normal")
            self.vista.Texttie.insert(0,f"{n:.2f}")
        elif choice == 3:
            self.vista.Textint.config(state="normal")
            self.vista.Textint.delete(0,tk.END)
            if S == "" or  P == "" or n == "":
                raise ValueError("Faltan datos para calcular el número de periodos (n)")
            i = (float(self.vista.TextVF.get()) / float(self.vista.TextVP.get())) ** (1 / float(self.vista.Texttie.get())) - 1
            self.vista.Textint.config(state="normal")
            self.vista.Textint.insert(0,f"{i:.4f}")

    def menu_Anualidades(self):
        elecci = int(self.vista.e.get())
        eleccion = int(self.vista.f.get())
        A = self.vista.TextAn.get()
        C = self.vista.TextCuo.get()
        i = self.vista.Textinter.get()
        n = self.vista.Texttiemp.get()
        m = self.vista.TextMti.get()
        self.calcular_Anualidad(elecci,eleccion,A,C,i,n,m)
    
    def Anualidad_dif(self):
        value = self.vista.e.get()
        print(f"Valor actual de 'e': {value}")  # Depuración para verificar el valor recibido
        m=self.vista.TextMti.get()

        if value == 4:
            print("Activando TextMti")  # Depuración para confirmar que entra aquí
            self.vista.TextMti.config(state="normal")
        else:
            print("Desactivando TextMti")  # Depuración para confirmar que entra aquí
            self.vista.TextMti.config(state="disabled")

        self.vista.root.update_idletasks()  

    def calcular_Anualidad(self,elecci,eleccion,A=None,C=None,i=None,n=None,m=None):
        if elecci == 0:
            if eleccion == 0:    
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.delete(0,tk.END)
                if C == "" or i == "" or n == "":
                    raise ValueError("Faltan datos para calcular la anualidad")
                A = float(self.vista.TextCuo.get()) * ((1 + float(self.vista.Textinter.get())) ** float(self.vista.Texttiemp.get()) - 1) / float(self.vista.Textinter.get())
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.insert(0,f"{A:.2f}")
            if eleccion == 1:
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.delete(0,tk.END)
                if A == "" or i == "" or n == "":
                    raise ValueError("Faltan datos para calcular la cuota")
                Cad = ((1 + float(self.vista.Textinter.get())) ** float(self.vista.Texttiemp.get()) - 1) / float(self.vista.Textinter.get())
                C = float(self.vista.TextAn.get())/ Cad
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.insert(0,f"{C:.2f}")
        if elecci == 1:
            if eleccion == 0:    
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.delete(0,tk.END)
                if C == "" or i == "" or n == "":
                    raise ValueError("Faltan datos para calcular la anualidad")
                A = float(self.vista.TextCuo.get()) * ((1 + float(self.vista.Textinter.get())) ** float(self.vista.Texttiemp.get()) - 1) / float(self.vista.Textinter.get())* (1 + float(self.vista.Textinter.get()))
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.insert(0,f"{A:.2f}")
            if eleccion == 1:
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.delete(0,tk.END)
                if A == "" or i == "" or n == "":
                    raise ValueError("Faltan datos para calcular la cuota")
                Cad = ((1 + float(self.vista.Textinter.get())) ** float(self.vista.Texttiemp.get()) - 1) / float(self.vista.Textinter.get())* (1 + float(self.vista.Textinter.get()))
                C = float(self.vista.TextAn.get())/ Cad
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.insert(0,f"{C:.2f}")
        if elecci == 2:
            if eleccion == 0:    
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.delete(0,tk.END)
                if C == "" or i == "" or n == "":
                    raise ValueError("Faltan datos para calcular la anualidad")
                A = float(self.vista.TextCuo.get()) * (1 - (1 + float(self.vista.Textinter.get())) ** -float(self.vista.Texttiemp.get()) ) / float(self.vista.Textinter.get())
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.insert(0,f"{A:.2f}")
            if eleccion == 1:
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.delete(0,tk.END)
                if A == "" or i == "" or n == "":
                    raise ValueError("Faltan datos para calcular la cuota")
                Cad=(1 - (1 + float(self.vista.Textinter.get())) ** -float(self.vista.Texttiemp.get()) ) / float(self.vista.Textinter.get())     
                C = float(self.vista.TextAn.get())/Cad 
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.insert(0,f"{C:.2f}")
        if elecci == 3:
            if eleccion == 0:    
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.delete(0,tk.END)
                if C == "" or i == "" or n == "":
                    raise ValueError("Faltan datos para calcular la anualidad")
                A = float(self.vista.TextCuo.get()) * (1 - (1 + float(self.vista.Textinter.get())) ** -float(self.vista.Texttiemp.get()) ) / float(self.vista.Textinter.get()) * (1 + float(self.vista.Textinter.get()))
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.insert(0,f"{A:.2f}")
            if eleccion == 1:
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.delete(0,tk.END)
                if A == "" or i == "" or n == "":
                    raise ValueError("Faltan datos para calcular la cuota")
                Cad=(1 - (1 + float(self.vista.Textinter.get())) ** -float(self.vista.Texttiemp.get()) ) / float(self.vista.Textinter.get()) * (1 + float(self.vista.Textinter.get()))    
                C = float(self.vista.TextAn.get())/Cad 
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.insert(0,f"{C:.2f}")   
        if elecci == 4 :
            if eleccion == 0:    
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.delete(0,tk.END)
                if C == "" or i == "" or n == "" or m == "":
                    raise ValueError("Faltan datos para calcular la anualidad")
                A = float(self.vista.TextCuo.get()) * ((1 - (1 + float(self.vista.Textinter.get())) ** -float(self.vista.Texttiemp.get())) / float(self.vista.Textinter.get())) * (1 + float(self.vista.Textinter.get())) ** -float(self.vista.TextMti.get())
                self.vista.TextAn.config(state="normal")
                self.vista.TextAn.insert(0,f"{A:.2f}")
            if eleccion == 1:
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.delete(0,tk.END)
                if A == "" or i == "" or n == "" or m == "":
                    raise ValueError("Faltan datos para calcular la cuota")
                Cad=((1 - (1 + float(self.vista.Textinter.get())) ** -float(self.vista.Texttiemp.get())) / float(self.vista.Textinter.get())) * (1 + float(self.vista.Textinter.get())) ** -float(self.vista.TextMti.get())
                C = float(self.vista.TextAn.get())/Cad 
                self.vista.TextCuo.config(state="normal")
                self.vista.TextCuo.insert(0,f"{C:.2f}")
             
    #______________________________________________________________

    def iniciar(self):
        """
        Inicia el bucle principal del tkinter para mostrar la interfaz gráfica al usuario.
        Esta función llama al método `mainloop()` de la raíz de la vista (`self.vista.root`),
        lo que inicia el bucle principal de tkinter y muestra la interfaz gráfica al usuario.

        Returns:
            None
    """
        
        
        
        self.vista.root.mainloop()
