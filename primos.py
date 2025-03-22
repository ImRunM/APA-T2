"""
Imelda Run Montes Martín

Pruebas unitarias:
>>> esPrimo(5)
True

>>> esPrimo(1)
True

>>> esPrimo(74211)
False

>>> primos(10)
(2, 3, 5, 7)

>>> primos(5)
(2, 3)

>>> primos(14)
(2, 3, 5, 7, 11, 13)

>>> descompon(28)
(2, 2, 7)

>>> descompon(30)
(2, 3, 5)

>>> descompon(1)
()

>>> descompon(60)
(2, 2, 3, 5)

>>> mcm(4, 5)
20

>>> mcm(6, 8)
24

>>> mcm(0, 5)
0

>>> mcm(5, 0)
0

>>> mcm(0, 0)
0

>>> mcd(18, 25)
1

>>> mcd(120, 30)
30

>>> mcd(4, 18)
2
"""

def esPrimo(numero):
    """
    Devuelve True si el número es primo, False si no lo es

    >>> for numero in range(2,10):
    ...     print(esPrimo(numero))
    True
    True
    False
    True
    False
    True
    False
    False
    """
    for prueba in range(2, numero):
        if numero % prueba == 0: return False
    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.

    >>> for numero in range(2,7):
    ...    print(primos(numero))
    ()
    (2,)
    (2, 3)
    (2, 3)
    (2, 3, 5)

    """
    return tuple(numero for numero in range(2, numero) if esPrimo(numero) == True)

def descompon(numero):
    """
    Devuelve una tupla con la desposición en factores primos de su argumento.
    
    >>> for numero in range(6, 9):
    ...     print(descompon(numero))
    (2, 3)
    (7,)
    (2, 2, 2)
    """
    factores = []
    divisor = 2

    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    
    return tuple(factores)

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> for numero in range(2, 4):
    ...     print(mcm(numero, numero*2))
    4
    6

    """
    if numero1 == 0 or numero2 == 0:
        return 0

    factoresNum1 = descompon(numero1)
    factoresNum2 = descompon(numero2)

    factores = []
    for factor in set(factoresNum1).union(set(factoresNum2)):
        maxExponente = max(factoresNum1.count(factor), factoresNum2.count(factor))
        factores.extend([factor] * maxExponente)

    mcm = 1
    for factor in factores:
        mcm *= factor

    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el  máximo común divisor de sus argumentos.

    >>> for numero in range(2, 4):
    ...     print(mcd(numero, numero*2))
    2
    3
    """
    if numero1 == 0 and numero2 == 0:
        return 0 

    factoresNum1 = descompon(numero1)
    factoresNum2 = descompon(numero2)

    factores = []
    for factor in set(factoresNum1).union(set(factoresNum2)):
        minExponente = min(factoresNum1.count(factor), factoresNum2.count(factor))
        factores.extend([factor] * minExponente)

    mcd = 1
    for factor in factores:
        mcd *= factor

    return mcd


if __name__ == "__main__":
    import doctest
    doctest.testmod()
