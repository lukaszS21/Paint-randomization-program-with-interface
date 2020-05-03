import pygame ,Funkcje
import polos
import kolory
import datetime
import random
import paint
import losowanie
from pygame import MOUSEBUTTONDOWN
from pygame import K_KP_ENTER
#inicjacja Pygame oraz ustwienia ekranu
pygame.init()
screen = pygame.display.set_mode((370, 600))  # szerosc i wysokosc
font = pygame.font.SysFont(None, 20)
pygame.display.set_caption("Kolo fortuny ")  # zmienia nazwe terminala
tlo = pygame.image.load('asety/tlo1.jpg')
#Czesc programu dziejaca się po losowaniu


def menu():
    introo = True

    screen = pygame.display.set_mode((370, 600))
    while introo:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    introo = False
                if event.key == pygame.K_ESCAPE:
                    introo = False
                    quit()
                if event.key == pygame.K_p:
                    paint.paint_2(menu)

            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx,my)
                if mx > 110 and mx < 264 and my > 200 and my < 240:
                    losowanie.wpisz(menu)
                if mx > 160 and mx < 270 and my > 250 and my < 290:
                    paint.paint_2(menu)
        screen.blit(tlo, (0, 0))


        now = datetime.datetime.now()
        cza = lambda x: str(x.hour)+":"+str(x.minute)+":"+str(x.second)
        Funkcje.napisz_zwykły(str(cza(now)), 293, 570, 20, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("Stwórz koło ", 110, 200, 30, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("Menu ", 140, 70, 40, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("Paint", 160, 250, 30, kolory.DarkBlue, kolory.cz2,screen)
        pygame.display.update()
menu()
