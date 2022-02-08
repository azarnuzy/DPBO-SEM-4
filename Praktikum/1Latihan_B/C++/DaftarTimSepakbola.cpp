#include <string>
#include <iostream>

using namespace std;

class DaftarTimSepakBola
{
private:
    string nama;
    string negara;
    string tahun_berdiri;
    string pemain;

public:
    DaftarTimSepakBola() {}

    DaftarTimSepakBola(string nama, string negara, string tahun_berdiri, string pemain)
    {
        this->nama = nama;
        this->negara = negara;
        this->tahun_berdiri = tahun_berdiri;
        this->pemain = pemain;
    }

    void setNama(string nama)
    {
        this->nama = nama;
    }

    string getNama()
    {
        return this->nama;
    }

    void setNegara(string negara)
    {
        this->negara = negara;
    }

    string getNegara()
    {
        return this->negara;
    }

    void setTahunBerdiri(string tahun_berdiri)
    {
        this->tahun_berdiri = tahun_berdiri;
    }

    string getTahunBerdiri()
    {
        return this->tahun_berdiri;
    }

    void setPemain(string pemain)
    {
        this->pemain = pemain;
    }

    string getPemain()
    {
        return this->pemain;
    }

    void printHasil()
    {
        cout << "Nama: " << this->nama << endl;
        cout << "Negara: " << this->negara << endl;
        cout << "Tahun Berdiri: " << this->tahun_berdiri << endl;
        cout << "Pemain: " << this->pemain << endl;
        cout << endl;
    }

    ~DaftarTimSepakBola() {}
};