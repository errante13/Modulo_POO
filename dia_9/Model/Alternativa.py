#!/usr/bin/python
#-*- coding: utf-8 -*-

class Alternativa:
    def __init__(self,contenido:str, ayuda:str):
        self.contenido = contenido
        self.ayuda = ayuda

    def Mostrar_alternativa(self, ):
        print(f"contenido: {self.contenido} \n ayuda: {self.contenido}")
