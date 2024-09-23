import numpy as np

class Cola:
    __arre: np.ndarrey
    __max : int
    __cant : int
    __pri : int
    __ul : int


    def __init__(self,xmax) -> None:
        self.__max = xmax
        self.__cant = 0
        self.__pri = 0
        self.__ul = 0
        self.__arre = np.empty(self.__max,dtype=int)


    def vacia(self):
        return (self.__cant == 0)
    
    def insertar(self,x):
        if self.__cant < self.__max:
            self.__arre[self.__ul] = x
            self.__ul = (self.__ul+1)%self.__max
            self.__cant += 1
        else:
            print("cola vacia")


    def suprimir(self):
        if not self.vacia():
            x = self.__arre[self.__pri]
            self.__pri = (self.__pri + 1) % self.__max
            self.__cant -= 1
            return x
        else:
            print("cola vacia no se puede suprimir")


    def recorrer(self):
        if self.vacia():
            print("ta vacia")
        else:
            i = self.__pri
            for _ in range(self.__cant):
                print(f"indice {i} elemento : {self.__arre[i]}")
                i = (i+1)%self.__max
