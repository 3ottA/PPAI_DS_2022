
from CambioEstadoTurno import *
from RecursoTecnologico import *


class Turno:
    def __init__(self, fechaGeneracion: int, diaSemana: str, fechaHoraInicio: int, fechaHoraFin: int, CambioEstadoTurno: CambioEstadoTurno, rt: RecursoTecnologico):
        self.fechaGeneracion = fechaGeneracion
        self.diaSemana = diaSemana
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.CambioEstadoTurno = CambioEstadoTurno
        self.rt = rt
        pass

    def obtenerEstadoActual():
        pass

    def generarGrillaTurnosPendienteYConfirmado(self, LISTA_ACT):
        fecInicio = self.getFechaHoraInicio()
        #print("fecInicio : ", fecInicio)
        fecFin = self.getFechaHoraFin()
        #print("fecFin : ", fecFin)
        tablaConCientifico = []
        for asignacion in LISTA_ACT:
            #print("\nNuestro Turno: ", str(self))
            #print("Asignacion : ", asignacion)
            cientifico = asignacion.buscarCientificoAsignado(self)
            if cientifico != None:
                tablaConCientifico.append([fecInicio, fecFin, cientifico])
        #print("tabla_enTurno", tablaConCientifico)
        return tablaConCientifico

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def getFechaHoraFin(self):
        return self.fechaHoraFin

    def mostrarTurno():
        pass

    def estasEnConfirmadoPendiente():

        pass

    def buscarTurnoConfirmadoPendiente(self, rtSeleccionado: RecursoTecnologico, fechaFin: int, LISTA_ACT):
        if self.rt == rtSeleccionado:
            if fechaFin > self.fechaHoraFin:
                if self.CambioEstadoTurno.esEstadoActual():
                    #print("Turno Actual")
                    if self.CambioEstadoTurno.esConfirmadoOPendiente():
                        # print("Confirmado")
                        #print("tabla_enTurno", tablaConCientifico)
                        return self.generarGrillaTurnosPendienteYConfirmado(LISTA_ACT)
                    else:
                        pass
            else:
                print("No existen turnos dentro del Plazo de Mantenimiento")
                pass

    def cancelarPorMantCorrectivo(self, fechaHoy, punteroEstado):
        self.crearCambioEstado(fechaHoy, punteroEstado)

    def crearCambioEstado(self, fechaHoy, punteroEstado):
        self.CambioEstadoTurno.setFechaHoraHasta(fechaHoy)
        self.CambioEstadoTurno = CambioEstadoTurno(
            fechaHoy, None, punteroEstado)
        pass

    def __str__(self) -> str:
        return " | TURNO: Fecha Gen "+str(self.fechaGeneracion)+" Dia "+str(self.diaSemana)+" "+str(self.fechaHoraInicio)+" "+str(self.fechaHoraFin)+" | CambEst: "+str(self.CambioEstadoTurno)+" NroRT: "+str(self.rt.getNroRT())

    def setEstado(self, estado: Estado):
        self.estado = estado


global TUR1
TUR1 = Turno(1, "Martes", 1, 5, CAMBIO_ESTADO_T1, RT2)
global TUR2
TUR2 = Turno(6, "Martes", 6, 10, CAMBIO_ESTADO_T2, RT2)
global TUR3
TUR3 = Turno(9, "Martes", 1, 5, CAMBIO_ESTADO_T3, RT3)
global TUR4
TUR4 = Turno(11, "Martes", 6, 7, CAMBIO_ESTADO_T4, RT3)
LISTA_TURNO = [TUR1, TUR2, TUR3, TUR4]
