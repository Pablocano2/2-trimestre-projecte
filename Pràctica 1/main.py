from funcions import calcul_mcm, calcul_MCD


nombres = [12, 15]


mcd = calcul_MCD(nombres)
mcm = calcul_mcm(nombres)


print(f"Els nombres són: {nombres}")
print(f"El Màxim Comú Divisor (MCD) és: {mcd}")
print(f"El mínim comú múltiple (mcm) és: {mcm}")