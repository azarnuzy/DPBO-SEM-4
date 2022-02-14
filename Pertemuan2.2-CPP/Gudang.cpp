#include <bits/stdc++.h>
#include "Aset.cpp"
#include "Bangunan.cpp"
using namespace std;

class Gudang : public Bangunan, public Aset
{
private:
    int kodeGudang;
    string namaGudang;
    string alamatGudang;

public:
    Gudang() {}

    void setKodeGudang(int kodeGudang)
    {
        this->kodeGudang = kodeGudang;
    }

    int getKodeGudang()
    {
        return this->kodeGudang;
    }

    void setNamaGudang(string namaGudang)
    {
        this->namaGudang = namaGudang;
    }

    string getNamaGudang()
    {
        return this->namaGudang;
    }

    void setAlamatGudang(string alamatGudang)
    {
        this->alamatGudang = alamatGudang;
    }

    string getAlamatGudang()
    {
        return this->alamatGudang;
    }

    ~Gudang() {}
};