#include<iostream>
using namespace std;
class CircularQueue
{
    public:
        string* Array;
        int capacity;
        int front;
        int rear;

        CircularQueue(int size)
        {
            Array=new string[size];
            capacity=size;
            front=-1;
            rear=-1;
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
        void Enqueue(string value)
        { 
            if(!IsFull())
            {
                if(IsEmpty())
                {
                    front=0;
                    rear=0;
                    Array[rear]=value;
                }
                else{
                    rear=(rear+1)%capacity;
                    Array[rear]=value;
                }
            }
        }
        string Dequeue()
        {
            if(IsEmpty())
            {
                return("No Elements available");
            }
            string elementtoremove=Array[front];
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
            return Array[front];
        }
        void DisplayCircularQueue()
        {
            if(IsEmpty())
            {
                cout<<"Circular Queue is Empty";
            }
            else{
            // cout<<"Circular Queue: ";
            int i=front;
            while(true)
            {
                cout<<Array[i]<<" ";
                if(i==rear)
                {
                    break;
                }
                i=(i+1)%capacity;
            }
            }

        }
};

class StackUsingQueue
{
    public:
        CircularQueue queue1;
        CircularQueue queue2;
        StackUsingQueue(int size):queue1(size),queue2(size)
        {}
        void Push(string value)
        {
            queue2.Enqueue(value);
            while(!queue1.IsEmpty())
            {
                queue2.Enqueue(queue1.Dequeue());
            }
            CircularQueue swap=queue1;
            queue1=queue2;
            queue2=swap;
        }
        string Pop()
        {
            return queue1.Dequeue();
        }
        string Peek()
        {
            return queue1.Peek();
        }
        void DisplayStack()
        {
            cout<<"Stack: ";
            queue1.DisplayCircularQueue();
        }
};

int main() {
    StackUsingQueue stack(8);

    stack.Push("A");
    stack.Push("B");
    stack.Push("C");
    stack.DisplayStack();
    cout << "Top Element after pushing A, B, C: " << stack.Peek() << endl;  // Should return C
    
    // Pop and display elements
    cout << "Popped: " << stack.Pop() << endl;  // Should return C
    cout << "Popped: " << stack.Pop() << endl;  // Should return B
    cout << "Popped: " << stack.Pop() << endl;  // Should return A
    
    // Try to pop from empty stack
    cout << "Popped: " << stack.Pop() << endl;  // Should indicate the stack is empty
    
    return 0;
}