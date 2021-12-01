class Cellule:
    """une cellule d'une liste chaînée"""

    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        return str(self.valeur)


class File:
    """structure de file"""

    def __init__(self):
        self.tete = None
        self.queue = None
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

    def enfiler(self, x):
        c = Cellule(x, None)
        if self.est_vide():
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c
        self.taille += 1

    def defiler(self):
        if self.est_vide():
            raise IndexError("retirer sur une file vide")
        v = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        self.taille -= 1
        return v