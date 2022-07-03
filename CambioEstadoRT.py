
from Estado import Estado


class CambioEstadoRT:
    def __init__(self, fechaHoraDesde: int, fechaHoraHasta: int, estado: Estado) -> None:
        self.fechaHoraDesde = fechaHoraDesde
        self.fechaHoraHasta = fechaHoraHasta
        self.estado = estado

    def esEstadoActual(self) -> bool:

        return self.fechaHoraDesde <= 3 <= self.fechaHoraHasta

    def mostrarResponsableTecnicoRT():
        pass

    def esDisponible(self) -> bool:

        return self.estado.esDisponible()

    def mostrarResponsableTecnicoRT():
        pass

    def misRT():
        pass
