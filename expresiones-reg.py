import re #importamos el modulo de expresiones regulares de python

#se define la exp reg
expresion = r"^[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{3,}$"


def validar_correo(correo):
    return bool(re.match(expresion, correo)) 
#If the whole string matches this regular expression, return a corresponding Match. 
#Return None if the string does not match the pattern; note that this is different from a zero-length match.


ciclo=1
while True:
    correo=str(input('ingrese el correo electronico: '))
    if validar_correo(correo):
        print(f"{correo} es válido ✅")
    else:
        print(f"{correo} no es válido ❌")
    ciclo=int(input('\n ingrese lo siguiente \n 1 = si quiere validar otra direccion de correo \n 2 = si quiere salir \n '))
    if ciclo == 2: 
        break




#bibliografia 
# https://docs.python.org/es/3/howto/regex.html