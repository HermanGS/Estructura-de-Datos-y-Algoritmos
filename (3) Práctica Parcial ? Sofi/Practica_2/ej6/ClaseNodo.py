class Nodo:
    __item:object
    __sig:object
    def __init__(self, item):
        self.__item = item
        self.__sig = None

    def obtener_item(self):
        return self.__item

    def cargar_item(self, xitem):
        self.__item = xitem

    def cargar_sig(self, xtope):
        self.__sig = xtope

    def obtener_sig(self):
        return self.__sig
