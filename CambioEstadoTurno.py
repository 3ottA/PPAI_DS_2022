from Estado import *


class CambioEstadoTurno:
    def __init__(self, fechaHoraDesde: int, fechaHoraHasta: int, estado: Estado):
        self.fechaHoraDesde = fechaHoraDesde
        self.fechaHoraHasta = fechaHoraHasta
        self.estado = estado

    def esConfirmadoOPendiente(self) -> bool:
        return self.estado.esConfirmadoOPendiente()

    def esEstadoActual(self):
        return self.fechaHoraHasta == None


# CREAMOS CAMBIOS DE ESTADOS TURNO
CAMBIO_ESTADO_T1 = CambioEstadoTurno(1, None, ESTADO1)
CAMBIO_ESTADO_T2 = CambioEstadoTurno(6, None, ESTADO2)
CAMBIO_ESTADO_T3 = CambioEstadoTurno(1, 2, ESTADO4)
CAMBIO_ESTADO_T4 = CambioEstadoTurno(1, 2, ESTADO4)
