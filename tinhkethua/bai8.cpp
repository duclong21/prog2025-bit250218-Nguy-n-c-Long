#include <iostream>
using namespace std;

class Account
{
protected:
    string accountNo;
    double balance;

public:
    Account(string no, double b)
    {
        accountNo = no;
        balance = b;
    }

    void deposit(double money)
    {
        balance += money;
    }

    void withdraw(double money)
    {
        if (money <= balance)
            balance -= money;
    }

    void display()
    {
        cout << "Balance: " << balance << endl;
    }
};

class SavingsAccount : public Account
{
protected:
    double interestRate;

public:
    SavingsAccount(string no, double b, double rate)
        : Account(no, b)
    {
        interestRate = rate;
    }

    virtual void addInterest()
    {
        balance += balance * interestRate;
    }
};

class VIPSavings : public SavingsAccount
{
public:
    VIPSavings(string no, double b, double rate)
        : SavingsAccount(no, b, rate)
    {
    }

    void addInterest()
    {
        balance += balance * (interestRate * 2);
    }
};

int main()
{
    SavingsAccount s("001", 10000, 0.05);
    VIPSavings v("002", 10000, 0.05);

    cout << "Savings Account" << endl;

    for (int i = 1; i <= 3; i++)
        s.addInterest();

    s.display();

    cout << endl;

    cout << "VIP Savings" << endl;

    for (int i = 1; i <= 3; i++)
        v.addInterest();

    v.display();

    return 0;
}