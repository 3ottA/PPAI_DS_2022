
from GestorIngresoMantCorrectivo import GestorIngresoMantCorrectivo


class PantallaIngresoRT:
    def __init__(self):
        pass

    def registrarIngresoCorrectivo(self):
        gestor = GestorIngresoMantCorrectivo()
        gestorIngresoRespTecRT = gestor.opcionRegistrarIngreso()
        print(str(gestorIngresoRespTecRT))
        buscarRTDisponible = gestor.buscarRecursoTecnologico()
        print(buscarRTDisponible)

    def habilitarVentana():
        pass

    def mostrarRT():
        pass

    def tomarSeleccionRT():
        pass

    def solicitarFechaFin():
        pass

    def tomarSeleccionFechaFin():
        pass

    def solicitarRazon():
        pass

    def tomarRazon():
        pass
