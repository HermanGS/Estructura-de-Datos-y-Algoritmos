import numpy as np  


class Grafo:

    def __init__(self) -> None:
        self.__arreglo = np.zeros((3,3),dtype=int)
        self.__arreglo[0,0] = 1
        self.__arreglo[1,1] = 2
        self.__arreglo[2,2] = 4
        self.__arreglo[0,1] = 3
        self.__arreglo[1,2] = 6
        self.__arreglo[2,0] = 5


    def mostrar(self):
        print(self.__arreglo)



if __name__ == '__main__':

    print("grafo")

    g = Grafo()
    g.mostrar()