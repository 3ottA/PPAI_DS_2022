import copy
import pandas as pd
from GestorIngresoMantCorrectivo import GestorIngresoMantCorrectivo
from RecursoTecnologico import *


class PantallaIngresoRT:
    def __init__(self):
        pass

    def registrarIngresoCorrectivo(self):
        gestor = GestorIngresoMantCorrectivo()
        gestorIngresoRespTecRT = gestor.opcionRegistrarIngreso()
        # print(str(gestorIngresoRespTecRT))
        buscarRTDisponible = gestor.buscarRecursoTecnologico(
            gestorIngresoRespTecRT)
        # rtObjeto = buscarRTDisponible.pop(-1)
        # print(buscarRTDisponible)
        print("\n")
        tabla = pd.DataFrame(buscarRTDisponible, columns=[
                             "NumeroRT", "Tipo de Recurso Nombre", "Tipo de Recurso Desc", "Marca", "Modelo", "objeto"],)
        print(tabla.loc[:, tabla.columns != "objeto"].sort_values(
            "Tipo de Recurso Desc"))

        while True:
            seleccion = input("\nSeleccione el RT ingresando su NumeroRT : ")
            if seleccion.isnumeric():
                rtSeleccionado = tabla.loc[tabla['NumeroRT'] == int(seleccion)]
                if len(rtSeleccionado) != 0:
                    print("\nRecurso seleccionado:\n",
                          rtSeleccionado)
                    fechaFin = input("\nDefinir una FechaFin : ")
                    if fechaFin.isnumeric():
                        ingresarRazon = input(
                            "\nIngresar razon de mantenimiento: ")
                        break
                    else:
                        print("\npor favor ingresar fecha correcta")
                else:
                    print("\nNo hay RT disponible con el Numero : ", seleccion)
            else:
                print("\npor favor ingresar Numero correcto")

        gestor.tomarSeleccionFechaFin(int(fechaFin))
        gestor.tomarRazon(ingresarRazon)
        seleccionado = rtSeleccionado.iloc[0]["objeto"]
        gestor.tomarSeleccionRT(seleccionado)
        #print("Seleccionado", seleccionado)

        turnosConfirmadoPendiente = gestor.buscarTurnosConfirmadoPendiente(
            seleccionado)
        listaTurnosCientificoCancelado = turnosConfirmadoPendiente.copy()
        #print( listaTurnosCientificoCancelado)

        datosPandas = copy.deepcopy(turnosConfirmadoPendiente)
        for i in range(len(datosPandas)):
            datosPandas[i][2] = datosPandas[i][2].getApellidoNombre()
        # print(datosPandas)

        tablaTurno = pd.DataFrame(datosPandas, columns=[
            "DiaInicio", "DiaFin", "Cientifico", "objetoTurno"],)
        print(tablaTurno.loc[:, tablaTurno.columns != "objetoTurno"].sort_values(
            "Cientifico"))

        # gestor.tomarConfirmacionIngreso(inp,datosPandas)
        self.solicitarOpcionDeNotificacion(gestor)
        inp = eval(
            input("Desea Confirmar el ingreso a Mantenimiento?\n ingresar True o False: "))

        gestor.tomarConfirmacionDeIngreso(
            inp, listaTurnosCientificoCancelado, seleccionado)

    def habilitarVentana():
        pass

    def mostrarRecursosTecnologicos(self):
        pass

    def solicitarFechaFin():
        pass

    def solicitarRazon():
        pass

    def solicitarOpcionDeNotificacion(self, gestor: GestorIngresoMantCorrectivo):
        while True:
            OpcionesNoti = input(
                "Seleccione una opcion de notificacion: \n 1. Email \n 2. SMS \n 3. Whatsapp \n")
            if OpcionesNoti == 1:
                nombreNot = "Email"
                break
            elif OpcionesNoti == 2:
                nombreNot = "SMS"
                break
            elif OpcionesNoti == 3:
                nombreNot = "Whatsapp"
                break
            else:
                nombreNot = "Email"
                break
        print("Seleccion : ", nombreNot)
        gestor.buscarOpcionesNotificacion(nombreNot)
        pass
