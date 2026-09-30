
# Instaciación del diccionario vacío
dic = {}

while True:
    # MENÚ DE OPCIONES
    opt = input("Seleccione una opción: " \
                "\n1. Añadir estudiante " \
                "\n2. Eliminar estudiante " \
                "\n3. Buscar estudiante " \
                "\n4. Listar estudiantes " \
                "\n5. Mostrar estadísticas " \
                "\n6. Salir \n")
    # opt -> Opción seleccionada por el usuario
    if opt == 1:
        dni = input("Introduzca DNI o nombre completo del estudiante")
        apellidos = input("Introduzca apellidos")
        nacimiento = input("Introduzca año de nacimiento")
        curso = input("Introduzca curso")
    elif opt == 2:
        elim = input("Introducir DNI o nombre completo del estudiante")
    elif opt == 6:
        print("Saliendo...")
    break