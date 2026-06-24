#include <iostream>
#include <string>
using namespace std;

class Shape
{
protected:
    string color;

public:
    Shape(string c)
    {
        color = c;
    }

    void describe()
    {
        cout << "Shape: " << color << endl;
    }

    virtual double area()
    {
        return 0;
    }
};

class Circle : public Shape
{
private:
    double radius;

public:
    Circle(string c, double r) : Shape(c)
    {
        radius = r;
    }

    double area()
    {
        return 3.14 * radius * radius;
    }

    void describe()
    {
        Shape::describe();
        cout << "Circle Radius: " << radius << endl;
    }
};

class Rectangle : public Shape
{
private:
    double width;
    double height;

public:
    Rectangle(string c, double w, double h) : Shape(c)
    {
        width = w;
        height = h;
    }

    double area()
    {
        return width * height;
    }

    void describe()
    {
        Shape::describe();
        cout << "Rectangle: " << width << " x " << height << endl;
    }
};

int main()
{
    Circle c("Red", 5);
    Rectangle r("Blue", 4, 6);

    c.describe();
    cout << "Area = " << c.area() << endl;

    cout << endl;

    r.describe();
    cout << "Area = " << r.area() << endl;

    return 0;
}