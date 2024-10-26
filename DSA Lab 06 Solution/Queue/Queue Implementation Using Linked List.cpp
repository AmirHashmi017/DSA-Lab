#include<iostream>
using namespace std;
struct Node
{
    string data;
    Node * next;
};
class Queue
{
    private:
        Node* head;
        Node* tail;
    public:
        Queue()
        {
            head=nullptr;
            tail=nullptr;
        }
        ~Queue()
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
        void Enqueue(string x)
        {
            Node * newNode=new Node();
            newNode->data=x;
            if(head==nullptr)
            {
            newNode->next=head;
            head=newNode;
            tail=newNode;
            }
            else{
                newNode->next=nullptr;
                tail->next=newNode;
                tail=newNode;
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
            return head->data;
        }

        bool IsEmpty()
        {
            if(head==nullptr){
                return true;}
            return false;
        }
};
int main() {
    Queue q;
    q.Enqueue("10");
    q.Enqueue("Amir");
    q.Enqueue("30");

    cout << "After Enqueuing 10, Amir, 30:" << endl;
    cout << "Peek: " << q.Peek() << endl;

    cout << "Dequeue: " << q.Dequeue() << endl;
    cout << "Dequeue: " << q.Dequeue() << endl; 
    cout << "Peek after Dequeueing of 2 elements: " << q.Peek() << endl;
    q.Enqueue("Amir");
    cout << "Peek after Dequeueing of 2 elements: " << q.Peek() << endl;
    q.Dequeue();
    cout << "Peek after Dequeueing of 2 elements: " << q.Peek() << endl;
    if(q.IsEmpty())
    {
        cout<<"Queue is Empty";
    } 
    else{
        cout<<"Queue is not Empty";
    }
    return 0;
}