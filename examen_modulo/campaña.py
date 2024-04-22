class Campana():
    #constructor
    def __init__(self,nombre,fecha_inicio,fecha_termino):
        self.__nombre=nombre
        self.__fecha_inicio =fecha_inicio
        self.__fecha_termino = fecha_termino
        
    def __str__(self) -> str:
        return f"la campaña es: "