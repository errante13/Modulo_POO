class Anuncio():
    def __init__(self,ancho:int,alto:int,url_archivo:str,
                 url_clip:str,sub_tipo:str):
        self.__ancho = ancho
        self.__alto = alto
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
        
    def comprimir_anuncios():
        pass
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
    ##falta terminar archivo
    @sub_tipo.setter
    def modificar_sub_tipo(sefl,sub_tipo):
        pass            
    
    
###### CLASE VIDEO ########      


class Video(Anuncio):
    #VARIABLES DE CLASES
    formato ="video"
    sub_tipo = ("instream","outstream")
    
    #CONSTRUCTOR    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clip: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clip, sub_tipo)
        self.__alto = 1
        self.__ancho  =1 
        
    def comprimir_anuncios():
        pass
    def redimencionar_anuncio():
        pass  
        
###### CLASE DISPLAY ########        
        
class Display(Anuncio):
    formato ="Display"
    sub_tipo = ("Tradicional","Nativo")
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clip: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clip, sub_tipo)

    def comprimir_anuncios():
        pass
    def redimencionar_anuncio():
        pass  
    
###### CLASE DISPLAY ########  

class Social(Anuncio):
    formato ="Social"
    sub_tipo = ("Facebook","Linkedin")
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clip: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clip, sub_tipo)
    
    
    def comprimir_anuncios():
        pass
    
    
    def redimencionar_anuncio():
        pass  