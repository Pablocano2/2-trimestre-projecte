from funcions import mostrar_f, f, compleix_bolzano, biseccio

tol=1e-10
a=float(input("Introdueix el valor de a: "))
b=float(input("Introdueix el valor de b: "))


while not compleix_bolzano(f,a,b):
    print("El valor de a i b no compleix el teorema de bolzano. Torna a introduir a i b.")
    a=float(input("Introdueix el valor de a: "))
    b=float(input("Introdueix el valor de b: "))


solucio, valor_f, iteracion = biseccio(f, a, b, tol)

print("Dades d'entrada: ")

print(mostrar_f(f))

print("Tolerància:" + str(tol))

print("Valor a: "+ str(a) + ".")

print("Valor b: "+ str(b) + ".")

print("Resultat d'aplicar el Mètode de la Bisecció: ")

print("Solució aproximada: x_b = "+ str(solucio) + ".")

print("f(x_b) = " + str(valor_f)+ "." )

print("Nombre d'iteracions: " +str(iteracion)+".")




