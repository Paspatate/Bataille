from _typeshed import Self
import random
from file import File
from pile import Pile

symbole = {1:"pique", 2:"trefle", 3:"coeur", 4:"carreau"}

#class de carte
class Carte:
    def __init__(self,v,s) -> None:
        self.valeur = v
        self.symbole = s
    def __str__(self) -> str:
        return f"valeur : {self.valeur},  signe :, {self.signe}"

#création d'une liste de carte mélanger
cartes = []

for i in range(1,5):
    for j in range(2,14):
        cartes.append(Carte(j,symbole[i]))
print(len(cartes))
random.shuffle(cartes)
print(cartes[3])

class parti:
    def __init__(self, jeu1, jeu2) -> None:
        self.joueur1 = jeu1
        self.joueur2 = jeu2
    
    def tour(self):
        pile_centrale = Pile()

        j1_carte = self.joueur1.defiler()
        j2_carte = self.joueur2.defiler()

        pile_centrale.empiler(j1_carte)
        pile_centrale.empiler(j2_carte)

        while j1_carte.valeur == j2_carte.valeur and not self.joueur1.est_vide() and not self.joueur2.est_vide():
            j1_carte = self.joueur1.defiler()
            j2_carte = self.joueur2.defiler()

            pile_centrale.empiler(j1_carte)
            pile_centrale.empiler(j2_carte)

            j1_carte = self.joueur1.defiler()
            j2_carte = self.joueur2.defiler()

            pile_centrale.empiler(j1_carte)
            pile_centrale.empiler(j2_carte)
        
        if j1_carte < j2_carte:
            for i in len(pile_centrale):
                self.joueur1.enfiler(pile_centrale.depiler())
        elif j2_carte < j1_carte:
            for i in len(pile_centrale):
                self.joueur2.enfiler(pile_centrale.depiler())
        else:
            raise SystemError("personne n'a gagner le tour tu n'a rien a faire la")

        def game_loop(self):
            #distribuer les carte
            while self.joueur1.est_vide() or self.joueur2.est_vide():
                self.tour()
            
            if self.joueur1.est_vide():
                return "Joueur 2 Gagne"
            else:
                return "joueur 1 Gagne"

