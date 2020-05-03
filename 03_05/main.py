import pygame ,Funkcje
import polos
import kolory
import datetime
import random
from pygame import MOUSEBUTTONDOWN
from pygame import K_KP_ENTER
#inicjacja Pygame oraz ustwienia ekranu
pygame.init()
screen = pygame.display.set_mode((370, 600))  # szerosc i wysokosc
font = pygame.font.SysFont(None, 20)
pygame.display.set_caption("Kolo fortuny ")  # zmienia nazwe terminala




#Czesc programu dziejaca się po losowaniu
def polosowaniu(b):
    xpoz=60
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
        Funkcje.napisz_zwykły("Wylosowano", 80, 100, 30, kolory.DarkBlue, kolory.cz2,screen)
        if len(b)<5:
            Funkcje.napisz_zwykły(str(b), 160, 140, 20, kolory.DarkBlue, kolory.cz2,screen)
        elif len(b)>5 and len(b)<15:
            Funkcje.napisz_zwykły(str(b), 100, 140, 20, kolory.DarkBlue, kolory.cz2, screen)
        else:
            Funkcje.napisz_zwykły(str(b), 30, 140, 20, kolory.DarkBlue, kolory.cz2, screen)
        Funkcje.napisz_zwykły("Wroc do menu", 80, 350, 30, kolory.DarkBlue, kolory.cz2,screen)
        pygame.display.update()
