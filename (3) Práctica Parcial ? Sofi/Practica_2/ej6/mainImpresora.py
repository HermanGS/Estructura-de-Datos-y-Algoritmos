import random
from ColaImpresora import Cola
from claseTrabajo import Trabajo

def simular_imprenta(tiempo_simulacion=60, intervalo_llegada=5, tiempo_max_proceso=5):
    cola = Cola()
    tiempos_espera = []
    trabajos_no_atendidos = 0
    tiempo_actual = 0

    # Insertar trabajos iniciales en la cola
    while tiempo_actual < tiempo_simulacion:
        tiempo_impresion = random.randint(1, 10)  # Tiempo aleatorio entre 1 y 10 minutos
        cola.insertar(Trabajo(tiempo_impresion))
        tiempo_actual += intervalo_llegada

    tiempo_actual = 0

    while tiempo_actual < tiempo_simulacion:
        if not cola.vacia():
            trabajo = cola.suprimir()
            tiempo_restante = trabajo.tiempo_impresion
            
            if tiempo_restante > tiempo_max_proceso:
                # Trabajo no terminado, vuelve a la cola con el tiempo restante
                tiempo_restante -= tiempo_max_proceso
                cola.insertar(Trabajo(tiempo_restante))
            else:
                # Trabajo terminado
                tiempos_espera.append(tiempo_actual)
        
        # Avanzar el tiempo de simulación
        tiempo_actual += intervalo_llegada

    # Contar trabajos no atendidos
    trabajos_no_atendidos = cola._Cola__cant

    # Calcular el promedio de espera
    if tiempos_espera:
        promedio_espera = sum(tiempos_espera) / len(tiempos_espera)
    else:
        promedio_espera = 0

    return trabajos_no_atendidos, promedio_espera
 
if __name__=='__main__':
# Ejecutar simulación
    trabajos_no_atendidos, promedio_espera = simular_imprenta()
    print(f"Cantidad de trabajos que quedaron sin atender: {trabajos_no_atendidos}")
    
    print(f"Promedio de espera de los trabajos impresos: {promedio_espera:.2f} minutos")
