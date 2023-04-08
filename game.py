import pygame

class Game:
    def __init__(self):
        #définir si jeu a commencé
        self.is_playing = False

    def start(self):
        self.is_playing = True

    def game_over(self):
        #remettre jeu à neuf
        self.is_playing = False

    def update (self, screen):
        # appliquer image du joueur
        screen.fill((0, 0, 0))