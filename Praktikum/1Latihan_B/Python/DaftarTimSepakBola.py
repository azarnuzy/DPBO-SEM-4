class DaftarTimSepakBola():
    __nama = ""
    __negara = ""
    __tahun_berdiri = ""
    __pemain = ""

    def __init__(self, nama="", negara="", tahun_berdiri="", pemain=""):
        self.__nama = nama
        self.__negara = negara
        self.__tahun_berdiri = tahun_berdiri
        self.__pemain = pemain

    def setNama(self, nama):
        self.__nama = nama

    def getNama(self):
        return self.__nama

    def setNegara(self, negara):
        self.__negara = negara

    def getNegara(self):
        return self.__negara

    def setTahunBerdiri(self, tahun_berdiri):
        self.__tahun_berdiri = tahun_berdiri

    def getTahunBerdiri(self):
        return self.__tahun_berdiri

    def setPemain(self, pemain):
        self.__pemain = pemain

    def getPemain(self):
        return self.__pemain

    def printHasil(self):
        print("Nama:" + str(self.__nama))
        print("Negara:" + str(self.__negara))
        print("Tahun Berdiri:" + str(self.__tahun_berdiri))
        print("Pemain:" + str(self.__pemain))
