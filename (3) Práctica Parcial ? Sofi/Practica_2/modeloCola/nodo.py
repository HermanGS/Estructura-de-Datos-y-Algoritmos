class Nodo:
    def __init__(self, item=0, sig=None):
        """Inicializa un nodo con un item y un puntero al siguiente nodo."""
        self.__item = item  # Valor almacenado en el nodo
        self.__sig = sig    # Puntero a la siguiente nodo

    def obtener_item(self):
        """Retorna el valor almacenado en el nodo."""
        return self.__item

    def cargar_item(self, xitem):
        """Cambia el valor almacenado en el nodo."""
        self.__item = xitem

    def cargar_sig(self, xtope):
        """Asigna el siguiente nodo."""
        self.__sig = xtope

    def obtener_sig(self):
        """Retorna el puntero al siguiente nodo."""
        return self.__sig
