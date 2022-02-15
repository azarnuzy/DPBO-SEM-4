#include <iostream>
#include <string>

using namespace std;

class IndustriKuliner
{
private:
    int noIjin;
    string namaPemilik;
    string kota;
    string deskripsi;

public:
    IndustriKuliner() {}

    void setNoIjin(int noIjin)
    {
        this->noIjin = noIjin;
    }

    int getNoIjin()
    {
        return this->noIjin;
    }

    void setNamaPemilik(int namaPemilik)
    {
        this->namaPemilik = namaPemilik;
    }

    string getNamaPemilik()
    {
        return this->namaPemilik;
    }

    void setKota(int kota)
    {
        this->kota = kota;
    }

    string getKota()
    {
        return this->kota;
    }

    void setDeskripsi(int deskripsi)
    {
        this->deskripsi = deskripsi;
    }

    string getDeskripsi()
    {
        return this->deskripsi;
    }

    ~IndustriKuliner() {}
};