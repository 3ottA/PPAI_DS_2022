from Marca import Marca
from Modelo import Modelo
from CambioEstadoRT import CambioEstadoRT
from TiposRecursoTecnologico import TipoRecursoTecnologico
from Turno import Turno


class RecursoTecnologico:
    def __init__(self, nroRT: int, fecha: str, imagen, periodicidadMantenimientoPrev: str, duracionMantenimientoPrev: int,
                 fraccionHorarioTurnos: str, cambioEstadoRT: CambioEstadoRT, turno: Turno, tipoRecursoTecnologico: TipoRecursoTecnologico, modelo: Modelo):
        self.nroRT = nroRT
        self.fecha = fecha
        self.imagen = imagen
        self.periodicidadMantenimientoPrev = periodicidadMantenimientoPrev
        self.duracionMantenimientoPrev = duracionMantenimientoPrev
        self.fraccionHorarioTurnos = fraccionHorarioTurnos
        self.cambioEstadoRT = cambioEstadoRT
        self.turno = turno
        self.tipoRecursoTecnologico = tipoRecursoTecnologico
        self.modelo = modelo
        pass

    def estasEnEstadoDisponible(self,):
        return self.buscarEstadoActual()

    def buscarEstadoActual(self):
        if self.cambioEstadoRT.esEstadoActual():
            cambioActual = self.cambioEstadoRT
            return cambioActual.esDisponible()

    def getNroRT(self):
        return self.nroRT

    def mostrarDatosRT(self):
        nroRT = self.getNroRT
        marca, modelo = Marca.getDatosDeRT(self.modelo)
        TipoRecursoTecnologicoN = TipoRecursoTecnologico.getNombre()
        TipoRecursoTecnologicoD = TipoRecursoTecnologico.getDescripcion()

        return nroRT, TipoRecursoTecnologicoN, TipoRecursoTecnologicoD, marca, modelo

    def esConfirmadoOPendiente():
        pass
