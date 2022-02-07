#include <iostream>
#include "Titik.cpp"

using namespace std;

/* fungsi main untuk mengetes kelas titik */
int main()
{
    Titik t1, t2(11, 9);

    t1.setX(10);
    t1.setY(20);

    cout << "t1: nilai X: " << t1.getX() << endl;
    cout << "t1: nilai Y: " << t1.getY() << endl;

    cout << "t2: nilai X: " << t2.getX() << endl;
    cout << "t2: nilai Y: " << t2.getY() << endl;
}