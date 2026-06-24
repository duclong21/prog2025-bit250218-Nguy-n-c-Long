#include <iostream>

using namespace std;

class Base
{
public:
    int pub = 10;

protected:
    int prot = 20;

private:
    int priv = 30;
};

class DerivedPublic : public Base
{
public:
    void test()
    {
        cout << "Public Inheritance" << endl;
        cout << "pub = " << pub << endl;
        cout << "prot = " << prot << endl;
        // cout << priv; // Lỗi
    }
};

class DerivedProtected : protected Base
{
public:
    void test()
    {
        cout << "Protected Inheritance" << endl;
        cout << "pub = " << pub << endl;
        cout << "prot = " << prot << endl;
        // cout << priv; // Lỗi
    }
};

class DerivedPrivate : private Base
{
public:
    void test()
    {
        cout << "Private Inheritance" << endl;
        cout << "pub = " << pub << endl;
        cout << "prot = " << prot << endl;
        // cout << priv; // Lỗi
    }
};

int main()
{
    DerivedPublic a;
    DerivedProtected b;
    DerivedPrivate c;

    a.test();
    cout << endl;

    b.test();
    cout << endl;

    c.test();
    cout << endl;

    // Chỉ public inheritance mới truy cập được từ bên ngoài
    a.pub = 100;
    cout << "a.pub = " << a.pub << endl;

    // b.pub = 100; // Lỗi
    // c.pub = 100; // Lỗi

    return 0;
}