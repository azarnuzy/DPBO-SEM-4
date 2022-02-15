#include <iostream>
#include <string>
#include "MasakanIndonesia.cpp"
using namespace std;

class MasakanAsing : public MasakanIndonesia
{
private:
    string negara;

public:
    MasakanAsing() {}

    void setNegara(int negara)
    {
        this->negara = negara;
    }

    string getNegara()
    {
        return this->negara;
    }

    ~MasakanAsing() {}
};