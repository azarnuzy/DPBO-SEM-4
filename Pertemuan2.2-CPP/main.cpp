#include <bits/stdc++.h>
using namespace std;

#include "Gudang.cpp"

int main(int argc, char const *argv[])
{
    Aset oaset;
    Bangunan obangunan;
    Gudang ogudang;

    oaset.setKodeAset(1);
    oaset.setJenisAset(1);
    oaset.setNilaiAset(30000000);

    cout << oaset.getKodeAset() << endl;
    cout << oaset.getJenisAset() << endl;
    cout << oaset.getNilaiAset() << endl;

    obangunan.setKodeBangunan(1);
    obangunan.setPemilikBangunan("BDG Aamiin");

    cout << obangunan.getKodeBangunan() << endl;
    cout << obangunan.getPemilikBangunan() << endl;

    ogudang.setKodeAset(3);
    ogudang.setJenisAset(3);
    ogudang.setNilaiAset(30000000);
    ogudang.setKodeBangunan(3);
    ogudang.setPemilikBangunan("BDG Aamiin");
    ogudang.setKodeGudang(1);
    ogudang.setNamaGudang("BDG Aamiin I");
    ogudang.setAlamatGudang("Bandung");

    return 0;
}
