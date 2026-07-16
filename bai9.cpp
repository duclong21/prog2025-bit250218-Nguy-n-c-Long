#include <iostream>
#include <string>

using namespace std;

//======================
// Abstract Class
//======================
class PaymentMethod {
public:
    virtual void pay(double amount) = 0;
    virtual string getName() const = 0;
    virtual ~PaymentMethod() {}
};

//======================
// MomoPayment
//======================
class MomoPayment : public PaymentMethod {
public:
    void pay(double amount) override {
        cout << "Thanh toan " << amount
             << " VND bang MoMo." << endl;
    }

    string getName() const override {
        return "MoMo";
    }
};

//======================
// ZaloPayment
//======================
class ZaloPayment : public PaymentMethod {
public:
    void pay(double amount) override {
        cout << "Thanh toan " << amount
             << " VND bang ZaloPay." << endl;
    }

    string getName() const override {
        return "ZaloPay";
    }
};

//======================
// QRPayment
//======================
class QRPayment : public PaymentMethod {
public:
    void pay(double amount) override {
        cout << "Thanh toan " << amount
             << " VND bang QR Code." << endl;
    }

    string getName() const override {
        return "QR Code";
    }
};

//======================
// ShopeePayment
//======================
class ShopeePayment : public PaymentMethod {
public:
    void pay(double amount) override {
        cout << "Thanh toan " << amount
             << " VND bang ShopeePay." << endl;
    }

    string getName() const override {
        return "ShopeePay";
    }
};

//======================
// Hàm Checkout
//======================
void checkout(PaymentMethod &method, double amount) {
    cout << "\nPhuong thuc: "
         << method.getName() << endl;

    method.pay(amount);

    cout << "Thanh toan thanh cong!" << endl;
}

//======================
// Main
//======================
int main() {

    int choice;
    double amount;

    cout << "===== PAYMENT GATEWAY =====" << endl;

    cout << "1. MoMo" << endl;
    cout << "2. ZaloPay" << endl;
    cout << "3. QR Code" << endl;
    cout << "4. ShopeePay" << endl;

    cout << "\nChon phuong thuc: ";
    cin >> choice;

    cout << "Nhap so tien: ";
    cin >> amount;

    PaymentMethod *payment = nullptr;

    switch (choice) {
        case 1:
            payment = new MomoPayment();
            break;

        case 2:
            payment = new ZaloPayment();
            break;

        case 3:
            payment = new QRPayment();
            break;

        case 4:
            payment = new ShopeePayment();
            break;

        default:
            cout << "Lua chon khong hop le!" << endl;
            return 0;
    }

    checkout(*payment, amount);

    delete payment;

    return 0;
}