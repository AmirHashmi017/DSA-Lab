#include<iostream>
using namespace std;
struct Node
{
    string data;
    Node* next;
    Node* previous;
};

class CircularLinkedList
{
    private:
        Node* head;
    public:
        CircularLinkedList()
        {
            head=nullptr;
        }
        ~CircularLinkedList()
        {
           if(head!=nullptr)
           {
            Node* current=head;
            while(current->next!=head)
            {
                Node* next=current->next;
                delete current;
                current=next;
            }
            delete current;
            head=nullptr;
           }
        }
        Node* GetHead()
        {
            return head;
        }
        void InsertAtHead(string value)
        {
            Node* newnode=new Node();
            newnode->data=value;
            if(head==nullptr)
            {
                newnode->previous=newnode;
                newnode->next=newnode;
                head=newnode;
            }
            else{
            Node* Tail=head->previous;
            newnode->next=head;
            newnode->previous=Tail;
            Tail->next=newnode;
            head->previous=newnode;
            head=newnode;
            } 
        }
        void InsertAtEnd(string value)
        {
            Node* newnode=new Node();
            newnode->data=value;
            if(head==nullptr)
            {
                newnode->next=newnode;
                newnode->previous=newnode;
                head=newnode;
            }
            else
            {
            Node* tail=head->previous;
            tail->next=newnode;
            newnode->previous=tail;
            newnode->next=head;
            head->previous=newnode;
        }
        }
        void InsertNode(string value,int index)
        {
            if(index==0)
            {
                InsertAtHead(value);
            }
            else if(head==nullptr&&index>0)
            {
                cout<<"Can't Insert";
            }
            else{
                Node* current=head;
                int i=0;
                while(current->next!=head&&i<index-1)
                {
                    current=current->next;
                    i++;
                }
                if(current->next==head && i==index-1)
                {
                    InsertAtEnd(value);
                }
                else if(i==index-1){
                    Node* newnode=new Node();
                    newnode->data=value;
                    newnode->next=current->next;
                    newnode->previous=current;
                    current->next->previous=newnode;
                    current->next=newnode;
                }
                else{
                    cout<<"Index out of Bounds of array"<<endl;
                }
            }
        }
        Node* DeleteAtHead()
        {
            if(head==nullptr)
            {
                cout<<"Circular Linked List is Empty.\n";
            }
            else if(head->next==head)
            {
                delete head;
                head=nullptr;
            }
            else{
            Node* Next=head->next;
            Node* Tail=head->previous;
            Next->previous=Tail;
            Tail->next=Next;
            delete head;
            head=Next;
            }
            return head;       
        }
        Node* DeleteAtEnd()
        {
            if(head==nullptr)
            {
                cout<<"Circular Linked List is Empty.\n";
            }
            else if(head->next==head)
            {
                delete head;
                head=nullptr;
            }
            else{
                Node* Tail=head->previous;
                Node* newcurrent=Tail->previous;
                newcurrent->next=head;
                head->previous=newcurrent;
                delete Tail;
            }
            return head;
        }
        Node* DeleteAtMiddle()
        {
            int mid=int(FindNumberOfElementsinList()/2);
            if(head==nullptr)
            {
                cout<<"No elements in list";
            }
            if(mid==0)
            {
                DeleteAtHead();
            }
            else{
                Node* current=head;
                int i=0;
                while(i<mid)
                {
                    current=current->next;
                    i++;
                }
                    current->previous->next=current->next;
                    current->next->previous=current->previous;
                    delete current;
            }
            return head;
        }
        int FindNumberOfElementsinList()
        {
            int count=0;
            if(head==nullptr)
            {
                return count;
            }
            Node* current=head;
            while(current->next!=head)
            {
                current=current->next;
                count++;
            }
            count++;
            return count;
        }
        bool FindNode(string value)
        {
            if(head==nullptr)
            {
                return false;
            }
            Node* current=head;
            do
            {
                if(current->data==value)
                {
                    return true;
                }
            } while (current!=head);
            return false;
            
        }
        bool DeleteNode(string value)
        {
            if(head==nullptr)
            {
                return false;
            }
            Node* current=head;
            do
            {
                if(current->data==value)
                {
                    if(current==head)
                    {
                        DeleteAtHead();
                    }
                    else if(current->next==head)
                    {
                        DeleteAtEnd();
                    }
                    else{
                        current->previous->next=current->next;
                        current->next->previous=current->previous;
                        delete current;
                    }
                    return true;
                }
                current=current->next;
            } while (current!=head);
            return false;
        }
        void DisplayList()
        {
            cout<<"\nCircular Linked List: ";
            Node* current=head;
            do
            {
                cout<<current->data<<"-->";
                current=current->next;
            }while (current!=head);
            cout<<"Repeat-->"<<current->data;
            
        }
        void DisplayList2(Node* list1)
        {
            cout<<"\nCircular Linked List: ";
            Node* current=list1;
            do
            {
                cout<<current->data<<"-->";
                current=current->next;
            }while (current!=list1);
            cout<<"Repeat-->"<<current->data;
            
        }
        void Sort()
        {
            for(Node* i=head;i->next!=head;i=i->next)
            {
                Node* minindex=i;
                for(Node* j=i->next;j!=head;j=j->next)
                {
                    if(j->data<minindex->data)
                    {
                        minindex=j;
                    }
                }
                swap(i->data,minindex->data);
            }
        }
        Node* MergeLists(Node* list1,Node* list2)
        {
            if(!list1)
            {
                return list2;
            }
            if(!list2)
            {
                return list1;
            }
            Node* head=nullptr;
            if(list1->data<list2->data)
            {
                head=list1;
                head->next=MergeLists(list1->next,list2);
                if(head->next!=nullptr)
                {
                    head->next->previous=head;
                }
            }
            else{
                head=list2;
                head->next=MergeLists(list1,list2->next);
                if(head->next!=nullptr)
                {
                    head->next->previous=head;
                }
            }
            Node* tail=head;
            while(tail->next!=nullptr)
            {
                tail=tail->next;
            }
            tail->next=head;
            head->previous=tail;
            DisplayList2(head);
            return head;
        }
        Node* ReverseList()
        {
            Node* current=head;
            do
            {
                Node* next=current->next;
                current->next=current->previous;
                current->previous=next;
                current=next;
            }
            while(current!=head);
            head=current->next;

            return head;
        }
};

int main()
{
    CircularLinkedList list;
    list.InsertAtHead("A");
    list.InsertAtEnd("B");
    
    list.DisplayList();
    list.InsertAtEnd("HOO");
    list.InsertNode("C",2);
    list.DisplayList();
    list.InsertAtHead("D");
    list.InsertAtHead("E");
    list.DisplayList();
    list.ReverseList();
    list.DisplayList();
    list.Sort();
    list.DisplayList();
    cout<<"\n"<<list.FindNode("E");
    list.DeleteNode("E");
    list.DisplayList();
    list.DeleteAtMiddle();
    list.DisplayList();
    list.DeleteAtHead();
    list.DisplayList();
    list.DeleteAtEnd();
    list.DisplayList();
    CircularLinkedList list2;
    list2.InsertAtHead("A");
    list2.InsertAtEnd("D");
    list2.InsertAtEnd("M");
    list2.InsertAtEnd("N");
    list2.DisplayList();
    list.MergeLists(list.GetHead(),list2.GetHead());
    
}