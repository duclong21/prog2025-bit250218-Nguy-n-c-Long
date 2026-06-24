#include <iostream>
#include <string>
using namespace std;

class Security final
{
private:
    string encryptionKey;

public:
    Security(string key)
    {
        encryptionKey = key;
    }

    void encrypt(string text)
    {
        cout << "Encrypting \"" << text << "\" with key: "
             << encryptionKey << endl;
    }
};

/*
// Uncomment để thấy lỗi

class SuperSecurity : public Security
{

};

*/

class Base
{
public:
    virtual void process() final
    {
        cout << "Processing..." << endl;
    }
};

/*
// Uncomment để thấy lỗi

class Derived : public Base
{
public:
    void process()
    {
        cout << "Override";
    }
};

*/

int main()
{
    Security s("ABC123");

    s.encrypt("Hello World");

    Base b;

    b.process();

    return 0;
}