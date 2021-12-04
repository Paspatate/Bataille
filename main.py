#from _typeshed import Self
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
        return f"valeur :{self.valeur}  symbole :{self.symbole} "

#création d'une liste de carte mélanger
cartes = []

for i in range(1,5):
    for j in range(2,15):
        cartes.append(Carte(j,symbole[i]))
print(len(cartes))
random.shuffle(cartes)


class parti:
    def __init__(self) -> None:
        self.joueur1 = File()
        self.joueur2 = File()

    def distribution(self):
        print("distribution")
        for j in range (len(cartes)):
            if j%2 ==0 :
                self.joueur1.enfiler(cartes.pop())
            else :
                self.joueur2.enfiler(cartes.pop())

    def __str__(self):
        return print(self.joueur1)

    def action_jeu(self,pile_centrale):
        j1_carte = Carte(0,0)
        j2_carte = Carte(0,0)

        j1_carte = self.joueur1.defiler()
        pile_centrale.empiler(j1_carte)

        j2_carte = self.joueur2.defiler()
        pile_centrale.empiler(j2_carte)

        return (j1_carte,j2_carte)

    def tour(self):
        pile_centrale = Pile()

        #j1_carte = self.joueur1.defiler()
        #j2_carte = self.joueur2.defiler()

        #pile_centrale.empiler(j1_carte)
        #pile_centrale.empiler(j2_carte)
        try:
            j1_carte, j2_carte = self.action_jeu(pile_centrale)
        except:
            return

        while j1_carte.valeur == j2_carte.valeur and not len(self.joueur1) == 0 and not len(self.joueur2) == 0:
            print("égalité")
            #j1_carte = self.joueur1.defiler()
            #j2_carte = self.joueur2.defiler()

            #pile_centrale.empiler(j1_carte)
            #pile_centrale.empiler(j2_carte)

            try:
                j1_carte, j2_carte = self.action_jeu(pile_centrale)
            except:
                return

            #j1_carte = self.joueur1.defiler()
            #j2_carte = self.joueur2.defiler()

            #pile_centrale.empiler(j1_carte)
            #pile_centrale.empiler(j2_carte)

            try:
                j1_carte, j2_carte = self.action_jeu(pile_centrale)
            except:
                return

            print("len pile_centrale ",len(pile_centrale))

        if j1_carte.valeur < j2_carte.valeur:
            print("joueur 2 gagne la manche")
            for i in range(len(pile_centrale)):
                self.joueur1.enfiler(pile_centrale.depiler())
        elif j2_carte.valeur < j1_carte.valeur:
            print("joueur 1 gagne la manche")
            for i in range(len(pile_centrale)):
                self.joueur2.enfiler(pile_centrale.depiler())
        else:
            return
            raise SystemError("personne n'a gagner le tour tu n'a rien a faire la")

    def game_loop(self):
        print("1")
        self.distribution()
        print("2")
        print(f" post tour len joueur1 {len(self.joueur1)} len joueur2 {len(self.joueur2)}")

        while not len(self.joueur1) == 0 and not len(self.joueur2) == 0:
            print(f"len joueur1 {len(self.joueur1)} len joueur2 {len(self.joueur2)}")
            self.tour()


        if len(self.joueur1) == 0:
            return "Joueur 2 Gagne"
        else:
            return "joueur 1 Gagne"
game = parti()

print(game.game_loop())
print(f"len joueur1 {len(game.joueur1)} len joueur2 {len(game.joueur2)}")
