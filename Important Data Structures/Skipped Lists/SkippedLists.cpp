#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

struct Node {
    int data;
    Node** next;
    Node(int data, int levels) {
        this->data = data;
        next = new Node*[levels]; 
        for (int i = 0; i < levels; i++) {
            next[i] = nullptr; 
        }
    }
};

class SkippedList {
    float probability;
    int maxLevels;
    Node* head;

public:
    SkippedList(int Value, float probability, int maxlevels) {
        maxLevels = maxlevels;
        this->probability = probability;
        int levels = getRandomLevels(); 
        head = new Node(Value, levels); 
    }

    int getRandomLevels() {
        int levels = 1;
        while (((float)rand() / RAND_MAX) < probability && levels < maxLevels) {
            levels++;
        }
        return levels;
    }

    void Insert(int value) {
        int levels = getRandomLevels(); 
        Node* newNode = new Node(value, levels);

        Node** update = new Node*[levels]; 
        for (int i = 0; i < levels; i++) {
            update[i] = nullptr;
        }

        Node* current = head;
        for (int i = maxLevels - 1; i >= 0; i--) {
            current=head;
            while (current->next[i] && current->next[i]->data < value) {
                current = current->next[i]; 
            }
            if (i < levels) {
                update[i] = current;
            }
        }

        for (int i = 0; i < levels; i++) {
            newNode->next[i] = update[i]->next[i]; 
            update[i]->next[i] = newNode; 
        }

        delete[] update;
    }

    bool Search(int value) {
        Node* current = head;
        for (int i = maxLevels - 1; i >= 0; i--) {
            current=head;
            while (current->next[i] && current->next[i]->data < value) {
                current = current->next[i]; 
            }
            if (current->next[i] && current->next[i]->data == value) {
                return true; 
            }
        }
        return false; 
    }

    void Print() {
        for (int i = maxLevels - 1; i >= 0; i--) {
            Node* current = head;
            cout << "\nLevel " << i << ": ";
            while (current->next[i]) {
                cout << current->next[i]->data << " --> ";
                current = current->next[i];
            }
            cout << "nullptr" << endl;
        }
    }
};

int main() {
    srand(time(0)); 

    SkippedList list(10, 0.5, 3); 

    list.Insert(20);
    list.Insert(30);
    list.Insert(25);

    list.Print();

    cout << "\n";
    cout << "Search 30: " << (list.Search(30) ? "Found" : "Not Found") << endl;
    cout << "Search 15: " << (list.Search(15) ? "Found" : "Not Found") << endl;

    return 0;
}
