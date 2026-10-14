'''
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
            activo_input=input("¿esta activo para la venta (s/n)?: ").lower()
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
                alerta=""
                if producto['unidades']<5 and producto['activo']==True:
                    alerta="[estock bajo]"
                    
                print(F"-producto: {producto['nombre'].capitalize()} | "
                    f"categoria: {producto['categoria'].capitalize()} | "
                    f"unidades: {producto['unidades']} | "
                    f"precio: {producto['precio']}€ | "
                    f"estado: {estado} ")

    #opcion 3: buscar el prodcuto por nombre
    elif opt==3:
        if len(inventario)==0:
            print("el inventario esta vacio")
        else:
            busqueda=input("introduce el nombre del producto a buscar: ").lower()
            encontrado=False
            for producto in inventario:
                #se usa la pertenencia (in) para buscar coincidencias parciales o totales en el nombre
                if busqueda in producto['nombre']:
                    estado="activo" if producto['activo'] else "inactivo"
                    print(f"\n producto encontrado"
                          f"\n- nombre: {producto['nombre'].capitalize()}"
                          f"\n- categoria: {producto['categoria'].capitalize()}"
                          f"\n- unidades:{producto['unidades']} "
                          f"\n- precio: {producto['precio']} €"
                          f"\n- estado: {estado}")
                    encontrado=True
            if not encontrado:
                print("no se encontro ningun prodcuto con ese nombre")

    #opcion 4: modificar stock de un producto
    elif opt==4:
        if len(inventario)==0:
            print("el inventario esta vacio")
        else:
            busqueda=input("introduzca el nombre del product cuyo stock desea modificar: ").lower()
            encontrado=False
            for producto in inventario:
                if producto['nombre']==busqueda:
                    encontrado=True
                    print(f"producto: {producto['nombre'].capitalize()} | unidades actuales: {producto['unidades']}")
                    try:
                        cambio=int(input("introduzca la cantidad a sumar o restar: "))
                        nuevo_stock=producto['unidades'] + cambio

                        #comprobacion  estricta para evitar stock negativo
                        if nuevo_stock<0:
                            print("error: el stocke resultante no puede ser negativo")
                        else:
                            producto['unidades']=nuevo_stock
                            print(f"stock actualizado. nuevas unidades: {producto['unidades']}")
                    except ValueError:
                        print("error. debe introducir un numero entero valido")
            if not encontrado:
                print("producto no encontrado en el inventario")

    #opcion 5:mostrar valor total del inventario
    elif opt==5:
        if len(inventario)==0:
            print("el inventario esta vacio")
        else:
            valor_total=0.0
            for producto in inventario:
                #operador aritmetico obligatorio: unidades*precio
                subtotal=producto['unidades']*producto['precio']
                valor_total += subtotal
            print(f"\n el valor total de todo el inventario es: {valor_total:.2f} €")

    #opcion 6:mostrar estadisticas por categoria (listas y tuplas)
    elif opt==6:
        if len(inventario)==0:
            print("el inventario esta vacio")
        else:
            #se crea una lista temporal para extraer las categorias unicas sin repetir
            categorias=[]
            for producto in inventario:
                # se usar el operador 'in' para comprobar si la categoria ya fue guardada
                if producto['categoria'] not in categorias:
                    categorias.append(producto['categoria'])

            print("\n--- estadisiticas por categoria---")
            #lista para guardar tuplas con fromato
            estadisticas=[]

            #se corre cada categoria unidad encontrada('cat')
            for cat in categorias:
                total_unidades=0
                valor_categoria=0.0

                #se recorre el inventaro buscando prodcutos que pertenezcan a esta categoria especifica
                for producto in inventario:
                    if producto['categoria']==cat:
                        total_unidades += producto['unidades']
                        valor_categoria += producto['unidades'] * producto['precio']

                #se crea una tupla ('stats_tupla') con los datos calculados
                stats_tupla=(cat, total_unidades, valor_categoria)
                #se añade a tupla generada a nuestra lista de estadisticas
                estadisticas.append(stats_tupla)

            #se recorre la lista de tuplas para mostrar los resultados ordenados
            for stat in estadisticas:
                #stat[0] accede a la categoria, stat[1] a las unidades, stat[2] al valor total
                print(f"categoriaa: {stat[0].capitalize()} |"
                      f"unidades totales: {stat[1]} | "
                      f"valor total en stock: {stat[2]:.2f} €")


    elif opt==0:
            print("saliendo del inventario...")
            break

    else:
         print("opcion fuera de rango (debe de ser del o al 6)")