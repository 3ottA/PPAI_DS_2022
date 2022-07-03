from Modelo import Modelo


class Marca:
    def _init_(self, nombre: str, modelos: Modelo):
        self.nombre = nombre
        self.modelos = modelos

    def getDatosDeRT(modelo: Modelo):

        return self.getMarca, modelo.getDatosModelo()

    def getMarca(self):
        return self.nombre
