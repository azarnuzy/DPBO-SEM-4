#include <bits/stdc++.h>
using namespace std;
// import class Hardware
#include "Hardware.cpp"

class Memory : public Hardware
// kelas yang digunakan untuk mengimplementasikan Memory dan juga turunan dari kelas Hardware
{
private:
    // private atribute dari kelas Memory
    string frequency;
    int memorySize;
    string supportsCuda;

public:
    // konstrutor
    Memory() {}

    // mengeset nilai atribut frequency
    void setFrequency(string frequency)
    {
        this->frequency = frequency;
    }

    // mengembalikan nilai atribut frequency
    string getFrequency()
    {
        return this->frequency;
    }

    // mengeset nilai atribut memorySize
    void setMemorySize(int memorySize)
    {
        this->memorySize = memorySize;
    }

    // mengembalikan nilai atribut memorySize
    int getMemorySize()
    {
        return this->memorySize;
    }

    // mengeset nilai atribut supportsCuda
    void setSupportsCuda(string supportsCuda)
    {
        this->supportsCuda = supportsCuda;
    }

    // mengembalikan nilai atribut supportsCuda
    string getSupportsCuda()
    {
        return this->supportsCuda;
    }

    // menampilkan atribut Memory
    void printMemory()
    {
        cout << "Frequency : " << this->getFrequency() << endl;
        cout << "Memory Size : " << this->getMemorySize() << endl;
        cout << "Support Cuda : " << this->getSupportsCuda() << endl;
    }

    // destructor
    ~Memory() {}
};