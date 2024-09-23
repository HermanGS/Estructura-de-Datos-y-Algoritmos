from nodo import Nodo
class Cola:
    def __init__(self):
        """Inicializa una cola vacía."""
        self.__pr = None  # Puntero al primer elemento
        self.__ul = None  # Puntero al último elemento
        self.__cant = 0   # Cantidad de elementos en la cola

    def vacia(self):
        """Verifica si la cola está vacía."""
        return self.__cant == 0

    def insertar(self, x):
        """Inserta un elemento en la cola."""
        nuevo_nodo = Nodo(item=x)  # Crea una nueva Nodo
        if self.__ul is None:
            # Si la cola está vacía, la nueva Nodo será tanto el frente como el final
            self.__pr = nuevo_nodo
        else:
            # De lo contrario, agrega la nueva Nodo al final
            self.__ul.cargar_sig(nuevo_nodo)
        self.__ul = nuevo_nodo
        self.__cant += 1
        return self.__ul.obtener_item()

    def suprimir(self):
        """Suprime y retorna el elemento del frente de la cola."""
        if self.vacia():
            print("Cola vacía")
            return None
        else:
            item = self.__pr.obtener_item()
            self.__pr = self.__pr.obtener_sig()
            self.__cant -= 1
            if self.vacia():
                self.__ul = None  # Si la cola queda vacía, el final también debe ser None
            return item

    def recorrer(self):
        """Recorre e imprime los elementos de la cola."""
        aux = self.__pr
        while aux is not None:
            print(aux.obtener_item())
            aux = aux.obtener_sig()
