#include <iostream>
#include <string>

using namespace std;

class Vehicle
{
protected:
    string brand;
    int year;

public:
    Vehicle(string b, int y)
    {
        brand = b;
        year = y;
        cout << "Vehicle ctor" << endl;
    }

    ~Vehicle()
    {
        cout << "Vehicle dtor" << endl;
    }
};

class Car : public Vehicle
{
private:
    int numDoors;

public:
    Car(string b, int y, int d) : Vehicle(b, y)
    {
        numDoors = d;
        cout << "Car ctor" << endl;
    }

    ~Car()
    {
        cout << "Car dtor" << endl;
    }

    void display()
    {
        cout << "Brand: " << brand << endl;
        cout << "Year: " << year << endl;
        cout << "Doors: " << numDoors << endl;
    }
};

int main()
{
    Car car("Toyota", 2024, 4);

    car.display();

    return 0;
}