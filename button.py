import pygame

BTN_COLOR = (0, 255, 0)
BTN_HOVER_COLOR = (100, 255, 100)

class Button:
    def __init__(self, x, y, w, h, font, text, action):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.font = font

        self.text = text

        self.action = action

    def isHovered(self, mx, my):
        return mx >= self.x and mx <= self.x + self.w \
            and my >= self.y and my <= self.y + self.h

    def handleClick(self, mousePos):
        if self.isHovered(*mousePos):
            print(self.action)

    def draw(self, surface, mousePos):
        if self.isHovered(*mousePos):
            color = BTN_HOVER_COLOR
        else:
            color = BTN_COLOR
        pygame.draw.rect(surface, color, [self.x, self.y, self.w, self.h])
        surface.blit(self.font.render(self.text, True, (255, 0, 0)), (self.x, self.y))
