class Te():
    
    #atributo de clase
    """ se define solo la duración ya que es el unico valor en común con el resto 
        de objetos creados por esta
    """
    duracion = 365
    
    #paso 1
    @staticmethod
    def tiempoPreparacion(sabor: int):
        """
        1: Corresponde a Té negro
        2: Corresponde a Té verde
        3: Corresponde a Agua de hierbas.
        
         El té negro tiene un tiempo de preparación de 3 minutos, 
         el té verde de 5 minutos y el agua de hierbas de 6 minutos
        """ 
        
        if sabor == 1: 
           # print("El té Negro tiene un tiempo de preparación de 3 minutos y \n se recomienda consumir al desayuno")
            return 3, "desayuno"
        elif sabor == 2:
            
           # print( "El té Verde tiene un tiempo de preparación de 5 minutos y \n se recomienda consumir al medio dia")
            return 5, "medio dia"
        else:
            #print( "El agua de hierbas tiene un tiempo de preparación de 6 minutos y \n se recomienda consumir al atardecer")
            return 6, "atardecer"
    #paso 2
    @staticmethod
    def calcularPrecio(tamano: int):
        """
        Los 3 sabores de té se pueden comprar en cualquiera de los 2 formatos, teniendo el formato
        de 300gr un valor de $3.000 y el de 500gr un valor de $5.000
        """
        if tamano == 300:
            return 3000
        else: 
            return 5000
        
