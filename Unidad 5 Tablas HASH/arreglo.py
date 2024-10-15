import numpy 



def main():
    arreglo = numpy.empty(2,dtype = int)
    arreglo[0] = 12
    print (arreglo[0])

def main2():
    k = 123
    parte = str(k)
    for i in range(len(parte)):
        print(sum(ord(parte[i])))

def main3():
    parte = 'hola'
    for i in parte:
        print(i)

def main4():
    k = 123
    parte = str(k)
    print(parte)

def main5():
    k = 123
    parte = str(k)
    for i in parte:
        print(i)

def main6():
    k = 123
    parte = str(k)
    for i in parte:
        print(ord(i))

def main7():
    k = 123
    parte = str(k)
    for i in parte:
        print(sum(ord(i))) # no funciona

def main8():
    k = 123
    parte = str(k)
    suma = 0
    for i in parte:
        suma = suma + ord(i)
        print(suma)
    print(suma)


def cuadrado1():
            k=98
            parte = str(k)
            numero_medio = int(len(parte)) // 2
            
            if len(parte) == 2:
                return int(parte)  # Podría usar el número completo
            
            # string slicing corta el STRING en un RANGO donde el primer valor se cuenta y el segundo NO es INCLUYENTE  b[2:5] (va desde el 2 al 4)
            # string slicing del numero medio Toma el numero_medio y uno anterior   si numero_medio = 2  entonces Toma (1,2) {numero_medio+1 para incluir al numero medio como FINAL}
            
            return int(parte[numero_medio-1:numero_medio+1]) % 131 


cuadrado1()