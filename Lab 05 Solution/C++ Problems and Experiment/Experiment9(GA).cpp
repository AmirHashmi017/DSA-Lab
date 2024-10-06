#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <stdexcept>

using namespace std;

template <typename T>

class AutoGrowingArray {
public:
    T* data;
    int size;
    int capacity;

    AutoGrowingArray() : size(0), capacity(1) {
        data = new T[capacity];
    }

    ~AutoGrowingArray() {
        delete[] data;
    }

    T operator[](int index) const {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return data[index];
    }

    T& operator[](int index) {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return data[index];
    }

    void PushBack(T value) {
        if (size >= capacity) {
            capacity *= 2;
            T* newData = new T[capacity];
            for (int i = 0; i < size; i++) {
                newData[i] = data[i];
            }
            delete[] data;
            data = newData;
        }
        data[size++] = value;
    }

    friend ostream& operator<<(ostream& out, const AutoGrowingArray& array) {
        out << "[ ";
        for (int i = 0; i < array.size; ++i) {
            out << array.data[i];
            if (i < array.size - 1) {
                out << ", ";
            }
        }
        out << " ]";
        return out;
    }
};


void CreateRandomFile(const string& fn, int size, int RN = 100) {
    srand(static_cast<unsigned>(time(0))); 
    ofstream writer(fn);
    for (int i = 0; i < size * 1024 * 1024; i++) {
        writer << rand() % RN << " "; 
    }
}

void LoadDataIntoVector(const string& fn, AutoGrowingArray<int>& GA) {
    ifstream reader(fn);
    int value;
    while (reader >> value) {
        GA.PushBack(value);
    }
}

int main() {
    string filename = "InputGA.txt";
    CreateRandomFile(filename, 2); 

    time_t start = time(0); 

    AutoGrowingArray<int> GA;
    LoadDataIntoVector(filename, GA);

    time_t end = time(0); 

    ofstream output("OutputGA.txt");
    output << GA; 

    double elapsed = difftime(end, start);
    cout << "Time taken to load data into General Array(GA): " << elapsed << " seconds" << endl;

    return 0;
}
