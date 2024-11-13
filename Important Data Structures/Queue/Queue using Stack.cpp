#include<iostream>
using namespace std;
class Stack
{
    public:
        string* Array;
        int capacity;
        int top;
        Stack(int size)
        {
            Array=new string[size];
            capacity=size;
            top=-1;
        }
        bool IsEmpty()
        {
            if(top==-1)
            {
                return true;
            }
            return false;
        }
        bool IsFull()
        {
            if(top==capacity-1)
            {
                return true;
            }
            return false;
        }
        void Push(string value)
        {
            if(!IsFull())
            {
                top++;
                Array[top]=value;
            }
            else{
                cout<<"Stack is Full";
            }
        }
        string Pop()
        {
            if(!IsEmpty())
            {
                string valuetodelete=Array[top];
                top--;
                return valuetodelete;
            }
            return "No Elements Available";
        }
        string Peek()
        {
            if(!IsEmpty())
            {
                return Array[top];
            }
           return "No Elements Available";
        }
        void DisplayStack()
        {
            cout<<"Stack: ";
            for(int i=0;i<=top;i++)
            {
                cout<<Array[i]<<" ";
            }
        }
};

class QueueUsingStack {
    private:
        Stack stack1;
        Stack stack2;

    public:
        QueueUsingStack(int size):stack1(size),stack2(size) 
        {}
        void Enqueue(string value)
        {
            stack1.Push(value);
        }
        string Dequeue()
        {
            if(stack2.IsEmpty())
            {
                while(!stack1.IsEmpty())
                {
                    stack2.Push(stack1.Pop());
                }
            }
            return stack2.Pop();
        }
        string Peek()
        {
            if(stack2.IsEmpty())
            {
                while(!stack1.IsEmpty())
                {
                    stack2.Push(stack1.Pop());
                }
            }
            return stack2.Peek();
        }
};

int main() {
    QueueUsingStack queue(8);

    queue.Enqueue("1");
    queue.Enqueue("2");
    queue.Enqueue("3");

    cout << "Front Element after enqueuing 1, 2, 3: " << queue.Dequeue() << endl; 

    cout << "Dequeued: " << queue.Dequeue() << endl; 
    cout << "Dequeued: " << queue.Dequeue() << endl; 

    cout << "Dequeued: " << queue.Dequeue() << endl; 
    
    return 0;
}

