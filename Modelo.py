class Modelo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        pass

    def getDatosModelo(self):
        return self.nombre


MOD1 = Modelo("MM-400/800")
MOD2 = Modelo("TXB622L")
