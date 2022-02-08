#include <bits/stdc++.h>
#include "DaftarTimSepakBola.cpp"

using namespace std;

int main(int argc, char const *argv[])
{
    DaftarTimSepakBola daftar1;
    daftar1.setNama("Barcelona");
    daftar1.setNegara("Spanyol");
    daftar1.setTahunBerdiri("1887");
    daftar1.setPemain("Sergio Ramos");
    daftar1.printHasil();

    DaftarTimSepakBola daftar2("Manchester United", "England", "1847", "Wayne Rooney");
    daftar2.printHasil();
    return 0;
}
