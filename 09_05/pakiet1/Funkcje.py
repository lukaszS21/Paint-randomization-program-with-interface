import random
import pygame
#funckje do koła----------------------------------------------

#zapis do pliku o nazwie nazwa tablicy tab
def zapisdopliku(nazwa,tab):
    plik = open(nazwa, 'w')
    plik.writelines(tab)
    plik.close()
#rozdziela słowa z tablicy odzielone ","
def zamiana(tab):
    b = ""
    tab2 = []
    for i in range(0, len(tab)):
        if tab[i] == ",":
            tab2.append(b)
            b = ""
        else:
            b = b + tab[i]
    print(tab2)

    return tab2
#odczytuje z pliku sprawdzajac czy nie jest pusty
def odczytzpliku(nazwa):
        tab=[]
        try:
            plik=open(nazwa,'r')
            znak=plik.read(1)
            tab.append(znak)
            while znak:
                znak=plik.read(1)
                tab.append(znak)
        except IOError:
            print("blad w odczytaniu pliku")
            return 0
        return tab
def losuj(lista):
    if len(lista)<1:
        print("pusta lista")
    else:

        x=random.randint(0,len(lista)-1)
        print(x)

        for i in range(len(lista)):
            if x==i:
                print("Wylosowano")
                print(lista[i])
                return lista[i]
#funckje do paint--------------------------------
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
#Funkcja wypisująca tekst na ekran korzytsajaca z pygame
def napisz_zwykły(tekst, x, y, rozmiar, kolor, czcionka,screen):
    cz = pygame.font.SysFont(czcionka, rozmiar)
    rend = cz.render(tekst, 1, kolor)
    screen.blit(rend, (x, y))