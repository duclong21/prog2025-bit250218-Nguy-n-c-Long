#include <iostream>
using namespace std;

class Vector2D {
private:
    double x, y;

public:
    // Constructor
    Vector2D(double x = 0, double y = 0) {
        this->x = x;
        this->y = y;
    }

    // Overload toán tử +
    Vector2D operator+(const Vector2D &other) const {
        return Vector2D(x + other.x, y + other.y);
    }

    // Overload toán tử -
    Vector2D operator-(const Vector2D &other) const {
        return Vector2D(x - other.x, y - other.y);
    }

    // Overload toán tử * (nhân với số thực)
    Vector2D operator*(double scalar) const {
        return Vector2D(x * scalar, y * scalar);
    }

    // Overload toán tử ==
    bool operator==(const Vector2D &other) const {
        return (x == other.x && y == other.y);
    }

    // Overload <<
    friend ostream& operator<<(ostream &out, const Vector2D &v) {
        out << "(" << v.x << ", " << v.y << ")";
        return out;
    }
};

int main() {
    Vector2D v1(2.5, 3.0);
    Vector2D v2(1.5, 4.0);

    Vector2D v3 = v1 + v2;
    Vector2D v4 = v1 - v2;
    Vector2D v5 = v1 * 3.0;

    cout << "v1 = " << v1 << endl;
    cout << "v2 = " << v2 << endl;
    cout << "v1 + v2 = " << v3 << endl;
    cout << "v1 - v2 = " << v4 << endl;
    cout << "v1 * 3 = " << v5 << endl;

    if (v1 == v2)
        cout << "v1 va v2 bang nhau." << endl;
    else
        cout << "v1 va v2 khong bang nhau." << endl;

    return 0;
}