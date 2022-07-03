import pandas as pd
from GestorIngresoMantCorrectivo import GestorIngresoMantCorrectivo


class PantallaIngresoRT:
    def __init__(self):
        pass

    def registrarIngresoCorrectivo(self):
        gestor = GestorIngresoMantCorrectivo()
        gestorIngresoRespTecRT = gestor.opcionRegistrarIngreso()
        print(str(gestorIngresoRespTecRT))
        buscarRTDisponible = gestor.buscarRecursoTecnologico(
            gestorIngresoRespTecRT)
        print("\n")
        tabla = pd.DataFrame(buscarRTDisponible, columns=[
                             "NumeroRT", "Tipo de Recurso Nombre", "Tipo de Recurso Desc", "Marca", "Modelo"],)
        print(tabla.sort_values("Tipo de Recurso Desc"))

        while True:
            seleccion = input("Seleccione el RT ingresando su NumeroRT : ")
            if seleccion.isnumeric():
                rtSeleccionado = tabla.loc[tabla['NumeroRT'] == int(seleccion)]
                if len(rtSeleccionado) != 0:
                    print("Recurso seleccionado:\n",
                          rtSeleccionado)

                    fechaFin = input("Definir una FechaFin : ")
                    if fechaFin.isnumeric():
                        ingresarRazon = input(
                            "Ingresar razon de mantenimiento: ")
                        break
                    else:
                        print("por favor ingresar fecha correcta")
                else:
                    print("No hay RT disponible con el Numero : ", seleccion)
            else:
                print("por favor ingresar Numero correcto")
        turnosConfirmadoPendiente = gestor.buscarTurnosConfirmadoPendiente(
            rtSeleccionado, fechaFin, ingresarRazon)
        print(turnosConfirmadoPendiente)

    def habilitarVentana():
        pass

    def mostrarRecursosTecnologicos(self):
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
