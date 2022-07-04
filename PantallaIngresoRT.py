import pandas as pd
from GestorIngresoMantCorrectivo import GestorIngresoMantCorrectivo
from RecursoTecnologico import *


class PantallaIngresoRT:
    def __init__(self):
        pass

    def registrarIngresoCorrectivo(self):
        gestor = GestorIngresoMantCorrectivo()
        gestorIngresoRespTecRT = gestor.opcionRegistrarIngreso()
        print(str(gestorIngresoRespTecRT))
        buscarRTDisponible = gestor.buscarRecursoTecnologico(
            gestorIngresoRespTecRT)
        # rtObjeto = buscarRTDisponible.pop(-1)
        print(buscarRTDisponible)
        print("\n")
        tabla = pd.DataFrame(buscarRTDisponible, columns=[
                             "NumeroRT", "Tipo de Recurso Nombre", "Tipo de Recurso Desc", "Marca", "Modelo", "objeto"],)
        print(tabla.loc[:, tabla.columns != "objeto"].sort_values(
            "Tipo de Recurso Desc"))

        while True:
            # input("Seleccione el RT ingresando su NumeroRT : ")
            seleccion = "222"
            if seleccion.isnumeric():
                rtSeleccionado = tabla.loc[tabla['NumeroRT'] == int(seleccion)]
                if len(rtSeleccionado) != 0:
                    print("Recurso seleccionado:\n",
                          rtSeleccionado)
                    fechaFin = int(11)  # int(input("Definir una FechaFin : "))
                    # if fechaFin.isnumeric():
                    # input( "Ingresar razon de mantenimiento: ")
                    ingresarRazon = "asdasd"
                    break
                    # else:
                    #    print("por favor ingresar fecha correcta")
                else:
                    print("No hay RT disponible con el Numero : ", seleccion)
            else:
                print("por favor ingresar Numero correcto")
        seleccionado = rtSeleccionado.iloc[0]["objeto"]
        print("Seleccionado", seleccionado)
        turnosConfirmadoPendiente = gestor.buscarTurnosConfirmadoPendiente(
            seleccionado, fechaFin)
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
