import numpy as np

import random

class Nodo:
    __dato : None
    __siguiente : None

    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None

    def retornaSig(self):
        return self.__siguiente
    
    def CambiarSig(self,x):
        self.__siguiente = x
        
    def retornaDato(self):
        return self.__dato
    
    def CambiarDato(self,x):
        self.__dato = x



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




class tablahash:
    __dimension : int
    __tabla : np.ndarray
    


    def __init__(self,dim):   # para tener listas de 3 NODOS en cada puntero del arreglo se divide el arreglo en 3 para tener un APROXIMADO

        self.__dimension = dim // 3
        self.__tabla = np.empty(self.__dimension,dtype=None)


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




    def insertar(self,x):

        h = self.hashing(x,'division')

        if 


        
            








if __name__ == '__main__':
    pass