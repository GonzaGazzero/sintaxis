# Función para verificar si un nombre de variable cumple con las reglas sintácticas
def validar_variable(variable):
    fallos=str('')
    conjunto1 = str("abcdefghijklmnopqrstuvwxyz")
    conjunto2 = str("0123456789-_;")
    conjunto3 = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    #1 nombre de la variable empieza con guion (-)
    if variable[0:1] != '-': fallos = fallos + 'regla 1,'

    #2 no puede contener espacios
    for x in range(len(variable)):
        if variable[x:x+1:]==' ':
            fallos = fallos + 'regla 2,'
    
    #3 debe terminar con ;
    if variable[:-2:-1]!=';': fallos = fallos + 'regla 3,'
    
    #4 long max 30 caract y min 3
    if len(variable)>30 or len(variable)<3: fallos = fallos + 'regla 4,'
    
    #5 no puede terminar con _ -
    if variable[-2:-1:]=='-' or variable[-2:-1:]=='_': fallos = fallos + 'regla 5,'
    
    #6 la variable debe contener al menos dos conjuntos
    
    #7 no puede comenzar con numero
    for x in range(9):
        if variable[1:2] == conjunto2[x:x+1]: fallos = fallos + 'regla 7,'
    
    #8 en lugar de un espacio debe haber _
    
    #9 despues de - debe seguir letra mayuscula
    bandera = False
    if variable[0:1:] == '-':
        for x in range(len(conjunto3)):
            if variable[1:2:] == conjunto3[x:x+1:]:
                bandera = True
    if bandera == False: fallos = fallos + 'regla 9,'
    
    #10 despues del guion _ debe seguir letra mayuscula
    bandera = False
    for x in range(len(variable)):
        if variable[x:x+1:] == '_':
            for m in range(len(conjunto3)):
                if variable[x+1:x+2:] == conjunto3[m:m+1:]:
                    bandera = True
            if bandera == False: fallos = fallos + 'regla 10,'
    
    return fallos

while True:
    nombre = str(input("Ingrese el nombre de la variable (o escriba 'salir' para salir): "))
    
    if nombre.lower() == "salir":
        break
    
    resultado=validar_variable(nombre)
    if resultado=='':print ('variable valida')
    else: print('variable no valida', resultado)

# variable = '-Autos_rojos-;'
# print(variable[-2:-1:])
