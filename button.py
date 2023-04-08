import pygame

BTN_COLOR = (100, 100, 100)

class Button:
    def __init(self, x, y, w, h, text, action):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.text = text

        self.action = action

    def isHovered(self, mx, my):
        return mx >= self.x and mx <= self.x + self.w \
            and my >= self.y and my <= self.y + self.h

    def handleClick(self, mousePos):
        if self.isHovered(*mousePos):
            print(self.action)


    def draw(self, surface):
        pygame.draw.rect(surface, BTN_COLOR, [self.x, self.y, self.w, self.h])
