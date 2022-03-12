# import kelas
from Penduduk import Penduduk
from KomoditasPertanian import KomoditasPertanian
# kelas yang digunakan untuk mengimplementasikan PemilikTengkulak
# kelas PemilikTengkulak


class PemilikTengkulak(Penduduk):
    # private atribute dari kelas PemilikTengkulak
    __idTengkulak = ""
    __namaTengkulak = ""
    __komoditasPertanian = KomoditasPertanian()

    def __init__(self, idTengkulak="", namaTengkulak="", KomoditasPertanian=KomoditasPertanian()):
        # konstruktor
        self.__idTengkulak = idTengkulak
        self.__namaTengkulak = namaTengkulak
        self.__komoditasPertanian = KomoditasPertanian

    # mengeset nilai atribut idTengkulak
    def setIdTengkulak(self, idTengkulak):
        self.__idTengkulak = idTengkulak

    # mengembalikan nilai atribut idTengkulak
    def getIdTengkulak(self):
        return self.__idTengkulak

    # mengeset nilai atribut namaTengkulak
    def setNamaTengkulak(self, namaTengkulak):
        self.__namaTengkulak = namaTengkulak

    # mengembalikan nilai atribut namaTengkulak
    def getNamaTengkulak(self):
        return self.__namaTengkulak

    # mengeset nilai atribut KomoditasPertanian
    def setKomoditasPertanian(self, KomoditasPertanian):
        self.__komoditasPertanian = KomoditasPertanian

    # mengembalikan nilai atribut KomoditasPertanian
    def getKomoditasPertanian(self):
        return self.__komoditasPertanian

    # menampilkan atribut PemilikTengkulak
    def printPemilikTengkulak(self):
        print("Id Tengkulak   : " + self.getIdTengkulak())
        print("Nama Tengkulak : " + self.getNamaTengkulak())
        self.__komoditasPertanian.printKomoditasPertanian()
