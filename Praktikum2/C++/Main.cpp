#include <bits/stdc++.h>
/*Saya Muhammad Azar Nuzy 2004191 mengerjakan Latihan 2 C1 dalam
mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin*/
using namespace std;
// mengimport kelas Memory
#include "Memory.cpp"

int main(int argc, char const *argv[])
{
    // instansiasi
    Memory comp[100];
    bool check = true;
    int i = 0;

    // kondisi untuk melakukan perulangan masukan
    while (check)
    {
        // instansiasi variabel untuk masukan
        string brand, model, frequency, supportsCuda;
        int price, idProduct, memorySize;

        // input untuk setiap atribut yang ada
        cout << "Input: " << endl;
        cout << "Id Product: ";
        cin >> idProduct;
        cout << "Price: ";
        cin >> price;
        cout << "Brand: ";
        cin >> brand;
        cout << "Model: ";
        cin >> model;
        cout << "Frequency: ";
        cin >> frequency;
        cout << "Memory Size: ";
        cin >> memorySize;
        cout << "Supports Cuda: ";
        cin >> supportsCuda;

        // mengeset isi atribut dari kelas-kelas pada memory
        comp[i].setIdProduct(idProduct);
        comp[i].setPrice(price);
        comp[i].setBrand(brand);
        comp[i].setModel(model);
        comp[i].setFrequency(frequency);
        comp[i].setMemorySize(memorySize);
        comp[i].setSupportsCuda(supportsCuda);

        // variabel untuk melakukan pengecekan apakah akan lanjut input atau berhenti
        char next;
        cout << "Lanjut memasukan data (Y/N): ";
        cin >> next;
        if (next == 'y' || next == 'Y')
        {
            check = true;
        }
        else
        {
            check = false;
        }
        // iterator
        i++;
    }

    // mencetak atribut ada kelas-kelas yang ada di Memory
    cout << "\n";
    for (int j = 0; j < i; j++)
    {
        cout << "Output ke-" << j + 1 << endl;
        comp[j].printProduct();
        comp[j].printHardware();
        comp[j].printMemory();
        cout << endl;
    }
    return 0;
}
