# Càlcul del mcm i Mcd

## Descripció

En aquesta pràctica es tenien de fer els clculs del mcm i el Mcd.

## Implementació

En la primera funció he fet uns calculs per saber els seus factors primers i les seves potències.

def descomposar(x):
    
    factors = {}
    divisor = 2
    while x >= 2:
        while x % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            x //= divisor
        divisor += 1
    return factors

En aquesta funció he calculat el mcm.

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

I en aquesta he calculat el MCD.

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

## Anàlisi dels resultats i conclusions y Dificultats i Solucions

Aquesta practicà m'ha resultat dificil perque no sabia com començar i fer les operacions, pero me mirat un video i crec que ja ho tinc apres.
### Enllaç video:

https://www.youtube.com/watch?v=EIMtWwMIPuc
