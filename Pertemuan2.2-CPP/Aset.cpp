#include <bits/stdc++.h>

using namespace std;

class Aset
{
private:
    int kodeAset;
    int jenisAset;
    double nilaiAset;

public:
    Aset() {}

    void setKodeAset(int kodeAset)
    {
        this->kodeAset = kodeAset;
    }

    int getKodeAset()
    {
        return this->kodeAset;
    }

    void setJenisAset(int jenisAset)
    {
        this->jenisAset = jenisAset;
    }

    int getJenisAset()
    {
        return this->jenisAset;
    }

    void setNilaiAset(int nilaiAset)
    {
        this->nilaiAset = nilaiAset;
    }

    int getNilaiAset()
    {
        return this->nilaiAset;
    }

    ~Aset() {}
};