#include <iostream>
#include <vector>
using namespace std;

struct Node {
    string data;
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

    void insertAtHead(string x) {
        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = head;
        head = newNode;
    }

    bool findNode(string x) const {
        Node* currentNode = head;
        while (currentNode != nullptr) {
            if (currentNode->data == x) {
                return true;
            }
            currentNode = currentNode->next;
        }
        return false;
    }
    string DeleteHead()
    {
        if(head==nullptr)
        return "None";
        Node* Next=head->next;
        string valuetodelete=head->data;
        delete head;
        head=Next;
        return valuetodelete;
    }
    bool deleteNode(string x) {
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

class Hashtable
{
    private:
        vector<LinkList>table;
        int tsize;
        int elementscount;
    public:
        Hashtable(int size):tsize(size)
        {
            table.resize(size);
        }
        void ReHash()
        {
            int newsize=tsize*2;
            vector<string>values;
            for(int i=0;i<tsize;i++)
            {
                while(!table[i].isEmpty())
                {
                    values.push_back(table[i].DeleteHead());
                }
            }
            table.clear();
            table.resize(newsize);
            tsize=newsize;
            elementscount=0;
            for(int i=0;i<values.size();i++)
            {
                InsertValue(values[i]);
            }
        }
        int GetAscii(string value) {
        int asciiSum = 0;
        for (int i=0;i<value.length();i++) {
            asciiSum += int(value[i]);
        }
        return asciiSum;
        }
        int HashMap(string value)
        {
            return GetAscii(value)%tsize;
        }
        void InsertValue(string value)
        {
            if((float(elementscount)/float(tsize))>0.75)
            {
                ReHash();
            }
            int index=HashMap(value);
            if(!table[index].findNode(value))
            {
                table[index].insertAtHead(value);
                elementscount++;
            }
        }
        bool SearchValue(string value)
        {
            int index=HashMap(value);
            return table[index].findNode(value);
        }
        bool DeleteValue(string value)
        {
            int index=HashMap(value);
            return table[index].deleteNode(value);
        }
        void DisplayHashtable()
        {
            for(int i=0;i<tsize;i++)
            {
                cout<<"Index[]"<<i<<"]: ";
                table[i].displayList();
            }
        }
};

int main() {
    int size = 7; 
    Hashtable ht(size);
    ht.InsertValue("ABA");
    ht.InsertValue("AAB");
    ht.InsertValue("Cat");
    ht.InsertValue("Dog");
    ht.InsertValue("AMir");
    ht.InsertValue("Hashmi");
    ht.InsertValue("Heavy");

    cout << "Hash Table with Separate Chaining:" << endl;
    ht.DisplayHashtable();

    cout << "\nSearching for value ABA: " << (ht.SearchValue("ABA") ? "Found" : "Not Found") << endl;
    cout << "Searching for value AAB: " << (ht.SearchValue("AAB") ? "Found" : "Not Found") << endl;
    cout << "Searching for value Hashmi: " << (ht.SearchValue("Hashmi") ? "Found" : "Not Found") << endl;
    cout << "Searching for non-existent value Hello: " << (ht.SearchValue("Hello") ? "Found" : "Not Found") << endl;

    cout << "\nRemoving value Dog." << endl;
    ht.DeleteValue("Dog");
    ht.DisplayHashtable();

    return 0;
}