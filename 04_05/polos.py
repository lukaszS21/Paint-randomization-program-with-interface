import pygame as pg
import pygame.gfxdraw
import sys,os,math
import kolory
class poz():
    def __init__(self,x1,x2,y1,y2,screen):

        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.screen=screen
    def wypisz(self):
        print( self.x1)
    def rysuj(self):

        pygame.draw.rect(self.screen, kolory.czarny, (self.x1, self.x2, self.y1, self.y2))
def ry(x,y,screen,kolor):
    pygame.draw.rect(screen, kolor, (x,y,40,40))
    pygame.display.update()
def ry2(x,y,screen,kolor):
    pygame.draw.rect(screen, kolor, (x,y,800,800))
    pygame.display.update()
