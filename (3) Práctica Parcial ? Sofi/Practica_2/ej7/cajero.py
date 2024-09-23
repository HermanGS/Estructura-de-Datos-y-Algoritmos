from colaEncadenada import ColaEncadenada

class Cajero:
    def __init__(self, tiempo_atencion):
        self.__cola = ColaEncadenada()
        self.__cont_clientes_ingresados = 0
        self.__cont_clientes_atendidos = 0
        self.__acum_tiempo_espera = 0
        self.__max_tiempo_espera = -1
        self.__acum_tiempo_espera_incompletas = 0
        self.__tiempo_atencion = tiempo_atencion
        self.__tiempo_restante = 0

    def agregar_cliente(self, reloj):
        self.__cola.insertar(reloj)
        self.__cont_clientes_ingresados += 1

    def atender_cliente(self, reloj, tms):
        if self.__tiempo_restante == 0 and not self.__cola.vacia():
            cliente = self.__cola.suprimir()
            tiempo_espera = reloj - cliente

            if reloj + self.__tiempo_atencion < tms:  # Puede ser atendido antes de que termine el tiempo de simulación
                self.__acum_tiempo_espera += tiempo_espera
                self.__cont_clientes_atendidos += 1
            else:
                self.__acum_tiempo_espera_incompletas += tiempo_espera

            if tiempo_espera > self.__max_tiempo_espera:
                self.__max_tiempo_espera = tiempo_espera

            self.__tiempo_restante = self.__tiempo_atencion

        if self.__tiempo_restante > 0:
            self.__tiempo_restante -= 1

    def obtener_estadisticas(self):
        return {
            'clientes_ingresados': self.__cont_clientes_ingresados,
            'clientes_atendidos': self.__cont_clientes_atendidos,
            'acum_tiempo_espera': self.__acum_tiempo_espera,
            'max_tiempo_espera': self.__max_tiempo_espera,
            'acum_tiempo_espera_incompletas': self.__acum_tiempo_espera_incompletas,
        }
