# import kelas
from Penduduk import Penduduk
from Lahan import Lahan
from KomoditasPertanian import KomoditasPertanian
# kelas yang digunakan untuk mengimplementasikan Petani
# kelas Petani


class Petani(Penduduk):
    # private atribute dari kelas Petani
    __idPetani = ""
    __status = ""
    __lahan = Lahan()
    __komoditasPertanian = KomoditasPertanian()

    def __init__(self, idPetani="", status="", lahan=Lahan(), komoditasPertanian=KomoditasPertanian()):
        # konstruktor
        self.__idPetani = idPetani
        self.__status = status
        self.__lahan = lahan
        self.__komoditasPertanian = komoditasPertanian

    # mengeset nilai atribut idPetani
    def setIdPetani(self, idPetani):
        self.__idPetani = idPetani

    # mengembalikan nilai atribut idPetani
    def getIdPetani(self):
        return self.__idPetani

    # mengeset nilai atribut status
    def setStatus(self, status):
        self.__status = status

    # mengembalikan nilai atribut status
    def getStatus(self):
        return self.__status

    # mengeset nilai atribut lahan
    def setLahan(self, lahan):
        self.__lahan = lahan

    # mengembalikan nilai atribut lahan
    def getLahan(self):
        return self.__lahan

    # mengeset nilai atribut komoditasPertanian
    def setKomoditasPertanian(self, komoditasPertanian):
        self.__komoditasPertanian = komoditasPertanian

    # mengembalikan nilai atribut komoditasPertanian
    def getKomoditasPertanian(self):
        return self.__komoditasPertanian

    # menampilkan atribut Petani
    def printPetani(self):
        print("Id Petani : " + self.getIdPetani())
        print("Status    : " + self.getStatus())
        print("Lahan     : ")
        self.__lahan.printLahan()
        print("Komoditas Pertanian :")
        self.__komoditasPertanian.printKomoditasPertanian()
