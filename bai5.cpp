#include <iostream>
#include <string>

using namespace std;

//======================
// Lớp cơ sở
//======================
class Animal {
public:
    virtual void speak() {
        cout << "Animal: ..." << endl;
    }

    virtual ~Animal() {}
};

//======================
// Lớp dẫn xuất
//======================
class Dog : public Animal {
private:
    string breed;

public:
    Dog(string b) {
        breed = b;
    }

    void speak() override {
        cout << "Dog (" << breed << "): Woof!" << endl;
    }
};

//======================
// Truyền by value
//======================
void byValue(Animal a) {
    cout << "byValue(): ";
    a.speak();
}

//======================
// Truyền bằng con trỏ
//======================
void byPointer(Animal* a) {
    cout << "byPointer(): ";
    a->speak();
}

//======================
// Truyền bằng tham chiếu
//======================
void byReference(Animal& a) {
    cout << "byReference(): ";
    a.speak();
}

//======================
// Main
//======================
int main() {

    Dog dog("Golden Retriever");

    cout << "===== OBJECT SLICING =====" << endl;

    byValue(dog);

    cout << endl;

    cout << "===== POINTER =====" << endl;

    byPointer(&dog);

    cout << endl;

    cout << "===== REFERENCE =====" << endl;

    byReference(dog);

    return 0;
}