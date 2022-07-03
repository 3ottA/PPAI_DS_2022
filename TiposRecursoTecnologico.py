
class TipoRecursoTecnologico:
    def __init__(self, nombre: str, descripcion: str) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        pass

    def getNombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion


# Creamos tipos recurso tecnologicos
TRT1 = TipoRecursoTecnologico(
    "Microscopio de medicion", "No se")
TRT2 = TipoRecursoTecnologico(
    "Balanza de precision", "Medicion que mide la medida mas precisa medible")
