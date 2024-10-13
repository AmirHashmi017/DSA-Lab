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
};
int main()
{
    Stack s(5);
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