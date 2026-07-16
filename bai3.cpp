#include <iostream>
using namespace std;

//===================
// PHẦN A: Không dùng virtual
//===================

class Animal {
public:
    void speak() {
        cout << "Animal: ..." << endl;
    }
};

class Dog : public Animal {
public:
    void speak() {
        cout << "Dog: Woof!" << endl;
    }
};

class Cat : public Animal {
public:
    void speak() {
        cout << "Cat: Meow!" << endl;
    }
};

//===================
// PHẦN B: Có virtual
//===================

class Animal2 {
public:
    virtual void speak() {
        cout << "Animal: ..." << endl;
    }

    virtual ~Animal2() {}
};

class Dog2 : public Animal2 {
public:
    void speak() override {
        cout << "Dog: Woof!" << endl;
    }
};

class Cat2 : public Animal2 {
public:
    void speak() override {
        cout << "Cat: Meow!" << endl;
    }
};

int main() {

    cout << "===== PHAN A: KHONG CO VIRTUAL =====" << endl;

    Animal* p1 = new Dog();
    Animal* p2 = new Cat();

    p1->speak();
    p2->speak();

    delete p1;
    delete p2;

    cout << "\n===== PHAN B: CO VIRTUAL =====" << endl;

    Animal2* p3 = new Dog2();
    Animal2* p4 = new Cat2();

    p3->speak();
    p4->speak();

    delete p3;
    delete p4;

    return 0;
}