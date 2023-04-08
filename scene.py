import math
import pygame

from button import Button

BG_COLOR = (255, 255, 0)
INPUT_FIELD_ACTIVE_COLOR = pygame.Color('lightskyblue3')
INPUT_FIELD_PASSIVE_COLOR = pygame.Color('chartreuse4')

BULLE_IMG_PATH = "./assets/bulle1.jpg"

class Scene:
    def __init__(self, surface, font, characterImage, characterDialog, text1, action1, text2, action2):
        self.action1 = action1
        self.action2 = action2

        image = pygame.image.load(characterImage)

        self.characterImage = pygame.transform.scale(image, (400, 200))
        self.characterImageRect = image.get_rect()
        self.characterImageRect.x = math.ceil(surface.get_width() / 6)
        self.characterImageRect.y = math.ceil(surface.get_height() / 3.33)

        self.characterDialog = characterDialog

        bulleImage = pygame.image.load(BULLE_IMG_PATH)
        self.bulleImage = pygame.transform.scale(bulleImage, (400, 200))
        self.bulleImageRect = self.bulleImage.get_rect()
        self.bulleImageRect.x = math.ceil(surface.get_width() / 2)
        self.bulleImageRect.y = math.ceil(surface.get_height() / 3.33)

        self.dialogText = font.render(characterDialog, True, (0, 0, 0))
        self.dialogTextRect = self.dialogText.get_rect()
        self.dialogTextRect.center = (self.bulleImageRect.x + 200, self.bulleImageRect.y + 100)

        self.button1 = Button(surface.get_width() / 6, surface.get_height() / 1.2, 340, 70, font, text1)
        self.button2 = Button(surface.get_width() / 2, surface.get_height() / 1.2, 340, 70, font, text2)

        self.inputRect = pygame.Rect(200, 200, 140, 32)


    def handleClick(self, mousePos):
        if self.button1.isHovered(*mousePos):
            print(self.action1)
        elif self.button2.isHovered(*mousePos):
            print(self.action2)


    def draw(self, surface):
        mousePos = pygame.mouse.get_pos()

        surface.fill(BG_COLOR)

        surface.blit(self.characterImage, self.characterImageRect)
        surface.blit(self.bulleImage, self.bulleImageRect)
        surface.blit(self.dialogText, self.dialogTextRect)

        # pygame.draw.rect(surface, INPUT_FIELD_PASSIVE_COLOR, self.inputRect, 0)

        self.button1.draw(surface, mousePos)
        self.button2.draw(surface, mousePos)
