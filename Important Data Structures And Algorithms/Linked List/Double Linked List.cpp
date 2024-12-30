#include<iostream>
using namespace std;
struct Node
{
    int data;
    Node * previous;
    Node * next;
};
class DoubleLinkList
{
    private:
        Node* head;
    public:
        DoubleLinkList()
        {
            head=nullptr;
        }
        ~DoubleLinkList()
        {
            Node * current=head;
            while(current!=nullptr)
            {
                Node* next=current->next;
                delete current;
                current=next;
            }
            head=nullptr;
        }
        Node* GetHead()
        {
            return head;
        }
        bool IsEmpty()
        {
            if(head==nullptr)
            {
                return true;
            }
            return false;
        }
        Node* insertNode(int index, int x)
        {           
            if(index<0)
            {
                return nullptr;
            }
            Node* newNode=new Node();
            newNode->data=x;
            if(index==0)
            {
                newNode->previous=nullptr;
                newNode->next=head;
                head=newNode;
            }
            else{
                Node * currentNode=head;
                for(int i=0;i<index-1&&currentNode!=nullptr;i++)
                {
                    currentNode=currentNode->next;
                }
                if(currentNode==nullptr)
                return nullptr;
                newNode->previous=currentNode;
                newNode->next=currentNode->next;
                newNode->next->previous=newNode;
                currentNode->next=newNode;
            }
            return head;
        }
        Node* insertAtHead(int x)
        {
            Node* newnode=new Node();
            newnode->data=x;
            newnode->previous=nullptr;
            newnode->next=head;
            head=newnode;
            return head;
        }
        Node* insertAtEnd(int x)
        {
            Node* newnode=new Node();
            newnode->data=x;
            if(head==nullptr)
            {
            newnode->previous=nullptr;
            newnode->next=head;
            head=newnode;
            }
            else{
            Node* last=head;
            while(last->next!=nullptr)
            {
                last=last->next;
            }
            newnode->previous=last;
            last->next=newnode;
            newnode->next=nullptr;
            }
            return head;
        }
        bool findNode(int x)
        {
            Node* current=head;
            while(current!=nullptr)
            {
                if(current->data==x)
                {
                    return true;
                }
                current=current->next;
            }
            return false;
        }
        bool deleteNode(int x)
        {
            while (head != nullptr && head->data == x) {
                Node* next = head->next;
                delete head;
                
                if (next != nullptr) {
                    next->previous = nullptr;
                }
                head = next;
            }

            if (head == nullptr) {
                return true;
            }
            Node* current=head;
            while (current != nullptr && current->next != nullptr) {
                if (current->next->data == x) {
                    Node* nodeToRemove = current->next;
                    current->next = nodeToRemove->next;
                    if (nodeToRemove->next != nullptr) {
                        nodeToRemove->next->previous = current;
                    }
                    delete nodeToRemove;
                } else {
                    current = current->next;
                }
            }

            return true;
        }
        bool deleteFromStart()
        {
            if(head==nullptr)
            {
                return false;
            }
            Node* next=head->next;
            next->previous=nullptr;
            delete head;
            head=next;
        }
        bool deleteFromEnd()
        {
            if(head==nullptr)
            {
                return false;
            }
            else if(head->next==nullptr)
            {
            delete head;
            head=nullptr;
            return true;
            }
            Node* last=head;
            while(last->next!=nullptr)
            {
                last=last->next;
            }
            last->previous->next=nullptr;
            delete last;
            return true;
            
        }
        void displayList()
        {
            Node * currentNode=head;
            cout<<"Linked List: ";
            while(currentNode!=nullptr)
            {
                cout<<currentNode->data<<"--->";
                currentNode=currentNode->next;
            }
            cout<<"Null"<<endl;
        }
        Node* reverseList()
        {
            Node * current=head;
            while(current!=nullptr)
            {
                Node* next=current->next;
                current->next=current->previous;
                current->previous=next;
                if(next==nullptr)
                {
                    head=current;
                }
                current=next;
            }
            return head;
        }
        Node* sortList(Node *list)
        {
            for(Node* i=list;i->next!=nullptr;i=i->next)
            {
                Node* minNode=i;
                for(Node* j=i->next;j!=nullptr;j=j->next)
                {
                    if(j->data<minNode->data)
                    {
                        minNode=j;
                    }
                }
                swap(i->data,minNode->data);
            }
            return list;
        }
        Node* removeDuplicates(Node *list)
        {
            Node* current=list;
            while(current!=nullptr&&current->next!=nullptr)
            {
                Node* remaining=current;
                while(remaining->next!=nullptr)
                {
                    if(current->data==remaining->next->data)
                    {
                        Node* nodetoremove=remaining->next;
                        remaining->next=nodetoremove->next;
                        if(nodetoremove->next!=nullptr)
                        {
                            nodetoremove->next->previous=remaining;
                        }
                        delete nodetoremove;
                    }
                    else
                    {
                        remaining=remaining->next;
                    }
                }
                current=current->next;
            }
            return list;
        }
        Node* mergeLists(Node* list1, Node* list2) {
        if (!list1) return list2;
        if (!list2) return list1;

        if (list1->data < list2->data) {
            list1->next = mergeLists(list1->next, list2);
            if (list1->next != nullptr) {
                    list1->next->previous = list1;
                }
                return list1;
            } else {
                list2->next = mergeLists(list1, list2->next);
                if (list2->next != nullptr) {
                    list2->next->previous = list2;
                }
                return list2;
            }
        }

        Node* interestLists(Node *list1, Node *list2)
        {
            DoubleLinkList intersection;
            Node* first=list1;
            Node*second;
            while(first!=nullptr)
            {
                second=list2;
                while(second!=nullptr)
                {
                    if(first->data==second->data)
                    {
                        if(!intersection.findNode(first->data))
                        {
                            intersection.insertAtEnd(first->data);
                        }
                    }
                    second=second->next;
                }
                first=first->next;
            }
            intersection.displayList();
            return intersection.GetHead();
        }

};
int main()
{
    DoubleLinkList list;
    DoubleLinkList list2;
    list.insertAtEnd(10);
    list.insertAtEnd(30);
    list.insertAtEnd(20);
    list.insertAtHead(30);
    list.insertAtHead(5);
    list.insertAtEnd(30);
    list.insertAtEnd(30);
    list.insertNode(3,3);
    list.displayList();
    list.deleteFromStart();
    list.displayList();
    list.deleteFromEnd();
    list.displayList();
    list.deleteNode(30);
    list.displayList();
    cout<<list.findNode(20)<<endl;
    cout<<list.findNode(2)<<endl;
    list2.insertAtEnd(3);
    list2.insertAtEnd(5);
    list2.insertAtEnd(7);
    list2.insertAtEnd(3);
    list2.insertAtEnd(7);
    list2.insertAtEnd(7);
    list2.displayList();
    Node * first=list2.GetHead();
    list2.sortList(first);
    list2.displayList();
    list2.removeDuplicates(first);
    list2.displayList();
    list2.reverseList();
    list2.displayList();
    Node * list3node=list.mergeLists(list.GetHead(),list2.GetHead());
    while(list3node!=nullptr)
    {
        cout<<list3node->data<<" ";
        list3node=list3node->next;
    }
}