
class TipoRecursoTecnologico:
    def __init__(self, nombre: str, descripcion: str) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        pass

    def getNombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion
