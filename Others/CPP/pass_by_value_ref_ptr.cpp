
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Pass by value (copy)
void modifyByValue(int x) {
    x += 10;
    cout << "Inside modifyByValue: x = " << x << endl;
}

// Pass by reference (&) - safer and cleaner
void modifyByReference(int& x) {
    x += 10;
    cout << "Inside modifyByReference: x = " << x << endl;
}

// Pass by pointer (*) - classic C-style
void modifyByPointer(int* x) {
    if (x != nullptr) {
        *x += 10;
        cout << "Inside modifyByPointer: x = " << *x << endl;
    }
}

// Vector by reference
void addElement(vector<int>& vec) {
    vec.push_back(100);
    cout << "Inside addElement: last element = " << vec.back() << endl;
}

// String by reference
void updateString(string& s) {
    s += " World!";
    cout << "Inside updateString: s = " << s << endl;
}

int main() {
    cout << "=== Basic Integer ===" << endl;
    int a = 5;
    modifyByValue(a);
    cout << "After modifyByValue: a = " << a << endl;

    modifyByReference(a);
    cout << "After modifyByReference: a = " << a << endl;

    modifyByPointer(&a);
    cout << "After modifyByPointer: a = " << a << endl;

    cout << "\n=== Vector Example ===" << endl;
    vector<int> numbers = {1, 2, 3};
    addElement(numbers);
    cout << "After addElement: size = " << numbers.size() << ", last = " << numbers.back() << endl;

    cout << "\n=== String Example ===" << endl;
    string msg = "Hello";
    updateString(msg);
    cout << "After updateString: msg = " << msg << endl;

    return 0;
}
