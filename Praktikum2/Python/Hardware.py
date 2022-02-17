from Product import Product
# mengimport kelas Product


class Hardware(Product):
    # kelas yang digunakan untuk mengimplementasikan kelas Hardware dan juga
    # turunan dari kelas product
    def __init__(self):
        # konstruktor
        self.brand = ""
        self.model = ""

    def setBrand(self, brand):
        # mengeset nilai atribut brand
        self.brand = brand

    def getBrand(self):
        # mengembalikan nilai atribut brand
        return self.brand

    def setModel(self, model):
        # mengeset nilai atribut model
        self.model = model

    def getModel(self):
        # mengembalikan nilai atribut model
        return self.model

    def printHardware(self):
        # menampilkan atribut hardware
        print("Brand: " + self.getBrand())
        print("Model: " + self.getModel())
