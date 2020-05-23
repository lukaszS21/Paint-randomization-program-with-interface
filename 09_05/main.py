import pygame
from pakiet1 import Funkcje, kolory, losowanie, paint
import datetime
from pygame import MOUSEBUTTONDOWN

#inicjacja Pygame oraz ustwienia ekranu
pygame.init()
screen = pygame.display.set_mode((370, 600))  # szerosc i wysokosc
font = pygame.font.SysFont(None, 20)
pygame.display.set_caption("Kolo fortuny ")  # zmienia nazwe terminala
tlo = pygame.image.load('asety/tlo1.jpg') #tlo


#główne menu
def menu():
    #tworzenie ekranu
    introo = True
    screen = pygame.display.set_mode((370, 600))
    #główna pętla
    while introo:
        #Eventy pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_p:
                    paint.paint_2(menu) #przejscie do Paint

            #Obsługa myszki i przejscia do dalszej części programu
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx,my)
                if mx > 110 and mx < 264 and my > 200 and my < 240:
                    losowanie.wpisz(menu) #przejscie do losowania
                if mx > 160 and mx < 270 and my > 250 and my < 290:
                    paint.paint_2(menu) #przejscie do Paint

        #Rysowanie tła oraz iterfejsu-----
        screen.blit(tlo, (0, 0))
        #wypisywanie aktualnego czasu za pomocą biblioteki datatime oraz wyrażenia lambda
        now = datetime.datetime.now()
        cza = lambda x: str(x.hour)+":"+str(x.minute)+":"+str(x.second)
        Funkcje.napisz_zwykły(str(cza(now)), 293, 570, 20, kolory.DarkBlue, kolory.cz2, screen)
        Funkcje.napisz_zwykły("Stwórz koło ", 110, 200, 30, kolory.DarkBlue, kolory.cz2, screen)
        Funkcje.napisz_zwykły("Menu ", 140, 70, 40, kolory.DarkBlue, kolory.cz2, screen)
        Funkcje.napisz_zwykły("Paint", 160, 250, 30, kolory.DarkBlue, kolory.cz2, screen)
        pygame.display.update()
menu()
