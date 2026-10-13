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