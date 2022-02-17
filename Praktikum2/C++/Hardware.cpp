#include <bits/stdc++.h>
#include "Product.cpp"
using namespace std;

class Hardware : public Product
{
private:
    string brand;
    string model;

public:
    Hardware() {}

    void setBrand(string brand)
    {
        this->brand = brand;
    }

    string getBrand()
    {
        return this->brand;
    }

    void setModel(string model)
    {
        this->model = model;
    }

    string getModel()
    {
        return this->model;
    }

    void printHardware()
    {
        cout << "Brand : " << getBrand() << endl;
        cout << "Model : " << getModel() << endl;
    }

    ~Hardware() {}
};