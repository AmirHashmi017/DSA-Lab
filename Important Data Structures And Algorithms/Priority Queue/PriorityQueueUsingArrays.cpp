#include<iostream>
using namespace std;
struct Element
{
    string data;
    int priority;
};
class PriorityQueue
{
    public:
        Element* Array;
        int capacity;
        int front;
        int rear;

        PriorityQueue(int size)
        {
            Array=new Element[size];
            capacity=size;
            front=-1;
            rear=-1;
        }
        ~PriorityQueue()
        {
            delete[] Array;
        }
        bool IsFull()
        {
            if((rear==capacity-1 && front==0)||rear+1==front)
            {
                return true;
            }
            return false;
        }
        bool IsEmpty()
        {
            if(front==-1)
            {
                return true;
            }
            return false;
        }
        void Enqueue(string value,int priority)
        {
            if(!IsFull())
            {
                Element newelement;
                newelement.data=value;
                newelement.priority=priority;
                if(IsEmpty())
                {
                    front=0;
                    rear=0;
                    Array[rear]=newelement;
                }
                else{
                    int i=rear;
                    rear=(rear+1)%capacity;
                    while(i!=front&&Array[i].priority<priority)
                    {
                        Array[(i+1)%capacity]=Array[i];
                        i=(i-1+capacity)%capacity;
                    }
                    if(i==front&&Array[i].priority<priority)
                    {
                        Array[(i+1)%capacity]=Array[i];
                        i=(i-1+capacity)%capacity;
                    }
                    Array[(i+1)%capacity]=newelement;
                }
            }
        }
        string Dequeue()
        {
            if(IsEmpty())
            {
                return("No Elements available");
            }
            string elementtoremove=Array[front].data;
            if(front==rear)
            {
                front=-1;
                rear=-1;
            }
            else
            {
            front=(front+1)%capacity;
            }
            return elementtoremove;
        }
        string Peek()
        {
            if(IsEmpty())
            {
                return("No Elements available");
            }
            return Array[front].data;
        }
        void DisplayQueue()
        {
            if(IsEmpty())
            {
                cout<<"Circular Queue is Empty";
            }
            else{
            cout<<"Priority Queue: \n";
            int i=front;
            while(true)
            {
                cout<<"Data: "<<Array[i].data<<" , Priority: "<<Array[i].priority<<"     ";
                if(i==rear)
                {
                    break;
                }
                i=(i+1)%capacity;
            }
            }
            cout<<"\n";
        }
};
int main() {
    PriorityQueue pq(5); // Capacity 5

pq.Enqueue("Task A", 3);
pq.Enqueue("Task B", 1);
pq.Enqueue("Task C", 4);
pq.Enqueue("Task D", 2);

pq.DisplayQueue();
cout << "Dequeued: " << pq.Dequeue() << endl;
pq.DisplayQueue();


    // Dequeue and display the highest-priority element
    cout << "Dequeued: " << pq.Dequeue() << endl;

    // Display the updated queue
    pq.DisplayQueue();

    return 0;
}
