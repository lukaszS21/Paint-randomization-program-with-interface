import random
import pygame
#funckje do koła----------------------------------------------


def zapisdopliku(nazwa,tab):
    '''
    :param nazwa: nazwa pliku
    :param tab: lista z naszymi słowami to zapisu
    '''
    plik = open(nazwa, 'w')
    plik.writelines(tab)
    plik.close()

def zamiana(tab):
    '''
    funkcja modyfikuje liste pozbywajac się , i oddzielajac słowa
    :param tab: lista z naszymi slowami
    '''
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

def odczytzpliku(nazwa):
        '''
        :param nazwa: nazwa pliku
        :return: zwraca pablice po odczytaniu z pliku
        '''
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
    '''

    :param lista: Lista z naszymi slowami do losowania
    :return: zwraca odpowiedni element listy
    '''
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
        '''

        :param srf: nasz ekran
        :param color: kolor
        :param start: początek rysowania
        :param end: koniec rysowania
        :param radius: promien koła
        :return:
        '''
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int(start[0] + float(i) / distance * dx)
            y = int(start[1] + float(i) / distance * dy)
            pygame.draw.circle(srf, color, (x, y), radius)
def kwadratl(srf, color, start, end,rozmiar):
        '''

        :param srf: ekran
        :param color: kolor
        :param start: poczatek rysowania
        :param end: koniec rysowania
        :param rozmiar: rozmiar kwadrata
        '''
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int(start[0] + float(i) / distance * dx)
            y = int(start[1] + float(i) / distance * dy)
            pygame.draw.rect(srf, color, (x,y,rozmiar,rozmiar))
#Funkcja wypisująca tekst na ekran korzytsajaca z pygame
def napisz_zwykły(tekst, x, y, rozmiar, kolor, czcionka,screen):
    '''

    :param tekst: tekst do wypisaia
    :param x: x
    :param y: y
    :param rozmiar: rozmiar tekstu
    :param kolor: kolor
    :param czcionka: czcionka
    :param screen: ekran
    :return:
    '''
    cz = pygame.font.SysFont(czcionka, rozmiar)
    rend = cz.render(tekst, 1, kolor)
    screen.blit(rend, (x, y))