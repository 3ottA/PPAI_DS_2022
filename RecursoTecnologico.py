
from Marca import *
from Modelo import *
from CambioEstadoRT import *
from TiposRecursoTecnologico import *


class RecursoTecnologico:
    def __init__(self, nroRT: int, fecha: str, imagen, periodicidadMantenimientoPrev: str, duracionMantenimientoPrev: int,
                 fraccionHorarioTurnos: str, cambioEstadoRT: CambioEstadoRT, tipoRecursoTecnologico: TipoRecursoTecnologico, modelo: Modelo):
        self.nroRT = nroRT
        self.fecha = fecha
        self.imagen = imagen
        self.periodicidadMantenimientoPrev = periodicidadMantenimientoPrev
        self.duracionMantenimientoPrev = duracionMantenimientoPrev
        self.fraccionHorarioTurnos = fraccionHorarioTurnos
        self.cambioEstadoRT = cambioEstadoRT
        self.tipoRecursoTecnologico = tipoRecursoTecnologico
        self.modelo = modelo
        pass

    def estasEnEstadoDisponible(self):
        return self.buscarEstadoActual()

    def buscarEstadoActual(self):
        if self.cambioEstadoRT.esEstadoActual():
            cambioActual = self.cambioEstadoRT
            return cambioActual.esDisponible()

    def getNroRT(self) -> int:
        return self.nroRT

    def mostrarDatosRT(self):
        nroRT = self.getNroRT()
        marca, modelo = Marca.getDatosDeRT(self.modelo)
        TipoRecursoTecnologicoN = self.tipoRecursoTecnologico.getNombre()
        TipoRecursoTecnologicoD = self.tipoRecursoTecnologico.getDescripcion()

        return nroRT, TipoRecursoTecnologicoN, TipoRecursoTecnologicoD, marca, modelo

    # def esConfirmadoOPendiente(self, fechaFin):
    #     for turno in LISTA_TURNO:
    #         turno.buscarTurnoConfirmadoPendiente(self, fechaFin)
    #     pass


RT1 = RecursoTecnologico(111, "12-10-2022", "imagen", "2 mes",
                         "15 dias", "fraccion: 15min", CAMBIO_ESTADO_RT1, TRT1, MOD1)
RT2 = RecursoTecnologico(222, "13-10-2022", "imagen", "2 mes",
                         "15 dias", "fraccion: 15min", CAMBIO_ESTADO_RT2, TRT2, MOD2)
RT3 = RecursoTecnologico(333, "14-10-2022", "imagen", "2 mes",
                         "15 dias", "fraccion: 15min", CAMBIO_ESTADO_RT3, TRT1, MOD1)
LISTA_RT = [RT1, RT2, RT3]
