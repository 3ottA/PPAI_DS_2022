
from Estado import *


class CambioEstadoRT:
    def __init__(self, fechaHoraDesde: int, fechaHoraHasta: int, estado: Estado) -> None:
        self.fechaHoraDesde = fechaHoraDesde
        self.fechaHoraHasta = fechaHoraHasta
        self.estado = estado

    def esEstadoActual(self) -> bool:
        return self.fechaHoraHasta == None

    def mostrarResponsableTecnicoRT():
        pass

    def esDisponible(self) -> bool:
        return self.estado.esDisponible()

    def mostrarResponsableTecnicoRT():
        pass

    def misRT():
        pass

    def setFechaHoraHasta(self, fechaHoraHasta: int) -> None:
        self.fechaHoraHasta = fechaHoraHasta

    def __str__(self) -> str:
        return str(self.fechaHoraDesde)+" "+str(self.fechaHoraHasta)+" Estado:"+str(self.estado)


# Creamos Cambios de estado
CAMBIO_ESTADO_RT1 = CambioEstadoRT(1, None, ESTADO3)
CAMBIO_ESTADO_RT2 = CambioEstadoRT(1, None, ESTADO3)
CAMBIO_ESTADO_RT3 = CambioEstadoRT(1, 5, ESTADO5)
