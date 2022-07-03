from CambioEstadoTurno import *


class Turno:
    def __init__(self, fechaGeneracion: int, diaSemana: int, fechaHoraInicio: int, fechaHoraFin: int, cambioEstadoFin: CambioEstadoTurno) -> None:
        self.fechaGeneracion = fechaGeneracion
        self.diaSemana = diaSemana
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.cambioEstadoFin = cambioEstadoFin

    def obtenerEstadoActual():
        pass

    def generarGrillaTurnosPendienteYConfirmado():
        pass

    def getFechaHoraInicio():
        pass

    def getFechaHoraFin():
        pass

    def mostrarTurno():
        pass


# CREAMOS LOS TURNOS
TUR1 = Turno(1, 5, 12, 20, CAMBIO_ESTADO_T1)
TUR2 = Turno(6, 6, 7, 10, CAMBIO_ESTADO_T2)
TUR3 = Turno(9, 9, 12, 15, CAMBIO_ESTADO_T3)
TUR4 = Turno(11, 11, 13, 23, CAMBIO_ESTADO_T4)
