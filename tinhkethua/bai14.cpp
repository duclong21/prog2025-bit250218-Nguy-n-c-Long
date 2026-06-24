#include <iostream>
#include <string>

using namespace std;

// Interface 1
class Printable
{
public:
    virtual void print() const = 0;
};

// Interface 2
class Serializable
{
public:
    virtual string serialize() const = 0;
};

// Lớp kế thừa cả hai interface
class Document : public Printable, public Serializable
{
private:
    string title;
    string content;

public:
    Document(string t, string c)
    {
        title = t;
        content = c;
    }

    void print() const override
    {
        cout << "----- Document -----" << endl;
        cout << "Title: " << title << endl;
        cout << "Content: " << content << endl;
    }

    string serialize() const override
    {
        return "{Title: \"" + title + "\", Content: \"" + content + "\"}";
    }
};

int main()
{

    Document doc("Inheritance", "Learning Abstract Class");

    doc.print();

    cout << endl;

    cout << "Serialized Data:" << endl;
    cout << doc.serialize() << endl;

    return 0;
}