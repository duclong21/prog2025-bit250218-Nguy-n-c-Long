#include <iostream>
#include <string>
using namespace std;

class Person
{
protected:
    string name;
    int age;

public:
    Person(string n, int a)
    {
        name = n;
        age = a;
    }
};

class Employee : public Person
{
protected:
    int employeeId;
    double salary;

public:
    Employee(string n, int a, int id, double s)
        : Person(n, a)
    {
        employeeId = id;
        salary = s;
    }
};

class Manager : public Employee
{
private:
    string department;
    int teamSize;

public:
    Manager(string n, int a, int id, double s, string d, int t)
        : Employee(n, a, id, s)
    {
        department = d;
        teamSize = t;
    }

    void display()
    {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Employee ID: " << employeeId << endl;
        cout << "Salary: " << salary << endl;
        cout << "Department: " << department << endl;
        cout << "Team Size: " << teamSize << endl;
    }
};

int main()
{
    Manager m("Long", 19, 1001, 15000000, "IT", 8);

    m.display();

    return 0;
}