Vowels = {"a","e","i","o","u"}
char = input("Introduce un caractér\n")
if len(char) == 1:
    if char.lower() in Vowels:
        print("Es una vocal")
    else:
        print("No es una vocal")
else:
    raise ValueError("El texto ingresado tiene mas de un caractér")

