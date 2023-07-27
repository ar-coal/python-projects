def plus(numbers):
    total = 0
    for n in numbers:
        total = total + int(n)
    return total


def times(numbers):
    total = 1
    for n in numbers:
        total = total * int(n)
    return total


if __name__ == '__main__':
    lista = input("Ingresa una lista separada de numeros separados por comas\n").split(",")
    x = input("Ingresa la opción y presiona enter para elegirla:\n 1)Sumar lista\n 2)Multiplicar lista\n")
    if x == "1":
        print(f"la suma de los números de la lista es {plus(lista)}")
    elif x == "2":
        print(f"la multiplicación de los números de la lista es {times(lista)}")
    else:
        print("opcion no valida")
