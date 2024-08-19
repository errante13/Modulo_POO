from datetime import date
from anuncio import Anuncio,Video,Display,Social
from error import LargoExcedidoError
class Campania():
    def __init__(self,nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios =[self.__instancia_de_anuncios(dicc)  for dicc in anuncios]
        # self.__anuncios =[Video, Video, Display, Social]
    #[{},{},{}]

    def __instancia_de_anuncios(self, anuncio: dict):
        
        ancho = anuncio.get("ancho")
        alto = anuncio.get("alto")
        url_archivo = anuncio.get("url_archivo")
        url_clip = anuncio.get("url_clip")
        #duracion = anuncio.get("duracion")
        
        return Anuncio(ancho,alto,url_archivo,url_clip)    
    
    @property
    def nombre(self):
        return self.__nombre
    
    """
        Al querer modificar el nombre de una campaña ya creada, 
        se debe validar que el nuevo nombre no supere los 250 caracteres. 
        De ser así, se debe lanzar una excepción LargoExcedidoException.
    
    """
    @nombre.setter
    def nombre(self,nombre):
        try: 
            if len(nombre) > 250:
                raise LargoExcedidoError("el valor excede el tamaño maximo permitido",nombre) 
            else:
                self.__nombre = nombre
        except LargoExcedidoError as lee:
            print(f"Error: {lee}")
            
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def  fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self,fecha_termino):
        self.__fecha_termino = fecha_termino
    
    @property
    def anuncio(self):
        for a in self.__anuncios:
            return a
        
    def __str__(self):
        video = 0
        social = 0
        display = 0
        for a in self.__anuncios:
           if a(isinstance(self,Video)):
                video +=1 
                break
           elif a(isinstance(self, Social)):
               social+1
           else:
               display+=1
                 
        return f"Nombre de la campaña: {self.__nombre} \n 
        Anuncios: videos: {video},display {display},social {social} "