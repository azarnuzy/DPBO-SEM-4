from Hardware import Hardware
# mengimport kelas hardware


class Memory(Hardware):
    # kelas yang digunakan untuk mengimplementasikan kelas Memory dan juga
    # turunan dari kelas Hardware
    def __init__(self):
        # konstruktor
        self.frequency = ""
        self.memorySize = 0
        self.supportsCuda = ""

    def setFrequency(self, frequency):
        # mengeset nilai atribut frequency
        self.frequency = frequency

    def getFrequency(self):
        # mengembalikan nilai atribut frequency
        return self.frequency

    def setMemorySize(self, memorySize):
        # mengeset nilai atribut memorySize
        self.memorySize = memorySize

    def getMemorySize(self):
        # mengembalikan nilai atribut memorySize
        return self.memorySize

    def setSupportsCuda(self, supportsCuda):
        # mengeset nilai atribut supportsCuda
        self.supportsCuda = supportsCuda

    def getSupportsCuda(self):
        # mengembalikan nilai atribut supportsCuda
        return self.supportsCuda

    def printMemory(self):
        # menampilkan atribut memory
        print("Frequency: " + self.getFrequency())
        print("Memory Size: " + str(self.getMemorySize()))
        print("Supports Cuda: " + self.getSupportsCuda())
