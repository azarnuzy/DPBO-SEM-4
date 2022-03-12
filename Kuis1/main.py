""" Saya Muhammad Azar Nuzy 2004191 mengerjakan Kuis 1 C1 dalam
mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin """
# mengimport kelas
from Alamat import Alamat
from MarketPlace import MarketPlace
from KomoditasPertanian import KomoditasPertanian
from Lahan import Lahan
from Penduduk import Penduduk
from Petani import Petani
from PemilikToko import PemilikToko
from PemilikTengkulak import PemilikTengkulak

# deklarasi variabel untuk masukan
petani = [Petani() for i in range(0, 5)]
pemilikTengkulak = [PemilikTengkulak() for i in range(0, 5)]
pemilikToko = [PemilikToko() for i in range(0, 5)]

# Inputan Petani
alamat1 = Alamat("Asri", "Sukasari", "Bandung", "Jawa Barat")
lahan1 = Lahan("1LA", "Gambut", 200, alamat1)
komoditasPertanian1 = KomoditasPertanian("1KP", "Padi", "Campur Sari")
petani[0] = Petani("1pn", "Buruh", lahan1, komoditasPertanian1)
alamatPenduduk1 = Alamat("Suka Makmur", "Pandeglang", "Pandeglang", "Banten")
petani[0].setIdPenduduk("1PD")
petani[0].setNama("Dodi")
petani[0].setAlamatPenduduk(alamatPenduduk1)

alamat2 = Alamat("Makmur", "Sukajadi", "Bandung", "Jawa Barat")
lahan2 = Lahan("2LA", "Gembur", 300, alamat2)
komoditasPertanian2 = KomoditasPertanian("2KP", "Kelapa", "Tunggal Tanam")
petani[1] = Petani("2pn", "Pemilik Lahan", lahan2, komoditasPertanian2)
alamatPenduduk2 = Alamat("Curug Anggur", "Kabayan", "Pandeglang", "Banten")
petani[1].setIdPenduduk("2PD")
petani[1].setNama("Sudrajat")
petani[1].setAlamatPenduduk(alamatPenduduk1)
print("          Output Petani            ")
print("===================================")
print("1")
petani[0].printPenduduk()
petani[0].printPetani()
print("-----------------------------------")
print("2")
petani[1].printPenduduk()
petani[1].printPetani()
print("-----------------------------------")

komoditasPertanian3 = KomoditasPertanian("3KP", "Palawijaya", "Campur Sari")
marketPlace1 = MarketPlace("Business To Customer",
                           "Offline", komoditasPertanian3)
pemilikToko[0] = PemilikToko("1PT", "Jaya Abadi", marketPlace1)
alamatPenduduk3 = Alamat("Kadomas", "Ujung Kulon", "Pandeglang", "Banten")
pemilikToko[0].setIdPenduduk("3PD")
pemilikToko[0].setNama("William")
pemilikToko[0].setAlamatPenduduk(alamatPenduduk3)

komoditasPertanian4 = KomoditasPertanian("4KP", "Gandum", "Campur Sari")
marketPlace2 = MarketPlace("Business To Customer",
                           "Online", komoditasPertanian4)
pemilikToko[1] = PemilikToko("2PT", "Permanent Express", marketPlace2)
alamatPenduduk4 = Alamat("Sukasari", "Kadu Hejo", "Pandeglang", "Banten")
pemilikToko[1].setIdPenduduk("4PD")
pemilikToko[1].setNama("Robert")
pemilikToko[1].setAlamatPenduduk(alamatPenduduk4)

print("         Output Pemilik Toko      ")
print("===================================")
print("1")
pemilikToko[0].printPenduduk()
pemilikToko[0].printPemilikToko()
print("-----------------------------------")
print("2")
pemilikToko[1].printPenduduk()
pemilikToko[1].printPemilikToko()
print("-----------------------------------")

# Input Pemilik Tengkulak

komoditasPertanian5 = KomoditasPertanian("5KP", "Cengkeh", "Tunggal Tanam")
pemilikTengkulak[0] = PemilikTengkulak(
    "1TK", "Tengkulak Makmur", komoditasPertanian5)
alamatPenduduk5 = Alamat("Baros", "Serang Baru", "Pandeglang", "Banten")
pemilikTengkulak[0].setIdPenduduk("5PD")
pemilikTengkulak[0].setNama("Henry")
pemilikTengkulak[0].setAlamatPenduduk(alamatPenduduk5)

komoditasPertanian6 = KomoditasPertanian(
    "6KP", "Kelapa Sawit", "Tunggal Tanam")
pemilikTengkulak[1] = PemilikTengkulak(
    "2TK", "Tengkulak Jaya", komoditasPertanian6)
alamatPenduduk6 = Alamat("Menes", "Labuan", "Pandeglang", "Banten")
pemilikTengkulak[1].setIdPenduduk("6PD")
pemilikTengkulak[1].setNama("Johnson")
pemilikTengkulak[1].setAlamatPenduduk(alamatPenduduk6)
print("         Output Pemilik Tengkulak      ")
print("===================================")
print("1")
pemilikTengkulak[0].printPenduduk()
pemilikTengkulak[0].printPemilikTengkulak()
print("-----------------------------------")
print("2")
pemilikTengkulak[1].printPenduduk()
pemilikTengkulak[1].printPemilikTengkulak()
print("-----------------------------------")
