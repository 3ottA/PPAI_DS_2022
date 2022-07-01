from tkinter import *


class PantallaIngresoRT:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ingreso de RT")
        self.ventana.geometry("400x200")
        self.ventana.resizable(0, 0)
        self.ventana.config(bg="white")

        self.ventana.mainloop()
