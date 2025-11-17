### Ejercicio 1

Escribe una función `my_gcd(a, b, verbose=False)` que calcule el máximo común divisor de dos números enteros positivos utilizando un algoritmo propio (por ejemplo, el algoritmo de Euclides).

La función debe devolver el MCD.

Si `verbose=True`, debe imprimir los pasos que sigue para encontrarlo.

Una vez implementada la función, compara el resultado con la función incorporada en Python `math.gcd(a, b)` para verificar que es correcto.

---

Antes de empezar a programar, he consultado información sobre el algoritmo de Euclides para refrescar la idea:

➡️ [Algoritmo de Euclides — Khan Academy](https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)

Una vez tenía claro el procedimiento, empecé a implementar la función.

---

### Error en la primera ejecución

Al probar la función, apareció este error:

![Error mostrado durante la ejecución](pantallazo_ejercicio_1_pec_2.png)

La causa era evidente: estaba utilizando `math.gcd` sin haber importado antes el módulo `math`.

Añadí la línea `import math` al principio del archivo y el problema quedó resuelto.

También corregí un lapsus en un comentario (“logaritmo” en lugar de “algoritmo”), cosas que pasan después de varias horas seguidas frente al ordenador.

---

### Resultado final

Una vez corregido todo, la función devuelve el mismo resultado que `math.gcd`, así que parece que está correcta.
