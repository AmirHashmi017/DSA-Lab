#include<iostream>
using namespace std;
class Stack
{
    private:
        string* Array;
        int top;
        int capacity;
    public:
        Stack(int size)
        {
            Array=new string[size];
            top=-1;
            capacity=size;
        }
        ~Stack()
        {
            delete[] Array;
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
            if(top>=capacity-1)
            {
                return true;
            }
            return false;
        }
        void Push(string value)
        {
            if(IsFull())
            {
                cout<<"Cannot Push Element.The Stack is Full";
            }
            else{
                top++;
                Array[top]=value;
            }
        }
        string Pop()
        {
            if(IsEmpty())
            {
                return "Stack is empty.Cannot Pop";
            }
            string valuetoremove=Array[top];
            top--;
            return valuetoremove;
        }
        string Peek()
        {
            return Array[top];
        }
        void DisplayStack()
        {
            if(IsEmpty())
            {
                cout<<"No elements available"<<endl;
            }
            else{
            cout<<"stack: ";
            for(int i=0;i<=top;i++)
            {
                cout<<Array[i]<<" ";
            }
            cout<<"\n";
            }
        }
        int GetTotalElements()
        {
            return top+1;
        }
};
class Stueue
{
    public:
        Stack original;
        Stack stack1;
        Stack stack2;
        Stueue(int size):original(size),stack1(size),stack2(size)
        {   
            DevideElements();    
        }
        void DevideElements()
        {
            int mid=int(original.GetTotalElements()/2);
            for(int i=0;i<mid;i++)
            {
                stack1.Push(original.Pop());
            }
            while(!stack1.IsEmpty())
            {
                stack2.Push(stack1.Pop());
            }
            while(!original.IsEmpty())
            {
                stack1.Push(original.Pop());
            }
        }
        void Regain()
        {
            if(stack1.IsEmpty()||stack2.IsEmpty())
            {
                GatherElements();
                DevideElements();
            }
        }
        void GatherElements()
        {
            while(!stack1.IsEmpty())
            {
                original.Push(stack1.Pop());
            }
            while(!stack2.IsEmpty())
            {
                stack1.Push(stack2.Pop());
            }
            while(!stack1.IsEmpty())
            {
                original.Push(stack1.Pop());
            }
        }
        void Push(string value)
        {
            Regain();
            stack2.Push(value);
        }
        void Enqueue(string value)
        {
            Regain();
            stack2.Push(value);
        }
        string Pop()
        {
            Regain();
            return stack2.Pop();
        }
        string Dequeue()
        {
            Regain();
            return stack1.Pop();
        }
        void DisplayStueue()
        {
            GatherElements();
            original.DisplayStack();
        }
};

int main()
{
    Stueue stu(10);
    stu.Push("23");
    stu.DisplayStueue();
    cout<<"After first Dequeue: "<<stu.Dequeue()<<"\n";
    stu.DisplayStueue();
    stu.Push("29");
    stu.Enqueue("22");
    stu.Push("40");
    cout<<"Dequeue: "<<stu.Dequeue()<<"\n";
    cout<<"Pop: "<<stu.Pop()<<"\n";
    stu.DisplayStueue();
}