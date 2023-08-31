# Función para verificar si un nombre de variable cumple con las reglas sintácticas
def validar_variable(nombre_variable):
    conjunto1 = {"abcdefghijklmnopqrstuvwxyz"}
    conjunto2 = {"0123456789-_"}
    conjunto3 = {"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    

# Mini lenguaje interactivo
while True:
    nombre = input("Ingrese el nombre de la variable (o escriba 'salir' para salir): ")
    
    if nombre.lower() == "salir":
        break
    
    if validar_variable(nombre):
        print("Nombre de variable válido.")
    else:
        print("Nombre de variable inválido.")
