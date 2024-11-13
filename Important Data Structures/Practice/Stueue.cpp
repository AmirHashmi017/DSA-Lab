#include<iostream>
using namespace std;
// class Stack
// {
//     public:
//         string * Array;
//         int top;
//         int capacity;
//         Stack(int size)
//         {
//             Array=new string[size];
//             top=-1;
//             capacity=-1;
//         }
//         bool IsEmpty()
//         {
//             if(top==-1)
//             {
//             return true;
//             }
//             return false;
//         }
//         bool IsFull()
//         {
//             if(top==capacity-1)
//             {
//             return true;
//             }
//             return false;
//         }
//         void Push(string newvalue)
//         {
//             if(!IsFull())
//             {
//             top++;
//             Array[top]=newvalue;
//             }
//             else{
//                 cout<<"Stack is Full";
//             }    
//         }
//         string Pop()
//         {
//             if(!IsEmpty())
//             {
//             string valuetodelete=Array[top];
//             top--;
//             return valuetodelete;
//             }
//             else{
//                 return"Stack is Empty";
//             }    
//         }
//         string Peek()
//          {
//             if(!IsEmpty())
//             {
//             return Array[top];
//             }
//             else{
//                 return"Stack is Empty";
//             }    
//         }
//         void Display()
//         {
//             cout<<"Stack: ";
//             for (int i=0;i<=top;i++)
//             {
//                 cout<<Array[i]<<" ";
//             }
//         }
// };
// class CircularQueue
// {
//     public:
//         string * Array;
//         int front;
//         int rear;
//         int capacity;
//         CircularQueue(int size)
//         {
//             Array=new string[size];
//             front=-1;
//             rear=-1;
//             capacity=-1;
//         }
//         bool IsEmpty()
//         {
//             if(front==-1)
//             {
//             return true;
//             }
//             return false;
//         }
//         bool IsFull()
//         {
//             if((rear==capacity-1&&front==0)||(rear==front-1))
//             {
//             return true;
//             }
//             return false;
//         }
//         void Enqueue(string newvalue)
//         {
//             if(!IsFull())
//             {
//             if(IsEmpty())
//             {
//             front=0;
//             rear=0;
//             }
//             else{
//                 rear=(rear+1)%capacity;
//             }
//             Array[rear]=newvalue;
//             }
//             else{
//                 cout<<"Queue is Full";
//             }    
//         }
//         string Dequeue()
//         {
//             if(!IsEmpty())
//             {
//             string valuetodelete=Array[front];
//             if(front==rear)
//             {
//                 front=-1;
//                 rear=-1;
//             }
//             else{
//                 front=(front+1)%capacity;
//             }
//             return valuetodelete;
//             }
//             else{
//                 return"Queue is Empty";
//             }    
//         }
//         string Peek()
//          {
//             if(!IsEmpty())
//             {
//             return Array[front];
//             }
//             else{
//                 return"Queue is Empty";
//             }    
//         }
//         void Display()
//         {
//             int i=front;
//             while(true)
//             {
//                 cout<<Array[i]<<" ";
//                 if(i==rear)
//                 {
//                     break;
//                 }
//                 i=(i+1)%capacity;
//             }
//         }
// };

struct Element
{
    string value;
    int priority;
};
class PriorityQueue
{
    public:
        Element * Array;
        int front;
        int rear;
        int capacity;
        PriorityQueue(int size)
        {
            Array=new Element[size];
            front=-1;
            rear=-1;
            capacity=size;
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
            if((rear==capacity-1&&front==0)||(rear==front-1))
            {
            return true;
            }
            return false;
        }
        void Enqueue(string newvalue,int Priority)
        {
            if(!IsFull())
            {
            Element newelement;
            newelement.value=newvalue;
            newelement.priority=Priority;
            if(IsEmpty())
            {
            front=0;
            rear=0;
            Array[rear]=newelement;
            }
            else{
                int i=rear;
                rear=(rear+1)%capacity;
                while(i!=front&&Array[i].priority<Priority)
                {
                    Array[(i+1)%capacity]=Array[i];
                    i=(i-1+capacity)%capacity;
                }
                if(i==front && Array[i].priority<Priority)
                {
                    Array[(i+1)%capacity]=Array[i];
                    i=(i-1+capacity)%capacity;
                }
                Array[(i+1)%capacity]=newelement;
            }
            
            }
            else{
                cout<<"Queue is Full";
            }    
        }
        string Dequeue()
        {
            if(!IsEmpty())
            {
            string valuetodelete=Array[front].value;
            if(front==rear)
            {
                front=-1;
                rear=-1;
            }
            else{
                front=(front+1)%capacity;
            }
            return valuetodelete;
            }
            else{
                return"Queue is Empty";
            }    
        }
        string Peek()
         {
            if(!IsEmpty())
            {
            return Array[front].value;
            }
            else{
                return"Queue is Empty";
            }    
        }
        void Display()
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
                cout<<"Data: "<<Array[i].value<<" , Priority: "<<Array[i].priority<<"     ";
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

pq.Display();
cout << "Dequeued: " << pq.Dequeue() << endl;
pq.Display();


    // Dequeue and display the highest-priority element
    cout << "Dequeued: " << pq.Dequeue() << endl;

    // Display the updated queue
    pq.Display();

    return 0;
}