#include <iostream>
using namespace std;

template <typename T>
class Vector {
public:
    T* arr;           
    int size;         
    int capacity;     

    Vector() : size(0), capacity(1) {
        arr = new T[capacity]; 
    }

    ~Vector() {
        delete[] arr;
    }

    void PushBack(T value) {
        if (size >= capacity) {
            capacity *= 2; 
            T* temp = new T[capacity]; 
            for (int i = 0; i < size; i++) {
            temp[i] = arr[i];
        }
        delete[] arr;   
        arr = temp; 
        }
        arr[size] = value;
        size++;
    }
    T& operator[](int index) {
        if (index >= size || index < 0) {
            throw out_of_range("Index out of bounds");
        }
        return arr[index];
    }

    T operator[](int index) const {
        if (index >= size || index < 0) {
            throw out_of_range("Index out of bounds");
        }
        return arr[index];
    }

    friend ostream& operator<<(ostream& out, const Vector& vec) {
        for (int i = 0; i < vec.size; i++) {
            out << vec[i] << " ";
        }
        return out;
    }
};

int main() {
    Vector<int> vec;
    vec.PushBack(10);
    vec.PushBack(20);
    vec.PushBack(30);
    cout << "Vector: " << vec << endl;
    cout << "Element at index 1: " << vec[1] << endl;
    vec.PushBack(40);
    vec.PushBack(50);
    cout << "Vector after adding more elements: " << vec << endl;

    return 0;
}

