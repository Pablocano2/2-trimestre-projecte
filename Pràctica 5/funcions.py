import csv
def llegir_registre():
    file= csv.read_csv('registre.csv')

    registre= []
    next(file)
    for i in file:
        registre.append(i[1],i[2])
    print(registre)
    
def escriure_registre():
    pass