import numpy as np

class Cola:
    __items:np.ndarray
    __pr:int
    __ul:int
    __cant:int
    def __init__(self):
        """Inicializa una cola con un tamaño máximo fijo."""
        
        self.__items = np.empty(5,dtype=int)# Arreglo para almacenar los elementos (inicialmente vacío)
        self.__pr = 0  # Índice del primer elemento (frente)
        self.__ul = 0  # Índice del último elemento (final)
        self.__cant = 0  # Cantidad de elementos en la cola

    def vacia(self):
        """Verifica si la cola está vacía."""
        return self.__cant == 0

    def llena(self):
        """Verifica si la cola está llena."""
        return self.__cant == len(self.__items)

    def insertar(self, x):
        """Inserta un elemento en la cola si no está llena."""
        if not self.llena():
            self.__items[self.__ul] = x
            self.__ul = (self.__ul + 1) % len(self.__items) # Ajusta el índice para la cola circular
            self.__cant += 1
            print(f"Elemento {x} insertado en la cola.")
        else:
            print("Error: La cola está llena, no se puede insertar el elemento.")

    def suprimir(self):
        """Suprime y retorna el elemento del frente de la cola si no está vacía."""
        if self.vacia():
            print("Error: Cola vacía")
            return None
        else:
            x = self.__items[self.__pr]
            self.__pr = (self.__pr + 1) % len(self.__items) # Ajusta el índice para la cola circular
            self.__cant -= 1
            return x

    def recorrer(self):
        """Recorre y muestra los elementos de la cola en orden."""
        if self.vacia():
            print("La cola está vacía.")
        else:
            print("Elementos en la cola:")
            i = self.__pr
            for _ in range(self.__cant):
                print(self.__items[i])
                i = (i + 1) % len(self.__items)  # Avanza de forma circular

   