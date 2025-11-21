### Ejercicio 6

Desde la llegada de ChatGPT, el procesamiento del lenguaje natural (“Natural Language Processing”) se ha convertido en una de las áreas más prometedoras de la inteligencia artificial y la ciencia de datos.
Parte de las técnicas que se utilizan están más allá del alcance de este curso, pero también son muy importantes algunas de las técnicas que hemos visto en estas primeras unidades de la asignatura.

En concreto, en este ejercicio hemos descargado dos libros de la web del proyecto Gutenberg:
"The Legend of Sleepy Hollow" de Washington Irving y "Drácula" de Bram Stoker, en formato .txt, y que ya deberías tener extraídos como resultado del ejercicio anterior.

En este ejercicio te pedimos que crees una función process_book que reciba como entrada la ruta de un archivo de texto (formato .txt) y una expresión regular (patrón) de Python, y devuelva una lista con las frases del archivo que contengan alguna coincidencia con el patrón.

En concreto, te pedimos que encuentres:

Todas las frases del libro "Drácula" que contengan la palabra Dracula o la palabra Castle.
Todas las frases del libro "SleepyHollow" que contengan la palabra sleep.
Notas importantes:

En ambos casos, los patrones no deben tener en cuenta mayúsculas y minúsculas.
Es decir, si la misma palabra que tienes que buscar aparece en mayúsculas o minúsculas, debes mostrar ambas.
Además, solo debes buscar la palabra exacta (por ejemplo, si aparece Castle será válido, pero no Newcastle, ya que es una palabra diferente aunque contenga “castle”).

Como parte del ejercicio, el texto debe separarse en frases. Este es un tema que puede llegar a ser muy complejo, por lo que en este ejercicio trabajaremos con una simplificación.
En concreto, consideraremos que las frases terminan siempre con un punto “.” o con un signo de interrogación “?”.
Además, el texto ha sido simplificado para no contener algunos símbolos conflictivos como los puntos suspensivos.
Ten en cuenta que muchas frases están repartidas en más de una línea de texto.
Las frases que se devuelvan deben incluir, en todo caso, el símbolo de final de frase (punto “.” o “?”).

Utiliza los principios de programación funcional que hemos visto en teoría para resolver este ejercicio y expresiones regulares.

En este notebook encontrarás una celda extra con código que puedes utilizar para comprobar que la función se ejecuta correctamente con unas entradas concretas.
Ten en cuenta que esto es solo una ayuda y que es tu responsabilidad probar el código de forma adecuada.
En concreto, durante la corrección se ejecutará el código con otros parámetros.

#### Manos a la obra

Tenemos que crear una función que reciba como entrada la ruta de un archivo de texto (formato .txt) y una expresión regular (patrón) de Python, y devuelva una lista con las frases del archivo que contengan alguna coincidencia con el patrón. 
Encuentro información del método Open:

https://es.stackoverflow.com/questions/383169/m%C3%A9todo-open-en-python

Antes de nada, hay que descargarse el módulo RE, que permite comparar en las cadenas de texto coincidencias

https://docs.python.org/es/3/library/re.html

No sabía bien como separar las frases que no llevan un punto al final o un signo de interrogación, busqué inoformación y encontré texto.replace:

https://es.stackoverflow.com/questions/227452/corregir-espacios-y-mayusculas

Compilo el patrón con la opción re.IGNORECASE para ignorar mayúsculas y minúsculas:

patron_compilado = re.compile(pattern, re.IGNORECASE)

En las indicaciones del ejercicio nos insta a aplicar la programación funcional, así que uso filter junto con una función lambda para quedarme solamente con las frases que contienen el patrón

frases_filtradas = list(
    filter(lambda s: patron_compilado.search(s) is not None, lista_frases)
)
#### Como no encontré la celda con las comprobaciones, pude ver en foro que ya habían preguntado por este tema, así que copié las indicaciones del profesor.




