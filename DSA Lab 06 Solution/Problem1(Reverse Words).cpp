#include<iostream>
using namespace std;
#include<string>
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
void ReverseWords(string sentence)
        {
            Stack s;
            string words="";
            int wordscount=0;
            for(int i=0;i<sentence.length();i++)
            {
                if(sentence[i]==' ')
                {
                    words+=' ';
                    s.Push(words);
                    wordscount++;
                    words="";
                }
                else{
                words+=sentence[i];}
                if(i==sentence.length()-1&& (!words.empty()))
                {
                    words+=' ';
                    s.Push(words);
                    wordscount++;
                }
            }
            
            cout<<"Output: ";
            for(int i=0;i<wordscount;i++)
            {
                cout<<s.Pop();
            }
        }
int main() {
    string input="I am from University of Engineering and Technology Lahore";
    ReverseWords(input);
    return 0;
}