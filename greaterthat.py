import re


def maax(a: int, b: int):
    if a < b:
        return False
    else:
        return True


if __name__ == '__main__':
    print("Número mayor")
    x = re.match(r"(-?\d+)(\D)\2*(-?\d+)",  input("ingresa dos numeros separados por cualquier caracter\n"))
    if x:
        if maax(int(x.group(1)),int(x.group(3))):
            print(f"{x.group(1)} es mayor que {x.group(3)}")
        else:
            print(f"{x.group(3)} es mayor que {x.group(1)}")
    else:
        print("Valores incorrectos, no se encontraron dos numeros")
