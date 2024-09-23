
def generar_menu(origen):
    #destino = ""
    print("-.-.- Generando Menu -.-.-")
    
    if origen == 'A':
        print("elija la torre Destino 'B' o 'C' ")
        destino = str(input("    "))
        
        #print(f"destino = {destino}")
        
        while destino != 'B' and destino!= 'C':
            print("VUELVA A ELEGIR -- elija la torre Destino 'B' o 'C' ")
            destino = input("    ")  
    
    
    elif origen == 'B':
        print("elija la torre Destino 'A' o 'C' ")
        destino = input("    ")
        
        while destino != 'A' and destino!= 'C':
            print("VUELVA A ELEGIR -- elija la torre Destino 'A' o 'C' ")
            destino = input("    ") 

    elif origen == 'C':
        print("elija la torre Destino 'A' o 'B' ")
        destino = input("    ")
        
        while destino != 'A' and destino!= 'B':
            print("VUELVA A ELEGIR -- elija la torre Destino 'A' o 'B' ")
            destino = input("    ")

    return destino
    

def accion_mover(origen,destino):
    
    if origen == 'A':
        x = pila1.suprimir()
        print("valor de x : ",x)
        
        if destino == 'B':
             
            if  pila2.vacia(): # Si está vacía la pila
                pila2.insertar(x)
            
            else:              # Si no esta vacía la pila
        
                y = pila2.suprimir()
                if x < y:  # si x es Menor inserción en DESTINO y si x es Mayor inserción como estaba ANTES
                    print("Se logro el pasaje")
                    pila2.insertar(y)
                    pila2.insertar(x)
                else:
                    print("No se pudo... Devolviendo cada uno a su lugar ...")
                    pila1.insertar(x)
                    pila2.insertar(y)

        elif destino == 'C':

            if pila3.vacia():
                pila3.insertar(x)

            else: 
                y = pila3.suprimir()
                
                if x < y: 
                    print("Se logro el pasaje")
                    pila3.insertar(y)
                    pila3.insertar(x)
                else:
                    print("No se pudo... Devolviendo cada uno a su lugar ...")
                    pila1.insertar(x)
                    pila3.insertar(y)
   
    elif origen == 'B':
    
        x = pila2.suprimir()
        print("valor de x : ",x)
        
        if destino == 'A':
                
            if  pila1.vacia(): # Si está vacía la pila
                pila1.insertar(x)
            
            else:              # Si no esta vacía la pila
        
                y = pila1.suprimir()
                if x < y:  # si x es Menor inserción en DESTINO y si x es Mayor inserción como estaba ANTES
                    print("Se logro el pasaje")
                    pila1.insertar(y)
                    pila1.insertar(x)
                else:
                    print("No se pudo... Devolviendo cada uno a su lugar ...")
                    pila2.insertar(x)
                    pila1.insertar(y)

        elif destino == 'C':

            if pila3.vacia():
                pila3.insertar(x)

            else: 
                y = pila3.suprimir()
                
                if x < y: 
                    print("Se logro el pasaje")
                    pila3.insertar(y)
                    pila3.insertar(x)
                else:
                    print("No se pudo... Devolviendo cada uno a su lugar ...")
                    pila2.insertar(x)
                    pila3.insertar(y)

    elif origen == 'C':
    
        x = pila3.suprimir()
        print("valor de x : ",x)
        
        if destino == 'A':
                
            if  pila1.vacia(): # Si está vacía la pila
                pila1.insertar(x)
            
            else:              # Si no esta vacía la pila
        
                y = pila1.suprimir()
                if x < y:  # si x es Menor inserción en DESTINO y si x es Mayor inserción como estaba ANTES
                    print("Se logro el pasaje")
                    pila1.insertar(y)
                    pila1.insertar(x)
                else:
                    print("No se pudo... Devolviendo cada uno a su lugar ...")
                    pila3.insertar(x)
                    pila1.insertar(y)

        elif destino == 'B':

            if pila2.vacia():
                pila2.insertar(x)

            else: 
                y = pila2.suprimir()
                
                if x < y: 
                    print("Se logro el pasaje")
                    pila2.insertar(y)
                    pila2.insertar(x)
                else:
                    print("No se pudo... Devolviendo cada uno a su lugar ...")
                    pila3.insertar(x)
                    pila2.insertar(y)



        




from PilaSecuencial import Pila

if __name__ == "__main__":
    print("Ejercicio 4 Columnas de juguete \n")


    numero = int(input("ingrese cantidad de discos para jugar: "))
    pila1 = Pila(numero)
    pila2 = Pila(numero)
    pila3 = Pila(numero)


    auxnum = numero
    """
    while auxnum != 0:
        pila1.insertar(auxnum)
        auxnum -= 1
    """
    
    for i in range(auxnum,0,-1):
        pila1.insertar(i)
    
    print("mostrando lo que tiene la PILA 1\n")
    pila1.recorrer()
    print("\nfin mostrar\n")

    #not pila1.vacia() NO SE como implementarlo
    while not pila3.lleno():

        print("-.-.- COMIENZA EL JUEGO -.-.- \n")
        
        pila_origen = str(input("seleccione con 'A', 'B', o 'C' la pila origen : "))
        
        
        #print("pila_origen : ",pila_origen)
        #print(f"origen == 'A' : {(pila_origen == 'A')}")

        pila_destino = generar_menu(pila_origen)
        
        print(f"La pila ORIGEN es '{pila_origen}' y la pila DESTINO es '{pila_destino}'")

        accion_mover(pila_origen,pila_destino)

        
        #print("Queres que se te muestre como quedaron las pilas?")
        #p = str(input("[y/n] :\n"))
        #if p == 'y':

        print("\n\n\n")
        print("MOSTRANDO COMO QUEDARON LAS PILAS :\n")
        print("pila A :\n")
        pila1.recorrer()
        print("")
        print("pila B :\n")
        pila2.recorrer()
        print("")
        print("pila C :\n")
        pila3.recorrer()
        print("")



        
         


        