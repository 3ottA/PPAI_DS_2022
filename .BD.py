from CambioEstadoRT import CambioEstadoRT
from PersonalCientifico import PersonalCientifico
from Sesion import Sesion
from TiposRecursoTecnologico import TipoRecursoTecnologico
from Usuario import Usuario
from RecursoTecnologico import RecursoTecnologico
from AsignacionResponsableTecnicoRT import AsignacionResponsableTecnicoRT
from Estado import Estado
from CambioEstadoTurno import CambioEstadoTurno
from Turno import Turno
from AsignacionCientificoDelCI import AsignacionCientificoDelCI

# Creamos Los usuarios para nuestros personales cientificos
USR1 = Usuario("Luis", 123, True)
USR2 = Usuario("Gustavo", 456, True)
USR3 = Usuario("Juan", 789, True)
# Usucarios en Sesion
SESION1 = Sesion(1, 5, USR1)
SESION2 = Sesion(1, 5, USR2)
SESION3 = Sesion(1, 5, USR3)
# Crearmos una n cantidad de Personales Cientificos para corroborrar con el Usuario
PERSONAL1 = PersonalCientifico("123", "Luis", "Spinetta", "43065215",
                               "escualadeluis@hotmai.com", "luisUwU@yahoo.com", "15415415400", USR3)
PERSONAL2 = PersonalCientifico("456", "Gustavo", "Cerati", "43065215",
                               "EscuelaDeRock@hotmai.com", "SoyElMasCapo123@yahoo.com", "154856741", USR2)
PERSONAL3 = PersonalCientifico("789", "Juan", "Perez", "43065216",
                               "juanperez@hotmai.com", "perezjuan@hotmai.com", "154856741", USR1)
LISTA_PERSONAL = [PERSONAL1, PERSONAL2, PERSONAL3]
# Creamos los Estados
ESTADO1 = Estado("Confirmado", "Turno Confirmado", "Turno", False, True)
ESTADO2 = Estado("Pendientes", "Turno es Pendiente", "Turno", False, True)
ESTADO3 = Estado("Disponible", "El Recurso esta Disponible",
                 "Recurso", True, False)
ESTADO4 = Estado("Finalizado", "Turno Finalizado", "Turno", False, False)
ESTADO5 = Estado("NoDisponible", "El Recurso no esta Disponible",
                 "Recurso", False, False)
# Creamos Cambios de estado
CAMBIO_ESTADO_RT1 = CambioEstadoRT(1, None, ESTADO3)
CAMBIO_ESTADO_RT2 = CambioEstadoRT(1, None, ESTADO3)
CAMBIO_ESTADO_RT3 = CambioEstadoRT(1, 5, ESTADO5)
# CREAMOS CAMBIOS DE ESTADOS TURNO
CAMBIO_ESTADO_T1 = CambioEstadoTurno(1, None, ESTADO1)
CAMBIO_ESTADO_T2 = CambioEstadoTurno(6, None, ESTADO2)
CAMBIO_ESTADO_T3 = CambioEstadoTurno(1, 2, ESTADO4)
CAMBIO_ESTADO_T4 = CambioEstadoTurno(1, 2, ESTADO4)
# CREAMOS LOS TURNOS
TUR1 = Turno(1, 5, 12, 20, CAMBIO_ESTADO_T1)
TUR2 = Turno(6, 6, 7, 10, CAMBIO_ESTADO_T2)
TUR3 = Turno(9, 9, 12, 15, CAMBIO_ESTADO_T3)
TUR4 = Turno(11, 11, 13, 23, CAMBIO_ESTADO_T4)
# Creamos asignaciones Cientifico
ACT1 = AsignacionCientificoDelCI(1, 5, TUR1, PERSONAL2)
ACT2 = AsignacionCientificoDelCI(6, 8, TUR2, PERSONAL3)
LISTA_ACT = [ACT1, ACT2, ]
# Creamos tipos recurso tecnologicos
TRT1 = TipoRecursoTecnologico(
    "Microscopio Marca Nikon Modelo MM-400/800", "Microscopio de medicion")
TRT2 = TipoRecursoTecnologico(
    "Balanza Marca Shidmazu,Modelo TXB622L", "Balanza de precision")
# Creamos Recuros tecnologicos
RT1 = RecursoTecnologico(111, "12-10-2022", "imagen", "1 mes", 10, "30 min")
RT2 = RecursoTecnologico(222, "13-10-2022", "imagen", "2 mes", 15, "30 min")
RT3 = RecursoTecnologico(333, "14-10-2022", "imagen", "1 mes", 20, "30 min")
RT4 = RecursoTecnologico(444, "15-10-2022", "imagen", "1 mes", 30, "30 min")
LISTA_RT = [RT1, RT2, RT3, RT4]
# Creamos asignaciones
ART1 = AsignacionResponsableTecnicoRT(1, 5, RT1, PERSONAL1)
ART2 = AsignacionResponsableTecnicoRT(1, 5, RT2, PERSONAL1)
ART3 = AsignacionResponsableTecnicoRT(6, 10, RT3, PERSONAL2)
ART4 = AsignacionResponsableTecnicoRT(11, 15, RT4, PERSONAL3)
LISTA_ART = [ART1, ART2, ART3, ART4]
