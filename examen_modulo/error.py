#se crea clase error que hereda de exception
class Error(Exception):
    pass


class LargoExcedidoError(Error):
    pass


class SubTipoInvalidoError(Error):
    def __init__(self, mensaje, subtipo):
        self.mensaje = mensaje
        self.subtipo = subtipo