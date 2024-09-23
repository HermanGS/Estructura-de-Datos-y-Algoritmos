from claseColaSecuencial import Cola

if __name__=='__main__':
    cola = Cola()  # Tamaño máximo de la cola es 5

# Insertar elementos
    cola.insertar(10)
    cola.insertar(20)
    cola.insertar(30)

# Recorrer e imprimir elementos
    cola.recorrer()

# Suprimir un elemento
    cola.suprimir()

# Recorrer e imprimir elementos después de la supresión
    cola.recorrer()

# Intentar insertar más elementos
    cola.insertar(40)
    cola.insertar(50)
    cola.insertar(60)  # Esto debería mostrar un mensaje de error

# Recorrer e imprimir todos los elementos
    cola.recorrer()

