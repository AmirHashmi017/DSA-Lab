#include<iostream>
using namespace std;
class Queue
{
    private:
        string* Array;
        int front;
        int rear;
        int capacity;
    public:
        Queue(int size)
        {
            Array=new string[size];
            front=-1;
            rear=-1;
            capacity=size;
        }
        ~Queue()
        {
            delete[] Array;
        }
        bool IsEmpty()
        {
            if(front==-1)
            {
                return true;
            }
            return false;
        }
        bool IsFull()
        {
            if(rear>=capacity-1)
            {
                return true;
            }
            return false;
        }
        void Enqueue(string value)
        {
            if(IsFull())
            {
                cout<<"Cannot Enqueue Element.The Queue is Full";
            }
            else{
                if(IsEmpty())
                {
                    front=0;
                }
                rear++;
                Array[rear]=value;
            }
        }
        string Dequeue()
        {
            if(IsEmpty())
            {
                return "Queue is empty.Cannot Dequeue";
            }
            string valuetoremove=Array[front];
            front++;
            return valuetoremove;
        }
        string Peek()
        {
            return Array[front];
        }
};
int main()
{
    Queue q(5);
    q.Enqueue("10");
    q.Enqueue("Amir");
    q.Enqueue("30");

    cout << "After Enqueuing 10, Amir, 30:" << endl;
    cout << "Peek: " << q.Peek() << endl;

    cout << "Dequeue: " << q.Dequeue() << endl;
    cout << "Dequeue: " << q.Dequeue() << endl; 
    cout << "Peek after Dequeueing of 2 elements: " << q.Peek() << endl;
    if(q.IsEmpty())
    {
        cout<<"Queue is Empty";
    } 
    else{
        cout<<"Queue is not Empty";
    }
    if(q.IsFull())
    {
        cout<<"\nQueue is Full";
    } 
    else{
        cout<<"\nQueue is not Full";
    }
    return 0;
}