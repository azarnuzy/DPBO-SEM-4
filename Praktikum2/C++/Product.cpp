#include <bits/stdc++.h>

using namespace std;

class Product
{
private:
    int price;
    int idProduct;

public:
    Product() {}

    void setPrice(int price)
    {
        this->price = price;
    }

    int getPrice()
    {
        return this->price;
    }

    void setIdProduct(int idProduct)
    {
        this->idProduct = idProduct;
    }

    int getIdProduct()
    {
        return this->idProduct;
    }

    void printProduct()
    {
        cout << "Id Product : " << getIdProduct() << endl;
        cout << "Price : " << getPrice() << endl;
    }

    ~Product() {}
};