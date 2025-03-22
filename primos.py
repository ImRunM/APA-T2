"""
Imelda Run Montes Martín
"""

def esPrimo(numero):
    """
    Devuelve True si el número es primo, False si no lo es

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2, numero):
        if numero % prueba == 0: return False
    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple(numero for numero in range(2, numero) if esPrimo(numero) == True)

def descompon(numero):
    """
    Devuelve una tupla con la desposición en factores primos de su argumento.
    
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
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

    >>> mcm(90, 14)
    630

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

    >>> mcd(924, 780)
    12
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

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcmN(42, 60, 70, 63)
    1260
    """
    if not numeros: return 0

    resultado = numeros[0]
    for argumento in numeros[1:]:
        resultado = mcm(resultado, argumento)

    return resultado
    
def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    if not numeros: return 0
    
    resultado = numeros[0]
    for argumento in numeros[1:]:
        resultado = mcd(resultado, argumento)

    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()
