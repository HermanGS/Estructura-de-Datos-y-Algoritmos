from clasePila3 import PilaEncadenada


if __name__ == '__main__':
    pila = PilaEncadenada()
    resultado = 1
    n = int(input('Ingrese un numero: '))
    
    while n >= 0:
        if n>0:
            pila.insertar(n)  # Empilar n en el Pila.
        elif n==0:
            pila.insertar(1)
        n-= 1
    while not pila.vacia():
            resultado *= pila.suprimir()

    print(f"Factorial :{resultado}")