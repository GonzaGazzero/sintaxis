# Función para verificar si un nombre de variable cumple con las reglas sintácticas
def validar_variable(variable):
    fallos=str(' ')
    conjunto1 = {"abcdefghijklmnopqrstuvwxyz"}
    conjunto2 = {"0123456789-_"}
    conjunto3 = {"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    #1 nombre de la variable empieza con guion (-)
    if variable[0:1]!= '-': fallos = fallos + 'regla 1,'
    #2 no puede contener espacios
    for x in range(len(variable)):
        if variable[x:x+1:]==' ':
            fallos = fallos + 'regla 2,'
        #7 no puede comenzar con numero
        
    #3 debe terminar con ;
    if variable[:-2:-1]!=';': fallos = fallos + 'regla 3,'
    #4 long max 30 caract y min 3
    elif len(variable)>30 or len(variable)<3: fallos = fallos + 'regla 4,'
    #5 no puede terminar con _ -
    elif variable[:-2:-1]=='-' or variable[:-2:-1]=='_': fallos = fallos + 'regla 5,'
    #6 la variable debe contener al menos dos conjuntos
    #8 en lugar de un espacio debe haber _
    #9 despues de - debe seguir letra mayuscula
    #10 despues del guion _ debe seguir letra mayuscula
    if fallos == ' ':
        return 'variable valida'
    return 'variable incorrecta', fallos

# Mini lenguaje interactivo
while True:
    nombre = input("Ingrese el nombre de la variable (o escriba 'salir' para salir): ")
    
    if nombre.lower() == "salir":
        break
    
    print(validar_variable(nombre))

# variable = '-Autos_rojos;'
# print(variable[:-2:-1])