#include <iostream>
#include <string>

using namespace std;

class Calculator {
public:
    // Cộng 2 số nguyên
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }

    // Nối 2 chuỗi
    string add(string a, string b) {
        return a + b;
    }
};

int main() {
    Calculator calc;

    cout << "Cong 2 so nguyen: "
         << calc.add(5, 8) << endl;

    cout << "Cong 2 so thuc: "
         << calc.add(3.5, 2.7) << endl;

    cout << "Cong 3 so nguyen: "
         << calc.add(1, 2, 3) << endl;

    cout << "Noi chuoi: "
         << calc.add("Hello ", "World") << endl;

    cout << "\nThu goi add(1, 2.5): "
         << calc.add(1.0, 2.5) << endl;

    return 0;
}