"""
1. En un archivo error.py, crear la excepción DimensionError derivada de Exception.
Sobreescribir el constructor, recibiendo los parámetros mensaje, dimension y maximo,
y asignándoles los respectivos atributos de instancia. 
""" 
class DimensionError(Exception):
    
    #Constructor 
    def __init__(self, mensaje, dimension, maximo):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        super().__init__(mensaje)
        
    """
    2. En la misma clase anterior, sobrecargar el método __str__, de forma tal que si sólo
    se ha ingresado mensaje al crear la excepción, se retorna el método de la clase padre.
    En caso contrario, crear y retornar un mensaje de retorno utilizando los atributos
    mensaje y/o dimension y/o maximo.
    """
    def __str__(self):
        if self.dimension is None or self.maximo is None:
            return super().__str__()
        else:
            return f"Las dimensiones no corresponden: {self.mensaje}. Dimension: {self.dimension}, Máximo: {self.maximo}"
