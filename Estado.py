
class Estado:
    def __init__(self, nombre: str, descripcion: str, ambito: str, esReservable: bool, esCancelable: bool):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ambito = ambito
        self.esReservable = esReservable
        self.esCancelable = esCancelable

    def esDisponible(self) -> bool:
        return self.nombre == "Disponible"

    def esConfirmadoOPendiente(self) -> bool:
        return self.nombre == "Confirmado" or self.nombre == "Pendiente"


# Creamos los Estados
ESTADO1 = Estado("Confirmado", "Turno Confirmado", "Turno", False, True)
ESTADO2 = Estado("Pendiente", "Turno es Pendiente", "Turno", False, True)
ESTADO3 = Estado("Disponible", "El Recurso esta Disponible",
                 "Recurso", True, False)
ESTADO4 = Estado("Finalizado", "Turno Finalizado", "Turno", False, False)
ESTADO5 = Estado("NoDisponible", "El Recurso no esta Disponible",
                 "Recurso", False, False)
