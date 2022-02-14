#include <bits/stdc++.h>
#include "DaftarTimSepakBola.cpp"

using namespace std;

int main(int argc, char const *argv[])
{
    int n;
    cout << "Banyaknya tim sepakbola: ";
    cin >> n;
    cout << endl;

    DaftarTimSepakBola daftar1[n];
    for (int i = 0; i < n; i++)
    {
        string nama, negara, tahunBerdiri, pemain;
        cout << "Input" << endl;
        cout << "Masukan Nama: ";
        cin >> nama;

        cout << "Masukan Negara: ";
        cin >> negara;

        cout << "Masukan Tahun Berdiri: ";
        cin >> tahunBerdiri;

        cout << "Masukan Pemain: ";
        cin >> pemain;

        cout << endl;
        cout << "Output" << endl;
        daftar1[i].setNama(nama);
        daftar1[i].setNegara(negara);
        daftar1[i].setTahunBerdiri(tahunBerdiri);
        daftar1[i].setPemain(pemain);
        daftar1[i].printHasil();
    }

    DaftarTimSepakBola daftar2("Manchester United", "England", "1847", "Wayne Rooney");
    daftar2.printHasil();
    return 0;
}
