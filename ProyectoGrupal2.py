'''
Desarrollaodres: Fabiana Pinto y Daniel Garcia

Proyecto de desarrollo de programa que debe de permitir añadir, modificar, eliminar
y consultar estudiantes con estadisiticas basicas
'''
# Importación de la librerías math y random para usarla en la generación de notas (randomizar y redondear)
import math
import random
# Instaciación de los diccionarios y esructura de datos prinicpales
dic={}          #diccionario principal para almacenar los datos del estudiante
dic_minmax={}
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
        nom=input("Introduzca nombre del estudiante: ")
        apll=input("Introduzca sus apellidos: ")
        notas=[random.randint(0,10) for x in range(6)]
        lista=(apll, notas)
        lista_minmax=(min(notas), max(notas))
        dic[nom]=lista
        print(dic)
        dic_minmax[nom]=lista_minmax
        print("Añadido con éxito.")
    elif opt==2:
        print(f"Lista de estudiantes: {dic.keys()}")
        print(f"Estudiantes con su nota mínima y máxima: {dic_minmax}")
    elif opt==3:
        print("") # Línea de prueba para que no de error por falta de instrucciones
    elif opt==4:
        print("Saliendo...")
        break
    