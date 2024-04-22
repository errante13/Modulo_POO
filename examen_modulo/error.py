class Error(Exception):
    pass

class SubTipoInvalidoException(Error):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)