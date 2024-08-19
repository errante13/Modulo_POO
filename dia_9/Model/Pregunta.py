#!/usr/bin/python
#-*- coding: utf-8 -*-
import Alternativa
class Pregunta:
    def __init__(self,enunciado:str,ayuda:str,requerido:bool,alternativas:list):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.Requerido = requerido
        self.__alternativas = [            
            Alternativa(dicc["contenido"],dicc["ayuda"]) for dicc in alternativas
        ]
        
    def mostrar_pregunta(self):
        print (self.enunciado)
        print(self.ayuda)
        for dicc in self.__alternativas:
            print(dicc.Mostrar_alternativa)

