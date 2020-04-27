import pygame ,Funkcje
import polos
import kolory
import datetime
import random
from pygame import MOUSEBUTTONDOWN
from pygame import K_KP_ENTER
#Kuba
#inicjacja Pygame oraz ustwienia ekranu
pygame.init()
screen = pygame.display.set_mode((370, 600))  # szerosc i wysokosc
font = pygame.font.SysFont(None, 20)
pygame.display.set_caption("Kolo fortuny ")  # zmienia nazwe terminala



#Funkcja wypisująca tekst na ekran korzytsajaca z pygame
def napisz_zwykły(tekst, x, y, rozmiar, kolor, czcionka):
    cz = pygame.font.SysFont(czcionka, rozmiar)
    rend = cz.render(tekst, 1, kolor)
    screen.blit(rend, (x, y))

#Czesc programu dziejaca się po losowaniu
def polosowaniu(b):
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
        screen.fill((128, 128, 128))


        napisz_zwykły("Wylosowano", 80, 100, 30, kolory.DarkBlue, kolory.cz2)
        napisz_zwykły(str(b), 80, 130, 30, kolory.DarkBlue, kolory.cz2)
        napisz_zwykły("Wroc do menu", 80, 350, 30, kolory.DarkBlue, kolory.cz2)
        pygame.display.update()
def wpisz():

    introo = True
    tab=[]
    slowa=[]
    v=0

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
                        tab2=list(filter(Funkcje.parzysta,slowa))
                        print(tab2)
                    slowa.append(',')
                    tab.clear()

                if event.key == pygame.K_SPACE:
                    tab.append(" ")
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                if mx > 156 and mx < 231 and my > 363 and my < 400:
                    if len(slowa)<=1:

                        wpisz()
                    print(slowa)
                    b=Funkcje.losuj(Funkcje.zamiana(slowa))
                    print(slowa)
                    polosowaniu(b)
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if mx > 120 and mx < 266 and my > 341 and my < 362:
                            for i in range(0, len(tab)):
                                slowa.append(tab[i])
                            slowa.append(',')
                            tab.clear()


        screen.fill((128, 128, 128))

        napisz_zwykły("Podaj slowo  ", 110, 100, 30, kolory.DarkBlue, kolory.cz2)
        napisz_zwykły("Losuj  ", 160, 360, 30, kolory.DarkBlue, kolory.cz2)
        napisz_zwykły("Zatwiedz  ", 120, 330, 30, kolory.DarkBlue, kolory.cz2)
        xz=100
        xz2=100
        xz3=100
        for i in range(0,len(tab)):
            if len(tab)>i:
                if xz2 > 300:
                    napisz_zwykły(str(tab[i]), xz3, 220, 20, kolory.DarkBlue, kolory.cz2)
                    xz3 = xz3 + 11
                elif xz > 300:
                    napisz_zwykły(str(tab[i]), xz2, 190, 20, kolory.DarkBlue, kolory.cz2)
                    xz2 = xz2 + 11
                else:
                    napisz_zwykły(str(tab[i]), xz, 160, 20, kolory.DarkBlue, kolory.cz2)
                    xz=xz+11

        pygame.display.update()
def paint():
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10
    rozmiar=10
    screen = pygame.display.set_mode((1000, 600))
    save = pygame.image.load('save.png')
    dom = pygame.image.load('home.png')
    kwadracik = pygame.image.load('rectangle.png')
    screen.fill((128, 128, 128))
    tryp_rys=False
    p1=polos.poz(800,0,20,600,screen)
    def roundline(srf, color, start, end, radius=1):
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int(start[0] + float(i) / distance * dx)
            y = int(start[1] + float(i) / distance * dy)
            pygame.draw.circle(srf, color, (x, y), radius)
    def kwadratl(srf, color, start, end,rozmiar):
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int(start[0] + float(i) / distance * dx)
            y = int(start[1] + float(i) / distance * dy)
            pygame.draw.rect(srf, color, (x,y,rozmiar,rozmiar))
    try:
        while True:
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                raise StopIteration
            if e.type == pygame.MOUSEBUTTONDOWN:
                #kolory---------------------------------------------------------
                if e.pos[0]>=820 and e.pos[0]<900 and e.pos[1]>0 and e.pos[1]<80:

                    color=kolory.blue
                if e.pos[0]>=900 and e.pos[0]<990 and e.pos[1]>0 and e.pos[1]<80:

                    color=kolory.black
                if e.pos[0]>=900 and e.pos[0]<990 and e.pos[1]>100 and e.pos[1]<190:

                    color=kolory.green
                if e.pos[0] >= 820 and e.pos[0] < 900 and e.pos[1] > 100 and e.pos[1] < 190:

                    color = kolory.red
                if e.pos[0] >= 820 and e.pos[0] < 900 and e.pos[1] > 200 and e.pos[1] < 290:

                    color = kolory.purple
                if e.pos[0]>=900 and e.pos[0]<990 and e.pos[1]>200 and e.pos[1]<290:

                    color=kolory.Aquamarine
                if e.pos[0]>=821 and e.pos[0]<853 and e.pos[1]>507 and e.pos[1]<539:
                    tryp_rys=True

                if e.pos[0] < 800:

                    if tryp_rys:
                        pygame.draw.rect(screen,color,(e.pos[0],e.pos[1],10,10))
                    else:
                        pygame.draw.circle(screen, color, e.pos, radius)
                    draw_on = True
                #zapis---------------------------------------------------------------
                if e.pos[0] >= 821 and e.pos[0] < 900 and e.pos[1] > 568 and e.pos[1] < 600:
                    pygame.image.save(screen, "screenshot.jpeg")
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION:
                if e.pos[0] < 800:
                    if draw_on:
                        if tryp_rys:
                            kwadratl(screen,color,e.pos,last_pos,10)
                        else:
                            roundline(screen, color, e.pos, last_pos, radius)
                    last_pos = e.pos
            p1.rysuj()
            polos.ry(920,0,screen,kolory.czarny)
            polos.ry(820, 0, screen,kolory.blue)
            polos.ry(920, 100, screen, kolory.green)
            polos.ry(820, 100, screen, kolory.red)
            polos.ry(820, 200, screen, kolory.purple)
            polos.ry(920, 200, screen, kolory.Aquamarine)
            screen.blit(save, (821, 568))
            screen.blit(dom, (854, 567))
            screen.blit(kwadracik, (821, 507))

            pygame.display.flip()

    except StopIteration:
        pygame.quit()
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
                    paint()

            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx,my)
                if mx > 110 and mx < 264 and my > 200 and my < 240:
                    wpisz()
                if mx > 160 and mx < 270 and my > 250 and my < 290:
                    paint()
        screen.fill((128, 128, 128))


        now = datetime.datetime.now()
        cza = lambda x: str(x.hour)+":"+str(x.minute)+":"+str(x.second)
        print(cza(now))
        napisz_zwykły(str(cza(now)), 293, 570, 20, kolory.DarkBlue, kolory.cz2)

        napisz_zwykły("Stwórz koło ", 110, 200, 30, kolory.DarkBlue, kolory.cz2)
        napisz_zwykły("Menu ", 140, 70, 40, kolory.DarkBlue, kolory.cz2)
        napisz_zwykły("Paint", 160, 250, 30, kolory.DarkBlue, kolory.cz2)


        pygame.display.update()
menu()
