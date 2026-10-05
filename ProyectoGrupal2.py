'''
Desarrollaodres: Fabiana Pinto y Daniel Garcia

Proyecto de desarrollo de programa que debe de permitir añadir, modificar, eliminar
y consultar estudiantes con estadisiticas basicas
'''

# Instaciación de los diccionarios y esructura de datos prinicpales
dic={}          #diccionario principal para almacenar los datos del estudiante

while True:

    # MENÚ DE OPCIONES
    # se muestra un menu interactivo en bucle hasta que el uusario decida salir
    opt=int(input("Seleccione una opción:" \
                "\n1. Añadir estudiante" \
                "\n2. Mostrar estudiantes" \
                "\n3. Gestionar notas " \
                "\n4. Salir \n"))
    
    # opt -> Opción seleccionada por el usuario
    
    if opt==1:
          print("linea de prueba")
    elif opt==6:
            print("Saliendo...")
            break
    