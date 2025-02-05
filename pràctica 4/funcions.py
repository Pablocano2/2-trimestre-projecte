def f(x):
    return 2*x-4

def compleix_bolzano(f, a, b):
    if f(a) * f(b) < 0:
        return True
    return False

def biseccio(f, a, b, tol):
    i = 0
    xm= (a+b)/2
    while f(xm)>tol:
        if f(a)*f(xm)<0:
            b=xm
        else:
            a=xm

        i += 1
    xm= (a+b)/2
    return xm,f(xm),i 