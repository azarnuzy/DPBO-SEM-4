class Product:
    # kelas yang digunakan untuk mengimplementasikan kelas Product
    def __init__(self):
        # konstruktor
        self.price = 0
        self.idProduct = 0

    def setPrice(self, price):
        # mengeset nilai atribut price
        self.price = price

    def getPrice(self):
        # mengembalikan nilai atribut price
        return self.price

    def setIdProduct(self, idProduct):
        # mengeset nilai atribut idProduct
        self.idProduct = idProduct

    def getIdProduct(self):
        # mengembalikan nilai atribut idProduct
        return self.idProduct

    def printProduct(self):
        # menampilkan atribut product
        print("Id Product: " + str(self.getIdProduct()))
        print("Price: " + str(self.getPrice()))
