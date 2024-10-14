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

main2()
