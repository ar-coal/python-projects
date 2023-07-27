import re
from greaterthat import maax

if __name__ == '__main__':
    print("Número mayor")
    x = re.match(r"(-?\d+)(\D)\2*(-?\d+)(\D)\2*(-?\d+)",  input("ingresa tres numeros separados por cualquier caracter del mismo tipo\n"))
    if x:
        if maax(int(x.group(1)),int(x.group(3))):
            top_value = int(x.group(1))

        else:
            top_value = int(x.group(3))

        if maax(top_value,int(x.group(5))):
            print(f"el valor mas grande es {top_value}")

        else:
            print(f"el valor mas grande es {x.group(5)}")

    else:
        print("Valores incorrectos, no se encontraron tres numeros")