class Usuario:
    def __init__(self, usuario, clave, habilitado) -> None:
        self.usuario = usuario
        self.clave = clave
        self.habilitado = habilitado
        pass
    # metodo toString, printea atributos de objeto

    def __str__(self):
        return "Usuario: "+self.usuario+"\nClave: "+str(self.clave)

    def getUsuario():
        pass
