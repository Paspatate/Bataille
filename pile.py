class Cellule:
    """une cellule d'une liste chaînée"""

    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        return str(self.valeur)


class Pile:
    """structure de pile"""

    def __init__(self):
        self.tete = None
        self.taille = 0

    def __str__(self):
        l = []
        c = self.tete
        while c is not None:
            l.append(c.__str__())
            c = c.suivante
        txt = '->'.join(l)
        return txt

    def __len__(self):
        return self.taille


    def est_vide(self):
        return self.tete is None

    def empiler(self, v):
        self.tete = Cellule(v, self.tete)
        self.taille += 1

    def depiler(self):
        if self.est_vide():
            raise IndexError("depiler sur une pile vide")
        v = self.tete.valeur
        self.tete = self.tete.suivante
        self.taille -= 1
        return v