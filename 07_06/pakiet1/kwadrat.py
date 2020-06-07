import pygame.gfxdraw
from pakiet1 import kolory

# tworzy obiekt rysujący kwadrat wykorzystywany do rysowania interfejsu
class poz():
    def __init__(self, x_1, x_2, y_1, y_2, screen):
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2
        self.screen = screen

    def wypisz(self):
        print(self.x_1)
        print(self.x_2)
        print(self.y_1)
        print(self.y_2)

    def rysuj(self):
        pygame.draw.rect(self.screen, kolory.CZARNY, (self.x_1, self.x_2, self.y_1, self.y_2))

# funckje do rysowania kradratu
def ry(x, y, screen, kolor):
    """

    :param x: 
    :param y:
    :param screen:
    :param kolor:
    :return:
    """
    pygame.draw.rect(screen, kolor, (x, y, 40, 40))
    pygame.display.update()

def ry2(x, y, screen, kolor):
    pygame.draw.rect(screen, kolor, (x, y, 800, 800))
    pygame.display.update()
