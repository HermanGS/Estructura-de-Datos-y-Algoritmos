import numpy as np

import random

class objetoT:
    __libre: bool

    def __init__(self):
        self.__dato = None
        self.__libre = True 

    def setDato(self,dato):
        self.__dato = dato

    def getDato(self):
        return self.__dato
    

    def getLibre(self):
        return self.__libre
    

    def setOcupado(self):
        self.__libre = False

    def setLibre(self):
        self.__libre = True

    
    def __str__(self):
        return f'{self.__dato}'




class tablahash:
    __dimension : int
    __tabla : np.ndarray
    


    def __init__(self,dim):
        self.__dimension = dim
        self.__tabla = np.empty(dim,dtype=objetoT)

        for i in range(self.__dimension):
            obj = objetoT()
            self.__tabla[i] = obj


    def hashing(self,k,metodo):
        
        if metodo == 'division':
            return (round(k % self.__dimension))
        
        elif metodo == 'extraccion':
            
            parte = str(k)
            
            if len(parte) == 1:
                parte = parte[-1:]

            elif len(parte) > 1 and len(parte) < 3:
                parte = parte[-2:]

            elif len(parte) >= 3:
                parte = parte[-3:]

        elif metodo == 'plegado':
            pass
        elif metodo =='cuadrado_medio':
            pass
        elif metodo == 'alfanumerico':
            pass

        else:
            return (round(k % self.__dimension))




if __name__ == '__main__':
    pass