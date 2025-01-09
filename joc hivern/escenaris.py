import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Escenari:
    def __init__(self, nom, descripcio, opcions, ascii_art):
        self.nom = nom
        self.descripcio = descripcio
        self.opcions = opcions
        self.ascii_art = ascii_art

    def mostra(self):
        clear_screen()
        print(self.ascii_art)
        print(f"\n{self.descripcio}\n")
        for clau, text in self.opcions.items():
            print(f"{clau}: {text}")

entrada = Escenari(
    "Entrada",
    "Ets en una habitació fosca amb una porta tancada davant teu. Veus un calaix petit i una espelma apagada.",
    {
        "1": "Consultar inventari",
        "2": "Obrir el calaix",
        "3": "Encendre l'espelma",
        "4": "Anar a la porta"
    },
    r"""
      .    !__________!    .    _______
     /_\   |____  ____|   /_\   |__*__|    <-Calaix
    __|__  {____}{____}  __|__  |__*__|
    __|_*_|__%%%%%%%%%%%%__|_*_|__|__*__|__
      |   | %%%%%%%%%%%%%% |   |  |/   \|
           %%%%%%%%%%%%%%%%
          %%%%%%%%%%%%%%%%%%       
         %%%%%%%%%%%%%%%%%%%%
        /||||||||||||||||||||\
        ||||||||||||||||||lc||
    """
)

passadis = Escenari(
    "Passadís",
    "Has obert la porta i ara ets en un passadís llarg. Hi ha un cofre tancat amb clau i una porta al final.",
    {
        "1": "Consultar inventari",
        "2": "Obrir el cofre",
        "3": "Anar a la cova",
        "4": "Anar a la biblioteca",  
        "5": "Anar al jardí"           
    },
    r"""
      +-------------------------------+
      |                               |
      |         [ Cofre tancat ]      | <- Cofre
      |                               |
      |                      ||       |
      |                      ||       | <- Porta
      +-------------------------------+
      |           Passadís            |
      +-------------------------------+
    """
)


cova = Escenari(
    "Cova",
    "Estàs dins d'una cova humida. Hi ha un passatge tancat a la teva esquerra i una paret amb runa.",
    {
        "1": "Consultar inventari",
        "2": "Explorar la paret",
        "3": "Entrar al passatge",
        "4": "Tornar al passadís"
    },
    r"""
      +---------------------+
      |       /\           |
      |      /  \          |
      |     /    \         |
      |    / Paret \        | <- Paret de pedra
      |     =======         |
      |    > Passatge       | <- Passatge
      +---------------------+
      |        Cova         |
      +---------------------+
    """
)

biblioteca = Escenari(
    "Biblioteca",
    "Et trobes en una antiga biblioteca amb llibres polsosos. A la taula hi ha un llibre obert i una antorxa.",
    {
        "1": "Consultar inventari",
        "2": "Agafar l'antorxa",
        "3": "Explorar la taula",
        "4": "Sortir per la porta ",  
    },
    r"""
      +----------------------------+
      |  ||||||||||||||||||||||||  | <- Estanteries de llibres
      |        [ Taula ]           |
      |         (____)             | <- Antorxa
      |                     ||     |
      |                     ||     | <- Porta
      +----------------------------+
      |        Biblioteca          |
      +----------------------------+
    """
)

jardi = Escenari(
    "Jardí",
    "Et trobes en un jardí amb una font al mig. Hi ha un banc i una porta oculta a l'extrem. A terra, veus un encenedor.",
    {
        "1": "Consultar inventari",
        "2": "Agafar l'encenedor",
        "3": "Explorar la font",
        "4": "Tornar al passadís"
    },
    r"""
      +---------------------------+
      |            _             |
      |         ~  (_)  ~        | <- Font
      |                           |
      |   [ Banc ]         ||     |
      |    (Encededor)      ||    | <- Porta oculta
      +---------------------------+
      |           Jardí           |
      +---------------------------+
    """
)

tresor = Escenari(
    "Sala del Tresor",
    "Has arribat a la Sala del Tresor! El joc ha acabat.",
    {
        "1": "Sortir del joc"
    },
    r"""
      +---------------------------+
      |          TRESOR!          |
      |         _________         |
      |        |$$$$$$$$$|        |
      |        |$$$$$$$$$|        |
      |        |_________|        |
      +---------------------------+
      |        FELICITATS         |
      +---------------------------+
    """
)










