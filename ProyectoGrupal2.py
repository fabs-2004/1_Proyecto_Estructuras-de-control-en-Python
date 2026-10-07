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
def media(list):
    avg=round(sum(list)/len(list), 2) #No encuentro manera de redondearlo con el módulo math
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
        print("Lista de estudiantes: ")
        for key, value in dic.items():
            print(f"{key} [Nota media: {value[2]}]")
        print(f"Estudiantes con su nota mínima y máxima: {dic_minmax}")
        print("Ordenados por nota media:", dict(sorted(dic.items(), key = lambda item : item[1][2])))
 
    elif opt==3:
        # se hace un buscador de estudiante junto a una consulta al usuario de si desea eliminar o modificar la nota del estudiante
        search=input ("introducir nombre de estudiante: ")
        if search in dic:
            print("datos de ", search, ":", dic[search])

            notas = dic[search][1]  # se extrae la lista de notas de la sublista
            #creamos una accion donde el usuario escribe que funcion quiere realizar
            accion = input("¿Quieres 'modificar' o 'eliminar' una nota?: ").lower()   #con lowe evitamos errores con las mayusuclas y las minusuclas
            #si el uusario introduce modificar selecciona que nota quiere modificar la nueva nota y la nota se modifica
            if accion == 'modificar': 
                vieja = int(input("Nota que quieres cambiar: "))
                nueva = int(input("Nueva nota: "))
                notas[notas.index(vieja)] = nueva  # Busca y cambia directamente
            #si el usuario quiere eliminar la not selecciona que nota quiere eliminar y se elimina de la lista
            elif accion == 'eliminar':
                borrar = int(input("Nota que quieres eliminar: "))
                notas.remove(borrar)  # Borra la nota indicada
                
            # Actualizamos todo automáticamente tras el cambio tanto la nota maxima, la minima y el promedio
            dic[search] = (dic[search][0], notas, media(notas))
            dic_minmax[search] = (min(notas), max(notas))
            print("¡Actualizado con éxito! Nuevos datos:", dic[search])
        else:
            print("no encontrado")
            
    elif opt==4:
        
        print("Saliendo...")
        break