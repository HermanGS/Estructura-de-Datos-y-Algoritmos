def main():
    numero = 980
    parte = int(str(numero)[-1:])  # Esto te da 80
    print(parte)



def main2():
    numero = 990
    if len(str(numero)) == 1:
        parte = str(numero)[-1:]
    elif len(str(numero)) > 1:
        parte = str(numero)[-2:]

    print('numero = ',numero,'parte = ',parte)

import numpy as np
def main3():


    arreglo = np.array([1, 2, 3, 4, 5])
    longitud = len(arreglo)  # También devuelve la cantidad de elementos
    print(longitud)


main3()
