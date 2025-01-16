def iteracions_MCD_Euclides(a, b):
    i = 0
    if  b < a:
        aux= b
        b = a
        a= aux
    while b != 0:
        a, b = b, a % b
        i += 1
    return i