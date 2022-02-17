from Memory import Memory
# mengimport kelas Memory

# instansiasi
comp = Memory()

# membuat masukan untuk nantinya diset ke atribut kelas-kelas yang ada di Memory
print("Input: ")
idProduct = int(input("Id Product: "))
price = int(input("Price: "))
brand = str(input("Brand: "))
model = str(input("Model: "))
frequency = str(input("Frequency: "))
memorySize = int(input("Memory Size: "))
supportsCuda = str(input("Supports Cuda: "))

# mengeset isi atribut dari kelas-kelas pada memory
comp.setIdProduct(idProduct)
comp.setPrice(price)
comp.setBrand(brand)
comp.setModel(model)
comp.setFrequency(frequency)
comp.setMemorySize(memorySize)
comp.setSupportsCuda(supportsCuda)

# mencetak atribut ada kelas-kelas yang ada di Memory
print("Output: ")
comp.printProduct()
comp.printHardware()
comp.printMemory()
