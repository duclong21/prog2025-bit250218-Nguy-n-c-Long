#include <iostream>
#include <string>
using namespace std;

class Animal
{
public:
    string name;

    Animal(string n)
    {
        name = n;
    }
};

class Mammal : virtual public Animal
{
public:
    Mammal(string n) : Animal(n)
    {
    }
};

class WingedAnimal : virtual public Animal
{
public:
    WingedAnimal(string n) : Animal(n)
    {
    }
};

class Bat : public Mammal, public WingedAnimal
{
public:
    Bat(string n)
        : Animal(n), Mammal(n), WingedAnimal(n)
    {
    }

    void display()
    {
        cout << "Name: " << name << endl;
    }
};

int main()
{
    Bat b("Batman");

    b.display();

    return 0;
}