# Projekt_JS
Porojekt_JS_
# Temat Paint plus program losujący
# Link do github:https://github.com/lukaszS21/Projekt_JS

# opis 
# W moim projektcie będę opierał się głównie o biblioteke pygame za pomocą której strzoże interfejs programu grafiki itp , oprócz tego z bibliotek random w celu kozystania z liczb pseudolosowych oraz biblioteki datetime do odczytania bierzącego czasu.

# Całość programu bedzie podzielona na kilka modółów z funkcjami.

# Po uruchomieniu aplikacji utworzy się okienko z Menu głównym , z którego będziemy mieli dostęp do dwóch części programu
# 1.polegająca na losowniu spośród jedej z wpisanych przez urzytkownika rzeczy.W celu uniknięcia interakcji urzytkownika z terminalem całość odbywa się w aplikacji za pomoca biblioteki pygame.(posiada funkcje odczytu i zapisu do pliku w celu zapisaniadanych do lowowania)
# 2.Prosty program graficzny posiadający funkcje zbliżone do prostego Painta tnz :możliwość wybrania koloru,rozmiara pedzla ,rodzaj pedzla,zapis swojego rysunku.

testy:
1:Kolo
-test zamiany balicy zanków odzielonych przecinkiem ,na słowa.
-zapis pustego pliku oraz do pliku słów, które chcemy zapamiętać
-Podanie dowolnej ilości słów do losowania
-Test interfejsu czy wszystkie słowa wykonują swoje funkcje to znaczy czy napis losuj wylosuje itp
-Przetestowanie działania wyłaczania programu
2:Paint
-Sprawdzenie czy naciśnięcie koloru go zmienia
-Zmiana rozmiaru pedzla oraz jego ksztaltu
-Zapis narysowanego obrazu
-Powrót do menu
-Próba rysowania poza obszarem dozwolonym
-Przetestowanie działania wyłaczania programu
3:Menu
-Sprawdzenie wyświetlanego czasu(gdyż menu posiada taką funkcje)
-Przetestowanie działania wyłaczania programu
wykorzystane konstrukcje:
Opis:
Projekt posiada parę folderów:
-asety-znajdują się tu wszystkie grafiki użyte do projektu
głównie ze strony https://pl.freepik.com/darmowe-ikony
-pliki dodatkowe-znajduje się tu plik wykorzystywany do zaplisu i odczytu słów do losowania oraz zrzut ekranu tworzony w momęcie zapisu obrazu w paint.
-zdj-przykładowe zdj urzytkowania programu
-pakiet1-wszyskie moduły urzywane do projektu
założenia:
Projekt ten rozpocząłem tuż po rozpoczęciu epidemi w celu nauki tego języka przez ten czas zmieniałem i dodawałem do projektu nowe rzeczy których się uczyłem, przykładem na to może być funkja ry() któr słuzyła mi do rysowania kwadratu ,którą pożniej zastąiłem klasa poz() rysująca go.Moim założeniem było stworzenie programu losującego pare rzeczy z przystępnym interfejsem , jednak uznałem że bedzię to dość mało jeśli chodzi o projekt zalczeniowy wiec dodałem do tego mój drugi projekt który tworzyłem równolegle do pierwszego i je połaczyłem w jedno(paint).

Szybki opis kodu:
main-tworzenie iterfejsu za pomoca biblioteki pygame,obsługa wydarzeń takich jak naciścnięcie esc lub dodanych przycisków w celu przejścia do dalszej częsci programu,wypisywanie aktualnego czasu z pomocą lambdy(opis niżej).
-losowanie-stworzenie wydarzenie gdy urzytkownik wciście litere z klawiatury trafia do tablicy,zakażdm razem gdy klikamy przycisk zstosuj zostaje dodany przecinek odzielający słowa,stworzenie całego interfejsu graficznego z biblioteki pygame
-paint-tworzenie całego interfejsu gdy klikniemy odpowiedni kolor to kolor naszego pedzla się zmienia,gdy klikniemy kwadrat pedzel zmieni się na rysowanie kwadratem itp.

a)lambda:
now = datetime.datetime.now()
cza = lambda x: str(x.hour) + ":" + str(x.minute) + ":" + str(x.second)
wykorzystuje do wypisania aktualnego czasu w menu głównym

b)clasy: klasa poz()
klasa tworzy obiekt który jest kwadratem,umożliwia jego narysowanie i odczytanie współrzędnych urzywane do rysowania interfejsu.
c)wyjątki:
używam w odczytywaniu z pliku słów do losowania ,zabezpiecza mnie to przed sytuacja gdy plik jest pusty
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
d)moduły
Projetk został podzielony na pare modółów które znajdują się w pakiecie o nazwie "pakiet1".
Funkcje.py-znajdują się tam funkcje urzywane do losowania,odczytu i zapisu do pliku oraz rysowania w paintcie.
-kolory-znajdują się tam wszystkie kolory oraz trzcionki
-kwadrat-znajduje się tam klasa służaca do tworzenia obietku tupu kwadrat
oraz funkcje rysujące kwadrat.
-losowanie.py-część programu odpowiadająca za losowanie z całym interfejsem itp.
-paint.py-część programu odpowiadająca za painta z całym interfejsem itp.
-test_Funkcje.py-Plik testujący pare wybranych funkcji z Funkcji.py