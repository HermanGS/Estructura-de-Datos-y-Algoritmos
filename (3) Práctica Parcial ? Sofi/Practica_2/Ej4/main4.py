from pila4 import PilaSecuencial
def hanoi():
    num_discos = int(input("Ingrese el número de discos: "))
    
    pila1 = PilaSecuencial()
    pila2 = PilaSecuencial()
    pila3 = PilaSecuencial()
    
    # Colocar los discos en la pila 1
    for i in range(num_discos, 0, -1):
        pila1.insertar(i)

    jugadas = 0
    min_jugadas = 2**num_discos - 1
    
    print("\nEstado inicial del juego:")
    print("Pila 1: ", end="")
    pila1.recorrer()
    print("Pila 2: ", end="")
    pila2.recorrer()
    print("Pila 3: ", end="")
    pila3.recorrer()

    while not (pila1.vacia() and pila2.vacia() and pila3.ver_tope() == 1):
        print("\nIngrese el movimiento (pila origen y pila destino):")
        origen = int(input("Pila origen (1, 2 o 3): ")) - 1
        destino = int(input("Pila destino (1, 2 o 3): ")) - 1

        # Seleccionar las pilas
        pilas = [pila1, pila2, pila3]
        pila_origen = pilas[origen]
        pila_destino = pilas[destino]

        # Validar si se puede mover el disco
        if pila_origen.vacia():
            print("Jugada imposible: la pila origen está vacía.")
        elif pila_origen.ver_tope() > pila_destino.ver_tope():
            print("Jugada imposible: no puedes mover un disco grande sobre uno más pequeño.")
        else:
            # Mover el disco
            disco = pila_origen.suprimir()
            pila_destino.insertar(disco)
            jugadas += 1

        # Mostrar el estado actual del juego
        print("\nEstado actual del juego:")
        print("Pila 1: ", end="")
        pila1.recorrer()
        print("Pila 2: ", end="")
        pila2.recorrer()
        print("Pila 3: ", end="")
        pila3.recorrer()

    print("\n¡Felicidades! Has completado el juego.")
    print(f"Jugadas realizadas: {jugadas}")
    print(f"Jugadas mínimas posibles: {min_jugadas}")

if __name__=='__main__':
    hanoi()