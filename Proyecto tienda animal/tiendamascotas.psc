Algoritmo tiendamascotas
	Definir opcion Como Entero
	definir stock_actual, cambio, nuevo_stock Como Entero
	definir nombre_producto Como Caracter
	
	// Menu principal del programa
	Escribir "===== INVENTARIO TIENDA MASCOTAS ====="
	Escribir "1. Añadir producto"
	Escribir "2. Mostrar inventario completo"
	Escribir "3. Buscar producto por nombre"
	Escribir "4. Modificar stock de un producto"
	Escribir "5. Mostrar valor total del inventario"
	Escribir "6. Mostrar estadísticas por categoría"
	Escribir "0. Salir"
	
	Escribir "Seleccione una opcion: "
	Leer opcion
	
	segun opcion hacer
		4:
			Escribir "---modificar stock de un prodcuto---"
			escribir"introduzca el nombre del prodcuto: "
			leer nombre_producto
			
			//simulacion del stock actual del producto encontrado
			stock_actual<-10
			Escribir "Producto: ", nombre_producto, " | Unidades actuales: ", stock_actual
			
			Escribir "Introduzca la cantidad a sumar o restar: "
			Leer cambio
			
			nuevo_stock<-stock_actual + cambio
			
			Si nuevo_stock < 0 Entonces
				Escribir "Error: El stock resultante no puede ser negativo."
			Sino
				stock_actual <- nuevo_stock
				Escribir "Stock actualizado con éxito. Nuevas unidades: ", stock_actual
			FinSi
			
		De Otro Modo:
			Escribir "Opción no disponible."
			
	FinSegun
	
FinAlgoritmo
	