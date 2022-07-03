
class Estado:
    def __init__(self, nombre: str, descripcion: str, ambito: str, esReservable: bool, esCancelable: bool):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ambito = ambito
        self.esReservable = esReservable
        self.esCancelable = esCancelable

    def esDisponible():
        pass

    def esConfirmadoOPendiente():
        pass


# Confirmados,Pendientes,Disponible
