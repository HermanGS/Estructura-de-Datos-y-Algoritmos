
import random
import numpy as np
class Nodo():
    
    dato: int
    siguiente: object

    def __init__(self,dato) -> None:
        self.dato = dato
        self.siguiente = None

    def __str__(self) -> str:
        return f"Dato: {self.dato} ----"


class Hash():
    arregloEncadenado: np.array
    cabeza: Nodo
    tamaño = 61


    def __init__(self) -> None:

        self.arregloEncadenado = np.full(self.tamaño, Nodo(None)) 
        
    def insertar(self,indice,valor):

        nuevo = Nodo(valor)
        
        if self.arregloEncadenado[indice] == None:
            self.arregloEncadenado[indice] = nuevo
            
        else:
            aux = self.arregloEncadenado[indice]
            self.arregloEncadenado[indice] = nuevo
            self.arregloEncadenado[indice].siguiente = aux

    
    def mostrar(self):

        for i in range(61):
            print(f"Indice {i}")
            h = 0
            
            if self.arregloEncadenado[i].siguiente == None:
                print(f"\n----El indice {i} no tiene ninguna ocurrencia-----")
            else:

                while self.arregloEncadenado[i].siguiente != None:
            
                    print(f"Dato del Nodo {h}: {self.arregloEncadenado[i].dato}")            
                    h+=1
                    self.arregloEncadenado[i].siguiente = self.arregloEncadenado[i].siguiente.siguiente
            
                
    def busqueda(self,valor):
        indiceResuelto = self.hash_plegado(valor)
        if self.arregloEncadenado[indiceResuelto] != None:
            print(f"\nValor buscado y encontrado : {self.arregloEncadenado[indiceResuelto].dato}\n")

        

    def hashing(self,clave=0):

        claveR = clave % self.tamaño

        return claveR
    
    def hash_plegado(self,clave=0):
      
        clave_str = str(clave)    
        n = 2
        partes = [clave_str[i:i+n] for i in range(0, len(clave_str), n)]
        suma = sum(int(part) for part in partes if part)
        ClaveFinal = self.hashing(suma)
        return ClaveFinal
    


if __name__ == "__main__":
    prueba = Hash()
    
    for i in range(61):
        valor = random.randint(0, 10000)
        IndiceFinal = prueba.hash_plegado(valor)
        prueba.insertar(IndiceFinal,valor)

        prueba.mostrar()
    op = "1"
    while op != "0":    
        op = input("ingrese una opcion\n")
        if op == "1":
            valor = input("ingrese un valor a buscar \n")
            prueba.busqueda(valor)
        else:
            op = "0"
