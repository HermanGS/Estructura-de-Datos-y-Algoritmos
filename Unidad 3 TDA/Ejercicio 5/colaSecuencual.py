import numpy as np


class Cola:
    __items: np.ndarray
    __primero: int
    __ultimo: int
    __cant : int
    __max : int


    def __init__(self,xmax=10):
        self.__max = xmax
        self.__primero = 0
        self.__ultimo = 0
        self.__cant = 0
        self.__items = np.empty(xmax,dtype=int)

        print("Cola Creada")

    def vacia(self):
        return (self.__cant == 0)

    def llena(self):
        return (self.__cant == self.__max)
    
    def insertar(self,x):
        if self.__cant < self.__max:
            self.__items[self.__ultimo] = x
            self.__ultimo = ( self.__ultimo + 1 ) % self.__max
            self.__cant += 1
            print(f"Elemento {x} insertado en la cola")
        else:
            print(f"cola llena no se puede ingresar {x} a la Cola")

    def suprimir(self):
        if not self.vacia():
            x = self.__items[self.__primero]
            self.__primero = (self.__primero + 1) % self.__max
            self.__cant -= 1
        else:
            x = "cola vacía"
        return x
    

    def recorrer(self):
        if self.vacia():
            print("cola vacia no hay nada que mostrar")
        
        else:
            i = self.__primero
            for _ in range(self.__cant):
                print(f" indice : {i}  elemento : {self.__items[i]}")
                i = (i+1)%self.__max