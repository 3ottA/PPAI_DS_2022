from CambioEstadoRT import CambioEstadoRT
from PersonalCientifico import PersonalCientifico
from Sesion import Sesion
from TiposRecursoTecnologico import TipoRecursoTecnologico
from Usuario import Usuario
from RecursoTecnologico import RecursoTecnologico
from AsignacionResponsableTecnicoRT import AsignacionResponsableTecnicoRT
from Estado import Estado
from AsignacionCientificoDelCI import AsignacionCientificoDelCI
from Bd import *


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

    def buscarRecursoTecnologico():
        recursosDisponiblesDeRT = []
        for asignacion in LISTA_ART:
            recursosDisponiblesDeRT.append(
                asignacion.buscarRecursoDisponible())
        return recursosDisponiblesDeRT

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

    def buscarTurnosConfirmadoPendiente():
        pass
