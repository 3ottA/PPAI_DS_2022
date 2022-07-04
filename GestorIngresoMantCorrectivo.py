from CambioEstadoRT import *
from Mantenimiento import Mantenimiento
from OpcionNotificacion import *
from PersonalCientifico import *
from Sesion import *
from TiposRecursoTecnologico import *
from Usuario import Usuario
from RecursoTecnologico import *
from AsignacionResponsableTecnicoRT import *
from Estado import *
from AsignacionCientificoDelCI import *
from Turno import LISTA_TURNO


class GestorIngresoMantCorrectivo:
    def __init__(self):
        self.confirmacionIngreso = False
        self.razon = None
        self.fecFin = None
        self.recursoTecnologico = None
        self.opcionNot = None
        pass

    def opcionRegistrarIngreso(self):
        sesionActual = self.identificarEmpleadoLogueado()  # busca la sesion Actual
        usuarioActual = sesionActual.obtenerUsuarioLogueado()  # busca el usuario Actual
        # print(sesionActual)
        # Recorremos todos los cientificos hasta encontrar al Usuario Actual
        for personal in LISTA_PERSONAL:  # mientras haya personalCientifico
            # print(personal)
            # print(personal.esTuUsuario(usuarioActual))
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

    def buscarTurnosConfirmadoPendiente(self, rtSeleccionado: RecursoTecnologico):
        tablaTurnosConfOPendiente = []
        for turno in LISTA_TURNO:
            ConfirOPendienteturno = turno.buscarTurnoConfirmadoPendiente(
                rtSeleccionado, self.fecFin, LISTA_ACT)
            if ConfirOPendienteturno != None:

                ConfirOPendienteturno = ConfirOPendienteturno[0]
                # ConfirOPendienteturno =
                ConfirOPendienteturno.append(turno)

                tablaTurnosConfOPendiente.append(
                    ConfirOPendienteturno)
        return tablaTurnosConfOPendiente

    def identificarEmpleadoLogueado(self) -> Sesion:
        # busca la sesion Actual
        return SESION1  # retorna la sesion actual

    def agruparPorTipoRecurso(self):
        pass

    def tomarSeleccionRT(self, rt: RecursoTecnologico):
        self.recursoTecnologico = rt
        pass

    def buscarFechaFin():
        pass

    def tomarSeleccionFechaFin(self, fechaFin):
        self.fecFin = fechaFin
        pass

    def tomarRazon(self, razon):
        self.razon = razon
        pass

    def tomarConfirmacionDeIngreso(self, conf: bool, turnosSeleccionado: list, rtSeleccionado: RecursoTecnologico):
        self.confirmacionIngreso = conf
        #punteroAmbito = Estado.esAmbitoTurno()
        punteroEstadoTurno = Estado.esCanceladoPorMantCorrectivo()
        self.cancelarPorMantenimientoCorrectivoTurno(
            turnosSeleccionado, punteroEstadoTurno)

        #print("Adentro TCDI", turnosSeleccionado)
        punteroEstadoRT = Estado.esConIngresoEnMantCorrectivo()
        #print("Ingresado a Mantenimiento : ", punteroEstadoRT, "\n")
        self.AsignarConIngresoEnMantCorrectivo(
            rtSeleccionado, punteroEstadoRT)

        notificacion = self.crearMantenimiento()
        self.generarNotificacion(turnosSeleccionado)
        pass

    def tomarOpcionNotificacion(self, OpcionNotificacion):
        self.opcionNot = OpcionNotificacion
        pass

    def buscarOpcionesNotificacion(self, OpcionNoti):
        self.tomarOpcionNotificacion(OpcionNoti)
        pass

    def obtenerFechayHoraActual():
        pass

    def cancelarPorMantenimientoCorrectivoTurno(self, turnosSeleccionado, punteroEstado):
        listaTurnosCientificoCancelado = []
        for turno in turnosSeleccionado:

            turno[3].cancelarPorMantCorrectivo(FECHA_HOY, punteroEstado)
            listaTurnosCientificoCancelado.append(turno)
            #print("Turnos Cancelados Por Correccion: ", str(turno[3]))

        return listaTurnosCientificoCancelado

    def AsignarConIngresoEnMantCorrectivo(self, rtSeleccionado: RecursoTecnologico, punteroEstadoRT):
        rtSeleccionado.AsignarConIngresoEnMantCorrectivo(
            FECHA_HOY, punteroEstadoRT)
        pass

    def crearMantenimiento(self):
        mantenimiento = Mantenimiento(FECHA_HOY, self.fecFin, self.razon)
        # print(str(mantenimiento))
        pass

    def generarNotificacion(self, TurnosCientificoCancelado: list):

        for i in TurnosCientificoCancelado:
            datos = i[2]
            email = i[2].getEmailInstitucional()
            turno = i[3]
            self.enviarMail(datos, email, turno)
        pass

    def enviarMail(self, datosPersoanal, email, turno):
        #print(f"{datosPersoanal} Se le ha enviado un email informando que\n {turno}\n{self.recursoTecnologico} \n ha sido cancelado porque {self.razon},enviado a la direccion es {email}")
        pass

    def finCU():
        print("Fin CU")
        pass
