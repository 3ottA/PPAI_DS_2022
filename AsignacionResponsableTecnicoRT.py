from Bd import FECHA_HOY
from PersonalCientifico import PersonalCientifico
from RecursoTecnologico import RecursoTecnologico


class AsignacionResponsableTecnicoRT:
    def __init__(self, fechaDesde: int, fechaHasta: int, recursos: RecursoTecnologico, rt: PersonalCientifico):
        self.fechaHoraDesde = fechaDesde
        self.fechaHoraHasta = fechaHasta
        self.recursos = recursos
        self.responsableTecnico = rt
        pass

    def conocerResponsableRT():
        validar()
        esDisponible()
        getDatos()
        ordenar()
        pass

    def buscarRecursoDisponible(self, responsableTecnicoActual: PersonalCientifico):
        # Valida que Hoy el recurso esta disponible
        esValidado = self.validarResponsableActual(
            FECHA_HOY, responsableTecnicoActual)
        if esValidado:  # laValidacion fue exitosa
            esDisponible = self.recursos.estasEnEstadoDisponible()
            if esDisponible:
                NroRT, tipoRecursoNombre, tipoRecursoDescripcion, marca, modelo = self.recursos.mostrarDatosRT()
                return NroRT, tipoRecursoNombre, tipoRecursoDescripcion, marca, modelo

    def validarResponsableActual(self, hoy: int, rtActual: PersonalCientifico) -> bool:

        return rtActual == self.responsableTecnico and self.fechaHoraDesde <= hoy <= self.fechaHoraHasta
