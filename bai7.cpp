#include <iostream>
using namespace std;

//======================
// Lớp cơ sở
//======================
class Shape {
public:
    virtual double area() const {
        return 0.0;
    }

    virtual void draw() const {
        cout << "Drawing Shape..." << endl;
    }

    virtual ~Shape() {}
};

//======================
// Circle
//======================
class Circle : public Shape {
protected:
    double radius;

public:
    Circle(double r) {
        radius = r;
    }

    double area() const override {
        return 3.14159 * radius * radius;
    }

    void draw() const final override {
        cout << "Drawing Circle..." << endl;
    }
};

//======================
// SpecialCircle
//======================
class SpecialCircle : public Circle {
public:
    SpecialCircle(double r) : Circle(r) {}

    // Được phép override
    double area() const override {
        return 3.14159 * radius * radius * 2;
    }

    /*
    // Nếu bỏ comment sẽ LỖI BIÊN DỊCH
    void draw() const override {
        cout << "Special Circle" << endl;
    }
    */

    /*
    // Ví dụ lỗi typo
    double Area() const override {
        return 0;
    }
    */
};

//======================
// Main
//======================
int main() {

    Shape* s1 = new Circle(5);
    Shape* s2 = new SpecialCircle(5);

    cout << "===== Circle =====" << endl;
    s1->draw();
    cout << "Area = " << s1->area() << endl;

    cout << endl;

    cout << "===== SpecialCircle =====" << endl;
    s2->draw();
    cout << "Area = " << s2->area() << endl;

    delete s1;
    delete s2;

    return 0;
}