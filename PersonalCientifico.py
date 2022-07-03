
from Usuario import *


class PersonalCientifico:
    def __init__(self, legajo: str, nombre: str, apellido: str, numeroDocumento: str, correoElectronicoInstitucional: str, correoElectronicoPersonal: str, telefonoCelular: str, usr: Usuario):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.numeroDocumento = numeroDocumento
        self.correoElectronicoInstitucional = correoElectronicoInstitucional
        self.correoElectronicoPersonal = correoElectronicoPersonal
        self.telefonoCelular = telefonoCelular
        self.usr = usr
        pass

    def esTuUsuario(self, usr_actual) -> bool:
        # Devuelve True o False dependiendo si los usuarios(Usuario actual con el Usuario del personal Seleccionado) son iguales
        return usr_actual == self.usr

    def getCientifico():
        pass

    def __str__(self) -> str:
        return "Legajo: "+self.legajo + " Nombre: "+self.nombre + " Apellido: "+self.apellido


# Crearmos una n cantidad de Personales Cientificos para corroborrar con el Usuario
PERSONAL1 = PersonalCientifico("123", "Luis", "Spinetta", "43065215",
                               "escualadeluis@hotmai.com", "luisUwU@yahoo.com", "15415415400", USR1)
PERSONAL2 = PersonalCientifico("456", "Gustavo", "Cerati", "43065215",
                               "EscuelaDeRock@hotmai.com", "SoyElMasCapo123@yahoo.com", "154856741", USR2)
PERSONAL3 = PersonalCientifico("789", "Juan", "Perez", "43065216",
                               "juanperez@hotmai.com", "perezjuan@hotmai.com", "154856741", USR3)
LISTA_PERSONAL = [PERSONAL1, PERSONAL2, PERSONAL3]
