#include <string>
#include <iostream>
using namespace std;
#include "Karyawan.cpp"

int main(int argc, char const *argv[])
{
    Manusia kmanusia;
    Karyawan kkaryawan;

    kmanusia.setNama("Gina");
    kmanusia.setAlamat("Bandung");
    kmanusia.setNoKtp("320.120.777");
    kmanusia.setNoTelepon("0812345768");

    cout << kmanusia.getNama() << endl;
    cout << kmanusia.getAlamat() << endl;
    cout << kmanusia.getNoKtp() << endl;
    cout << kmanusia.getNoTelepon() << endl;

    kkaryawan.setNama("Adi");
    kkaryawan.setAlamat("Jakarta");
    kkaryawan.setNoKtp("123.333.222");
    kkaryawan.setNoTelepon("02123458332");
    kkaryawan.setNomorPegawai("0123421234");
    kkaryawan.setJabatan("-");
    kkaryawan.setDepartemen("-");

    cout << kkaryawan.getNama() << endl;
    cout << kkaryawan.getAlamat() << endl;
    cout << kkaryawan.getNoKtp() << endl;
    cout << kkaryawan.getNoTelepon() << endl;
    cout << kkaryawan.getNomorPegawai() << endl;
    cout << kkaryawan.getDepartemen() << endl;
    return 0;
}
