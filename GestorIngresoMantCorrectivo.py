from PersonalCientifico import PersonalCientifico
from Sesion import Sesion
from Usuario import Usuario
# Creamos Los usuarios para nuestros personales cientificos
USR1 = Usuario("Luis", 123, True)
USR2 = Usuario("Gustavo", 456, True)
USR3 = Usuario("Juan", 789, True)
SESION1 = Sesion(1, 5, USR1)
# Crearmos una n cantidad de Personales Cientificos para corroborrar con el Usuario
PERSONAL1 = PersonalCientifico("123", "Luis", "Spinetta", "43065215",
                               "escualadeluis@hotmai.com", "luisUwU@yahoo.com", "15415415400", USR3)
PERSONAL2 = PersonalCientifico("456", "Gustavo", "Cerati", "43065215",
                               "EscuelaDeRock@hotmai.com", "SoyElMasCapo123@yahoo.com", "154856741", USR2)
PERSONAL3 = PersonalCientifico("789", "Juan", "Perez", "43065216",
                               "juanperez@hotmai.com", "perezjuan@hotmai.com", "154856741", USR1)
LISTA_PERSONAL = [PERSONAL1, PERSONAL2, PERSONAL3]


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

    def identificarEmpleadoLogueado(self) -> Sesion:
        # busca la sesion Actual
        return SESION1  # retorna la sesion actual

    def buscarRecursoTecnologico():
        pass

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
