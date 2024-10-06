#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <stdexcept>

using namespace std;

template <typename T>

class ArrayList {
public:
    T* arr;
    int size;
    int capacity;

    ArrayList() : size(0), capacity(2) {
        arr = new T[capacity];
    }

    ~ArrayList() {
        delete[] arr;
    }

    void PushBack(T value) {
        if (size >= capacity) {
            capacity = static_cast<int>(capacity * 1.5);
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

    friend ostream& operator<<(ostream& out, const ArrayList& arrList) {
        for (int i = 0; i < arrList.size; i++) {
            out << arrList[i] << " ";
        }
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

void LoadDataIntoVector(const string& fn, ArrayList<int>& Arraylist) {
    ifstream reader(fn);
    int value;
    while (reader >> value) {
        Arraylist.PushBack(value);
    }
}

int main() {
    string filename = "InputArraylist.txt";
    CreateRandomFile(filename, 2); 

    time_t start = time(0); 

    ArrayList<int> Arraylist;
    LoadDataIntoVector(filename, Arraylist);

    time_t end = time(0); 

    ofstream output("OutputArraylist.txt");
    output << Arraylist; 

    double elapsed = difftime(end, start);
    cout << "Time taken to load data into ArrayList: " << elapsed << " seconds" << endl;

    return 0;
}
