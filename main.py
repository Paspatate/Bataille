import random
from file import File
from pile import Pile

symbole = {1:"♠", 2:"♣", 3:"♥", 4:"♦"}
Valeur = {14:"A", 13:"K", 12:"Q", 11:"J"}
#class de carte
class Carte:
    def __init__(self,v,s) -> None:
        self.valeur = v
        self.symbole = s
    def __str__(self) -> str:
        if self.valeur>=11:
            return f"{Valeur[self.valeur]} de {self.symbole} "
        else:
            return f"{self.valeur} de {self.symbole} "

#création d'une liste de carte mélanger
cartes = []

for i in range(1,5):
    for j in range(2,15):
        cartes.append(Carte(j,symbole[i]))
random.shuffle(cartes)

#création d'une classe qui créer la partie
class parti:
    def __init__(self) -> None:
        self.joueur1 = File()
        self.joueur2 = File()
        self.nbr_tour = 0
        self.j1_carte = Carte(0,0)
        self.j2_carte = Carte(0,0)

#Méthode pour distibuer l'ensemble des cartes aux 2 joueurs
    def distribution(self):
        #print("distribution")
        for j in range (len(cartes)):
            if j%2 ==0 :
                self.joueur1.enfiler(cartes.pop())
            else :
                self.joueur2.enfiler(cartes.pop())

#affiche les cartes du joueur 1 et du joueur 2
    def __str__(self):
        return print("Joueur 1 : ",self.joueur1, "/n Joueur 2 : ",self.joueur2)

#empile les cartes dans une pile centrale
    def action_jeu(self,pile_centrale):
        j1_carte = Carte(0,0)
        j2_carte = Carte(0,0)

        self.j1_carte = self.joueur1.defiler()
        pile_centrale_j1.empiler(self.j1_carte)

        self.j2_carte = self.joueur2.defiler()
        pile_centrale_j2.empiler(self.j2_carte)

        return (self.j1_carte,self.j2_carte)

#fait un tour de jeu
    def tour(self):
        pile_centrale_j1 = Pile()
        pile_centrale_j2 = Pile()

        try:
            j1_carte, j2_carte = self.action_jeu(pile_centrale_j1,pile_centrale_j2)
        except:
            return

        if j1_carte.valeur == j2_carte.valeur:

        while j1_carte.valeur == j2_carte.valeur and not len(self.joueur1) == 0 and not len(self.joueur2) == 0:
            print(f"Tour {self.nbr_tour}:\nJoueur 1 : {j1_carte}    Joueur 2 : {j2_carte}")
            print("égalité")
            self.nbr_tour+=1

            try:
                j1_carte, j2_carte = self.action_jeu(pile_centrale)
                print(f"Joueur 1 : {j1_carte}    Joueur 2 : {j2_carte}")
            except:
                return

            try:
                j1_carte, j2_carte = self.action_jeu(pile_centrale)
                print(f"Joueur 1 : {j1_carte}    Joueur 2 : {j2_carte}")
            except:
                return

        if j1_carte.valeur < j2_carte.valeur:
            print(f"Tour {self.nbr_tour}:\nJoueur 1 : {j1_carte}    Joueur 2 : {j2_carte}")
            print("joueur 2 gagne la manche")

            ran=random.randint(0,10)
            if ran>=5:
                for i in range(len(pile_centrale)):
                    self.joueur2.enfiler(pile_centrale.depiler())
            else:
                for i in range(0,len(pile_centrale),2):
                    varrr= pile_centrale.depiler()
                    self.joueur2.enfiler(pile_centrale.depiler())
                    self.joueur2.enfiler(varrr)
        elif j2_carte.valeur < j1_carte.valeur:
            print(f"Tour {self.nbr_tour}:\n Joueur 1 : {j1_carte}    Joueur 2 : {j2_carte}")
            print("joueur 1 gagne la manche")
            for i in range(len(pile_centrale)):
                self.joueur1.enfiler(pile_centrale.depiler())
        else:
            return
            raise SystemError("personne n'a gagner le tour tu n'a rien a faire la")
#définit le déroulement d'une partie
    def game_loop(self):
        self.distribution()

        while not len(self.joueur1) == 0 and not len(self.joueur2) == 0:
            print(f"Le joueur 1 a {len(self.joueur1)} cartes et le joueur 2 a {len(self.joueur2)} cartes")
            self.tour()
            self.nbr_tour+=1

        print("Il y a eu : ",self.nbr_tour, " tours")

        if len(self.joueur1) == 0:

            return "Joueur 2 Gagne!!!!!!!!!!!!!!!!!!!"
        else:
            return "joueur 1 Gagne!!!!!!!!!!!!!!!!!!!"
game = parti()

#print(game.game_loop())
#print(f"len joueur1 {len(game.joueur1)} len joueur2 {len(game.joueur2)}")
