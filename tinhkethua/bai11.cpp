#include <iostream>
using namespace std;

class Account
{
private:
    double balance;

protected:
    double getBalance() const
    {
        return balance;
    }

    void setBalance(double b)
    {
        if (b >= 0)
            balance = b;
    }

public:
    Account()
    {
        balance = 0;
    }

    void deposit(double money)
    {
        balance += money;
    }

    void displayBalance() const
    {
        cout << "Balance: " << balance << endl;
    }
};

class PremiumAccount : public Account
{
public:
    void bonus(double money)
    {
        double b = getBalance();
        setBalance(b + money);
    }
};

int main()
{
    PremiumAccount p;

    p.deposit(1000);
    p.displayBalance();

    p.bonus(500);
    p.displayBalance();

    return 0;
}