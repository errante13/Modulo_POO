#!/usr/bin/python
#-*- coding: utf-8 -*-

from Encuesta import Encuesta

class EncuestaLimitadaPorEdad(Encuesta):
    def __init__(self):
        self.edad_minima = None
        self.edad_maxima = None

    def agregar_listado_respuesta(self, ):
        pass

