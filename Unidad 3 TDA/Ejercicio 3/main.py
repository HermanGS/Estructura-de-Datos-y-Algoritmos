
from PilaSecuencial import Pila

if __name__ =="__main__":
    print("Ejercicio 3 factorial")

    

    num = int(input("Ingrese el numero para calcular su factorial = "))
    
    pila1 = Pila(num-1)

    aux = num

    while aux != 1:
        pila1.insertar(aux)
        aux = aux -1

    while not pila1.vacia():
        aux = aux * pila1.suprimir()

    print(f"Del numero {num} se obtiene su factorial = {aux} ")

        

