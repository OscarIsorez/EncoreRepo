import pygame
import math
from narratif import gameNaratif
from button import Button
from scene import Scene
from game import Game

gameStart = Game()

game = gameNaratif.Naratif()

pygame.init()

# définir une clock
clock = pygame.time.Clock()
FPS = 60
FONT = pygame.font.Font(None, 32)
game = gameNaratif.Naratif()
running = True

# générer la fenêtre du jeu
pygame.display.set_caption("trouver le dealer de winnie")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('./assets/th.jpg')

play_button = pygame.image.load('./assets/start.jpg')
play_button = pygame.transform.scale(play_button, (700, 400))
play_button_rect = play_button.get_rect()
# on place l'image au centre de l'écran
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 3.33)

button_one = pygame.draw.rect(screen, (100, 100, 100), [
                              screen.get_width()/2, screen.get_height()/2, 140, 40])

button_two = pygame.draw.rect(screen, (100, 100, 100), [
                              screen.get_width()/2, screen.get_height()/2, 140, 40])




# mickey = pygame.image.load('./assets/mickey.svg')
scene1 = Scene(screen, FONT, "./assets/" + game.paragraphCourant()[0] + ".jpg", game, game.paragraphCourant()[1],"Bouton1", "bouton 1 scene", "Bouton2", "bouton 2 scene")

# mickey = pygame.transform.scale(mickey, (400, 200))
# mickey_rect = mickey.get_rect()
# # on place l'image au centre de la partie gauche de l'écran
# mickey_rect.x = math.ceil(screen.get_width() / 6)
# mickey_rect.y = math.ceil(screen.get_height() / 3.33)

# créer une surface de dessin (buffer) pour afficher les éléments du jeu en arrière-plan
buffer = pygame.Surface(screen.get_size())

# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''

# create rectangle
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')

# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive

active = False


def get_text_rect_dimensions(text, font, screen):
    # Définition des couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Création de la surface de texte
    text_surface = font.render(text, True, BLACK, WHITE)
    text_rect = text_surface.get_rect()

    # Vérification si le texte dépasse la taille maximale de l'écran divisée par 3
    if text_rect.width > screen.get_width() / 3:
        # Calcul de la largeur du rectangle pour le texte sur 2 lignes
        rect_width = screen.get_width() / 3
        rect_height = text_rect.height * 2 + 10  # Ajout d'un espace entre les 2 lignes
    else:
        # Utilisation de la largeur du texte comme largeur du rectangle
        rect_width = text_rect.width
        rect_height = text_rect.height

    # Calcul du left et top pour centrer le rectangle sur l'écran
    rect_left = (screen.get_width() - rect_width) / 2
    rect_top = (screen.get_height() - rect_height) / 2

    # Retourne les dimensions idéales pour le rectangle
    return rect_left, rect_top, rect_width, rect_height


def update(screen):
    # Dessiner la surface de dessin sur l'écran de jeu
    # screen.blit(buffer, (0, 0))
    # Dessiner la zone de texte de l'utilisateur avec la couleur appropriée

    scene1.draw(screen)
    
    #Recupére les informations à afficher
    image = game.paragraphCourant()[0]
    text = game.paragraphCourant()[1]

    scene1.setDialog(text)
    scene1.setCharacter("./assets/" + image + ".jpg")

    buttonText = game.getChoices()
    if not (buttonText is None):
        scene1.setchoices(buttonText[0], buttonText[1])
    else : scene1.setChoices("", "")


    # on dessine sur l'écran le resultat de la fonction create_text_rect
    # screen.blit(create_text_rect(choix1, base_font, screen), (screen.get_width() / 6, screen.get_height() / 2))
# the variable as a tuple
    


# Générer la fenetre de dialogue
font = pygame.font.SysFont(None, 24)
BLACK = "#000000"
personnage = "mickey"

dialog_out = font.render('hello', True, BLACK)
dialog_out = pygame.transform.scale(dialog_out, (600, 400))
photo_personnage = pygame.image.load('./assets/' + personnage + ".jpg")


# boucle tant que condition est vrai
while running:

    # vérifier si notre jeu a commencé ou non
    if gameStart.is_playing:
        # déclencher les éléments de la maprtie
        update(buffer)  # dessiner les éléments du jeu sur la surface de dessin
    else:
        # ajouter mon écran de bienvenue
        # remplir l'écran de jeu avec une couleur blanche
        # dessiner le bouton play sur la surface de dessin
        buffer.blit(play_button, (400, 300))

    # copier la surface de dessin sur l'écran de jeu
    screen.blit(buffer, (0, 0))

    # mettre à jour
    # pygame.display.flip()

    for event in pygame.event.get():

        # que l'évenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detecter si un joueur lache la touche du clvier

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérifier si la souris est en collision avec le bouton play
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancé en changeant
                gameStart.start()

            mouse = pygame.mouse.get_pos()

            scene1.handleClick(mouse)

        elif event.type == pygame.KEYDOWN:
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
            # Unicode standard is used for string
            # formation
            else:
                # Ajouter le caractère tapé à la chaîne de texte de l'utilisateur
                user_text += event.unicode
    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter le nombre de FPS
    clock.tick(FPS)

pygame.quit()
