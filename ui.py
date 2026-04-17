import pygame
from utils.colors import *

class Button:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action
        self.font = pygame.font.SysFont("arial", 18)

    def draw(self, win):
        mouse = pygame.mouse.get_pos()
        color = BUTTON_HOVER if self.rect.collidepoint(mouse) else BUTTON

        pygame.draw.rect(win, color, self.rect)

        txt = self.font.render(self.text, True, TEXT)
        win.blit(txt, (self.rect.x + 10, self.rect.y + 10))

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()