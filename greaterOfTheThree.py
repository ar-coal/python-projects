import re
from greaterthat import maax

if __name__ == '__main__':
    print("Número mayor")
    x = re.match(r"(-?\d+)(\D)\2*(-?\d+)(\D)\2*(-?\d+)",  input("ingresa tres numeros separados por cualquier caracter\n"))
    if x:
        if maax(int(x.group(1)),int(x.group(3))):
            if maax(int(x.group(1)),int(x.group(5))):
                print(f"el número mas grande es {x.group(1)}")
            else:
                print(f"el número mas grande es {x.group(5)}")
        else:
            if maax(int(x.group(3)), int(x.group(5))):
                print(f"el número mas grande es {x.group(3)}")
            else:
                print(f"el número mas grande es {x.group(5)}")
    else:
        print("Valores incorrectos, no se encontraron dos numeros")