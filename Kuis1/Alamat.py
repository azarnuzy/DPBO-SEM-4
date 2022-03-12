# kelas yang digunakan untuk mengimplementasikan Alamat
# kelas Alamat
class Alamat:
    # private atribute dari kelas Alamat
    __desa = ""
    __kecamatan = ""
    __kota = ""
    __provinsi = ""

    def __init__(self, desa="", kecamatan="", kota="", provinsi=""):
        # konstruktor
        self.__desa = desa
        self.__kecamatan = kecamatan
        self.__kota = kota
        self.__provinsi = provinsi

    # mengeset nilai atribut desa
    def setDesa(self, desa):
        self.__desa = desa

    # mengembalikan nilai atribut desa
    def getDesa(self):
        return self.__desa

    # mengeset nilai atribut kecamatan
    def setKecamatan(self, kecamatan):
        self.__kecamatan = kecamatan

    # mengembalikan nilai atribut kecamatan
    def getKecamatan(self):
        return self.__kecamatan

    # mengeset nilai atribut kota
    def setKota(self, kota):
        self.__kota = kota

    # mengembalikan nilai atribut kota
    def getKota(self):
        return self.__kota

    # mengeset nilai atribut provinsi
    def setProvinsi(self, provinsi):
        self.__provinsi = provinsi

    # mengembalikan nilai atribut provinsi
    def getProvinsi(self):
        return self.__provinsi

    # menampilkan atribut Alamat
    def printAlamat(self):
        print("Desa      : " + self.getDesa())
        print("Kecamatan : " + self.getKecamatan())
        print("Kota      : " + self.getKota())
        print("Provinsi  : " + self.getProvinsi())
