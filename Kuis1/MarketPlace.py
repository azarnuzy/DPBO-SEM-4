# import kelas
from KomoditasPertanian import KomoditasPertanian

# kelas yang digunakan untuk mengimplementasikan MarketPlace
# kelas MarketPlace


class MarketPlace:
    # private atribute dari kelas MarketPlace
    __jenisBisnis = ""
    __jenisPelayanan = ""
    __komoditasPertanian = KomoditasPertanian()

    def __init__(self, jenisBisnis="", jenisPelayanan="", komoditasPertanian=KomoditasPertanian()):
        # konstruktor
        self.__jenisBisnis = jenisBisnis
        self.__jenisPelayanan = jenisPelayanan
        self.__komoditasPertanian = komoditasPertanian

    # mengeset nilai atribut jenisBisnis

    def setJenisBisnis(self, jenisBisnis):
        self.__jenisBisnis = jenisBisnis

    # mengembalikan nilai atribut jenisBisnis
    def getJenisBisnis(self):
        return self.__jenisBisnis

    # mengeset nilai atribut jenisPelayanan
    def setJenisPelayanan(self, jenisPelayanan):
        self.__jenisPelayanan = jenisPelayanan

    # mengembalikan nilai atribut jenisPelayanan
    def getJenisPelayanan(self):
        return self.__jenisPelayanan

    # mengeset nilai atribut komoditasPertanian
    def setKomoditasPertanian(self, komoditasPertanian):
        self.__komoditasPertanian = komoditasPertanian

    # mengembalikan nilai atribut komoditasPertanian
    def getKomoditasPertanian(self):
        return self.__komoditasPertanian

    # menampilkan atribut MarketPlace
    def printMarketPlace(self):
        print("Jenis Bisnis    : " + self.getJenisBisnis())
        print("Jenis Pelayanan : " + self.getJenisPelayanan())
        self.__komoditasPertanian.printKomoditasPertanian()
