#include<iostream>
using namespace std;
struct Node
{
    int data;
    Node * previous;
    Node * next;
};
class CircularDoubleLinkList
{
    private:
        Node* head;
    public:
        CircularDoubleLinkList()
        {
            head=nullptr;
        }
        ~CircularDoubleLinkList()
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
            if(head==nullptr)
            {
                newNode->previous=newNode;
                newNode->next=newNode;
                head=newNode;
            }
            if(index==0)
            {
                Node* Tail=head->previous;
                newNode->previous=Tail;
                newNode->next=head;
                Tail->next=newNode;
                head=newNode;
            }
            else{
                Node * currentNode=head;
                for(int i=0;i<index-1&&currentNode->next!=head;i++)
                {
                    currentNode=currentNode->next;
                }
                if(currentNode->next==head)
                {
                    currentNode->next=newNode;
                    newNode->previous=currentNode;
                    newNode->next=head;
                    head->previous=newNode;
                }
                else{
                newNode->previous=currentNode;
                newNode->next=currentNode->next;
                newNode->next->previous=newNode;
                currentNode->next=newNode;
                }
            }
            return head;
        }
        Node* insertAtHead(int x)
        {
            Node* newnode=new Node();
            newnode->data=x;
            if(head==nullptr)
            {
                newnode->next=newnode;
                newnode->previous=newnode;
                head=newnode;
            }
            else{
                 Node * tail=head->previous;
                 newnode->next=head;
                 newnode->previous=tail;
                 tail->next=newnode;
                 head=newnode;
            }
            
            return head;
        }
        Node* insertAtEnd(int x)
        {
            Node* newnode=new Node();
            newnode->data=x;
            if(head==nullptr)
            {
            newnode->previous=newnode;
            newnode->next=newnode;
            head=newnode;
            }
            else{
            Node* Tail=head->previous;
            newnode->previous=Tail;
            newnode->next=head;
            Tail->next=newnode;
            head->previous=newnode;
            }
            return head;
        }
        bool findNode(int x)
        {
            if(head==nullptr)
            {
                return false;
            }
            Node* current=head;
            do
            {
                if(current->data==x)
                {
                    return true;
                }
                current=current->next;
            }
            while(current->next!=head);
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
            Node * tail=head->previous;
            next->previous=tail;
            tail->next=next;
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
            Node*tail=head->previous;
            tail->previous->next=head;
            head->previous=tail->previous;
            delete tail;
            return true;
            
        }
       void displayList()
        {
            if (head == nullptr) {
                cout << "Linked List is empty" << endl;
                return;
            }

            cout << "Linked List: ";
            Node* currentNode = head;

            do {
                cout << currentNode->data << " ---> ";
                currentNode = currentNode->next;
            } while (currentNode != head);

            cout << "Back to Head" << endl; 
        }

        Node* reverseList()
        {
            Node * current=head;
            while(current->next!=nullptr)
            {
                current=current->next;
            }
            head=current;
            while(current!=nullptr)
            {
                Node* next=current->previous;
                current->previous=current->next;
                current->next=next;
                current=current->next;
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
            CircularDoubleLinkList intersection;
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
    CircularDoubleLinkList list;
    CircularDoubleLinkList list2;
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