from colaSecuencial import Cola

if __name__=='__main__':
    
    cola = Cola(5)  # Tamaño máximo de la cola es 5

    cola.insertar(10)
    cola.insertar(20)
    cola.insertar(30)

    cola.recorrer()  # Muestra los elementos en la cola

    cola.suprimir()  # Suprime el primer elemento
    cola.recorrer()  # Muestra los elementos restantes

    cola.insertar(40)
    cola.insertar(50)
    cola.insertar(60)  # Intenta insertar más allá del límite

    cola.recorrer()  # Muestra los elementos en la cola