import pygame
import main

pygame.init()

clock = pygame.time.Clock()

W = 1280  # variable de la taille de la fenêtre
H = 720

pygame.display.set_caption("Bataille")  # création de la fenêtre
screen = pygame.display.set_mode((W, H))

class Draw:
    def __init__(self):
        path_prefix = "png-cards"
        cardsName = []
        keyCard = []

        self.dictCard = dict()


        for i in ["♠","♣","♥","♦"]:
            for e in range(2,15):
                cardsName.append(f"{e}{i}")

        for j in ["P","T","C","Q"]:
            for k in range(2,15):
                keyCard.append(f"{k}-{j}")

        for i in range(len(keyCard)):
            self.dictCard[cardsName[i]] = pygame.image.load(f"{path_prefix}/{keyCard[i]}.png").convert_alpha()

        self.defaultFont = pygame.font.Font(pygame.font.get_default_font(), 35)

draw = Draw()


main.game.distribution()
n=0
run = True
while run:

    screen.fill(color=(25,150,25))

    #print(f" post tour len joueur1 {len(self.joueur1)} len joueur2 {len(self.joueur2)}")
    if not len(main.game.joueur1) == 0 and not len(main.game.joueur2) == 0:
        #print(f"len joueur1 {len(self.joueur1)} len joueur2 {len(self.joueur2)}")
        main.game.tour()
        j1pos = ((W//2)-draw.dictCard["2♦"].get_size()[0]//2, 10)
        j2pos = ((W//2)-draw.dictCard["2♦"].get_size()[0]//2, H-draw.dictCard["2♦"].get_size()[1]-10)

        j1played = str(main.game.j1_carte.valeur)+ str(main.game.j1_carte.symbole)
        j2played = str(main.game.j2_carte.valeur)+ str(main.game.j2_carte.symbole)

        print(j1played)
        print(j2played)

        screen.blit(draw.dictCard[j1played], j1pos)
        screen.blit(draw.dictCard[j2played], j2pos)



        n += 1
        if main.game.state == 2:
            screen.blit(draw.defaultFont.render("Joueur 2 Gagne",True,(0,0,0)),((W//2)-100,H//2))
        if main.game.state == 1:
            screen.blit(draw.defaultFont.render("Joueur 1 Gagne", True, (0,0,0)), ((W//2)-100,H//2))

        screen.blit(draw.defaultFont.render(f"paquet joueur 1 {len(main.game.joueur1)}",True,(0,0,0)),(j1pos[0]-350,j1pos[1]))
        screen.blit(draw.defaultFont.render(f"paquet joueur 2 {len(main.game.joueur2)}",True,(0,0,0)),(j2pos[0]-350,j2pos[1]))
        screen.blit(draw.defaultFont.render(f"pile de bataille {len(main.game.pile_centrale)}",True,(0,0,0)),(0,H-30))


        #pygame.display.flip()

    if len(main.game.joueur1) == 0 or len(main.game.joueur2) == 0:
        if main.game.state == 2:
            screen.blit(draw.defaultFont.render("Joueur 2 Gagne",True,(0,0,0)),((W//2)-100,H//2))
        if main.game.state == 1:
            screen.blit(draw.defaultFont.render("Joueur 1 Gagne", True, (0,0,0)), ((W//2)-100,H//2))

        screen.blit(draw.defaultFont.render(f"nbre de tour : {n}", True, (0,0,0)),(W//2,H//2))

        pygame.display.flip()

    if not run:
        break
    pygame.display.flip()
    clock.tick(60)
    # teste des events
    for event in pygame.event.get():
        # joueur quitte ?
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
