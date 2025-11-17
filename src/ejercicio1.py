def my_gcd(a, b, verbose=False):
    """
    Calcula el máximo común divisor de dos números enteros positivos
    utilizando el algoritmo de Euclides.

    Args:
        a (int): Primer número entero positivo.
        b (int): Segundo número entero positivo.
        verbose: Si es True, muestra los pasos del algoritmo.

    Returns:
        int: Máximo común divisor de a y b.
    """

# Aplicamos el algoritmo de Euclides usando el bucle repetitivo while
    while True: 
        resto = a % b
        if verbose: # Si es true se mostrarán los valores en cada paso.
            print("a =", a, ", b =", b, ", resto =", resto)

        if resto == 0: # Si el resto es 0, tendremos el máximo común divisor.
            return b
        else: # Y sí no es 0, repetimos el proceso usando dl valor de b como nuevo a y el valor del resto como nuevo b.
            a = b
            b = resto
import math

print("my_cgd:", my_gcd(24, 12))
print("math.gcd: ", math.gcd(24, 12))





