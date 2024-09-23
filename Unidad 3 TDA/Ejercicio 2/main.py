from  PilaSecuencialE2 import Pila


if __name__ == "__main__":
    print("Ejercicio 2 Division Sucesivas hasta pasar de DECIMAL a Binario")

    pila1 = Pila(20)

    num = int(input("Ingrese un numero para convertir de DECIMAL a BINARIO : "))
    aux = num
    
    while aux!= 0:

        pila1.insertar(aux % 2)
        
        aux = aux // 2

    print("Resultado en Binario : ",end="")
    while not pila1.vacia():
        elemento = pila1.suprimir()
        print(f"{elemento}",end="")
