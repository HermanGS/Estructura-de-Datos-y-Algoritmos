class Celda:
    __tiempoAsociado : int
    __tiempoEspera : int
    __sig: None

    def __init__(self, tiempoAsociado=None, tiempoEspera=None,sig=None):
        self.__tiempoAsociado = tiempoAsociado
        self.__tiempoEspera = tiempoEspera
        self.__sig = sig
    
    def obtenerTiempoAsociado(self):
        return self.__tiempoAsociado
    
    
    def obtenerTiempoEspera(self):
        return self.__tiempoEspera
    

    def cargaTiempoAsociado(self,ta ):
        self.__tiempoAsociado = ta
        
    def cargaTiempoEspera(self, te):
        self.__tiempoEspera = te
    
        
    def obtenerSig(self):
        return self.__sig
    
    def cargarSig(self, sig):
        self.__sig = sig