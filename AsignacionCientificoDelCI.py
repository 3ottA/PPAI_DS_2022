from Turno import Turno, TUR1, TUR2
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
ACT1 = AsignacionCientificoDelCI(1, 5, TUR1, PERSONAL2)
ACT2 = AsignacionCientificoDelCI(6, 8, TUR2, PERSONAL3)
LISTA_ACT = [ACT1, ACT2]
