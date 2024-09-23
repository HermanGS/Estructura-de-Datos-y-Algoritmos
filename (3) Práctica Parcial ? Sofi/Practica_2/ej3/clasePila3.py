from Nodo import Nodo

class PilaEncadenada:
    __tope:Nodo
    __cont:int
    def __init__(self):
        self.__tope = None
        self.__cont=0


    def insertar(self, item):
        """Inserta un nuevo elemento en la pila."""
        nuevo_nodo = Nodo(item)
        nuevo_nodo.setSiguiente(self.__tope)
        self.__tope = nuevo_nodo
        self.__cont +=1

    def suprimir(self):
        """Elimina el elemento en el tope de la pila y lo retorna."""
        if self.vacia():
            print("Pila vacía")
            return None
        else:
            item = self.__tope.getItem()
            self.__tope = self.__tope.getsiguiente()
            self.__cont -=1
            return item
    def recorrer(self):
        aux=self.__tope
        while aux is not None:
            print(aux.getItem())
            aux=aux.getsiguiente()

    def vacia(self):
        """Verifica si la pila está vacía."""
        return self.__cont == 0


    
