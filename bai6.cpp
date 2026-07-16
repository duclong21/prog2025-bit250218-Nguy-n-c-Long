#include <iostream>

using namespace std;

//======================
// PHẦN A: KHÔNG CÓ VIRTUAL DESTRUCTOR
//======================

class Base {
public:
    ~Base() {
        cout << "~Base()" << endl;
    }
};

class Derived : public Base {
private:
    int* data;

public:
    Derived() {
        data = new int[100];
        cout << "Cap phat bo nho cho Derived." << endl;
    }

    ~Derived() {
        cout << "~Derived()" << endl;
        delete[] data;
    }
};

//======================
// PHẦN B: CÓ VIRTUAL DESTRUCTOR
//======================

class Base2 {
public:
    virtual ~Base2() {
        cout << "~Base2()" << endl;
    }
};

class Derived2 : public Base2 {
private:
    int* data;

public:
    Derived2() {
        data = new int[100];
        cout << "Cap phat bo nho cho Derived2." << endl;
    }

    ~Derived2() override {
        cout << "~Derived2()" << endl;
        delete[] data;
    }
};

//======================
// MAIN
//======================

int main() {

    cout << "===== PHAN A: KHONG CO VIRTUAL DESTRUCTOR =====" << endl;

    Base* p = new Derived();

    delete p;

    cout << endl;

    cout << "===== PHAN B: CO VIRTUAL DESTRUCTOR =====" << endl;

    Base2* p2 = new Derived2();

    delete p2;

    return 0;
}