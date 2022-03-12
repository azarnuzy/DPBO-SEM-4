# import kelas
from Alamat import Alamat

# kelas yang digunakan untuk mengimplementasikan Lahan
# kelas Lahan


class Lahan:
    # private atribute dari kelas Lahan
    __IdLahan = ""
    __jenisTanah = ""
    __luas = 0
    __alamatLahan = Alamat()

    def __init__(self, IdLahan="", jenisTanah="", luas=0, Alamat=Alamat()):
        # konstruktor
        self.__IdLahan = IdLahan
        self.__jenisTanah = jenisTanah
        self.__luas = luas
        self.__alamatLahan = Alamat

    # mengeset nilai atribut IdLahan
    def setIdLahan(self, IdLahan):
        self.__IdLahan = IdLahan

    # mengembalikan nilai atribut IdLahan
    def getIdLahan(self):
        return self.__IdLahan

    # mengeset nilai atribut jenisTanah
    def setJenisTanah(self, jenisTanah):
        self.__jenisTanah = jenisTanah

    # mengembalikan nilai atribut jenisTanah
    def getJenisTanah(self):
        return self.__jenisTanah

    # mengeset nilai atribut luas
    def setluas(self, luas):
        self.__luas = luas

    # mengembalikan nilai atribut luas
    def getluas(self):
        return self.__luas

    # mengeset nilai atribut alamatLahan
    def setAlamatLahan(self, alamatLahan):
        self.__alamatLahan = alamatLahan

    # mengembalikan nilai atribut alamatLahan
    def getAlamatLahan(self):
        return self.__alamatLahan

    # menampilkan atribut Lahan
    def printLahan(self):
        print("Id Lahan    : " + self.getIdLahan())
        print("Jenis Tanah : " + self.getJenisTanah())
        print("Luas        : " + str(self.getluas()))
        print("Alamat Lahan:")
        self.__alamatLahan.printAlamat()
