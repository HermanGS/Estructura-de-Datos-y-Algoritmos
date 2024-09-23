class Nodo:
    __valor:object
    __siguiente:object
    def __init__(self,valor):
        self.__valor = valor
        self.__siguiente = None
    
    def getvalor(self):
        return self.__valor
    def getsiguiente(self):
        return self.__siguiente
    def setvalor(self,unvalor):
        self.__valor=unvalor
    def setsiguiente(self,sig):
        self.__siguiente=sig