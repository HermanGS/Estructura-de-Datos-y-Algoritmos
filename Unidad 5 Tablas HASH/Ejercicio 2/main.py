'''
Ejercicio Nº 1

Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones
" direccionamiento abierto ", utilizando como " función de transformación de claves el método de la
división ", procesando las claves sinónimas a través de la " secuencia de Prueba Lineal " y considerando
trabajar con 1000 claves numéricas que serán generadas aleatoriamente a través de la función rand.
Se pide calcular la Longitud de la Secuencia de Prueba al Buscar una clave teniendo en cuenta:

1. El tamaño de la tabla Hash no es un número primo.
2. El tamaño de la tabla Hash sí es un número primo.

Realice un breve análisis comparativo basado en las dos consideraciones anteriores.
Realice un breve análisis comparativo basado en las dos consideraciones anteriores.

'''
import random



import numpy as np

class tablahash:

    __dimension: int
    __tabla : np.ndarray
    __cant : int

    # -------------------------------Funciones Principales------------------------------- #

    def __init__(self,dim):
        self.__dimension = dim
        self.__tabla = np.zeros(self.__dimension,dtype=int)
        self.__cant = 0

    
    def hashing(self,k,metodo):
        
        if metodo == 'division':
            return (  round(k % self.__dimension) ) # M is self.__dimension   #round para redondear
        
        elif metodo == 'extraccion': #Solamente extrae la parte más varible


            parte = str(k)
            if len(parte) == 1:
                parte = parte[-1:]
                
            elif len(parte) > 1:
                parte = parte[-2:]

            parte = int(parte)
            return     (round( parte % self.__dimension))  

        elif metodo == 'plegado':
            return
        
        elif metodo == 'cuadrado_medio':
            return
        
        elif metodo == 'alfanumerico':
            return
        
        else: # se usa el método de la división si no se especifica ningún otro
            return (  round(k % self.__dimension) ) # M is self.__dimension   #round para redondear




    def division(self,k):
        return (  round(k % self.__dimension) ) # M is self.__dimension   #round para redondear




    
    def insertar(self,elemento):
        
        h = self.hashing(elemento,'extraccion')
        hinicial = h
        
        contador = 0

        # 0 es el valor por defecto que hace que nos demos cuenta de que la celda está desocupada

        if self.__tabla[h]  == 0:
            self.__tabla[h] = elemento
            self.__cant += 1  # Incrementar el contador de elementos
            
        else:
            while self.__tabla[h] != 0 and  contador < self.__dimension  :   #  h != hinicial NO ANDA  # contador < self.__dimension
                h = (h-1) % self.__dimension  # se podria hacer con self.hashing(h-1)

                contador = contador + 1

            # v1 inserción porque h != hinicial me dice termino el WHILE sin terminar el CICLO y SI HAY un lugar disponible
            # if h != hinicial: 
            #   self.__tabla[h] = elemento

            # v2 :
            if self.__tabla[h] == 0: 
                self.__tabla[h] = elemento 
                self.__cant += 1  # Incrementar el contador de elementos


            else:
                print("la tabla está llena")

        return contador


    def insertar2(self, elemento):
        h = self.hashing(elemento)
        hinicial = h
        contador = 0  # Para rastrear intentos de inserción

        # 0 es el valor por defecto que hace que nos demos cuenta de que la celda está desocupada
        while self.__tabla[h] != 0 and contador < self.__dimension:
            h = (h - 1) % self.__dimension  # Avanzar hacia adelante en prueba lineal
            contador += 1

        if self.__tabla[h] == 0:
            self.__tabla[h] = elemento
            self.__cant += 1  # Incrementar el contador de elementos
        else:
            print("La tabla está llena")




    def insertardirecto(self,ele):
        self.__tabla[0] = ele



    def buscar(self, elemento):
        h = self.hashing(elemento,'division')
        i = h
        count = 0
        while self.__tabla[i] != elemento and count != self.__dimension:    # {i ! h} no se cumple  reemplazo por    {count != self.__dimension}
            i = (i + 1) % self.__dimension
            count += 1
        return count
        

    # -------------------------------Funciones Secundarias------------------------------- #

    def vacia(self):
        return self.__cant
    
    def mostrar(self):
        for i in range(len(self.__tabla)):
            print(f"{i} ==> {self.__tabla[i]}")



if __name__ == "__main__":

    print("Ejercicio 2")
    
    print("Para saber:\nNumeros Primos > 1000: \n1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061\n")

    print("Ingrese el tamaño de la tabla hash (Puede ser un Numero Primo o No)")
    
    m = int(input("su respuesta :  "))
    
    tabla = tablahash(m) # Se crea una tabla de dimensión M
    
    #abla.insertardirecto(5)
    #tabla.mostrar()

    for i in range(1000):
        #print(f"{i}  ==>  {random.random()}")

        valor_random = random.randint(0,999)

        longitudSP = tabla.insertar(valor_random)
        print("en el indice ",i,"la longitud del valor ",valor_random," es ",longitudSP,"\n\n\n")
    tabla.mostrar()
        

    print("ahora vamos a ver cuanto es la longitud de la secuencia de prueba lineal de la ultima inserción : ",valor_random )
    print("longitud : ",tabla.buscar(valor_random))
    print("longitud : ",tabla.buscar(542))
        

















'''
(1)
Siempre definir un arreglo de mayor cantidad que el numero de elementos que queremos almacenar si es de 1000 elementos
que la tabla hash sea un arreglo de 1309 por ejemplo, es FUNDAMENTAL ==> estaría mal si no se hace (FACTOR DE CARGA) == > N/M < 0
(1.2)
y que como plus sea un número PRIMO para que cuando se hagan los saltos En DIRECCIONAMIENTO ABIERTO
Sea mas PROBABLE caer en un ESPACIO BLANCO o VACIO

(2)
se busca y se inserta con la misma función de transformación es FUNDAMENTAL
para que se pueda establecer que
AL BUSCAR si NO se encuentra que deje de buscar cuando encuentre un espacio vacío

(3)
al CREAR la TABLA HASH hay que INICIALIZAR o cerear :

lo ideal sería INICIALIZAR con un objeto de datos que tenga 2 CAMPOS 1 campo para el DATO y OTRO campo para DISPONIBILIDAD

(dato (cualquier objeto de datos), Ocupado = True/False)



(4)

Depende de los datos pero para poder ingresar correctamente Datos a la Tabla Hash
se debe analizar bien los datos 
determinar bien la función de Transformación viendo los datos

depende mucho de M  (tamaño de la TABLA HASH)

pero tiene que haber un equilibrio entre la parte variable y la longitud ( se tiene que parecer a M)










'''





