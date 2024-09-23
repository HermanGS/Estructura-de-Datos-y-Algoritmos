class Nodo:
    __dato : int
    __sig : None



    def __init__(self):
        self.__dato = None
        self.__sig = None


    def setDato(self,x):
        self.__dato = x

    def setSig(self,s):
        self.__sig = s

    def obtenerDato(self):
        return self.__dato
    
    def obtenerSig(self):
        return self.__sig