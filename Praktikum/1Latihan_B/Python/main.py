from DaftarTimSepakBola import DaftarTimSepakBola

daftar1 = DaftarTimSepakBola()
daftar1.setNama("Barcelona")
daftar1.setNegara("Spanyol")
daftar1.setTahunBerdiri("1887")
daftar1.setPemain("Sergio Ramos")
daftar1.printHasil()

daftar2 = DaftarTimSepakBola(
    "Manchester United", "England", "1847", "Wayne Rooney")
daftar2.printHasil()
