#include<iostream>
using namespace std;
class CircularQueue
{
    private:
        string* Array;
        int front;
        int rear;
        int capacity;
    public:
        CircularQueue(int size)
        {
            Array=new string[size];
            front=-1;
            rear=-1;
            capacity=size;
        }
        ~CircularQueue()
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
            if((rear==capacity-1&&front==0)||rear+1==front)
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
                    rear=0;
                }
                else
                {
                    rear=(rear+1)%capacity;
                }
                
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
            if(front==rear)
            {
                front=rear=-1;
            }
            else{
            front=(front+1)%capacity;
            }
            return valuetoremove;
        }
        string Peek()
        {
            return Array[front];
        }
        void DisplayQueue() {
        if (IsEmpty()) {
            cout << "Queue is empty.\n";
            return;
        }
        cout << "Queue: ";
        int i = front;
        while (true) {
            cout << Array[i] << " ";
            if (i == rear) {
                break;
            }
            i = (i + 1) % capacity;
        }
        cout << "\n";
    }
};
int main() {
    CircularQueue q(5);
    q.Enqueue("10");
    q.Enqueue("Amir");
    q.Enqueue("30");
    q.DisplayQueue();

    cout << "Peek: " << q.Peek() << endl;

    cout << "Dequeue: " << q.Dequeue() << endl;
    cout << "Dequeue: " << q.Dequeue() << endl;
    q.DisplayQueue();
    cout << "Peek after Dequeueing 2 elements: " << q.Peek() << endl;

    q.Enqueue("40");
    q.Enqueue("50");
    q.Enqueue("60");
    q.DisplayQueue();
    
    q.Enqueue("70");
    q.DisplayQueue();

    if (q.IsEmpty()) {
        cout << "Queue is Empty\n";
    } else {
        cout << "Queue is not Empty\n";
    }

    if (q.IsFull()) {
        cout << "Queue is Full\n";
    } else {
        cout << "Queue is not Full\n";
    }

    return 0;
}