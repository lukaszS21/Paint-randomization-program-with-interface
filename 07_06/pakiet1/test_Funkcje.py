import unittest
import pygame
from main import menu
from pakiet1.Funkcje import zamiana, odczytzpliku, losuj, zapisdopliku
from pakiet1.paint import paint_2


class Test(unittest.TestCase):
    def test_zamiana(self):
        lista=["o","l","a",",","j","e",","]
        x=zamiana(lista)
        self.assertEqual(x,["ola","je"])

    def test_zmiana2(self):
        lista2=[]
        x = zamiana(lista2)
        self.assertEqual(x, [])
    def test_zmiana3(self):
        lista3=["2"]
        x = zamiana(lista3)
        self.assertEqual(x, [])
    def test_losuj1(self):
        lista=[]
        losuj(lista)
    def test_losuj2(self):
        lista=[1,2,3,4,5]
        losuj(lista)
    def test_losuj3(self):
        lista=["ola","michał",2,4,2,1]
        losuj(lista)
    def test_zapis1(self):
        tab=[]
        zapisdopliku("test.txt",tab)
    def test_zapis2(self):
        tab=["ola","to"]
        zapisdopliku("test.txt",tab)

if __name__ =='__main__':
    unittest.main()