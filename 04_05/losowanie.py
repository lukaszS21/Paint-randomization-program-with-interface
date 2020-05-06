import pygame ,Funkcje
import polos
import kolory
import datetime
import random
import paint

from pygame import MOUSEBUTTONDOWN
from pygame import K_KP_ENTER
def polosowaniu(b,menu):

    screen = pygame.display.set_mode((370, 600))  # szerosc i wysokosc
    font = pygame.font.SysFont(None, 20)
    pygame.display.set_caption("Kolo fortuny ")  # zmienia nazwe terminala
    tlo = pygame.image.load('asety/tlo1.jpg')
    xpoz=60
    tlo = pygame.image.load('asety/tlo1.jpg')
    introo = True
    #Program będzie trwał dopóki introo nie zmieni swojej wartości na Fale lub spełni się inny warunek końca tej pętli taki jak Quit lub wywołanie innego ekranu np menu()
    while introo:
        #inicjacja jakiegos wydarzenia
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Funkcje wbudowane w pygame odpowiadające wydarzeniu jakim jest wciśnięcie klawiszów jeśli wcisniemy ESCape program sie zakonczy

                if event.key == pygame.K_ESCAPE:
                    introo = False
                    quit()
            # Funkcje wbudowane w pygame odpowiadające wydarzeniu jakim jest wciśnięcie myszki
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                if mx > 79 and mx < 296 and my > 359 and my < 390:
                        menu()
        #
        screen.blit(tlo, (0, 0))
        Funkcje.napisz_zwykły("Wylosowano", 80, 100, 30, kolory.DarkBlue, kolory.cz2,screen)
        try:
            if len(b)<5:
                Funkcje.napisz_zwykły(str(b), 160, 140, 20, kolory.DarkBlue, kolory.cz2,screen)
            elif len(b)>5 and len(b)<15:
                Funkcje.napisz_zwykły(str(b), 100, 140, 20, kolory.DarkBlue, kolory.cz2, screen)
            else:
                Funkcje.napisz_zwykły(str(b), 30, 140, 20, kolory.DarkBlue, kolory.cz2, screen)
        except :
            print("pusty plik-----")
            return 0
        Funkcje.napisz_zwykły("Wroc do menu", 80, 350, 30, kolory.DarkBlue, kolory.cz2,screen)
        pygame.display.update()
def wpisz(menu):

    screen = pygame.display.set_mode((370, 600))  # szerosc i wysokosc
    font = pygame.font.SysFont(None, 20)
    pygame.display.set_caption("Kolo fortuny ")  # zmienia nazwe terminala
    tlo = pygame.image.load('asety/tlo1.jpg')
    tlo = pygame.image.load('asety/tlo1.jpg')
    introo = True
    tab=[]
    slowa=[]
    v=0
    tym=[]
    b=""
    while introo:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    tab.append('q')
                if event.key == pygame.K_ESCAPE:
                    introo = False
                    quit()
                if event.key == pygame.K_a:
                    tab.append('a')
                    v=v+5
                if event.key == pygame.K_b:
                    tab.append('b')
                if event.key == pygame.K_z:
                    tab.append('z')
                if event.key == pygame.K_x:
                    tab.append('x')
                if event.key == pygame.K_c:
                    tab.append('c')
                if event.key == pygame.K_v:
                    tab.append('v')
                if event.key == pygame.K_b:
                    tab.append('b')
                if event.key == pygame.K_n:
                    tab.append('n')
                if event.key == pygame.K_m:
                    tab.append('m')
                if event.key == pygame.K_s:
                    tab.append('s')
                if event.key == pygame.K_d:
                    tab.append('d')
                if event.key == pygame.K_f:
                    tab.append('f')
                if event.key == pygame.K_g:
                    tab.append('g')
                if event.key == pygame.K_h:
                    tab.append('h')
                if event.key == pygame.K_j:
                    tab.append('j')
                if event.key == pygame.K_k:
                    tab.append('k')
                if event.key == pygame.K_l:
                    tab.append('l')
                if event.key == pygame.K_w:
                    tab.append('w')
                if event.key == pygame.K_e:
                    tab.append('e')
                if event.key == pygame.K_r:
                    tab.append('r')
                if event.key == pygame.K_t:
                    tab.append('t')
                if event.key == pygame.K_y:
                    tab.append('y')
                if event.key == pygame.K_u:
                    tab.append('u')
                if event.key == pygame.K_i:
                    tab.append('i')
                if event.key == pygame.KMOD_CTRL and pygame.K_l:
                    tab.append('ł')
                if event.key == pygame.K_o:
                    tab.append('o')
                if event.key == pygame.K_p:
                    tab.append('p')
                if event.key == pygame.K_1:
                    print(tab)
                if event.key == pygame.K_BACKSPACE:
                    tab.pop()
                if event.key == pygame.K_KP_ENTER:

                    for i in range(0, len(tab)):
                        slowa.append(tab[i])
                    slowa.append(',')
                    tab.clear()

                if event.key == pygame.K_SPACE:
                    tab.append(" ")
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                if mx > 156 and mx < 231 and my > 363 and my < 400:
                    if len(slowa)<1:
                        wpisz(menu)


                    b = Funkcje.losuj(Funkcje.zamiana(slowa))
                    polosowaniu(b,menu)
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if mx > 120 and mx < 266 and my > 341 and my < 362:
                            for i in range(0, len(tab)):

                                slowa.append(tab[i])

                            slowa.append(',')
                            print(slowa)
                            tab.clear()
                #zapisuje słowa do pliku-----------------------
                if mx > 110 and mx < 288 and my > 390 and my < 430:
                    Funkcje.zapisdopliku("los.txt", slowa)
                #odczyt z pliku-------------------------------
                if mx > 100 and mx < 310 and my > 430 and my < 460:
                    slowa=Funkcje.odczytzpliku("los.txt")



        screen.blit(tlo, (0, 0))
        Funkcje.napisz_zwykły("Podaj slowo  ", 110, 100, 30, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("Losuj  ", 160, 360, 30, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("Zatwiedz  ", 120, 330, 30, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("zapisz slowa", 110, 390, 30, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("odczytaj slowa", 100, 420, 30, kolory.DarkBlue, kolory.cz2,screen)

        xz=100
        xz2=100
        xz3=100
        for i in range(0,len(tab)):
            if len(tab)>i:
                if xz2 > 300:
                    Funkcje.napisz_zwykły(str(tab[i]), xz3, 220, 20, kolory.DarkBlue, kolory.cz2,screen)
                    xz3 = xz3 + 11
                elif xz > 300:
                    Funkcje.napisz_zwykły(str(tab[i]), xz2, 190, 20, kolory.DarkBlue, kolory.cz2,screen)
                    xz2 = xz2 + 11
                else:
                    Funkcje.napisz_zwykły(str(tab[i]), xz, 160, 20, kolory.DarkBlue, kolory.cz2,screen)
                    xz=xz+11

        pygame.display.update()