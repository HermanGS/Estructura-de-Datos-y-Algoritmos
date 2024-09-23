from colaSecuencual import Cola


if __name__ =="__main__":
    print("cola")
    cola= Cola(5)


# Insertar elementos
    cola.insertar(10)
    cola.insertar(20)
    cola.insertar(30)

# Recorrer e imprimir elementos
    cola.recorrer()

# Suprimir un elemento
    cola.suprimir()
    print("....")
# Recorrer e imprimir elementos después de la supresión
    cola.recorrer()

# Intentar insertar más elementos
    cola.insertar(40)
    cola.insertar(50)
    cola.insertar(60)  # Esto debería mostrar un mensaje de error

# Recorrer e imprimir todos los elementos
    print("")
    cola.recorrer()
    



