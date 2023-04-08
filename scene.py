import math
import pygame

from button import Button
from narratif.gameNaratif import Naratif

BG_COLOR = (255, 255, 0)
INPUT_FIELD_ACTIVE_COLOR = pygame.Color('lightskyblue3')
INPUT_FIELD_PASSIVE_COLOR = pygame.Color('chartreuse4')

BULLE_IMG_PATH = "./assets/bulle1.jpg"

class Scene:
    def __init__(self, surface, font, characterImage, gameNaratif, characterDialog, text1, action1, text2, action2):
        self.gameNaratif: Naratif = gameNaratif

        self.action1 = action1
        self.action2 = action2

        self.surface = surface
        self.font = font

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

        self.dialogSurface = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
        # self.setDialog(characterDialog)

        self.button1 = Button(surface.get_width() / 6, surface.get_height() / 1.2, 340, 70, font, text1)
        self.button2 = Button(surface.get_width() / 2, surface.get_height() / 1.2, 340, 70, font, text2)

        self.inputRect = pygame.Rect(200, 200, 140, 32)


    def updateDialog(self):
        dialog = self.gameNaratif.paragraphCourant()[1]
        self.setDialog(dialog)

        # self.button1.text = self.gameNaratif.courant.choix[0]
        # self.button2.text = self.gameNaratif.courant.choix[1]
        self.button1.text = ""
        self.button2.text = ""


    def setDialog(self, text):
        dialog = text.split("\n")
        n = 0
        for line in dialog: 
            
            dialogText = self.font.render(line, True, (0, 0, 0))
            dialogText.set_colorkey(pygame.Color(0, 0, 0))
            dialogTextRect = dialogText.get_rect()
            dialogTextRect.center = (self.bulleImageRect.x + 200, self.bulleImageRect.y + 100 + 10*n)
            self.dialogSurface.blit(dialogText, dialogTextRect,)
            n += 1

        pygame.display.update()


    def setCharacter(self, path):
        image = pygame.image.load(path)
        self.characterImage = pygame.transform.scale(image, (400, 200))
        self.characterImageRect = image.get_rect()
        self.characterImageRect.x = math.ceil(self.surface.get_width() / 6)
        self.characterImageRect.y = math.ceil(self.surface.get_height() / 3.33)


    def setChoices(self, c1, c2):
        self.button1.text = c1
        self.button2.text = c2


    def handleClick(self, mousePos):
        if self.button1.isHovered(*mousePos):
            # print(self.action1)
            self.gameNaratif.buttonClick(0)
        elif self.button2.isHovered(*mousePos):
            # print(self.action2)
            self.gameNaratif.buttonClick(1)

        self.updateDialog()


    def draw(self, surface):
        mousePos = pygame.mouse.get_pos()

        surface.fill(BG_COLOR)
        self.dialogSurface.fill(pygame.Color(0, 0, 0, 0))
        surface.blit(self.characterImage, self.characterImageRect)
        surface.blit(self.bulleImage, self.bulleImageRect)
        surface.blit(self.dialogSurface, self.dialogSurface.get_rect())

        # pygame.draw.rect(surface, INPUT_FIELD_PASSIVE_COLOR, self.inputRect, 0)

        self.button1.draw(surface, mousePos)
        self.button2.draw(surface, mousePos)

        pygame.display.update()
