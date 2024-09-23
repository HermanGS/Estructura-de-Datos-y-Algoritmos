from cajero import Cajero
from random import uniform, choice

def llega_cliente():
    return uniform(0, 1) <= 0.5  # Probabilidad de 1/2

def elegir_cajero(cajeros):
    opciones_libres = [i for i, cajero in enumerate(cajeros, start=1) if cajero.obtener_estadisticas()['clientes_ingresados'] == cajero.obtener_estadisticas()['clientes_atendidos']]
    if opciones_libres:
        return choice(opciones_libres)
    
    # Si no hay cajeros libres, elegir el que tenga menos clientes
    return min(range(1, 4), key=lambda i: cajeros[i-1].obtener_estadisticas()['clientes_ingresados'] - cajeros[i-1].obtener_estadisticas()['clientes_atendidos'])

if __name__ == "__main__":
    cajeros = [Cajero(5), Cajero(3), Cajero(4)]
    tms = 120
    reloj = 0

    while reloj < tms:
        if llega_cliente():
            cajero_elegido = elegir_cajero(cajeros)
            cajeros[cajero_elegido - 1].agregar_cliente(reloj)

        for cajero in cajeros:
            cajero.atender_cliente(reloj, tms)

        reloj += 1

    # Mostrar resultados
    for i, cajero in enumerate(cajeros, start=1):
        stats = cajero.obtener_estadisticas()
        print(f"Cajero {i}:")
        print(f"  Tiempo máximo de espera: {stats['max_tiempo_espera']}")
        print(f"  Clientes atendidos: {stats['clientes_atendidos']}")
        print(f"  Clientes sin atender: {stats['clientes_ingresados'] - stats['clientes_atendidos']}")
        if stats['clientes_atendidos'] > 0:
            print(f"  Promedio de espera clientes atendidos: {stats['acum_tiempo_espera'] / stats['clientes_atendidos']}")
        if stats['clientes_ingresados'] > stats['clientes_atendidos']:
            print(f"  Promedio de espera clientes sin atender: {stats['acum_tiempo_espera_incompletas'] / (stats['clientes_ingresados'] - stats['clientes_atendidos'])}")

