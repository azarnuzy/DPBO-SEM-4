#include <iostream>
#include <string>
#include "IndustriKuliner.cpp"
using namespace std;

class Restoran : public IndustriKuliner
{
private:
    int kode;
    string jenis;
    string pangsaPasar;

public:
    Restoran() {}

    void setKode(int kode)
    {
        this->kode = kode;
    }

    int getKode()
    {
        return this->kode;
    }

    void setJenis(int jenis)
    {
        this->jenis = jenis;
    }

    string getJenis()
    {
        return this->jenis;
    }

    void setPangsaPasar(int pangsaPasar)
    {
        this->pangsaPasar = pangsaPasar;
    }

    string getPangsaPasar()
    {
        return this->pangsaPasar;
    }

    ~Restoran() {}
};