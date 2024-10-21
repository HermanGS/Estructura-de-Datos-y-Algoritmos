import numpy as np

import random


class objeto:
    pass

    def __init__(self,):
        self.__dato = None

    def __str__(self) -> str:
        return f'{self.__dato}'

    def insertar(self,x):
        self.__dato = x

class buckit:
    __arreglo : np.ndarray
    __dimension : int
    __cant : int

    def __init__(self,dim):
        self.__arreglo = np.empty(dim,dtype=object)
        self.__dimension = dim
        self.__cant = 0

        for i in range(self.__dimension):
            obj = objeto()
            self.__arreglo[i] = obj


    def esta_lleno(self):
        return self.__cant >= self.__dimension

    def insertar(self,x):
        if self.esta_lleno():
            print("Buckit lleno - metodo de Buckit (peligro - falla logica)")
        else: 
            self.__arreglo[self.__cant].insertar(x)  # le insertamos el valor a un campo de un buckit
            self.__cant += 1

    def __str__(self) -> str:
        cadena = ''
        for i in range(self.__cant):
            cadena = cadena + f'{self.__arreglo[i]} - '
        return cadena + f' || cantidad de elementos : {self.__cant} '


class tablahash:
    __tabla : np.ndarray
    __dimension : int
    __buckets : int


    def __init__(self,claves,buckets): #TODAVIA tengo que ver el tema de inicializar los BUCKITS
        self.__buckets = buckets
        self.__dimension = int((claves/self.__buckets)) 
        

        self.__overflow_dim = int((claves/self.__buckets) * 0.2)
        self.__overflow_inicio = self.__dimension

        self.__dimension_total = self.__dimension + self.__overflow_dim

        self.__tabla = np.empty(self.__dimension_total ,dtype=buckit)


        for i in range(self.__dimension_total):
            obj = buckit(self.__buckets)  # self.__buckets es 3 del main
            self.__tabla[i] = obj




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
        h = self.hashing(x,'division')   #sacamos el indice hash

        
        
        cont = 0
        if self.__tabla[h].esta_lleno():  # llegamos al PRIMER buckit y preguntamos si esta lleno ?
            aux_inicio = self.__overflow_inicio # Guardamos el INDICE inicial del Overflow

            while aux_inicio != self.__dimension_total and self.__tabla[aux_inicio].esta_lleno(): #Si esta lleno vamos OVERFLOW
                aux_inicio = aux_inicio + 1

            if aux_inicio == self.__dimension_total:
                print("No hay espacio en OVERFLOW")
            else:
                self.__tabla[aux_inicio].insertar(x)

        else:                           # Si no esta lleno , Insertamos en el PRIMER buckit
            self.__tabla[h].insertar(x)

    def mostrar(self):

        for i in range(len(self.__tabla)):
            print(self.__tabla[i])



if __name__ == '__main__':
    claves = 1000

    print("la cantidad de elementos a almacenar es de : ",claves)

    #print("Ingrese el tamaño de la tabla Hash : ")
    #m = int(input("tamaño : "))


    tabla = tablahash(claves,3)

    for i in range(0,999):
        tabla.insertar(random.randint(0,999))


    tabla.mostrar()

