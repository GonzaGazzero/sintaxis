# Dado un alfabeto, determinar si las palabras ingresadas, están
# formadas por dicho alfabeto (mostrar mensaje OK o NO OK, según el
# caso) . En el caso de contener otros elementos que no pertenezcan al
# alfabeto, mostrar cuales son los elementos diferentes.

def ejercicio3(alfabeto):
    incorrectos = str()
    bandera = False
    palabra=str(input('Ingrese una palabra: '))
    for x in range(len(palabra)):
        for i in range(len(alfabeto)):
            if palabra[x:x+1:]==alfabeto[i:i+1:]:
                bandera=True
                break
            elif palabra[x:x+1:]!=alfabeto[i:i+1:] and i!=(len(alfabeto)-1):
                None
            else:
                incorrectos= incorrectos + (f'{palabra[x:x+1:]}')
                bandera=False
    if bandera:
        return 'OK'
    else:
        return 'NO OK', incorrectos
while True:
    alfabeto = str(input('ingrese alfabeto: '))
    print(ejercicio3(alfabeto))
    salir=int(input('si desea salir presione 0, sino 1: '))
    if salir == 0:
        break
