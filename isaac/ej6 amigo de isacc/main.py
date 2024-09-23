from clase_cola import Cola
import random

if __name__ == "__main__":

    cola = Cola()
    
    tms = 20
    cajero1 = 0
    cajero2= 0
    frecuencia_clientes = 3
    tc1 = 4
    tc2 = 5
    contar_clientes = 0
    acumula_tiempo= 0

    reloj = 0

    while reloj <= tms:

        if(0 < random.random() <= 1/frecuencia_clientes):
            cola.insertar(reloj)
            print(f"Ingreso un cliente en el minuto  {reloj}")
            if(cajero1 == 0 and not cola.vacia()):
                cliente = cola.suprimir()
                tiempo_espera = reloj - cliente
                acumula_tiempo += tiempo_espera
                contar_clientes += 1
                print(f"cliente atendido en el minuto {reloj} por el cajero 1, y se tardo un tiempo de: {tiempo_espera} minutos")
                cajero1 += tc1
            elif(cajero2 == 0 and not cola.vacia()):
                cliente = cola.suprimir()
                tiempo_espera = reloj - cliente
                acumula_tiempo += tiempo_espera
                contar_clientes += 1
                print(f"cliente atendido en el minuto {reloj} por el cajero 2, y se tardo un tiempo de: {tiempo_espera} minutos")
                cajero2 += tc2
            
            if(cajero1>0):
                cajero1 -= 1
            if(cajero2>0):
                cajero2-= 1
            
            reloj += 1

    print(f"tiempo promedio de espera: {acumula_tiempo/contar_clientes}")
    print(f"cantidad de clientes: {contar_clientes}")



