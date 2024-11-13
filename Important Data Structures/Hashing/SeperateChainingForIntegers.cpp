#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class LinkList {
private:
    Node* head;
public:
    LinkList() {
        head = nullptr;
    }
    ~LinkList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
        head = nullptr;
    }

    bool isEmpty() const {
        return head == nullptr;
    }

    void insertAtHead(int x) {
        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = head;
        head = newNode;
    }

    bool findNode(int x) const {
        Node* currentNode = head;
        while (currentNode != nullptr) {
            if (currentNode->data == x) {
                return true;
            }
            currentNode = currentNode->next;
        }
        return false;
    }

    bool deleteNode(int x) {
        if (head == nullptr) return false;
        if (head->data == x) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return true;
        }

        Node* current = head;
        while (current->next != nullptr && current->next->data != x) {
            current = current->next;
        }
        if (current->next == nullptr) return false;

        Node* temp = current->next;
        current->next = temp->next;
        delete temp;
        return true;
    }

    void displayList() const {
        Node* currentNode = head;
        while (currentNode != nullptr) {
            cout << currentNode->data << " --> ";
            currentNode = currentNode->next;
        }
        cout << "Null" << endl;
    }
};

class HashTable {
private:
    vector<LinkList> table;
    int tableSize;

    

public:
    HashTable(int size) : tableSize(size) {
        table.resize(tableSize);
    }
    int hashFunction (int key) const {
        return key % tableSize;
    }
    void insert(int key) {
        int index = hashFunction(key);
        if (!table[index].findNode(key)) {
            table[index].insertAtHead(key);
        }
    }

    bool search(int key) const {
        int index = hashFunction(key);
        return table[index].findNode(key);
    }

    void remove(int key) {
        int index = hashFunction(key);
        table[index].deleteNode(key);
    }

    void displayHashTable() const {
        for (int i = 0; i < tableSize; i++) {
            cout << "Index " << i << ": ";
            table[i].displayList();
        }
    }
};

int main() {
    int size = 7; 
    HashTable ht(size);
    ht.insert(1);
    ht.insert(3);
    ht.insert(5);
    ht.insert(2);
    ht.insert(14);
    ht.insert(19);
    ht.insert(27);

    cout << "Hash Table with Separate Chaining:" << endl;
    ht.displayHashTable();

    cout << "\nSearching for value 5: " << (ht.search(5) ? "Found" : "Not Found") << endl;
    cout << "Searching for value 14: " << (ht.search(14) ? "Found" : "Not Found") << endl;
    cout << "Searching for non-existent value 10: " << (ht.search(10) ? "Found" : "Not Found") << endl;

    cout << "\nRemoving value 14." << endl;
    ht.remove(14);
    ht.displayHashTable();

    return 0;
}
