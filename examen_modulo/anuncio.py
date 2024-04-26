from abc import ABC,abstractmethod
from error import SubTipoInvalidoError

class Anuncio():
    def __init__(self,ancho:int,alto:int,url_archivo:str,
                 url_clip:str,sub_tipo:str):
        #validar que se ingrese un valor mayor a cero para ancho 
        self.__ancho = ancho if ancho > 0 else 1
        #validar que se ingrese un valor mayor a cero para alto 
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo= url_archivo
        self.__url_clip= url_clip
        self.__sub_tipo = sub_tipo
    
    @staticmethod
    def mostrar_formatos (formato:str, subtipo: tuple):
        print(" Mostrar Formatos")
        print ("----------------")
        print(formato)
        print ("----------------")
        for i in subtipo: 
            print(subtipo[i])
    
    @abstractmethod  
    def comprimir_anuncios():
        pass
    @abstractmethod
    def redimencionar_anuncio():
        pass  
    
    
    #######  GETTER Y SETTER #######  
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if ancho > 0: 
            self.__ancho = ancho
        else: 
            self.__ancho = 1
    
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        if alto > 0: 
            self.__ancho = alto
        else: 
            self.__ancho = 1
            
    @property 
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self,url):
        self.__url_archivo = url
    
    @property
    def url_clip(self):
        return self.__url_clip
    
    @url_clip.setter
    def modificar_url_clip(self, url):
        self.__url_clip = url
        
    
    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self,sub_tipo):
        try:
            if (isinstance(self,Video) and sub_tipo not in Video.SUB_TIPOS or
            isinstance(self,Display) and sub_tipo not in Display.SUB_TIPOS or
            isinstance(self,Social) and sub_tipo not in Social.SUB_TIPOS) :
                raise SubTipoInvalidoError("No es un subtipos permitidos para las instancias",sub_tipo)
            else:
                self.__sub_tipo = sub_tipo
        except SubTipoInvalidoError as stie:
            print(f"Error:: {stie.mensaje}",stie.subtipo)            
    
    
###### CLASE VIDEO ########      


class Video(Anuncio):
    #VARIABLES DE CLASES
    formato ="video"
    sub_tipo = ("instream","outstream")
    
    #CONSTRUCTOR    
    def __init__(self, url_archivo: str, url_clip: str, sub_tipo: str, duracion):
        super().__init__(url_archivo, url_clip, sub_tipo)
        self.ancho = 1
        self.alto = 1
        self.__duracion = duracion
        
    #METODOS GET Y SET QUE DEBEN SOBREESCRIBIRSE PARA EVITAR MODIFICAR DATOS
    @property
    def ancho(self):
        return self.__ancho
    @property
    def alto(self):
        return self.__alto
    
    @ancho.setter
    def ancho(self, ancho):
        pass
    @alto.setter
    def alto(self, alto):
        pass

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5 

    #metodos implementados por herencia
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
    
    
    
###### CLASE DISPLAY ########        
        
class Display(Anuncio):
    formato ="Display"
    sub_tipo = ("Tradicional","Nativo")
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

    
###### CLASE SOCIAL ########  

class Social(Anuncio):
    formato ="Social"
    sub_tipo = ("Facebook","Linkedin")
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")