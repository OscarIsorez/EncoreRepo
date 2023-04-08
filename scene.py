import math
import pygame

from button import Button

BG_COLOR = (255, 255, 0)
INPUT_FIELD_ACTIVE_COLOR = pygame.Color('lightskyblue3')
INPUT_FIELD_PASSIVE_COLOR = pygame.Color('chartreuse4')

class Scene:
    def __init__(self, surface, font, characterImage, characterDialog, text1, action1, text2, action2):
        image = pygame.image.load(characterImage)

        self.characterImage = pygame.transform.scale(image, (400, 200))
        self.imageRect = image.get_rect()
        self.imageRect.x = math.ceil(surface.get_width() / 6)
        self.imageRect.y = math.ceil(surface.get_height() / 3.33)

        self.characterDialog = characterDialog

        self.button1 = Button(surface.get_width() / 6, surface.get_height() / 1.2, 340, 70, font, text1, action1)
        self.button2 = Button(surface.get_width() / 2, surface.get_height() / 1.2, 340, 70, font, text2, action2)

        self.inputRect = pygame.Rect(200, 200, 140, 32)


    def handleClick(self, mousePos):
        self.button1.handleClick(mousePos)
        self.button2.handleClick(mousePos)


    def draw(self, surface):
        mousePos = pygame.mouse.get_pos()

        surface.fill(BG_COLOR)

        surface.blit(self.characterImage, self.imageRect)

        # pygame.draw.rect(surface, INPUT_FIELD_PASSIVE_COLOR, self.inputRect, 0)

        self.button1.draw(surface, mousePos)
        self.button2.draw(surface, mousePos)
