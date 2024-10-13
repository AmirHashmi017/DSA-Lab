#include<iostream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cctype>
using namespace std;
struct Node
{
    int data;
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
        void Push(int x)
        {
            Node * newNode=new Node();
            newNode->data=x;
            newNode->next=head;
            head=newNode;
        }
        int Pop()
        {
            Node * next=head->next;
            int todelete=head->data;
            delete head;
            head=next;
            return  todelete;
        }
        int Peek()
        {
            return head->data;
        }
        bool IsEmpty()
        {
            if(head==nullptr){
                return true;}
            return false;
        }
        bool PerformBinary()
        {
            if(head!=nullptr&&head->next!=nullptr)
            {
                return true;
            }
            return false;
        }
        void toString()
        {
            cout<<"Stack: ";
            Node * current=head;
            while(current!=nullptr)
            {
                cout<<current->data<<" ";
                current=current->next;
            }
            cout<<"\n";
        }
};

bool EvaluatePostfix(Stack& stack,string expression) {
    istringstream tokens(expression);
    string token;

    while (tokens >> token) {
        if (isdigit(token[0]) || (token[0] == '-' && token.length() > 1)) 
        {
            stack.Push(stoi(token));
        } 
        else {
            if ((token == "+" || token == "-" || token == "*" || token == "/" || token == "%") && stack.PerformBinary()) {
                int operand2 = stack.Pop();
                int operand1 = stack.Pop();
                int result;
                if (token == "+") {
                    result = operand1 + operand2;
                } 
                else if (token == "-") {
                    result = operand1 - operand2;
                } 
                else if (token == "*") {
                    result = operand1 * operand2;
                } 
                else if (token == "/") {
                    if(operand2!=0)
                    result = operand1 / operand2;
                } else if (token == "%") {
                    if (operand2 != 0)
                    result = operand1 % operand2;
                }
                stack.Push(result);
            } 
            else if (token == "?") 
            {
                stack.toString();
            } 
            else if (token == "^"&&(!stack.IsEmpty())) 
            {
                cout<<stack.Pop()<<endl;
            }
            else if (token == "!") 
            {
                return false;
            }  
        }
    }
    return true;
}


int main()
{
    Stack s;
    cout<<"Enter a postfix expression (use space to separate tokens), or type '!' to exit:\n";
    while(true)
    {
        string input;
        cout<<">>";
        getline(cin,input);
        if(!EvaluatePostfix(s,input))
        {
            break;
        }
    }
    return 0;
}