from funcions import accions_entrada, accions_passadis, accions_cova, accions_biblioteca, accions_jardi
from escenaris import entrada, passadis, cova, biblioteca, jardi, tresor

def joc():
    escenari_actual = entrada
    inventari = []

    while True:
        escenari_actual.mostra()
        accio = input("\nQuè vols fer? ")

        if escenari_actual.nom == "Entrada":
            escenari_actual, inventari = accions_entrada(accio, inventari)
        elif escenari_actual.nom == "Passadís":
            escenari_actual, inventari = accions_passadis(accio, inventari)
        elif escenari_actual.nom == "Cova":
            escenari_actual, inventari = accions_cova(accio, inventari)
        elif escenari_actual.nom == "Biblioteca":
            escenari_actual, inventari = accions_biblioteca(accio, inventari)
        elif escenari_actual.nom == "Jardí":
            escenari_actual, inventari = accions_jardi(accio, inventari)
        elif escenari_actual.nom == "Sala del Tresor":
            print("\nGràcies per jugar! El joc ha acabat.")
            break

        input("\nPrem Enter per continuar...")

if __name__ == "__main__":
    joc()