# import kelas
from Penduduk import Penduduk
from MarketPlace import MarketPlace

# kelas yang digunakan untuk mengimplementAsikan Toko
# kelas Toko


class PemilikToko(Penduduk):
    # private atribute dari kelas Toko
    __idPemilikToko = ""
    __namaToko = ""
    __marketPlace = MarketPlace()

    def __init__(self, idPemilikToko="", namaToko="", marketPlace=MarketPlace()):
        # konstruktor
        self.__idPemilikToko = idPemilikToko
        self.__namaToko = namaToko
        self.__marketPlace = marketPlace

    # mengeset nilai atribut idPemilikToko
    def setIdPemilikToko(self, idPemilikToko):
        self.__idPemilikToko = idPemilikToko

    # mengembalikan nilai atribut idPemilikToko
    def getIdPemilikToko(self):
        return self.__idPemilikToko

    # mengeset nilai atribut namaToko
    def setNamaToko(self, namaToko):
        self.__namaToko = namaToko

    # mengembalikan nilai atribut namaToko
    def getNamaToko(self):
        return self.__namaToko

    # mengeset nilai atribut marketPlace
    def setmarketPlace(self, marketPlace):
        self.__marketPlace = marketPlace

    # mengembalikan nilai atribut marketPlace
    def getmarketPlace(self):
        return self.__marketPlace

    # menampilkan atribut Toko

    def printPemilikToko(self):
        print("Id Pemilik Toko : " + self.getIdPemilikToko())
        print("Nama Toko       : " + self.getNamaToko())
        self.__marketPlace.printMarketPlace()
