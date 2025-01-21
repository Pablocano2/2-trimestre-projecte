
def iteracions_MCD_Euclides(x, y):
    a = max(x, y)
    b = min(x, y)
    i = 0
   
    while b != 0:
        i += 1
        r = a % b
        a = b
        b = r
       
    return i 
