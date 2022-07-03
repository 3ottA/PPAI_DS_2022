from Usuario import *


class Sesion:
    def __init__(self, fechaInicio, fechaFin, usr: Usuario):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.usr = usr

    def obtenerUsuarioLogueado(self):
        return self.usr

    def __str__(self):
        return "Sesion: Desde:"+str(self.fechaInicio)+"hasta: "+str(self.fechaFin)+"\n"+self.usr.__str__()


# Usucarios en Sesion
SESION1 = Sesion(1, 5, USR1)
SESION2 = Sesion(1, 5, USR2)
SESION3 = Sesion(1, 5, USR3)
