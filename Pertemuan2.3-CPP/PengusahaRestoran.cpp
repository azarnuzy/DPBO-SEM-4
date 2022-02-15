#include <iostream>
#include <string>

using namespace std;

class PengusahaRestoran
{
private:
    int kode;
    string nama;
    string kota;
    string kodeRestoran;

public:
    PengusahaRestoran() {}

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

    void setKota(int kota)
    {
        this->kota = kota;
    }

    string getKota()
    {
        return this->kota;
    }

    void setKodeRestoran(int kodeRestoran)
    {
        this->kodeRestoran = kodeRestoran;
    }

    string getKodeRestoran()
    {
        return this->kodeRestoran;
    }

    ~PengusahaRestoran() {}
};