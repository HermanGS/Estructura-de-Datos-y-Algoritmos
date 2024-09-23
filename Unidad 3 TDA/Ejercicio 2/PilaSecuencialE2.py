#es estática la Pila secuencial
#la podemos hacer con un arreglo numpy

#LA UNICA DIFERENCIA ES QUE RECORRER MUESTRA SIN SALTO DE LINEA o algunas lineas comentadas



import numpy as np

class Pila:
    __items : np.ndarray
    __tope : int
    __cant : int # es para la creación de la pila como la DIMENSION
    #__dimension : int # crear la pila con la cantidad reservada en memoria de dimension
    def __init__(self,cant=10,tope=-1):
        self.__items = np.empty(cant,dtype=int)
        self.__tope = tope
        self.__cant = cant
     #  self.__dimension = dimension
        print(f"PILA CREADA, tope = [{self.__tope}] (debe de ser -1)")

    def insertar(self,x): # se usa el tope para acceder a la PILA como INDICE porque la POLITCA implica insertar y suprimir por el mismo lugar
        #print("tope = ",self.__tope)
        #print("cant = ",self.__cant)
        if self.__tope < self.__cant -1: # tope(cantidad de elementos disponibles) y cantidad (cantidad de espacios disponibles)
            self.__tope += 1 # tope deja de ser -1 y ahora puede usarse como 0 para acceder a la Pila
            self.__items[self.__tope] = x
            
            print(f"Despues de INSERTAR : {x} \ntope = ",self.__tope)
            print("cant = ",self.__cant - 1)
        else:
            print("La Pila esta llena NO SE PUEDE agregar otro elemento")

    def suprimir(self):
        if self.vacia(): 
            print("La Pila esta vacia NO SE PUEDE suprimir el ultimo elemento")
        else:    
            x = self.__items[self.__tope] 
            self.__tope -=1
            #print("elemento eleminado : ",x)
            return x      

    def recorrer(self):
        if not self.vacia():
            for i in range(self.__tope, -1, -1):  # Itera desde el tope hacia abajo Argumentos (inicio, fin, cantidad de pasos)
                print(f"i = {i}, elemento = {self.__items[i]}")
        else:
            print("la Pila esta vacia no hay nada que recorrer")

    def vacia(self):
        return (self.__tope == -1) # si tope = -1 significa que la pila está vacía, está analizando la expresión
    
    def lleno(self):
        return (self.__tope == self.__cant - 1)

    
