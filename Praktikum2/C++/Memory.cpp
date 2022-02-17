#include <bits/stdc++.h>
#include "Hardware.cpp"
using namespace std;

class Memory : public Hardware
{
private:
    string frequency;
    int memorySize;
    string supportsCuda;

public:
    Memory() {}

    void setFrequency(string frequency)
    {
        this->frequency = frequency;
    }

    string getFrequency()
    {
        return this->frequency;
    }

    void setMemorySize(int memorySize)
    {
        this->memorySize = memorySize;
    }

    int getMemorySize()
    {
        return this->memorySize;
    }

    void setSupportsCuda(string supportsCuda)
    {
        this->supportsCuda = supportsCuda;
    }

    string getSupportsCuda()
    {
        return this->supportsCuda;
    }

    void printMemory()
    {
        cout << "Frequency : " << this->getFrequency() << endl;
        cout << "Memory Size : " << this->getMemorySize() << endl;
        cout << "Support Cuda : " << this->getSupportsCuda() << endl;
    }

    ~Memory() {}
};