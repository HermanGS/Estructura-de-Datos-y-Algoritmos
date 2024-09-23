from nodo import Nodo

class ColaEncadenada:
    __primero:Nodo
    __ultimo:Nodo
    __cont:int
    def __init__(self):
        """Operación Crear: Inicializa una cola vacía."""
        self.__primero = None  # Referencia a__primero de la cola
        self.__ultimo = None   # Referencia al final de la cola
        self.__cont=0
    
    def vacia(self):
        """Verifica si la cola está vacía."""
        return self.__cont== 0

    def insertar(self, elemento):
        """Operación Insertar: Inserta un elemento al final de la cola."""
        nuevo_nodo = Nodo(elemento)
        if self.vacia():
            self.__primero = nuevo_nodo
        else:
            self.__ultimo.setsiguiente(nuevo_nodo)
        self.__ultimo = nuevo_nodo
        self.__cont +=1
        print(f"Elemento {elemento} encolado.")

    def suprimir(self):
        """Operación Suprimir: Elimina el elemento a__primero de la cola."""
        if self.vacia():
            print("Error: La cola está vacía.")
            return None
        else:
            elemento = self.__primero.getvalor()
            self.__primero = self.__primero.getsiguiente()
            self.__cont -=1
            if self.__primero is None:  # Si la cola queda vacía
                self.__ultimo = None
            print(f"Elemento {elemento} desencolado.")
            return elemento

    def recorrer(self):
        """Operación Recorrer: Recorre los elementos de la cola e imprime su contenido."""
        if self.vacia():
            print("La cola está vacía.")
        else:
            actual = self.__primero
            while actual is not None:
                print(actual.getvalor())
                actual = actual.getsiguiente()
            print()  # Nueva línea después de recorrer

    

