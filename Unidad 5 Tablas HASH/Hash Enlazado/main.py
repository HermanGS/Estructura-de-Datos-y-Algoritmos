"""

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

"""







import numpy as np

import random

class Nodo:
    __dato : None
    __siguiente : None

    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None

    def getSig(self):
        return self.__siguiente
    
    def setSig(self,x):
        self.__siguiente = x
        
    def getDato(self):
        return self.__dato
    
    def setDato(self,x):
        self.__dato = x




class tablahash:
    __dimension : int
    __tabla : np.ndarray
    


    def __init__(self,dim):   # para tener listas de 3 NODOS en cada puntero del arreglo se divide el arreglo en 3 para tener un APROXIMADO

        self.__dimension = dim // 3

        print("dimension final de ",self.__dimension,"para tener APROXIMADAMENTE 3 Colisiones por campo del Arreglo")

        self.__tabla = np.empty(self.__dimension,dtype=object)


    

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


    #primero punteros o primero nodo

    #primero puntero
    def insertar(self,x):

        h = self.hashing(x,'division')
        
        # da igual si esta ocupado o si no
        # se crea un nodo igual porque se sabe que se lo va a insertar

        # self.__tabla[h] es el tope/cabeza/puntero inicial de cada lista

        nuevoNodo = Nodo(x)
        nuevoNodo.setSig(self.__tabla[h])
        self.__tabla[h] = nuevoNodo


    def buscar(self,x):
        h = self.hashing(x,'division')

        
        aux = self.__tabla[h]
        bandera = False

        while aux != None and x != aux.getDato():
            aux = aux.getSig()
            
        if aux != None:
            bandera = True
            return f'Se encontro : {bandera} , valor encontrado : {aux.getDato()}'
        else:
            return f'No se encontro el valor {x}'
        
            
            


    def mostrar(self): #simple sin mostrar a qué campo pertenece
        
        for i in range(self.__dimension):
            
            aux = self.__tabla[i]
            while aux!= None:
                print(f"{aux.getDato()}")
                aux = aux.getSig()
            
        
    def mostrar_2(self):

        for i in range(self.__dimension):
            aux = self.__tabla[i]
            print(f"\n\n Campo {i}\n")
            while aux != None:
                print(f" valor : {aux.getDato()}")
                aux = aux.getSig()

            




if __name__ == '__main__':
    
    elementos = 100
    print("Elementos a ingresar : ",elementos,"\n")
    print("Ingrese la dimension de la tabla hash Encadenada")
    
    m = int(input("ingrese : "))
    
    tabla = tablahash(m)

    for i in range(elementos):
        tabla.insertar(random.randint(0,99))


    #tabla.insertar(55)

    tabla.mostrar_2()

    print( tabla.buscar(22) )



    

    
