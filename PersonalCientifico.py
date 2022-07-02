
from Usuario import Usuario


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
