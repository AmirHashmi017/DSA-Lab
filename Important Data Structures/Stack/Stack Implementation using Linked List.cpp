#include<iostream>
using namespace std;
struct Node
{
    string data;
    Node * next;
};
class Stack
{
    private:
        Node* head;
    public:
        Stack()
        {
            head=nullptr;
        }
        ~Stack()
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
        void Push(string x)
        {
            Node * newNode=new Node();
            newNode->data=x;
            newNode->next=head;
            head=newNode;
        }
        string Pop()
        {
            if(IsEmpty())
            {
                return "No elements to pop";
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
    Stack s;
    s.Push("10");
    s.Push("Amir");
    s.Push("30");

    cout << "After pushing 10, Amir, 30:" << endl;
    cout << "Peek: " << s.Peek() << endl;

    cout << "Pop: " << s.Pop() << endl;
    cout << "Pop: " << s.Pop() << endl; 
    cout << "Peek after pop of 2 elements: " << s.Peek() << endl; 
    return 0;
}