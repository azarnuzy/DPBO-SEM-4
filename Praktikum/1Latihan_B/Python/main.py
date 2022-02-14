from DaftarTimSepakBola import DaftarTimSepakBola

daftar1 = DaftarTimSepakBola()
print("Input:")
nama = str(input("Nama: "))
negara = str(input("Negara: "))
tahunBerdiri = str(input("Tahun Berdiri: "))
pemain = str(input("Pemain: "))
print("Output:")
daftar1.setNama(nama)
daftar1.setNegara(negara)
daftar1.setTahunBerdiri(tahunBerdiri)
daftar1.setPemain(pemain)
daftar1.printHasil()

daftar2 = DaftarTimSepakBola(
    "Manchester United", "England", "1847", "Wayne Rooney")
daftar2.printHasil()
