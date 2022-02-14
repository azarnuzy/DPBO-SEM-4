#include <bits/stdc++.h>

using namespace std;

class Bangunan
{
private:
    int kodeBangunan;
    string pemilikBangunan;

public:
    Bangunan()
    {
    }

    void setKodeBangunan(int kodeBangunan)
    {
        this->kodeBangunan = kodeBangunan;
    }

    int getKodeBangunan()
    {
        return this->kodeBangunan;
    }

    void setPemilikBangunan(string pemilikBangunan)
    {
        this->pemilikBangunan = pemilikBangunan;
    }

    string getPemilikBangunan()
    {
        return this->pemilikBangunan;
    }
};