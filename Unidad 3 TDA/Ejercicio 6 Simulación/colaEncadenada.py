import numpy as np 
from Nodo import Nodo

class Cola:
    __pri : Nodo
    __ul : Nodo
    __cant : int

    def __init__(self):
        self.__pri = None
        self.__ul = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        nuevoNodo = Nodo()
        nuevoNodo.setDato(x)
        nuevoNodo.setSig = None

        if self.__ul == None:
            self.__pri = nuevoNodo
        
        else:
            self.__ul.setSig(nuevoNodo)
        self.__ul = nuevoNodo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print("cola vacia no se puede suprimir")
        else:
            aux = self.__pri
            x = self.__pri.obtenerDato()
            self.__pri = self.__pri.obtenerSig()
            self.__cant -= 1
            del(aux)
            return x
        
        