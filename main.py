# main.py
import tkinter as tk
from Controladores.controlador import Controlador

root = tk.Tk()
app = Controlador(root)
app.iniciar()