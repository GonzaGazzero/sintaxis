import itertools 

def noalfabeto(alfabeto,palabra):
    nocaracter=''
    cont=0
    for j in range(len(palabra)):
        cont=0
        for i in range(len(alfabeto)):
            if alfabeto[i]!='{' and alfabeto[i]!='}' and alfabeto[i]!=',':
                if palabra[j]==alfabeto[i]:
                    cont+=1
        if cont<=0:
            nocaracter+=palabra[j]            
    return nocaracter

alfabeto = input("Ingrese el alfabeto utilizado (sin espacios): ")
palabra = input("Ingrese la palabra a permutar: ")

nocaract = noalfabeto(alfabeto,palabra)
nueva_palabra = str('')
for i in range(len(nocaract)):
    if i == 0:
        nueva_palabra = palabra.replace(nocaract[i],"")
    else: nueva_palabra = nueva_palabra.replace(nocaract[i],"")


print('los caracteres no pertenecientes son: ' + nocaract)

if nueva_palabra==(''):
    permutaciones = list(itertools.permutations(palabra))
else: permutaciones = list(itertools.permutations(nueva_palabra))

for i,p in enumerate(permutaciones):
    print(str(i + 1) + " - " + "".join(p))
