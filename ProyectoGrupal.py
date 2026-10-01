
# Instaciación del diccionario vacío
dic={}
dic_nac={}
sorted_dic={}
while True:
    # MENÚ DE OPCIONES
    opt=int(input("Seleccione una opción: " \
                "\n1. Añadir estudiante " \
                "\n2. Eliminar estudiante " \
                "\n3. Buscar estudiante " \
                "\n4. Listar estudiantes " \
                "\n5. Mostrar estadísticas " \
                "\n6. Salir \n"))
    # opt -> Opción seleccionada por el usuario
    if opt==1:
        dni=input("Introduzca DNI o nombre completo del estudiante: ")
        apellidos=input("Introduzca apellidos: ")
        nacimiento=input("Introduzca año de nacimiento: ")
        curso=input("Introduzca curso: ")
        tupla = (apellidos, nacimiento, curso)
        dic[dni] = tupla
        dic_nac[dni] = nacimiento
        print(dic)
        print("Añadido con éxito.")
    elif opt==2:
        elim=input("Introducir DNI o nombre completo del estudiante: ")
        if elim in dic:
            dic.pop(elim)
            print("Estudiante", elim, "Eliminado con éxito.")
        else:
            print("Estudiante no encontrado.")
    elif opt==3:
        search=input("Introducir DNI o nombre completo del estudiante: ")
        if search in dic:
            print("Datos de", search, ": ", dic[search])
        else:
            print("Estudiante no encontrado.")
    elif opt==4:
        print(dic.keys())
    elif opt==5:
        print("Número de estudiantes:", len(dic))
        for key in sorted(dic_nac, key=dic_nac.get):
            sorted_dic[key]=dic_nac[key]
        print(sorted_dic)
    elif opt==6:
        print("Saliendo...")
        break