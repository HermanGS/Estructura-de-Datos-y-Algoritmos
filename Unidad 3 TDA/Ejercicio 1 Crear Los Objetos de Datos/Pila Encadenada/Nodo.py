class Nodo:
    __dato : None
    __siguiente : None

    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None

    def retornaSig(self):
        return self.__siguiente
    
    def CambiarSig(self,x):
        self.__siguiente = x
        
    def retornaDato(self):
        return self.__dato
    
    def CambiarDato(self,x):
        self.__dato = x

     
    
    