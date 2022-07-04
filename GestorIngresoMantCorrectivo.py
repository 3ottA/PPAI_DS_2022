from CambioEstadoRT import *
from PersonalCientifico import *
from Sesion import *
from TiposRecursoTecnologico import *
from Usuario import Usuario
from RecursoTecnologico import *
from AsignacionResponsableTecnicoRT import *
from Estado import *
from AsignacionCientificoDelCI import *
from Bd import *
from Turno import *


class GestorIngresoMantCorrectivo:
    def __init__(self):
        pass

    def opcionRegistrarIngreso(self):
        sesionActual = self.identificarEmpleadoLogueado()  # busca la sesion Actual
        usuarioActual = sesionActual.obtenerUsuarioLogueado()  # busca el usuario Actual
        # print(sesionActual)
        # Recorremos todos los cientificos hasta encontrar al Usuario Actual
        for personal in LISTA_PERSONAL:  # mientras haya personalCientifico
            print(personal)
            print(personal.esTuUsuario(usuarioActual))
            # si el usuario actual es igual al del personal devolver el personalCientifico(ResponsableTecnico)
            if personal.esTuUsuario(usuarioActual):
                return personal

    def buscarRecursoTecnologico(self, respActual):
        recursosDisponiblesDeRT = []
        for asignacion in LISTA_ART:
            validado = asignacion.buscarRecursoDisponible(respActual)
            if validado != None:
                recursosDisponiblesDeRT.append(validado)
            # print(recursosDisponiblesDeRT)
        return recursosDisponiblesDeRT

    def buscarTurnosConfirmadoPendiente(self,rtSeleccionado: RecursoTecnologico, fechaFin: int):
        return Turno.buscarTurnoConfirmadoPendiente(rtSeleccionado, fechaFin)

    def identificarEmpleadoLogueado(self) -> Sesion:
        # busca la sesion Actual
        return SESION1  # retorna la sesion actual

    def agruparPorTipoRecurso():
        pass

    def tomarSeleccionRT():
        pass

    def buscarFechaFin():
        pass

    def tomarSeleccionFechaFin():
        pass

    def tomarRazon():
        pass
