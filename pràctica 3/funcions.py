import random
def genera_llista(rang, longitud):
    
    llista = []
    for i in range(longitud):
        llista.append(random.randint(1, rang))
    return llista

def compta_repeticions(llista):
    llista_elements = []
    num_repeticions = []
    
    for element in llista:
        num_rep=0
        for element2 in llista:
            if element == element2:
                num_rep += 1
        llista_elements.append(element)
        num_repeticions.append(num_rep)
    return llista_elements, num_repeticions



def ordena_manual(llista):
    llista_ordenada = llista[:]

    for i in range(len(llista_ordenada)):
        for j in range(i + 1, len(llista_ordenada)):
            if llista_ordenada[i] > llista_ordenada[j]:
                llista_ordenada[i], llista_ordenada[j] = llista_ordenada[j], llista_ordenada[i]

    return llista_ordenada

