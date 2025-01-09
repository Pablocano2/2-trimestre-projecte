
from escenaris import entrada, passadis, cova, biblioteca, jardi, tresor

def mostrar_inventari(inventari):
    if not inventari:
        print("\nOps! Tens l'inventari buit...")
    else:
        print("\nAixò és el que tens ara mateix a l'inventari:")
        for element in inventari:
            print(f"  - {element}")

def accions_entrada(accio, inventari):
    escenari_actual = entrada

    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        if "clau petita" not in inventari:
            print("\nTrobes una clau petita dins del calaix!")
            inventari.append("clau petita")
        else:
            print("\nEl calaix està buit.")
    elif accio == "3":
        print("\nL'espelma necessita un encenedor.")
    elif accio == "4":
        if "clau petita" in inventari:
            print("\nObres la porta amb la clau petita i entres al passadís.")
            escenari_actual = passadis
        else:
            print("\nLa porta està tancada amb clau.")
    else:
        print("\nOpció no vàlida.")

    return escenari_actual, inventari

def accions_passadis(accio, inventari):
    escenari_actual = passadis

    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        if "antorxa" in inventari:
            print("\nTrobes un cofre, però no hi ha res important dins.")
        else:
            print("\nEl cofre està buit.")
    elif accio == "3":
        if "antorxa encesa" in inventari:
            print("\nAvances cap a la cova amb l'antorxa encesa.")
            escenari_actual = cova
        else:
            print("\nNo pots avançar sense llum. Necessites una antorxa encesa.")
    elif accio == "4":
        print("\nTornes a la biblioteca.")
        escenari_actual = biblioteca  # Modificat perquè torni a la biblioteca
    elif accio == "5":
        if "antorxa" in inventari:
            print("\nPasses per la biblioteca i arribes al jardí.")
            escenari_actual = jardi
        else:
            print("\nPer accedir al jardí, primer necessites passar per la biblioteca.")
    else:
        print("\nOpció no vàlida.")

    return escenari_actual, inventari

def accions_cova(accio, inventari):
    escenari_actual = cova

    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        print("\nExplores la paret i descobreixes un passatge bloquejat per pedres.")
    elif accio == "3":
        if "antorxa encesa" in inventari:
            print("\nCreues el passatge i arribes a la Sala del Tresor!")
            escenari_actual = tresor  # Canvia a la Sala del Tresor
        else:
            print("\nNo pots entrar al passatge sense llum.")
    elif accio == "4":
        print("\nTornes al passadís.")
        escenari_actual = passadis
    else:
        print("\nOpció no vàlida.")

    return escenari_actual, inventari

def accions_biblioteca(accio, inventari):
    escenari_actual = biblioteca

    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        if "antorxa" not in inventari:
            print("\nAgafes l'antorxa de la taula!")
            inventari.append("antorxa")
        else:
            print("\nJa has agafat l'antorxa.")
    elif accio == "3":
        print("\nLa taula és plena de pols i llibres antics.")
    elif accio == "4":
        print("\nSurts per la porta i arribes al jardí.")
        escenari_actual = jardi
    elif accio == "5":
        print("\nTornes al passadís.")
        escenari_actual = passadis
    else:
        print("\nOpció no vàlida.")

    return escenari_actual, inventari

def accions_jardi(accio, inventari):
    escenari_actual = jardi

    if accio == "1":
        mostrar_inventari(inventari)
    elif accio == "2":
        if "encenedor" not in inventari:
            print("\nTrobes un encenedor al terra i l'agafes!")
            inventari.append("encenedor")
        else:
            print("\nJa tens l'encenedor.")
    elif accio == "3":
        if "antorxa" in inventari and "encenedor" in inventari and "antorxa encesa" not in inventari:
            print("\nEncens l'antorxa amb l'encenedor. Ara pots avançar amb seguretat.")
            inventari.remove("antorxa")
            inventari.append("antorxa encesa")
        elif "antorxa encesa" in inventari:
            print("\nL'antorxa ja està encesa.")
        else:
            print("\nNecessites tenir una antorxa i un encenedor per encendre-la.")
    elif accio == "4":
        print("\nTornes al passadís.")
        escenari_actual = passadis
    else:
        print("\nOpció no vàlida.")

    return escenari_actual, inventari

def accions_tresor(accio, inventari):
    escenari_actual = tresor

    if accio == "1":
        print("\nGràcies per jugar! El joc ha acabat.")
        exit()  
    else:
        print("\nOpció no vàlida.")
    
    return escenari_actual, inventari

