#include <iostream>
using namespace std;

class Auditor;

class Wallet
{
private:
    double money;

public:
    Wallet(double m)
    {
        money = m;
    }

    friend void inspect(const Wallet &w);
    friend class Auditor;
};

void inspect(const Wallet &w)
{
    cout << "Money: " << w.money << endl;
}

class Auditor
{
public:
    void audit(const Wallet &w)
    {
        cout << "Audit: " << w.money << endl;
    }
};

int main()
{
    Wallet w(5000);

    inspect(w);

    Auditor a;
    a.audit(w);

    return 0;
}