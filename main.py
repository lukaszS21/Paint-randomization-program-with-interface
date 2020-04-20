import pygame ,Funkcje
from pygame import MOUSEBUTTONDOWN
from pygame import K_KP_ENTER
pygame.init()
screen = pygame.display.set_mode((370, 600))  # szerosc i wysokosc
font = pygame.font.SysFont(None, 20)
pygame.display.set_caption("Kolo fortuny ")  # zmienia nazwe terminala


DodgerBlue = (60, 199, 255)
ForestGreen = (34, 139, 34)
DarkBlue = (00, 0, 0)
LightBlue = (173, 216, 230)
Aquamarine = (127, 255, 212)
cz1 = "Kristen ITC"
cz2 = "Kristen ITC"
def napisz_zwykły(tekst, x, y, rozmiar, kolor, czcionka):
    cz = pygame.font.SysFont(czcionka, rozmiar)
    rend = cz.render(tekst, 1, kolor)
    screen.blit(rend, (x, y))

def polosowaniu(b):
    introo = True

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
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                if mx > 79 and mx < 296 and my > 359 and my < 390:


                        menu()

        screen.fill((128, 128, 128))


        napisz_zwykły("Wylosowano", 80, 100, 30, DarkBlue, cz2)
        napisz_zwykły(str(b), 80, 130, 30, DarkBlue, cz2)
        napisz_zwykły("Wroc do menu", 80, 350, 30, DarkBlue, cz2)
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
                    print(tab)
                    print(slowa)
                    for i in range(0, len(tab)):
                        slowa.append(tab[i])
                    slowa.append(',')
                    tab.clear()
                    print(tab)
                    print(slowa)
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

        napisz_zwykły("Podaj slowo  ", 110, 100, 30, DarkBlue, cz2)
        napisz_zwykły("Losuj  ", 160, 360, 30, DarkBlue, cz2)
        napisz_zwykły("Zatwiedz  ", 120, 330, 30, DarkBlue, cz2)
        xz=100
        xz2=100
        xz3=100
        for i in range(0,len(tab)):
            if len(tab)>i:
                if xz2 > 300:
                    napisz_zwykły(str(tab[i]), xz3, 220, 20, DarkBlue, cz2)
                    xz3 = xz3 + 11
                elif xz > 300:
                    napisz_zwykły(str(tab[i]), xz2, 190, 20, DarkBlue, cz2)
                    xz2 = xz2 + 11
                else:
                    napisz_zwykły(str(tab[i]), xz, 160, 20, DarkBlue, cz2)
                    xz=xz+11




        pygame.display.update()

def menu():
    introo = True


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
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if mx > 110 and mx < 264 and my > 200 and my < 240:
                    wpisz()


        screen.fill((128, 128, 128))

        napisz_zwykły("Stwórz koło ", 110, 200, 30, DarkBlue, cz2)
        napisz_zwykły("Kolo Decuduje ", 80, 100, 30, DarkBlue, cz2)
        napisz_zwykły("o twoim zyciu", 100, 130, 30, DarkBlue, cz2)

        pygame.display.update()

menu()