def wpisz():

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
                        wpisz()


                    b = Funkcje.losuj(Funkcje.zamiana(slowa))
                    polosowaniu(b)
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



        screen.fill((128, 128, 128))
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
def paint():
    draw_on = False
    last_pos = (0, 0)
    color = kolory.black
    radius = 10
    screen = pygame.display.set_mode((1000, 600))
    #ikonki do paint
    kolo= pygame.image.load('circle.png')
    save = pygame.image.load('save.png')
    dom = pygame.image.load('home.png')
    kwadracik = pygame.image.load('rectangle.png')
    minus= pygame.image.load('minus.png')
    plus = pygame.image.load('plus.png')
    tencza = pygame.image.load('rainbow.png')
    screen.fill((128, 128, 128))
    tryp_rys=False
    p1=polos.poz(800,0,20,600,screen)
    p2=polos.poz(980,0,20,600,screen)
    tenczaa = False
    j = random.randint(0, 255)
    l = random.randint(0, 255)
    k = random.randint(0, 255)
    d = kolory.kolor_w(j, k, l)
    try:
        while True:
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                raise StopIteration
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                #kolory---------------------------------------------------------
                #rózowe
                if e.pos[0]>=820 and e.pos[0]<860 and e.pos[1]>0 and e.pos[1]<40:
                    color=kolory.pink
                if e.pos[0]>=860 and e.pos[0]<900 and e.pos[1]>0 and e.pos[1]<40:
                    color=kolory.HotPink
                if e.pos[0]>=900 and e.pos[0]<940 and e.pos[1]>0 and e.pos[1]<40:
                    color=kolory.Violet
                if e.pos[0]>=940and e.pos[0]<980 and e.pos[1]>0 and e.pos[1]<40:
                    color=kolory.DeepPink
                #czerwone
                if e.pos[0]>=820 and e.pos[0]<860 and e.pos[1]>40 and e.pos[1]<80:
                    color=kolory.Red
                if e.pos[0]>=860 and e.pos[0]<900 and e.pos[1]>40 and e.pos[1]<80:
                    color=kolory.Crimson
                if e.pos[0] >= 900 and e.pos[0] < 940 and e.pos[1] > 40 and e.pos[1] < 80:
                    color = kolory.DarkRed
                if e.pos[0]>=940and e.pos[0]<980 and e.pos[1]>40 and e.pos[1]<80:
                    color=kolory.LightCoral
                 # pomaranczowe
                if e.pos[0]>=820 and e.pos[0]<860 and e.pos[1]>80 and e.pos[1]<120:
                    color=kolory.OrangeRed
                if e.pos[0]>=860 and e.pos[0]<900 and e.pos[1]>80 and e.pos[1]<120:
                    color=kolory.DarkOrange
                if e.pos[0] >= 900 and e.pos[0] < 940 and e.pos[1] > 80 and e.pos[1] < 120:
                    color = kolory.Orange
                if e.pos[0]>=940and e.pos[0]<980 and e.pos[1]>80 and e.pos[1]<120:
                    color=kolory.Tomato





                if e.pos[0]>=821 and e.pos[0]<853 and e.pos[1]>507 and e.pos[1]<539:
                    tryp_rys=True
                if e.pos[0]>=861 and e.pos[0]<893 and e.pos[1]>507 and e.pos[1]<539:
                    tryp_rys=False
                if e.pos[0]>=821 and e.pos[0]<853 and e.pos[1]>400 and e.pos[1]<432:
                    color=d
                    tenczaa=True

                #rysowanie gdy sie nacisnie sie myszke--------------------------------------
                if e.pos[0] < 800-radius:
                    if tryp_rys:
                        pygame.draw.rect(screen,color,(e.pos[0],e.pos[1],radius,radius))
                    else:
                        pygame.draw.circle(screen, color, e.pos, radius)
                    draw_on = True
                #zapis---------------------------------------------------------------
                if e.pos[0] >= 821 and e.pos[0] < 900 and e.pos[1] > 568 and e.pos[1] < 600:
                    pygame.image.save(screen, "screenshot.jpeg")
                #powrót do menu
                    if e.pos[0] >= 854 and e.pos[0] < 896 and e.pos[1] > 567 and e.pos[1] < 600:
                        menu()
                #zmiana rozmiaru rysowania-------------------------
                if e.pos[0] >= 821 and e.pos[0] < 853 and e.pos[1] > 447 and e.pos[1] < 507:
                        if radius >=10:
                            radius=radius-10
                            pygame.draw.rect(screen,kolory.gray, (905,447,100,24))
                            Funkcje.napisz_zwykły(str(radius), 905, 447, 20, kolory.DarkBlue, kolory.cz2,screen)
                if e.pos[0] >= 861 and e.pos[0] < 893 and e.pos[1] > 447 and e.pos[1] < 507:
                        radius=radius+10
                        pygame.draw.rect(screen,kolory.gray, (905,447,100,24))
                        Funkcje.napisz_zwykły(str(radius), 905, 447, 20, kolory.DarkBlue, kolory.cz2,screen)


            #gdy przytrzymana myszka ------------------------------------
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION:
                if e.pos[0] < 800-radius:
                    if draw_on:
                        if tryp_rys:
                            Funkcje.kwadratl(screen,color,e.pos,last_pos,radius)
                        else:
                            Funkcje.roundline(screen, color, e.pos, last_pos, radius)
                    last_pos = e.pos
            #rysowanie ikon itp---------------------------------------
            p1.rysuj()
            p2.rysuj()
            #kolory------------------------------
            #rozowy
            polos.ry(820,0,screen,kolory.pink)
            polos.ry(860, 0, screen, kolory.HotPink)
            polos.ry(900, 0, screen, kolory.Violet)
            polos.ry(940, 0, screen, kolory.DeepPink)
            #czerwony
            polos.ry(820, 40, screen, kolory.Red)
            polos.ry(860, 40, screen, kolory.Crimson)
            polos.ry(900, 40, screen, kolory.DarkRed)
            polos.ry(940, 40, screen, kolory.LightCoral)
            #pomaranczowe
            polos.ry(820, 80, screen, kolory.OrangeRed)
            polos.ry(860, 80, screen, kolory.DarkOrange)
            polos.ry(900, 80, screen, kolory.Orange)
            polos.ry(940, 80, screen, kolory.Tomato)
            # zólte
            gold = (255, 215, 0)
            Yellow = (255, 255, 0)
            LightYellow = (255, 255, 224)
            Khaki = (240, 230, 140)
            polos.ry(820, 80, screen, kolory.OrangeRed)
            polos.ry(860, 80, screen, kolory.DarkOrange)
            polos.ry(900, 80, screen, kolory.Orange)
            polos.ry(940, 80, screen, kolory.Tomato)
            if tenczaa==True:
                j=random.randint(0,255)
                l = random.randint(0, 255)
                k = random.randint(0, 255)
                d=kolory.kolor_w(j,k,l)

            screen.blit(tencza, (821, 400))
            screen.blit(save, (821, 568))
            screen.blit(dom, (854, 567))
            screen.blit(kwadracik, (821, 507))
            screen.blit(minus, (821, 447))
            screen.blit(plus, (861, 447))
            screen.blit(kolo, (861, 507))
            Funkcje.napisz_zwykły("zmiana rozmiaru", 820, 420, 20, kolory.DarkBlue, kolory.cz2,screen)
            Funkcje.napisz_zwykły("zmiana pedzla", 820, 480, 20, kolory.DarkBlue, kolory.cz2,screen)
            Funkcje.napisz_zwykły("menu", 820, 538, 20, kolory.DarkBlue, kolory.cz2,screen)

            pygame.display.flip()

    except StopIteration:
        pygame.quit()
def menu():
    introo = True
    tlo = pygame.image.load('tlo1.jpg')
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
        screen.blit(tlo, (0, 0))


        now = datetime.datetime.now()
        cza = lambda x: str(x.hour)+":"+str(x.minute)+":"+str(x.second)
        Funkcje.napisz_zwykły(str(cza(now)), 293, 570, 20, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("Stwórz koło ", 110, 200, 30, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("Menu ", 140, 70, 40, kolory.DarkBlue, kolory.cz2,screen)
        Funkcje.napisz_zwykły("Paint", 160, 250, 30, kolory.DarkBlue, kolory.cz2,screen)


        pygame.display.update()
menu()
