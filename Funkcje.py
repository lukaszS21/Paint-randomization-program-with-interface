import random
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

def losuj(lista):
    x=random.randint(0,len(lista)-1)
    print(x)
    for i in range(len(lista)):
        if x==i:
            print("Wylosowano")
            print(lista[i])
            return lista[i]