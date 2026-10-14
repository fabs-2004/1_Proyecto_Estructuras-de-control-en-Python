'''
Desarrollaodres: Fabiana Pinto y Daniel Garcia

Proyecto de desarrollo de programa ampliado de estudiantes, en este caso el programa debe de tener
un manejo de exepciones y de forma adicional una exportacion e importacion de archivos 
'''

# Importación de la librerías math y random para usarla en la generación de notas (randomizar y redondear)
import math
import random
#importamos pjson para que podamos exportar e importar archivos
import json

def media(list):
    avg=math.ceil(sum(list)/len(list))
    return avg
# Instaciación de los diccionarios y esructura de datos prinicpales
dic={}          #diccionario principal para almacenar los datos del estudiante
dic_minmax={}
opt=0
while True:
    try:
        # MENÚ DE OPCIONES
        # se muestra un menu interactivo en bucle hasta que el usuario decida salir
        opt=int(input("Seleccione una opción:" \
                    "\n1. Añadir estudiante" \
                    "\n2. Mostrar estudiantes" \
                    "\n3. Gestionar notas " \
                    "\n4. Importar/Exportar" \
                    "\n5. Salir \n"))
    except ValueError:
        print("el numero de opcion no exisite")
    # opt -> Opción seleccionada por el usuario
    # Opcion 1--> se introduce el nombre del estudiante con sus apellidos
    if opt==1:
        nom=input("Introduzca nombre del estudiante: ").lower()
        apll=input("Introduzca sus apellidos: ").lower()
        
        # se genera 6 notas del 1 al 6 de forma aleatoria y se las introduce a una lista
        notas=[random.randint(0,10) for x in range(6)]
        nota_media=media(notas)
        lista=(apll, notas, nota_media)
        lista_minmax=(min(notas), max(notas))
        dic[nom]=lista
        # creamos una lista a parte con las notas ordenadas
        print(dic)
        dic_minmax[nom]=lista_minmax
        print("Añadido con éxito.")

    elif opt==2:
        try:
            assert len(dic)>0,"error, la lista de estudiantes esta vacia"
            #implementar aqui el assert
            print("Lista de estudiantes: ")
            for key, value in dic.items():
                print(f"{key} [Nota media: {value[2]}]")
            print(f"Estudiantes con su nota mínima y máxima: {dic_minmax}")
            print("Ordenados por nota media:", dict(sorted(dic.items(), key = lambda item : item[1][2])))

        except AssertionError as error:
            print(error)

    elif opt==3:
        # se hace un buscador de estudiante junto a una consulta al usuario de si desea eliminar o modificar la nota del estudiante
        search=input ("introducir nombre de estudiante: ").lower()
        if search in dic:
            print("datos de ", search, ":", dic[search])

            #AÑADIR OPCION DE AÑADIR NOTA PARA QUE SE HAGA ASSERT DE LIMITAR A 10 NOTAS


            notas = dic[search][1]  # se extrae la lista de notas de la sublista
            #creamos una accion donde el usuario escribe que funcion quiere realizar
            accion = input("¿Quieres 'modificar', 'eliminar' o 'añadir' una nota?: ").lower()   #con lowe evitamos errores con las mayusuclas y las minusuclas
            #si el uusario introduce modificar selecciona que nota quiere modificar la nueva nota y la nota se modifica
            if accion == 'modificar': 
                vieja = int(input("Nota que quieres cambiar: "))
                try:
                    nueva = int(input("Nueva nota: "))
                    notas[notas.index(vieja)] = nueva  # Busca y cambia directamente
                except ValueError:
                    "Nota no válida."
            #si el usuario quiere eliminar la nota selecciona que nota quiere eliminar y se elimina de la lista
            elif accion == 'eliminar':
                borrar = int(input("Nota que quieres eliminar: "))
                notas.remove(borrar)  # Borra la nota indicada
                
            #si el usuario quiere añadir otra nota adicional
            elif accion=='añadir':
                try:
                    assert len(notas)<10, "error: el estudiante supera el maximo de notas"
                    
                    añadir=int(input("que nota quieres añadir: "))
                    notas.append(añadir)
                except AssertionError as error:
                    print(error)
                
            # Actualizamos todo automáticamente tras el cambio tanto la nota maxima, la minima y el promedio 
            try:
                dic[search] = (dic[search][0], notas, media(notas))
            except ZeroDivisionError:
                print("No es posible hacer una media sin notas.")
            dic_minmax[search] = (min(notas), max(notas))
            print("¡Actualizado con éxito! Nuevos datos:", dic[search])
        else:
            print("no encontrado")

    elif opt==4:
        print("\n1. exportar datos \n2. importar datos")
        try:
            sub_opt=int(input("selecciona una opcion: "))

            if sub_opt==1:
                #exportar_ guarda el diccionario prinicpal directamente
                with open("estudiantes.json", "w", encoding="utf-8") as f:
                    json.dump(dic,f,ensure_ascii=False,indent=4)
                print("exportado correctamente")
            elif sub_opt==2:
                #importar: carga los datos del archivo al diccionario
                try:
                    with open("estudiantes.json","r",encoding="utf-8")as f:
                        dic.clear()
                        dic.update(json.load(f))
                    print("importado con exito")
                except FileNotFoundError:
                    print("error: aun no hya ningun archivo guardado")
        except ValueError:
            print("entrada no valida")

    elif opt==5:
        print("Saliendo...")
        break
 