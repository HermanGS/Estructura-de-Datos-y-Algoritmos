import numpy as np

class PilaSecuencial:
    __items:np.ndarray
    __tope:int
    def __init__(self):
        self.__items = np.empty(10, dtype=object)  # Crear un arreglo vacío de enteros
        self.__tope = -1  # Inicializar el índice del tope en -1
        

    def vacia(self):
        return self.__tope == -1
    def llena(self):
        return self.__tope== len(self.__items)
    
    def insertar(self, item):
        if self.llena()is False:
            self.__tope += 1
            self.__items[self.__tope] = item
        else:   
            print( 'NO es posible insertar el elemento, la pila esta llena')

    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
            return None
        item = self.__items[self.__tope]
        self.__tope -= 1
        return item

    def recorrer(self):
        if self.vacia():
            print("Pila vacía")
        else:
            for i in range(self.__tope, -1, -1):
                print(self.__items[i])
    
    def ver_tope(self):
        if self.vacia():
            return float('inf')  # Retornar infinito si la pila está vacía (para comparaciones)
        return self.__items[self.__tope]