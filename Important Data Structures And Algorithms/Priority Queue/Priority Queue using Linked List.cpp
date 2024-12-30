#include<iostream>
using namespace std;
struct Node
{
    string data;
    int priority;
    Node * next;
};
class PriorityQueue
{
    private:
        Node* head;
    public:
        PriorityQueue()
        {
            head=nullptr;
        }
        ~PriorityQueue()
        {
            Node * current=head;
            while (current!=nullptr)
            {
            Node * next=current->next;
            delete current;
            current=next;
            }
            head=nullptr;
        }
        void Enqueue(string x, int priority) {
        Node* newNode = new Node();
        newNode->data = x;
        newNode->priority = priority;
        newNode->next = nullptr;

        if (head == nullptr) {
            head = newNode;
        }
        else if (head->priority < newNode->priority) {
            newNode->next = head;  
            head = newNode;        
        }
        else {
            Node* position = head;
            while (position->next != nullptr && position->next->priority >= newNode->priority) {
                position = position->next;
            }
            newNode->next = position->next;
            position->next = newNode;
        }
        }

        string Dequeue()
        {
            if(IsEmpty())
            {
                return "No elements to Dequeue";
                
            }
            Node * next=head->next;
            string todelete=head->data;
            delete head;
            head=next;
            return  todelete;
            
        }
        string Peek()
        {
            string peekvalue=head->data;
            return peekvalue;
        }

        bool IsEmpty()
        {
            if(head==nullptr){
                return true;}
            return false;
        }
};
int main() {
    PriorityQueue q;
    q.Enqueue("10",3);
    q.Enqueue("Amir",1);
    q.Enqueue("30",3);

    cout << "After Enqueuing 10, Amir, 30:" << endl;
    cout << "Peek: " << q.Peek() << endl;

    cout << "Dequeue: " << q.Dequeue() << endl;
    cout << "Dequeue: " << q.Dequeue() << endl; 
    cout << "Peek after Dequeueing of 2 elements: " << q.Peek() << endl;
    if(q.IsEmpty())
    {
        cout<<"Priority Queue is Empty";
    } 
    else{
        cout<<"Priority Queue is not Empty";
    }
    return 0;
}