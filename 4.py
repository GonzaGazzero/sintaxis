# Resolver algorítmicamente el siguiente enunciado.
# Dado dos lenguajes como entradas (L1 y L2) y un texto que contenga
# concatenaciones que pueden obtenerse de los lenguajes de entrada,
# verificar que las concatenaciones ingresadas se correspondan con los
# lenguajes L1 y L2.

def concatenar(l1,l2):
    resultado = str()
    for x in range(len(l1)):
        for i in range(len(l2)):
            resultado=resultado+(l1[x]+l2[i])+','
    return resultado
l1=['ca','ma']
l2=['nta','sa']

print(concatenar(l1,l2))