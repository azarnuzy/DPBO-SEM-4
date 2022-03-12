# import kelas
from Alamat import Alamat

# kelas yang digunakan untuk mengimplementAsikan Penduduk
# kelas Penduduk


class Penduduk:
    # private atribute dari kelas Penduduk
    __idPenduduk = ""
    __nama = ""
    __alamatPenduduk = Alamat()

    def __init__(self, idPenduduk="", nama="", alamatPenduduk=Alamat()):
        # konstruktor
        self.__idPenduduk = idPenduduk
        self.__nama = nama
        self.__alamatPenduduk = alamatPenduduk

    # mengeset nilai atribut idPenduduk
    def setIdPenduduk(self, idPenduduk):
        self.__idPenduduk = idPenduduk

    # mengembalikan nilai atribut idPenduduk
    def getIdPenduduk(self):
        return self.__idPenduduk

    # mengeset nilai atribut nama
    def setNama(self, nama):
        self.__nama = nama

    # mengembalikan nilai atribut nama
    def getNama(self):
        return self.__nama

    # mengeset nilai atribut alamatPenduduk
    def setAlamatPenduduk(self, alamatPenduduk):
        self.__alamatPenduduk = alamatPenduduk

    # mengembalikan nilai atribut alamatPenduduk
    def getAlamatPenduduk(self):
        return self.__alamatPenduduk

    # menampilkan atribut Penduduk

    def printPenduduk(self):
        print("Id Penduduk     : " + self.getIdPenduduk())
        print("Nama            : " + self.getNama())
        print("Alamat Penduduk : ")
        self.__alamatPenduduk.printAlamat()
