def descomposar(x):
    
    factors = {}
    divisor = 2
    while x >= 2:
        while x % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            x=x // divisor
        divisor += 1
    return factors


def calcul_mcm(x,y):
    
    llista_primers_x = descomposar(x)
    llista_primers_y = descomposar(y)
    mcm = 1

    for i in llista_primers_x:
        if i not in llista_primers_y:
            mcm *= i
        elif llista_primers_x.count(i) >= llista_primers_y.count(i):
            mcm *= i
   
    for i in llista_primers_y:
        if i not in llista_primers_x:
            mcm *= i
        elif llista_primers_x.count(i) < llista_primers_y.count(i):
            mcm *= i

    return mcm
def calcul_MCD(x,y):
    
    llista_primers_x = descomposar(x)
    llista_primers_y = descomposar(y)
    MCD = 1

    for i in llista_primers_x:
        for j in llista_primers_y:
            if (i == j):
                MCD *= i
                llista_primers_y.remove(j)
                break
    return MCD