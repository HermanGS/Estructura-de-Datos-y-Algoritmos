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



    
    def insertar(self,dato):
        self.__dato = dato
        self.__libre = False


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



            


        


    def insertar(self,x): # la clave en si es el dato

        h = self.hashing(x,'division')

        if self.__tabla[h].getLibre():
            self.__tabla[h].setDato(x)
            self.__tabla[h].setOcupado()

        else :
            contador = 0
            while self.__tabla[h].getLibre() == False and contador < self.__dimension:
                h = (h-1) % self.__dimension
                contador = contador + 1

            if self.__tabla[h].getLibre() == True:
                self.__tabla[h].insertar(x)  # inserta y pone OCUPADO (libre = False)


    

    def mostrar(self):
        for i in range(self.__dimension):
            print('indice : ',i,' valor : ',self.__tabla[i])


    def buscar(self,x):

        h = self.hashing(x,'division')

        bandera = False

        while self.__tabla[h].getDato() != x and self.__tabla[h].getLibre() == False:
            h = (h-1) % self.__dimension

        if self.__tabla[h].getLibre() == False:
            bandera = True

        return bandera
            

if __name__ == '__main__':
    
    print("Ejercicio 2 Corregido Con un buen factor de carga")
    
    elementos = 1000

    print("la cantidad de elementos a ingresar es de ",elementos)
    
    
    print("Ingrese el tamño de la tabla hash 8 (Mejor si es numero PRIMO) ")

    m = int(input('Ingrese el tamanio :  '))

    tabla = tablahash(m)


    tabla.insertar(1230)

    for i in range(1000):
        tabla.insertar(random.randint(0,998))

    tabla.mostrar()


    print("buscando 1230")
    b = tabla.buscar(1230)

    if b == True:
        print("Se encontro el elemento")
    else:
        print("No se encontro el elemento")




