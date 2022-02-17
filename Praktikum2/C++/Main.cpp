#include <bits/stdc++.h>
using namespace std;

#include "Memory.cpp"

int main(int argc, char const *argv[])
{
    Memory comp[100];
    bool check = true;
    int i = 0;
    while (check)
    {
        string brand, model, frequency, supportsCuda;
        int price, idProduct, memorySize;

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

        comp[i].setIdProduct(idProduct);
        comp[i].setPrice(price);
        comp[i].setBrand(brand);
        comp[i].setModel(model);
        comp[i].setFrequency(frequency);
        comp[i].setMemorySize(memorySize);
        comp[i].setSupportsCuda(supportsCuda);
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
        i++;
    }

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
