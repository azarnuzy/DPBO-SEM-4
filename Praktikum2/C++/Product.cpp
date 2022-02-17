#include <bits/stdc++.h>

using namespace std;

class Product
// kelas yang digunakan untuk mengimplementasikan product
{
private:
    // private atribute dari kelas product
    int price;
    int idProduct;

public:
    // konstrutor
    Product() {}

    // mengeset nilai atribut price
    void setPrice(int price)
    {
        this->price = price;
    }

    // mengembalikan nilai atribut price
    int getPrice()
    {
        return this->price;
    }

    // mengeset nilai atribut idProduct
    void setIdProduct(int idProduct)
    {
        this->idProduct = idProduct;
    }

    // mengembalikan nilai atribut idProduct
    int getIdProduct()
    {
        return this->idProduct;
    }

    // menampilkan atribut product
    void printProduct()
    {
        cout << "Id Product : " << this->getIdProduct() << endl;
        cout << "Price : " << this->getPrice() << endl;
    }

    // destruktor
    ~Product() {}
};