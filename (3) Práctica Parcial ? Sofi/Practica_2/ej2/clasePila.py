import numpy as np
class Pila:
    __datos:np.ndarray
    __tope:int

    def __init__(self):
        self.__datos=np.empty(6,dtype=object)
        self.__tope=-1

    def vacia(self):
        return self.__tope== -1

    def llena(self):
        return self.__tope== len(self.__datos)
    
    def insertar(self,dato):
        if not self.llena():
            self.__tope +=1
            self.__datos[self.__tope]=dato
        else:
            print("Pila llena")

    def suprimir(self):
        if self.vacia():
            print('pila vacia')
            return None
        dato=self.__datos[self.__tope]
        self.__tope -=1
        return dato

    def recorrer(self):
        if not self.vacia():
            for i in range(self.__tope,-1,-1):
                print(self.__datos[i])
                


   