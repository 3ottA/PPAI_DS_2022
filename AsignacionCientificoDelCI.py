from Turno import *
from PersonalCientifico import *


class AsignacionCientificoDelCI:
    def __init__(self, fechaDesde: int, fechaHasta: int, turno: Turno, personal: PersonalCientifico) -> None:
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta
        self.turno = turno
        self.personal = personal
        pass

    def conocerCientificoAsignado(self, turnoActual) -> PersonalCientifico:

        if self.turno == turnoActual:
            return self.personal.getCientifico()

    def buscarCientificoAsignado():
        pass


# Creamos asignaciones Cientifico
# CREAMOS LOS TURNOS
# TUR1 = Turno(1, "Martes", 1, 5, CAMBIO_ESTADO_T1, RT2)
# TUR2 = Turno(6, "Martes", 6, 10, CAMBIO_ESTADO_T2, RT2)
# TUR3 = Turno(9, "Martes", 1, 5, CAMBIO_ESTADO_T3, RT3)
# TUR4 = Turno(11, "Martes", 6, 7, CAMBIO_ESTADO_T4, RT3)
# LISTA_TURNO = [TUR1, TUR2, TUR3, TUR4]

# ACT1 = AsignacionCientificoDelCI(1, 5, TUR1, PERSONAL2)
# ACT2 = AsignacionCientificoDelCI(6, 8, TUR2, PERSONAL3)
# LISTA_ACT = [ACT1, ACT2]


#LISTA_ACT = AsignacionCientificoDelCI[ACT1, ACT2]
global ACT1
ACT1 = AsignacionCientificoDelCI(1, 5, TUR1, PERSONAL2)
global ACT2
ACT2 = AsignacionCientificoDelCI(6, 8, TUR2, PERSONAL3)
LISTA_ACT = [ACT1, ACT2]
