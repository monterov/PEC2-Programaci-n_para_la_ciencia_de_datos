import csv
from functools import reduce

def create_dictionary(ruta_csv, customer_id):
    """
    Crea un diccionario que agrupa por país todos los productos comprados por un
    cliente concreto, acumulando también las cantidades totales de cada producto.

    Args:
        ruta_csv (str): Ruta del archivo CSV con los datos de la tienda.
        customer_id (str): Identificador del cliente para el que se quiere
            obtener el resumen de compras.

    Returns:
        dict: Diccionario donde cada clave es un país y cada valor es una lista
        de tuplas con el formato (producto, unidades_totales) correspondiente a
        ese cliente.
    """
    with open(ruta_csv, "r", encoding="latin-1") as f:
        lector = csv.DictReader(f, delimiter=";")

        # Viendo en el foro la salida esperada, tendremos que filtrar por clientes y crear una función que recorra cada fila, vaya añadiendo la clave del país,
        # acumule productos y también acumule las cantidades de esos productos.

        # Función para filtrar por cliente
        
        def filtrado_por_cliente(fila):
            return fila["CustomerID"] == str(customer_id)

        filas_cliente = filter(filtrado_por_cliente, lector)

        # Función acumuladora: recorre las filas y construye el diccionario

        def juntar_productos_cantidades(diccionario, fila):
            pais = fila["Country"]  #Primero, el país
            producto = fila["Product"]  # Segundo, el producto
            cantidad = int(fila["Quantity"])  # Tercero, la cantidad

            # Usamos setdefault para evitar el ErrorKey cuando aparece un país nuevo

            diccionario.setdefault(pais, {})

            # Acumulamos cantidades del producto dentro de ese país
            diccionario[pais][producto] = diccionario[pais].get(producto, 0) + cantidad

            return diccionario

        # Construimos el diccionario de países acumulando todas las filas

        diccionario_de_paises = reduce(juntar_productos_cantidades, filas_cliente, {})

        # Convertimos los diccionarios internos en listas de tuplas

        for pais in diccionario_de_paises:
            diccionario_de_paises[pais] = [
                (producto, unidades)
                for producto, unidades in diccionario_de_paises[pais].items()
            ]

    return diccionario_de_paises
    
# Probamos la función

ruta = "/content/drive/MyDrive/Colab Notebooks/Activity_2/data/botiga_en_linia.csv"
create_dictionary(ruta, "C5780")

