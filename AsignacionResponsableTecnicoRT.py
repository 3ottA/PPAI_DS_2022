from Bd import FECHA_HOY
from PersonalCientifico import *
from RecursoTecnologico import *


class AsignacionResponsableTecnicoRT:
    def __init__(self, fechaDesde: int, fechaHasta: int, recursos: RecursoTecnologico, rt: PersonalCientifico):
        self.fechaHoraDesde = fechaDesde
        self.fechaHoraHasta = fechaHasta
        self.recursos = recursos
        self.responsableTecnico = rt
        pass

    def conocerResponsableRT():

        pass

    def buscarRecursoDisponible(self, responsableTecnicoActual: PersonalCientifico):
        # Valida que Hoy el recurso esta disponible
        print("Validar")
        esValidado = self.validarResponsableActual(
            FECHA_HOY, responsableTecnicoActual)
        if esValidado:  # laValidacion fue exitosa
            print("esDisponible")
            esDisponible = self.recursos.estasEnEstadoDisponible()
            if esDisponible:
                print("mostrarDatos")
                NroRT, tipoRecursoNombre, tipoRecursoDescripcion, marca, modelo = self.recursos.mostrarDatosRT()
                return [NroRT, tipoRecursoNombre, tipoRecursoDescripcion, marca, modelo, self.recursos]

    def validarResponsableActual(self, hoy: int, rtActual: PersonalCientifico) -> bool:
        return rtActual == self.responsableTecnico and self.fechaHoraDesde <= hoy <= self.fechaHoraHasta


ART1 = AsignacionResponsableTecnicoRT(1, 5, RT1, PERSONAL1)
ART2 = AsignacionResponsableTecnicoRT(1, 5, RT2, PERSONAL1)
ART3 = AsignacionResponsableTecnicoRT(6, 10, RT3, PERSONAL2)
LISTA_ART = [ART1, ART2, ART3]
