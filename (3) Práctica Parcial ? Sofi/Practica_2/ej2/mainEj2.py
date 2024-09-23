from clasePila import Pila

def decimal_a_binario(numero_decimal):
    pila = Pila()

    while numero_decimal > 0:
        residuo = numero_decimal % 2
        pila.insertar(residuo)
        numero_decimal //= 2

    binario = ""
    while not pila.vacia():
        binario += str(pila.suprimir())

    return binario

if __name__ == "__main__":
    numero_decimal = int(input("Introduce un número decimal: "))
    binario = decimal_a_binario(numero_decimal)
    print(f"La representación binaria de {numero_decimal} es {binario}")