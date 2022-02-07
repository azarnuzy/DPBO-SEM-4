class Titik
{
    /* Kelas yang digunakan untuk mengimplementasikan sebuah tipe titik */

private:
    int x; /*koordinat x*/
    int y; /* koordinat y */

public:
    Titik()
    {
        /* konstruktor */
        x = 0;
        y = 0;
    }

    Titik(int xp, int yp)
    {
        /* konstruktor */
        x = xp;
        y = yp;
    }

    void setX(int xp)
    {
        /* mengeset nilai koordinat x */
        x = xp;
    }

    int getX()
    {
        /* mengembalikan nilai koordinat x */
        return x;
    }

    void setY(int yp)
    {
        /* mengeset nilai koordinat x */
        y = yp;
    }

    int getY()
    {
        /* mengembalikan nilai koordinat x */
        return y;
    }

    ~Titik()
    {
        /* destruktor */
    }
};