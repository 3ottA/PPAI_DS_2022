from Modelo import *


class Marca:
    def __init__(self, nombre: str, modelos: Modelo):
        self.nombre = nombre
        self.modelos = modelos
        pass

    def getDatosDeRT(modelo: Modelo):
        nombreModelo = modelo.getDatosModelo()
        for marca in LISTA_MARCA:
            if marca.modelos.getDatosModelo() == nombreModelo:
                return marca.getMarca(), nombreModelo

    def getMarca(self) -> str:
        return self.nombre


MAR1 = Marca("Nikon", MOD1)
MAR2 = Marca("Shidmazu", MOD2)
LISTA_MARCA = [MAR1, MAR2]
