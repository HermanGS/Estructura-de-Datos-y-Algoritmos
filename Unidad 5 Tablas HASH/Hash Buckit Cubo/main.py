import numpy as np

import random


class objeto:
    pass

    def __init__(self,dato):
        self.__dato = dato


class buckit:
    __arreglo : np.ndarray
    __cant : int

    def __init__(self,dim):
        self.__arreglo = np.empty(dim,dtype=object)
        self.__cant = 0

class tablahash:
    __tabla : np.ndarray
    __dimension : int
    __buckets : int


    def __init__(self,claves,buckets):
        self.__buckets = buckets

        self.__dimension = (claves/self.__buckets) 
        
        self.__tabla = np.empty(self.__dimension + (claves/self.__buckets) * 0.2 ,dtype=object)



    def hashing(self,k,metodo):
        
        if metodo == 'division':
            return (int(k % self.__dimension))
        

        elif metodo == 'extraccion':
            
            parte = str(k)
            
            if len(parte) == 1:
                parte = parte[-1:]

            elif len(parte) > 1 and len(parte) < 3:
                parte = parte[-2:]

            elif len(parte) >= 3:
                parte = parte[-3:]

            return parte % self.__dimension
        

        elif metodo == 'extraccion_v2':
            parte = str(k)[-3:]   # simplifica todo lo de arriba en una sola linea
            
            return int(parte) if parte else 0    #retorna la conversion a entero SII existe la cadena SINO 0


        elif metodo == 'plegado': #conviene totalmente que el resultado supere al tamaño M para así ocupar todas los campos del Arreglo Hash
            pass


        elif metodo =='numero_medio':
            
        
            
            parte = str(k)
            numero_medio = int(len(parte)) // 2
            
            if len(parte) == 2:
                return int(parte )  % self.__dimension  # Usa el número completo 
            
            # string slicing corta el STRING en un RANGO donde el primer valor se cuenta y el segundo NO es INCLUYENTE  b[2:5] (va desde el 2 al 4)
            # string slicing del numero medio Toma el numero_medio y uno anterior   si numero_medio = 2  entonces Toma (1,2) {numero_medio+1 para incluir al numero medio como FINAL}
            
            return ( int(parte[numero_medio-1:numero_medio+1])  % self.__dimension )
            

        elif metodo == 'cuadrado_medio':
            parte = str(k)
            numero_medio = int(len(parte)) // 2

            if len(parte) == 2:
                return ( ( int(parte) ) ** 2 ) % self.__dimension
            
            return ( ( int(parte[numero_medio-1:numero_medio+1]) ) ** 2 ) % self.__dimension 
            
            
        elif metodo == 'alfanumerico':
            
            parte = str(k)
            suma = 0
            for i in parte:
                suma = suma + ord(i)
            
            return suma % self.__dimension
            
                
                

        else:
            return (round(k % self.__dimension))

    def insertar(self,x):
        pass

if __name__ == '__main__':
    claves = 1000

    print("la cantidad de elementos a almacenar es de : ",claves)

    print("Ingrese el tamaño de la tabla Hash : ")
    m = int(input("tamaño : "))


    tabla = tablahash(claves,3)



