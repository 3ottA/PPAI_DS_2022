from CambioEstadoRT import CambioEstadoRT
from TiposRecursoTecnologico import TipoRecursoTecnologico
from Turno import Turno
from Marca import Marca


class RecursoTecnologico:
    def __init__(self, nroRT: int, fecha: int, imagen, periodicidadMantenimientoPrev: str, duracionMantenimientoPrev: int,
                 fraccionHorarioTurnos: str, cambioEstadoRT: CambioEstadoRT, turno: Turno, tipoRecursoTecnologico: TipoRecursoTecnologico):
        self.nroRT = nroRT
        self.fecha = fecha
        self.imagen = imagen
        self.periodicidadMantenimientoPrev = periodicidadMantenimientoPrev
        self.duracionMantenimientoPrev = duracionMantenimientoPrev
        self.fraccionHorarioTurnos = fraccionHorarioTurnos
        self.cambioEstadoRT = cambioEstadoRT
        self.turno = turno
        self.tipoRecursoTecnologico = tipoRecursoTecnologico
        pass

    def estasEnEstadoDisponible(self,):
        self.buscarEstadoActual()
        pass

    def buscarEstadoActual(self):
        if self.cambioEstadoRT.esEstadoActual():
            cambioActual = self.cambioEstadoRT
            return cambioActual.esDisponible()

    def getNroRT(self):
        return self.nroRT

    def mostrarDatosRT(self):
        marca = Marca.getNombre()
        datosRTDisponible = [self.getNroRT,
                             TipoRecursoTecnologico.getNombre(), TipoRecursoTecnologico.getDescripcion(), ]
        return

    def esConfirmadoOPendiente():
        pass
