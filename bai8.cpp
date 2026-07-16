#include <iostream>

using namespace std;

//======================
// Không có virtual
//======================
class NoVirtual {
public:
    int x;

    void show() {
        cout << "NoVirtual" << endl;
    }
};

//======================
// Có virtual
//======================
class WithVirtual {
public:
    int x;

    virtual void show() {
        cout << "WithVirtual" << endl;
    }

    virtual ~WithVirtual() {}
};

//======================
// Kế thừa
//======================
class Derived : public WithVirtual {
public:
    int y;

    void show() override {
        cout << "Derived" << endl;
    }
};

//======================
// Main
//======================
int main() {

    cout << "===== SIZE OF OBJECT =====" << endl;

    cout << "sizeof(NoVirtual)   = "
         << sizeof(NoVirtual) << " bytes" << endl;

    cout << "sizeof(WithVirtual) = "
         << sizeof(WithVirtual) << " bytes" << endl;

    cout << "sizeof(Derived)     = "
         << sizeof(Derived) << " bytes" << endl;

    cout << endl;

    const int n = 1000000;

    long long mem1 = 1LL * sizeof(NoVirtual) * n;
    long long mem2 = 1LL * sizeof(WithVirtual) * n;
    long long mem3 = 1LL * sizeof(Derived) * n;

    cout << "===== BO NHO CHO 1,000,000 DOI TUONG =====" << endl;

    cout << "NoVirtual   : "
         << mem1 / 1024.0 / 1024 << " MB" << endl;

    cout << "WithVirtual : "
         << mem2 / 1024.0 / 1024 << " MB" << endl;

    cout << "Derived     : "
         << mem3 / 1024.0 / 1024 << " MB" << endl;

    cout << endl;

    cout << "Chenh lech (WithVirtual - NoVirtual): "
         << (mem2 - mem1) / 1024.0 / 1024
         << " MB" << endl;

    return 0;
}