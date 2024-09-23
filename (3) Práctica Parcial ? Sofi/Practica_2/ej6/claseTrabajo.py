import random

class Trabajo:
    __tiempo_impresion:int
    __tiempo_espera:int
    def __init__(self, tiempo_impresion,tiempo_espera):
        self.__tiempo_impresion = tiempo_impresion
        self.__tiempo_espera=tiempo_espera
    
    def gettiempoImpresion(self):
        return self.__tiempo_impresion
    def gettiempoEspera(self):
        return self.__tiempo_espera

