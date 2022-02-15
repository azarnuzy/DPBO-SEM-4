#include <iostream>
#include <string>

using namespace std;

class MasakanIndonesia
{
private:
    int kode;
    string nama;
    string bahan;
    string harga;

public:
    MasakanIndonesia() {}

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

    void setBahan(int bahan)
    {
        this->bahan = bahan;
    }

    string getBahan()
    {
        return this->bahan;
    }

    void setHarga(int harga)
    {
        this->harga = harga;
    }

    string getHarga()
    {
        return this->harga;
    }

    ~MasakanIndonesia() {}
};