from Turno import *
from PersonalCientifico import *
import PersonalCientifico


class AsignacionCientificoDelCI:
    def __init__(self, fechaDesde: int, fechaHasta: int, turno: Turno, personal: PersonalCientifico) -> None:
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta
        pass

    def conocerCientificoAsignado():
        pass

    def buscarCientificoAsignado():
        pass


# Creamos asignaciones Cientifico
ACT1 = AsignacionCientificoDelCI(1, 5, TUR1, PERSONAL2)
ACT2 = AsignacionCientificoDelCI(6, 8, TUR2, PERSONAL3)
LISTA_ACT = [ACT1, ACT2, ]
