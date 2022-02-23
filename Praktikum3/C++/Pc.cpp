#include <bits/stdc++.h>
using namespace std;

#include "Processor.cpp"
#include "Disk.cpp"
#include "Ram.cpp"

class Pc
// kelas yang digunakan untuk mengimplementasikan Pc
{
private:
    // private atribute dari kelas Pc
    Processor itemProcessor;
    Disk itemDisk;
    Ram itemRam;
    int totalPrice;

public:
    // konstruktor
    Pc() {}

    // mengeset nilai atribut capacity
    void setCapacity(string capacity)
    {
        this->capacity = capacity;
    }

    // mengembalikan nilai atribut capacity
    string getCapacity()
    {
        return this->capacity;
    }

    // mengeset nilai atribut price
    void setPrice(int price)
    {
        this->price = price;
    }

    // mengembalikan nilai atribut price
    int getPrice()
    {
        return this->price;
    }

    // menampilkan atribut Pc
    void printPc()
    {
        cout << "Pc Capacity : " << this->getCapacity() << endl;
        cout << "Pc Price : " << this->getPrice() << endl;
    }

    // destructor
    ~Pc() {}
};