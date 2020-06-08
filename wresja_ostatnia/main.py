'''
18.05.2020
'''
import datetime
import pygame
from pygame import MOUSEBUTTONDOWN
from pakiet1 import Funkcje, kolory, losowanie, paint
# inicjacja Pygame oraz ustwienia ekranu
pygame.init()
SCREEN_ = pygame.display.set_mode((370, 600))  # szerosc i wysokosc
FONT = pygame.font.SysFont(None, 20)
pygame.display.set_caption("Kolo fortuny ")  # zmienia nazwe terminala
TLO = pygame.image.load('asety/TLO1.jpg')  # TLO
# główne menu
def menu():
    introo = True
    SCREEN = pygame.display.set_mode((370, 600))
    # główna pętla
    while introo:
        '''Eventy pygame'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_p:
                    paint.paint_2(menu)  # przejscie do Paint
            # Obsługa M_Yszki i przejscia do dalszej części programu
            if event.type == MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                print(m_x, m_y)
                if  110 < m_x < 264 and  200 < m_y < 240:
                    losowanie.wpisz(menu)  # przejscie do losowania
                if 160 < m_x < 270 and 250 < m_y < 290:
                    paint.paint_2(menu)  # przejscie do Paint
        # Rysowanie tła oraz iterfejsu-----
        SCREEN.blit(TLO, (0, 0))
        # wypisywanie aktualnego czasu za pomocą biblioteki datatime oraz wyrażenia lambda
        now = datetime.datetime.now()
        cza = lambda x: str(x.hour) + ":" + str(x.minute) + ":" + str(x.second)
        Funkcje.napisz_zwykły(str(cza(now)), 293, 570, 20, kolory.DARKBLUE, kolory.CZ2, SCREEN)
        Funkcje.napisz_zwykły("Stwórz koło ", 110, 200, 30, kolory.DARKBLUE, kolory.CZ2, SCREEN)
        Funkcje.napisz_zwykły("Menu ", 140, 70, 40, kolory.DARKBLUE, kolory.CZ2, SCREEN)
        Funkcje.napisz_zwykły("Paint", 160, 250, 30, kolory.DARKBLUE, kolory.CZ2, SCREEN)
        pygame.display.update()
        
if __name__ == '__main__':
    menu()

