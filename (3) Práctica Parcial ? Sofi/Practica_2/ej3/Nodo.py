
class Nodo:
    __item:object
    __siguiente:object
    def __init__(self, item):
        self.__item = item
        self.__siguiente = None
    
    def getItem(self):
        return self.__item
    def setItem(self,nuevoItem):
        self.__item=nuevoItem
    def getsiguiente(self):
        return self.__siguiente
    def setSiguiente(self,sig):
        self.__siguiente=sig