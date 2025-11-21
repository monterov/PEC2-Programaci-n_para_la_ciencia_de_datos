def Diccionario_productos_filtrados_por_nombre():
    """
    Devuelve un diccionario con los productos cuyo nombre contiene 'ni' o 'te',
    en mayúsculas o minúsculas, o que empiezan por la letra 'u' o 'U'. El valor
    devuelto para cada producto es su precio unitario.

    Returns:
        dict: Diccionario con productos filtrados y sus precios unitarios.
    """

    productos_filtrados = {} # Creamos el diccionario vacío

    for _, fila in df_botiga.iterrows(): # Recorremos cada fila
        producto = fila["Product"] # Por producto
        precio = fila["UnitPrice"] # Por precio unitario

    # Necesitamos que solo salgan los productos que contengan "ni", "te" y comiencen por "U". 

        if ("ni" in producto) or ("Ni" in producto) or \
           ("te" in producto) or ("Te" in producto) or \
           producto.startswith("u") or producto.startswith("U"):

    # Añadimos entrada al diccionario usando como clave el producto y su valor por unidad

           productos_filtrados[producto] = precio

    return productos_filtrados

# Probamos la función

Diccionario_productos_filtrados_por_nombre()
