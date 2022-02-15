#include <iostream>
#include <string>

using namespace std;

class BahanMasakan
{
private:
    int kode;
    string nama;
    string deskripsi;

public:
    BahanMasakan() {}

    void setKode(int kode)
    {
        this->kode = kode;
    }

    int getKode()
    {
        return this->kode;
    }

    void setNama(int nama)
    {
        this->nama = nama;
    }

    string getNama()
    {
        return this->nama;
    }

    void setDeskripsi(int deskripsi)
    {
        this->deskripsi = deskripsi;
    }

    string getDeskripsi()
    {
        return this->deskripsi;
    }

    ~BahanMasakan() {}
};