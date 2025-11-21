#Importamos librerías

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

df_botiga = pd.read_csv(
    '/content/drive/MyDrive/Colab Notebooks/Activity_2/data/botiga_en_linia.csv',
    sep=';',encoding='latin-1' # El archivo no estaba en UtF-8 y hubo que codificarlo a latin-1
)  
df_botiga.head() # Creado el dataframe, verificamos 

 # 2.1 Devuelve los primeros 100 valores del dataframe ordenado por país y fecha.

from datetime import date

# Transformamos la columna date en formato datatime.
df_botiga["Date"] = pd.to_datetime(df_botiga["Date"])
df_botiga_por_pais_fecha = df_botiga.sort_values(by=['Country', 'Date']) # Con sort_value() ordenamos primero por países usando la columna Country y después por fecha, usando la columna Date.
df_botiga_por_pais_fecha.head(100) 

# 2.2 En primer lugar, se quiere crear una nueva columna en el dataframe para la Fecha, en formato dd/mm/yyyy.

# Creamos columna y cambiamos formato usando dt.strftime

df_botiga["Date_format"] = df_botiga["Date"].dt.strftime("%d/%m/%Y")
df_botiga[["Date_format"]].head() # Se comprueba columna 

# 2.3

def Retorna_productes_categoria(categoria):
    """
    Devuelve un diccionario con los productos que pertenecen a una categoría dada
    y el total de unidades vendidas de esa categoría.

    Args:
        categoria (str): Nombre de la categoría sobre la que se desea obtener la información.

    Returns:
        dict: Diccionario con la categoría, la lista de productos únicos
        y la cantidad total de unidades vendidas.
    """

    df_botiga_categoria = df_botiga[df_botiga["Category"] == categoria]
    botiga_lista_productos = df_botiga_categoria["Product"].unique().tolist()
    botiga_total_productos_vendidos = df_botiga_categoria["Quantity"].sum()

    resultado = {
        "Categoría": categoria,
        "Productos": botiga_lista_productos,
        "Total productos vendidos": botiga_total_productos_vendidos
    }
# Probamos la función

Retorna_productes_categoria("Oficina")
    return resultado

# 2.4 

def Import_total_tipus_pagament(metodo_pago, fecha_inicio, fecha_fin):
    """
    Calcula el importe total cobrado mediante un método de pago entre dos fechas
    dadas, dentro del intervalo especificado.

    Args:
        metodo_pago (str): Método de pago por el que se desea filtrar
            (por ejemplo, 'Targeta', 'Efectiu', etc.).
        fecha_inicio (str): Fecha inicial en formato 'dd/mm/yyyy'.
        fecha_fin (str): Fecha final en formato 'dd/mm/yyyy'.

    Returns:
        str: Mensaje con el importe total cobrado con ese método de pago
        entre las fechas proporcionadas.
    """
    # Necesitamos cambiar el formato de las columnas Date, Total y las fechas de inicio y final

    df_botiga["Total"] = df_botiga["Total"].str.replace(",", ".").astype(float)  # Transformamos la columna Total en formato numérico
    df_botiga["Date"] = pd.to_datetime(df_botiga["Date"], dayfirst=True)  # Convertimos la fecha a datetime 
    fecha_entrada_inicio = pd.to_datetime(fecha_inicio, dayfirst=True)  # Convertimos fecha de inicio a datetime
    fecha_entrada_fin = pd.to_datetime(fecha_fin, dayfirst=True)  # Convertimos fecha de fin a datetime

    # Ahora debemos filtrar por el método de pago y por el rango de fechas de inicio y fin

    filtro_pago = df_botiga["PaymentMethod"] == metodo_pago 
    filtro_fechas = (
        (df_botiga["Date"] >= fecha_entrada_inicio) &
        (df_botiga["Date"] <= fecha_entrada_fin)
    )

    df_filtrado = df_botiga[filtro_pago & filtro_fechas]

    # Calculamos el importe total

    importe_total = df_filtrado["Total"].sum()
    total_str = f"{importe_total:.2f}".replace(".", ",")

    # Formato de salida que requiere el ejercicio

    mensaje = (
        f"Por el método de pago {metodo_pago}, se han cobrado {total_str} euros "
        f"entre el {fecha_inicio} y el {fecha_fin}."
    )

    return mensaje

# Probamos la función

Import_total_tipus_pagament("Targeta", "01/01/2023", "31/03/2023")
