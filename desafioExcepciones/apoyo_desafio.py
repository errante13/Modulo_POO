from error import DimensionError
class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, valor):
        if valor < 1 or valor > self.MAX:
            raise DimensionError("El rango del valor debe estar entre 1 y 2500", valor, self.MAX)
        self.__ancho = valor
    
    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, valor):
        if valor < 1 or valor > self.MAX:
            raise DimensionError("El rango del valor debe estar entre 1 y 2500", valor, self.MAX)
        self.__alto = valor
        
        
"""
3. En el archivo foto.py entregado, modificar los métodos setter de alto y ancho, de forma
tal que se lance una excepción de tipo DimensionError en caso de que el nuevo valor
ingresado no cumpla con las condiciones descritas. En caso contrario, asignar el
nuevo valor al atributo de instancia correspondiente        
"""