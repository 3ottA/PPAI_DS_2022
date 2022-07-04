class Mantenimiento:
    def __init__(self, fechaFin: int, fechaInicio: int, motivoMantenimiento: str):
        self.fechaFin = fechaFin
        self.fechaInicio = fechaInicio
        self.fechaInicioPrevista = None
        self.motivoMantenimiento = motivoMantenimiento
        pass
