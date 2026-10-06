'''
Desarrollaodres: Fabiana Pinto y Daniel Garcia

Proyecto de desarrollo de programa ampliado de estudiantes, en este caso el programa debe de tener
adicional las funciones de añadir nota, calculo de promedio y promedio mas alto, calculo de nota min y max
y permitir actualizacion de notas o eliminarlas 
'''

'''
Por hacer
- añadir estudiante                                     HECHO
	nombre                                              hecho
	apellidos                                           hecho
	nota (varias randomizadas)                          hecho
- mostrar estudiantes                                   
	mostrar todos los estudiantes                       hecho
	nota max y min por estudiante                       hecho
	mostrar estudiante con nota media mas alta
	ordenados por nota media
	- opcional - filtrar por nota media superior a x
- cambiar o borrar nota de estudiantes
	introducir estudiante
	cambiar notas???
- salir                                                 HECHO
'''

# Importación de la librerías math y random para usarla en la generación de notas (randomizar y redondear)
import math
import random
#value[1]
def media(list):
    avg=sum(list)/len(list)
    return avg
# Instaciación de los diccionarios y esructura de datos prinicpales
dic={}          #diccionario principal para almacenar los datos del estudiante
dic_minmax={}
while True:

    # MENÚ DE OPCIONES
    # se muestra un menu interactivo en bucle hasta que el usuario decida salir
    opt=int(input("Seleccione una opción:" \
                "\n1. Añadir estudiante" \
                "\n2. Mostrar estudiantes" \
                "\n3. Gestionar notas " \
                "\n4. Salir \n"))
    
    # opt -> Opción seleccionada por el usuario
    # Opcion 1--> se introduce el nombre del estudiante con sus apellidos
    if opt==1:
        nom=input("Introduzca nombre del estudiante: ")
        apll=input("Introduzca sus apellidos: ")

        # se genera 6 notas del 1 al 6 de forma aleatoria y se las introduce a una lista
        notas=[random.randint(0,10) for x in range(6)]
        nota_media=media(notas)
        lista=(apll, notas, nota_media)
        lista_minmax=(min(notas), max(notas))
        dic[nom]=lista
        # dentro de la lista las notas hacemos el orden de mayor a menor nota 
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