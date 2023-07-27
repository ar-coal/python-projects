string = ""
or_str = input("Ingresa una cadena para escribirla en reversa\n")
for i in range(len(or_str),0,-1):
    string = string + or_str[i-1]
print(string)
