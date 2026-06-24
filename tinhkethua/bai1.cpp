#include <iostream>
#include <string>

using namespace std;

class Animal
{
protected:
    string name;
    int age;

public:
    Animal(string n, int a)
    {
        name = n;
        age = a;
    }

    void eat()
    {
        cout << name << " is eating..." << endl;
    }
};

class Dog : public Animal
{
private:
    string breed;

public:
    Dog(string n, int a, string b) : Animal(n, a)
    {
        breed = b;
    }

    void bark()
    {
        cout << name << " is barking..." << endl;
    }

    void display()
    {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Breed: " << breed << endl;
    }
};

int main()
{
    Dog dog("Lucky", 3, "Husky");

    dog.display();
    dog.eat();
    dog.bark();

    return 0;
}