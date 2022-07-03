

#from AsignacionCientificoDelCI import LISTA_ACT
from CambioEstadoTurno import *
from RecursoTecnologico import *


class Turno:
    def __init__(self, fechaGeneracion: int, diaSemana: str, fechaHoraInicio: int, fechaHoraFin: int, CambioEstadoTurno: CambioEstadoTurno, rt: RecursoTecnologico) -> None:
        self.fechaGeneracion = fechaGeneracion
        self.diaSemana = diaSemana
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.CambioEstadoTurno = CambioEstadoTurno
        self.rt = rt
        pass

    def obtenerEstadoActual():
        pass

    def generarGrillaTurnosPendienteYConfirmado(self):
        fecInicio = self.getFechaHoraInicio()
        fecFin = self.getFechaHoraFin()
        for asignacion in LISTA_ACT:
            cientifico = asignacion.conocerCientificoAsignado(self)
        return [cientifico, fecInicio, fecFin]

    def getFechaHoraInicio():
        pass

    def getFechaHoraFin():
        pass

    def mostrarTurno():
        pass

    def estasEnConfirmadoPendiente():

        pass

    def buscarTurnoConfirmadoPendiente(self, rtSeleccionado: RecursoTecnologico, fechaFin):

        if self.rt == rtSeleccionado:
            if fechaFin > self.fechaHoraFin:
                if self.CambioEstadoTurno.esEstadoActual():
                    print("Turno Actual")
                    if self.CambioEstadoTurno.esConfirmadoOPendiente():
                        print("Confirmado")
                        return self.generarGrillaTurnosPendienteYConfirmado()
                    else:
                        pass
            else:
                print("No existen turnos dentro del Plazo de Mantenimiento")
                pass


# CREAMOS LOS TURNOS
TUR1 = Turno(1, "Martes", 1, 5, CAMBIO_ESTADO_T1, RT2)
TUR2 = Turno(6, "Martes", 6, 10, CAMBIO_ESTADO_T2, RT2)
TUR3 = Turno(9, "Martes", 1, 5, CAMBIO_ESTADO_T3, RT3)
TUR4 = Turno(11, "Martes", 6, 7, CAMBIO_ESTADO_T4, RT3)
LISTA_TURNO = [TUR1, TUR2, TUR3, TUR4]
