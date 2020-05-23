import pygame
from pakiet1 import Funkcje, kolory, polos
import random


def paint_2(menu):
    clock = pygame.time.Clock()
    FPS=120
    draw_on = False
    last_pos = (0, 0)
    color = kolory.black
    radius = 10
    screen = pygame.display.set_mode((1000, 600))
    #ikonki do paint
    kolo= pygame.image.load('asety/circle.png')
    save = pygame.image.load('asety/save.png')
    dom = pygame.image.load('asety/home.png')
    kwadracik = pygame.image.load('asety/rectangle.png')
    minus= pygame.image.load('asety/minus.png')
    plus = pygame.image.load('asety/plus.png')
    tencza = pygame.image.load('asety/rainbow.png')
    Rubber = pygame.image.load('asety/rubber.png')
    pedzel = pygame.image.load('asety/paint.png')
    screen.fill((255,255,255))
    tryp_rys=False
    p1= polos.poz(800, 0, 20, 600, screen)
    p2= polos.poz(980, 0, 20, 600, screen)
    tenczaa = False
    j = random.randint(0, 255)
    l = random.randint(0, 255)
    k = random.randint(0, 255)
    d = kolory.kolor_w(j, k, l)
    jeden=0
    try:
        while True:
            clock.tick(FPS)
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                raise StopIteration
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                #kolory---------------------------------------------------------
                #rózowe
                if e.pos[0]>=820 and e.pos[0]<860 and e.pos[1]>0 and e.pos[1]<40:
                    color= kolory.pink
                if e.pos[0]>=860 and e.pos[0]<900 and e.pos[1]>0 and e.pos[1]<40:
                    color= kolory.HotPink
                if e.pos[0]>=900 and e.pos[0]<940 and e.pos[1]>0 and e.pos[1]<40:
                    color= kolory.Violet
                if e.pos[0]>=940and e.pos[0]<980 and e.pos[1]>0 and e.pos[1]<40:
                    color= kolory.DeepPink
                #czerwone
                if e.pos[0]>=820 and e.pos[0]<860 and e.pos[1]>40 and e.pos[1]<80:
                    color= kolory.Red
                if e.pos[0]>=860 and e.pos[0]<900 and e.pos[1]>40 and e.pos[1]<80:
                    color= kolory.Crimson
                if e.pos[0] >= 900 and e.pos[0] < 940 and e.pos[1] > 40 and e.pos[1] < 80:
                    color = kolory.DarkRed
                if e.pos[0]>=940and e.pos[0]<980 and e.pos[1]>40 and e.pos[1]<80:
                    color= kolory.LightCoral
                 # pomaranczowe
                if e.pos[0]>=820 and e.pos[0]<860 and e.pos[1]>80 and e.pos[1]<120:
                    color= kolory.OrangeRed
                if e.pos[0]>=860 and e.pos[0]<900 and e.pos[1]>80 and e.pos[1]<120:
                    color= kolory.DarkOrange
                if e.pos[0] >= 900 and e.pos[0] < 940 and e.pos[1] > 80 and e.pos[1] < 120:
                    color = kolory.Orange
                if e.pos[0]>=940and e.pos[0]<980 and e.pos[1]>80 and e.pos[1]<120:
                    color= kolory.Tomato
                # zólte
                if e.pos[0]>=820 and e.pos[0]<860 and e.pos[1]>120 and e.pos[1]<160:
                    color= kolory.gold
                if e.pos[0]>=860 and e.pos[0]<900 and e.pos[1]>120 and e.pos[1]<160:
                    color= kolory.Yellow
                if e.pos[0] >= 900 and e.pos[0] < 940 and e.pos[1] > 120 and e.pos[1] < 160:
                    color = kolory.LightYellow
                if e.pos[0]>=940and e.pos[0]<980 and e.pos[1]>120 and e.pos[1]<160:
                    color= kolory.Khaki
                #zielone
                if e.pos[0] >= 820 and e.pos[0] < 860 and e.pos[1] > 160 and e.pos[1] < 200:
                    color = kolory.Greenyellow
                if e.pos[0] >= 860 and e.pos[0] < 900 and e.pos[1] > 160 and e.pos[1] <200:
                    color = kolory.Lime
                if e.pos[0] >= 900 and e.pos[0] < 940 and e.pos[1] > 160 and e.pos[1] < 200:
                    color = kolory.Green
                if e.pos[0] >= 940 and e.pos[0] < 980 and e.pos[1] > 160 and e.pos[1] < 200:
                    color = kolory.SpringGreen
                # niebieskie
                if e.pos[0] >= 820 and e.pos[0] < 860 and e.pos[1] > 200 and e.pos[1] < 240:
                    color = kolory.Aqua
                if e.pos[0] >= 860 and e.pos[0] < 900 and e.pos[1] > 200 and e.pos[1] <240:
                    color = kolory.SteelBlue
                if e.pos[0] >= 900 and e.pos[0] < 940 and e.pos[1] > 200 and e.pos[1] < 240:
                    color = kolory.Blue
                if e.pos[0] >= 940 and e.pos[0] < 980 and e.pos[1] > 200 and e.pos[1] < 240:
                    color = kolory.LightBlue
                # brazowe

                if e.pos[0] >= 820 and e.pos[0] < 860 and e.pos[1] > 240 and e.pos[1] < 280:
                    color = kolory.SaddleBrown
                if e.pos[0] >= 860 and e.pos[0] < 900 and e.pos[1] > 240 and e.pos[1] <280:
                    color = kolory.Sienna
                if e.pos[0] >= 900 and e.pos[0] < 940 and e.pos[1] > 240 and e.pos[1] < 280:
                    color = kolory.Chocolate
                if e.pos[0] >= 940 and e.pos[0] < 980 and e.pos[1] > 240 and e.pos[1] < 280:
                    color = kolory.Tan
                #biale

                if e.pos[0] >= 820 and e.pos[0] < 860 and e.pos[1] > 280 and e.pos[1] < 320:
                    color = kolory.Gray
                if e.pos[0] >= 860 and e.pos[0] < 900 and e.pos[1] > 280 and e.pos[1] <320:
                    color = kolory.LightGray
                if e.pos[0] >= 900 and e.pos[0] < 940 and e.pos[1] > 280 and e.pos[1] < 320:
                    color = kolory.Black
                if e.pos[0] >= 940 and e.pos[0] < 980 and e.pos[1] > 280 and e.pos[1] < 320:
                    color = kolory.DarkSlate

                if e.pos[0]>=821 and e.pos[0]<853 and e.pos[1]>507 and e.pos[1]<539:
                    tryp_rys=True
                if e.pos[0]>=861 and e.pos[0]<893 and e.pos[1]>507 and e.pos[1]<539:
                    tryp_rys=False
                if e.pos[0]>=821 and e.pos[0]<853 and e.pos[1]>395 and e.pos[1]<427:
                    if tenczaa==False:
                        color=d
                        tenczaa=True
                    else:
                        tenczaa=False
                if e.pos[0] >= 855 and e.pos[0] < 887 and e.pos[1] > 395 and e.pos[1] < 427:
                    color= kolory.white

                if e.pos[0] >= 887 and e.pos[0] < 919 and e.pos[1] > 395 and e.pos[1] < 427:
                    polos.ry2(0, 0, screen, color)
                #rysowanie gdy sie nacisnie sie myszke--------------------------------------
                if e.pos[0] < 810-radius:
                    if tryp_rys:
                        pygame.draw.rect(screen,color,(e.pos[0],e.pos[1],radius,radius))
                    else:
                        pygame.draw.circle(screen, color, e.pos, radius)
                    draw_on = True
                #zapis---------------------------------------------------------------
                if e.pos[0] >= 821 and e.pos[0] < 853 and e.pos[1] > 568 and e.pos[1] < 600:
                    pygame.image.save(screen, "pliki dodatkowe/screenshot.jpeg")
                #powrót do menu
                if e.pos[0] >= 854 and e.pos[0] < 896 and e.pos[1] > 567 and e.pos[1] < 600:
                            menu()

                #zmiana rozmiaru rysowania-------------------------
                if e.pos[0] >= 821 and e.pos[0] < 853 and e.pos[1] > 447 and e.pos[1] < 507:
                        if radius >=10:
                            radius=radius-5
                            pygame.draw.rect(screen, kolory.white, (905, 447, 100, 24))
                            Funkcje.napisz_zwykły(str(radius), 905, 447, 20, kolory.DarkBlue, kolory.cz2, screen)
                if e.pos[0] >= 861 and e.pos[0] < 893 and e.pos[1] > 447 and e.pos[1] < 507:
                        radius=radius+5
                        pygame.draw.rect(screen, kolory.white, (905, 447, 100, 24))
                        Funkcje.napisz_zwykły(str(radius), 905, 447, 20, kolory.DarkBlue, kolory.cz2, screen)


            #gdy przytrzymana myszka ------------------------------------
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION:
                if e.pos[0] < 810-radius:
                    if draw_on:
                        if tryp_rys:
                            Funkcje.kwadratl(screen, color, e.pos, last_pos, radius)
                        else:
                            Funkcje.roundline(screen, color, e.pos, last_pos, radius)
                    last_pos = e.pos
            #rysowanie ikon itp---------------------------------------
            p1.rysuj()
            p2.rysuj()
            #kolory------------------------------
            # jeden jest to zmienna odpowiedzialna za to zeby kolory były rysowane tylko raz
            if jeden==0:
                #rozowy
                polos.ry(820, 0, screen, kolory.pink)
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
                polos.ry(820, 120, screen, kolory.gold)
                polos.ry(860, 120, screen, kolory.Yellow)
                polos.ry(900, 120, screen, kolory.LightYellow)
                polos.ry(940, 120, screen, kolory.Khaki)
                # zielone
                polos.ry(820, 160, screen, kolory.Greenyellow)
                polos.ry(860, 160, screen, kolory.Lime)
                polos.ry(900, 160, screen, kolory.Green)
                polos.ry(940, 160, screen, kolory.SpringGreen)
                # niebieskie

                polos.ry(820, 200, screen, kolory.Aqua)
                polos.ry(860, 200, screen, kolory.SteelBlue)
                polos.ry(900, 200, screen, kolory.Blue)
                polos.ry(940, 200, screen, kolory.LightBlue)
                # brazowe

                polos.ry(820, 240, screen, kolory.SaddleBrown)
                polos.ry(860, 240, screen, kolory.Sienna)
                polos.ry(900, 240, screen, kolory.Chocolate)
                polos.ry(940, 240, screen, kolory.Tan)
                # białe

                polos.ry(820, 280, screen, kolory.Gray)
                polos.ry(860, 280, screen, kolory.LightGray)
                polos.ry(900, 280, screen, kolory.Black)
                polos.ry(940, 280, screen, kolory.DarkSlate)
                screen.blit(tencza, (821, 395))
                screen.blit(save, (821, 568))
                screen.blit(dom, (854, 567))
                screen.blit(kwadracik, (821, 507))
                screen.blit(minus, (821, 447))
                screen.blit(plus, (861, 447))
                screen.blit(kolo, (861, 507))
                screen.blit(Rubber, (855, 395))
                screen.blit(pedzel, (887, 395))
                Funkcje.napisz_zwykły("zmiana rozmiaru", 820, 420, 20, kolory.DarkBlue, kolory.cz2, screen)
                Funkcje.napisz_zwykły("zmiana pedzla", 820, 480, 20, kolory.DarkBlue, kolory.cz2, screen)
                Funkcje.napisz_zwykły("menu", 820, 538, 20, kolory.DarkBlue, kolory.cz2, screen)
                jeden=1
            if tenczaa==True:
                j=random.randint(0,255)
                l = random.randint(0, 255)
                k = random.randint(0, 255)
                d= kolory.kolor_w(j, k, l)
                color=d



            pygame.display.flip()

    except StopIteration:
        pygame.quit()