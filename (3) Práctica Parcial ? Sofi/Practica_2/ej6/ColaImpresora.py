from ClaseNodo import Nodo
class Cola:
    __pr:Nodo
    __ul:Nodo
    __cant:int
    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0

    def insertar(self, x):
        nuevo_nodo = Nodo(item=x)
        if self.__ul is None:
            self.__pr = nuevo_nodo
        else:
            self.__ul.cargar_sig(nuevo_nodo)
        self.__ul = nuevo_nodo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            return None
        else:
            item = self.__pr.obtener_item()
            self.__pr = self.__pr.obtener_sig()
            self.__cant -= 1
            if self.vacia():
                self.__ul = None
            return item

    def recorrer(self):
        aux = self.__pr
        while aux is not None:
            print(aux.obtener_item())
            aux = aux.obtener_sig()
