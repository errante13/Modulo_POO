# #Definición de un constructor

# #nombre de la clase
# class Pelota():
    
#  #METODO CONSTRUCTOR   
#  def __init__(self):#SE DEBE USAR __INIT__ JUNTO CON EL PARAMETRO (SELF)
#     """
#         NO PUEDE RETORNAR NADA A NO SER QUE SEA UN "NONE"
#         SE ASIGNAN VALORES A LOS ATRIBUTOS(VARIABLES) DE LA CLASE
#     """
#     self.color = "blanco"#---> color es el atributo, y se le asigna el "blanco" como valor 
#     self.tamanio = 20
#     self.material = "plástico"
#     #print en el ejemplo
#     print("¡Se ha creado una pelota!")


# # Salida: "¡Se ha creado una pelota!"
# p = Pelota()

class Pelota():
    def __init__(self):
        self.tamanio_pelota = 1
        
    @property
    def tamanio(self):
        return self.tamanio_pelota
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        
        if tamanio >0:
            self.tamanio_pelota = tamanio 
        else:
           self.tamanio_pelota = 1 
        
      
        
        
        
p = Pelota()
# Salida: 1
print(p.tamanio)
p.tamanio = 0
# Salida: 1
print(p.tamanio)