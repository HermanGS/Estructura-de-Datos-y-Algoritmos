#Es Dinamica la pila Encadenada
#La podemos hacer con un arreglo numpy

import numpy as np
from Nodo import Nodo

class Pila:
    #__items : np.ndarray No se NECESITA arreglo para esta Estructura, EL TOPE funciona como CABEZA de la lista PILA
    __tope : None
    __cant : int # La cantidad acá se usa de manera diferente, ya no es el tope de los ESPACIOS DISPONIBLES sino que es un CONTADOR me parece
    #Contador de la cantida de NODOS que existen

    def __init__(self,tope = None, cant = 0) -> None:
        self.__tope = tope
        self.__cant = cant
        #self.__items = np.empty

    def vacia(self):
        return (self.__cant == 0)

    def insertar(self,x):
        NuevoNodo = Nodo(x)
        #NuevoNodo.CambiarDato(x)
        NuevoNodo.CambiarSig(self.__tope)
        self.__tope = NuevoNodo
        self.__cant += 1
        print(f"cantidad de elementos en pila : {self.__cant}")
        return NuevoNodo.retornaDato()

    def suprimir(self):
        if self.vacia():
            print("No se puede suprimir, esta vacia")
        else:
            aux = self.__tope
            x = aux.retornaDato()
            self.__tope = self.__tope.retornaSig()
            self.__cant -= 1
            del(aux)
            return (x)


    def recorrer(self): # para eliminar # para recorrer # UNO VA A USAR UN AUXILIAR PARA NO PERDER LA CABEZA (TOPE)
        if self.vacia():
            print("La Pila esta vacia No se puede Recorrer")
        else:
            aux = self.__tope

            print("Recorriendo la PILA")

            while aux != None:
                print(f"{aux.retornaDato()}")
                aux = aux.retornaSig()


    def desapilar(self): # para eliminar # para recorrer # UNO VA A USAR UN AUXILIAR PARA NO PERDER LA CABEZA (TOPE)
        if self.vacia():
            print("La Pila esta vacia No se puede Desapilar")
        else:
            aux = self.__tope

            print("Desapilando la PILA")

            while aux != None:
                print(f"{self.suprimir()}")
                aux = aux.retornaSig()
