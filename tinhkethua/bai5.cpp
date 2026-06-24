#include <iostream>
using namespace std;

class BankAccount
{
protected:
    double balance;

public:
    BankAccount(double b)
    {
        balance = b;
    }

    void deposit(double money)
    {
        balance += money;
    }

    virtual void withdraw(double money)
    {
        if (money <= balance)
        {
            balance -= money;
            cout << "Withdraw successful" << endl;
        }
        else
        {
            cout << "Not enough money" << endl;
        }
    }

    void display()
    {
        cout << "Balance: " << balance << endl;
    }
};

class SavingsAccount : public BankAccount
{
private:
    double minimumBalance;

public:
    SavingsAccount(double b, double min) : BankAccount(b)
    {
        minimumBalance = min;
    }

    void withdraw(double money)
    {
        if (balance - money >= minimumBalance)
        {
            balance -= money;
            cout << "Withdraw successful" << endl;
        }
        else
        {
            cout << "Cannot withdraw. Minimum balance required." << endl;
        }
    }
};

int main()
{
    SavingsAccount acc(1000, 200);

    acc.display();

    acc.withdraw(500);
    acc.display();

    acc.withdraw(400);
    acc.display();

    return 0;
}