'''
diccionario:
▪ nombre (str): nombre del producto.
▪ categoria (str): categoría del producto.
▪ unidades (int): unidades disponibles.
▪ precio (float): precio por unidad.
▪ activo (bool): si está disponible para vender

Estructura prinicpal:
Lista de diccionarios: inventario = []

menu del programa:
===== INVENTARIO TIENDA MASCOTAS =====
1. Añadir producto
2. Mostrar inventario completo
3. Buscar producto por nombre
4. Modificar stock de un producto
5. Mostrar valor total del inventario
6. Mostrar estadísticas por categoría (tuplas y listas)
0. Salir

Requisitos especificos:
Tipos simples obligatorios: int, float, str, bool
Tipos complejos: Lista de diccionarios + uso de tuplas/listas en la opción 6

Operadores obligatorios:
▪ Aritméticos: unidades * precio
▪ Comparación: unidades < 5
▪ Lógicos: unidades < 5 and activo == True
▪ Pertenencia: 'nombre' in producto

pseudocodigo:
Deberéis realizar el pseudocódigo en PSeInt, desarrollando únicamente completa
la opción 4 del menú. 

lo que se debe entregar:
1. pseudocodigo
2. diagrama de flujo
3. codigo python
4. documentacion con explicacion

pruebas recomendadas:
• Añadir al menos 4 productos de distintas categorías:
▪ Pienso cachorro 3 kg – Alimentación.
▪ Champú perro pelo corto – Higiene.
▪ Collar acolchado talla M – Accesorios.
▪ Juguete cuerda nudos – Juguetes.
• Buscar por nombre existente y no existente.
• Modificar stock con incrementos y decrementos; comprobar que no permita
stock negativo.
• Calcular el valor total del inventario y verificarlo manualmente.
• Validar las estadísticas por categoría (suma de unidades y de unidades*precio).
'''
#estructura principal: lista de diccionarios
inventario=[]

opt=0
while True:
    try:
        #menu de opciones
        opt=int(input("\nSeleccione una opcion: "
                      "\n1. añadir producto"
                      "\n2. mostrar inventario completo"
                      "\n3. buscar producto por nombre"
                      "\n4. modificar stock de un producto"
                      "\n5. mostrar valor total del inventario"
                      "\n6. mostrar estadisticas por cateogria"
                      "\n0. salir \n> "))
    except ValueError:
        print("el numero de opcion no existe o no es valido")
        continue

    #opcion1. añadir producto al invetario
    if opt==1:
        #se solicitan los datos asegurando los tipos simples obligatorios
        nombre=input("introduzca el nombre del producto: ").lower()
        categoria=input("introduzca la categoria : ").lower()

        try:
            unidades=int(input("introduzca las unidades disponibles: "))
            precio=float(input("introduzca el precio por unidad: "))
            
            #pedimos el booleano comprobando si esta activo
            activo_input=input("¿esta activo para la venta (s/n)?: ").lower
            activo=True if activo_input=='s' else False

            #creamos el diccionario con el producto
            producto={
                "nombre":nombre,
                "categoria":categoria,
                "unidades":unidades,
                "precio":precio,
                "activo":activo
            }

            #añadimos el diccionario a la lista principal
            inventario.append(producto)
            print("producto añadido")

        except ValueError:
            print("error las unidades deben ser un numero entero")

    #opcion 2: mostrar inventario completo
    elif opt==2:
        #verificamos si la lista tiene elementos antes de mostrarla
        if len(inventario)==0:
            print("el inventario esta actualmente vacio")
        else:
            print("\n---lista completa de inventario ----")
            #recorremos la lista de diccionarios para mostrar cada producto
            for producto in inventario:
                estado="activo" if producto["activo"] else "inactivo"
                print(F"-producto: {producto['nombre'].capitalize()} | "
                      f"categoria: {producto['categoria'].capitalize()} | "
                      f"unidades: {producto['unidades']} | "
                      f"precio: {producto['precio']}€ | "
                      f"estado: {estado} ")

    elif opt==3:
        #buscar producto por nombre
        print("pendiente")

    elif opt==4:
            #modificar stock de un producto
            print("pendiente")

    elif opt==5:
            #mostrar valor total del inventario
            print("pendiente")

    elif opt==6:
            #mostrar estadisticas por categoria
            print("pendiente")

    elif opt==0:
            print("saliendo del programa...")
            break

    else:
         print("opcion fuera de rango (debe de ser del o al 6)")