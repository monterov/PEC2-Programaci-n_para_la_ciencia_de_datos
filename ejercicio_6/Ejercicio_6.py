import re

def process_book(ruta_txt, pattern):
    """
    Lee un libro de texto y devuelve una lista con las frases
    que contienen alguna coincidencia con el patrón indicado.

    Las frases se consideran fragmentos de texto que terminan en '.'
    o en '?', y se conserva el signo final.

    Args:
        ruta_txt (str): Ruta del archivo de texto a analizar.
        pattern (str): Expresión regular a buscar dentro de las frases.

    Returns:
        list[str]: Lista de frases donde aparece el patrón.
    """

       # Leemos el archivo
    with open(ruta_txt, "r", encoding="utf-8") as f:
        texto = f.read()
    
    # Unificamos líneas porque las frases pueden estar partidas
    texto = texto.replace("\n", " ")
    
    # Separamos en frases (terminan en '.' o '?')
    frases = []
    frase_actual = ""
    
    for caracter in texto:
        frase_actual += caracter
        if caracter in ".?":
            frase_actual = frase_actual.strip()
            if frase_actual:
                frases.append(frase_actual)
            frase_actual = ""
    
    # Buscamos el patrón (sin distinguir mayúsculas/minúsculas)
    patron = re.compile(pattern, re.IGNORECASE)
    
    # Filtramos las frases que coinciden
    resultado = [frase for frase in frases if patron.search(frase)]
    
    return resultado

# Probamos la función usando lo compartido en el foro por tu parte

ruta_dracula = "/content/drive/MyDrive/Colab Notebooks/Activity_2/data/libros_descomprimidos/Dracula.txt"
ruta_sleepy = "/content/drive/MyDrive/Colab Notebooks/Activity_2/data/libros_descomprimidos/SleepyHollow.txt"

# Test vampírico
pattern = r'\b(?:Dracula|Castle)\b'
ret = process_book(ruta_dracula, pattern)
print("Dracula matches:", len(ret))

assert len(ret) > 0
pat = re.compile(pattern, re.IGNORECASE)
assert all(pat.search(s) for s in ret)
assert any(re.search(r'\bDracula\b', s, re.IGNORECASE) for s in ret)
assert any(re.search(r'\bCastle\b',  s, re.IGNORECASE) for s in ret)
assert all(s.strip().endswith('.') or s.strip().endswith('?') for s in ret)

print("Dracula test OK")

# Test del Jinete sin cabeza
pattern = r'\bsleep\b'
ret = process_book(ruta_sleepy, pattern)
print("Sleep matches:", len(ret))

assert len(ret) > 0
pat = re.compile(pattern, re.IGNORECASE)
assert all(pat.search(s) for s in ret)
assert all(s.strip().endswith('.') or s.strip().endswith('?') for s in ret)

print("Sleepy Hollow test OK") 
