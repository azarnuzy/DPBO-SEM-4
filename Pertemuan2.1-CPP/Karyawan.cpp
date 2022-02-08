#include <iostream>
#include <string>
#include "Manusia.cpp"
using namespace std;

class Karyawan : public Manusia
{
private:
    string nomor_pegawai;
    string jabatan;
    string departemen;

public:
    Karyawan() {}

    void setNomorPegawai(string nomor_pegawai)
    {
        this->nomor_pegawai = nomor_pegawai;
    }

    string getNomorPegawai()
    {
        return this->nomor_pegawai;
    }

    void setJabatan(string jabatan)
    {
        this->jabatan = jabatan;
    }

    string getJabatan()
    {
        return this->jabatan;
    }

    void setDepartemen(string departemen)
    {
        this->departemen = departemen;
    }

    string getDepartemen()
    {
        return this->departemen;
    }

    ~Karyawan() {}
};