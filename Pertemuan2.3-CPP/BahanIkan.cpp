#include <iostream>
#include <string>
#include "BahanMasakan.cpp"
using namespace std;

class BahanIkan : public BahanMasakan
{
private:
    string jenisIkan;

public:
    BahanIkan() {}

    void setJenisIkan(int jenisIkan)
    {
        this->jenisIkan = jenisIkan;
    }

    string getJenisIkan()
    {
        return this->jenisIkan;
    }

    ~BahanIkan() {}
};