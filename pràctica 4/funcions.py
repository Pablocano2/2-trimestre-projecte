def f(x):
    return 2*x-4
def compleix_bolzano(f, a, b):
    if f(a) * f(b) < 0:
        return True
    return False