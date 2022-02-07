class Titik:
    """ 
    kelas yang digunakan untuk mengimplementasikan  
    sebuah tipe titik
    """

    def __init__(self, x, y):
        # konstruktor
        self.x = x
        self.y = y

    def setX(self, x):
        # mengeset nilai koordinat x
        self.x = x

    def getX(self):
        # mengembalikan nilai koordinat x
        return self.x

    def setY(self, y):
        # mengeset nilai koordinat y
        self.y = y

    def getY(self):
        # mengembalikan nilai koordinat y
        return self.y
