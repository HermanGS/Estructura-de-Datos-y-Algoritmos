class Cola:
    def __init__(self, maximo=0):
        """Inicializa una cola con un tamaño máximo fijo."""
        self.__max = maximo  # Tamaño máximo de la cola
        self.__items = [None] * maximo  # Arreglo para almacenar los elementos (inicialmente vacío)
        self.__pr = 0  # Índice del primer elemento (frente)
        self.__ul = 0  # Índice del último elemento (final)
        self.__cant = 0  # Cantidad de elementos en la cola

    def vacia(self):
        """Verifica si la cola está vacía."""
        return self.__cant == 0

    def insertar(self, x):
        """Inserta un elemento en la cola si no está llena."""
        if self.__cant < self.__max:
            self.__items[self.__ul] = x
            self.__ul = (self.__ul + 1) % self.__max  # Ajusta el índice para la cola circular
            self.__cant += 1
            return x
        else:
            return 0  # La cola está llena

    def suprimir(self):
        """Suprime y retorna el elemento del frente de la cola si no está vacía."""
        if self.vacia():
            print("Error: Cola vacía")
            return 0
        else:
            x = self.__items[self.__pr]
            self.__pr = (self.__pr + 1) % self.__max  # Ajusta el índice para la cola circular
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
                i = (i + 1) % self.__max  # Avanza de forma circular


