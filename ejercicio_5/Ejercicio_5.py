# 5.1 

import zipfile
import os

def zip_decompression(zip_path, extraer_en):
    """
    Descomprime un archivo ZIP en la carpeta indicada.

    Args:
        zip_path (str): Ruta completa del archivo ZIP.
        extraer_en (str): Ruta completa de la carpeta donde descomprimir.

    """

    # Creamos carpeta para alojar el archivo zip.
    os.makedirs(extraer_en)
    

    # Le damos la orden de descomprimir
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extraer_en)

    print(f"Archivo descomprimido en: {extraer_en}")

# Probamos función creando una carpeta en Drive

zip_path = "/content/drive/MyDrive/Colab Notebooks/Activity_2/data/books.zip"
carpeta_destino = "/content/drive/MyDrive/Colab Notebooks/Activity_2/data/libros_descomprimidos"

zip_decompression(zip_path, carpeta_destino)

# 5.2 

def file_sizes_in_mb(archivo1, archivo2):
    """
    Calcula el tamaño en megabytes de dos archivos y lo muestra por pantalla.

    Args:
        path1 (str): Ruta del primer archivo.
        path2 (str): Ruta del segundo archivo.

    Returns:
         Información de resultados en pantalla.
    """
# Obtenemos el tamaño del archivo en bytes y lo convertimos en MB
    size1 = os.path.getsize(archivo1) / (1024 * 1024) 
    size2 = os.path.getsize(archivo2) / (1024 * 1024) 

    print("El archivo {} tiene un tamaño de {:.4f} MB".format(os.path.basename(archivo1), size1))
    print("El archivo {} tiene un tamaño de {:.4f} MB".format(os.path.basename(archivo2), size2))

# Probamos la función

ruta_dracula = "/content/drive/MyDrive/Colab Notebooks/Activity_2/data/libros_descomprimidos/Dracula.txt"
ruta_sleepyhollow = "/content/drive/MyDrive/Colab Notebooks/Activity_2/data/libros_descomprimidos/SleepyHollow.txt"

file_sizes_in_mb(ruta_dracula, ruta_sleepyhollow)
