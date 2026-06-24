#include <iostream>
#include <string>
using namespace std;

class Employee
{
protected:
    string name;
    double hoursWorked;
    double hourlyRate;

public:
    Employee(string n, double h, double r)
    {
        name = n;
        hoursWorked = h;
        hourlyRate = r;
    }

    virtual double calculatePay()
    {
        return hoursWorked * hourlyRate;
    }

    void display()
    {
        cout << "Name: " << name << endl;
        cout << "Salary: " << calculatePay() << endl;
    }
};

class Manager : public Employee
{
private:
    double bonus;

public:
    Manager(string n, double h, double r, double b)
        : Employee(n, h, r)
    {
        bonus = b;
    }

    double calculatePay()
    {
        return Employee::calculatePay() + bonus;
    }
};

class Intern : public Employee
{
public:
    Intern(string n, double h, double r)
        : Employee(n, h, r)
    {
    }

    double calculatePay()
    {
        return Employee::calculatePay() * 0.8;
    }
};

int main()
{
    Employee e("An", 160, 50);

    Manager m("Binh", 160, 50, 5000);

    Intern i("Cuong", 160, 50);

    cout << "Employee" << endl;
    e.display();

    cout << endl;

    cout << "Manager" << endl;
    m.display();

    cout << endl;

    cout << "Intern" << endl;
    i.display();

    return 0;
}