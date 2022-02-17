#include <bits/stdc++.h>
using namespace std;
// import class product
#include "Product.cpp"

class Hardware : public Product
// kelas yang digunakan untuk mengimplementasikan Hardware dan juga turunan dari kelas Product
{
private:
    // private atribute dari kelas Hardware
    string brand;
    string model;

public:
    // konstruktor
    Hardware() {}

    // mengeset nilai atribut brand
    void setBrand(string brand)
    {
        this->brand = brand;
    }

    // mengembalikan nilai atribut brand
    string getBrand()
    {
        return this->brand;
    }

    // mengeset nilai atribut model
    void setModel(string model)
    {
        this->model = model;
    }

    // mengembalikan nilai atribut model
    string getModel()
    {
        return this->model;
    }

    // menampilkan atribut Hardware
    void printHardware()
    {
        cout << "Brand : " << this->getBrand() << endl;
        cout << "Model : " << this->getModel() << endl;
    }

    // destructor
    ~Hardware() {}
};