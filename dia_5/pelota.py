#se importa para crear una clase ABSTRACTA
from abc import ABC, abstractmethod

class Pelota():
    
    #definición del metodo, este no tiene implementación osea que no hace nada.
    def rebotar (self, altura:int):
        pass 

class PelotaDeJuguete(Pelota):
    
    def __init__(self):
        self.rebotes=[]
    
    # def rebotar (self, altura:int):
    #   print (altura)

pelotota = Pelota()    
pelotita = PelotaDeJuguete()