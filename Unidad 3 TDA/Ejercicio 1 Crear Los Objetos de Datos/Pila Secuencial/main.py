from PilaSecuencial import Pila

if __name__ == "__main__":
    
    pila1 = Pila()
    
    print("Pila Secuencial")

    
    print("Elja una Opción :")
    
    print("1. Ingresar un elemento a la Pila.\n2. Suprimir un elemento de la Pila.\n3. Recorrer la Pila.\n4. Verificar si esta vacia.\n5. Salir de las operaciones\n6. Consultar si esta llena?")

    op = input("Ingrese 1 o 2 o 3 o 4 o 5 :    ")
    op = int(op)
    #pollo
    while op != 5:
        

        if op == 1:
            print("\nIngrese el valor del elemento a la Pila.")
            x = int(input(" valor : "))
            pila1.insertar(x)

        elif op == 2:
            print("\nSuprimir un elemento de la Pila (Se suprime el ultimo elemento por ser FIFO)")
            pila1.suprimir()

        elif op == 3:
            print("\nRecorriendo la Pila.")
            pila1.recorrer()

        elif op == 4:
            print("\nVerificando si esta vacia.")
            if pila1.vacia():
                print("La Pila Esta Vacia")
            else:
                print("La Pila Tiene Elementos")
        elif op == 5:
            print("\nSaliendo de las operaciones ...")
            
        elif op == 6:
            if pila1.lleno():
                print("La PILA esta LLENA, no se puede agregar otro elemento")
            else:
                print("La PILA NO esta LLENA, si se pueden agregar otros elementos")

        print("\n1. Ingresar un elemento a la Pila.\n2. Suprimir un elemento de la Pila.\n3. Recorrer la Pila.\n4. Verificar si esta vacia.\n5. Salir de las operaciones\n6. Consultar si esta llena?")
        op = int(input("Ingrese 1 o 2 o 3 o 4 o 5 o 6 :    "))
