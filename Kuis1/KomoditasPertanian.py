# kelas yang digunakan untuk mengimplementasikan KomoditasPertanian
# kelas KomoditasPertanian
class KomoditasPertanian:
    # private atribute dari kelas KomoditasPertanian
    __idKomoditas = ""
    __namaKomoditas = ""
    __sistemTanam = ""

    def __init__(self, idKomoditas="", namaKomoditas="", sistemTanam=""):
        # konstruktor
        self.__idKomoditas = idKomoditas
        self.__namaKomoditas = namaKomoditas
        self.__sistemTanam = sistemTanam

    # mengeset nilai atribut idKomoditas
    def setIdKomoditas(self, idKomoditas):
        self.__idKomoditas = idKomoditas

    # mengembalikan nilai atribut idKomoditas
    def getIdKomoditas(self):
        return self.__idKomoditas

    # mengeset nilai atribut namaKomoditas
    def setNamaKomoditas(self, namaKomoditas):
        self.__namaKomoditas = namaKomoditas

    # mengembalikan nilai atribut namaKomoditas
    def getNamaKomoditas(self):
        return self.__namaKomoditas

    # mengeset nilai atribut sistemTanam
    def setSistemTanam(self, sistemTanam):
        self.__sistemTanam = sistemTanam

    # mengembalikan nilai atribut sistemTanam
    def getSistemTanam(self):
        return self.__sistemTanam

    # menampilkan atribut KomoditasPertanian
    def printKomoditasPertanian(self):
        print("Id Komoditas    : " + self.getIdKomoditas())
        print("Nama Komoditas  : " + self.getNamaKomoditas())
        print("Sistem Tanam    : " + self.getSistemTanam())
