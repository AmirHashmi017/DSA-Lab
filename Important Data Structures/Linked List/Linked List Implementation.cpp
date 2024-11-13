#include<iostream>
using namespace std;
struct Node
{
    int data;
    Node * next;
};

class LinkList
{
    private:
        Node * head;
    public:
        LinkList()
        {
            head=nullptr;
        }
        ~LinkList()
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
        Node * GetHead()
        {
            return head;
        }
        bool isEmpty()
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
                newNode->next=currentNode->next;
                currentNode->next=newNode;
            }
            return head;
        }
        Node* insertAtHead(int x)
        {
            Node * newNode=new Node();
            newNode->data=x;
            newNode->next=head;
            head=newNode;
            return head;
        }
        Node* insertAtEnd(int x)
        {
            Node * newNode=new Node();
            newNode->data=x;
            newNode->next=nullptr;
            if(head==nullptr)
            {
                head=newNode;
            }
            else{
            Node * lastNode=head;
            while(lastNode->next!=nullptr)
            {
                lastNode=lastNode->next;
            }
            lastNode->next=newNode;
            }
            return head;
        }
        bool findNode(int x)
        {
            Node * currentNode=head;
            while(currentNode!=nullptr)
            {
                if(currentNode->data==x)
                {
                    return true;
                }
                currentNode=currentNode->next;
            }
            return false;
        }
        bool deleteNode(int x)
        {
            if(findNode(x))
            {
                while (head != nullptr && head->data == x) {
                Node* next = head->next;
                delete head;
                head=next;
                }
                if (head == nullptr) {
                    return true;
                }
                Node * nodestodelete=head;
                while(nodestodelete->next!=nullptr)
                {
                    if(nodestodelete->next->data==x)
                    {
                        Node * DeletedNode=nodestodelete->next;
                        nodestodelete->next=DeletedNode->next;
                        delete DeletedNode;

                    }
                    else
                    nodestodelete=nodestodelete->next;
                }
                return true;
            }
            return false;
        }
        bool deleteFromStart()
        {
            if(head==nullptr)
                return false;
            Node * next=head->next;
            delete head;
            head=next;
            return true;
        }
        bool deleteFromEnd()
        {
            if(head==nullptr)
                return false;
            if(head->next==nullptr)
            {
                delete head;
                head=nullptr;
            }
            else{
            Node * NodeToDelete=head;
            while(NodeToDelete->next->next!=nullptr)
            {
                NodeToDelete=NodeToDelete->next;
            }
            delete NodeToDelete->next;
            NodeToDelete->next=nullptr;
            }
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
            Node * previous=nullptr;
            Node * next=nullptr;
            Node * current=head;
            while(current!=nullptr)
            {
                next=current->next;
                current->next=previous;
                previous=current;
                current=next;
            }
            head=previous;
            return head;
        }
        Node* sortList(Node *list)
        {
            for(Node * i=list;i!=nullptr;i=i->next)
            {
                Node * Minnode=i;
                for(Node * j=i->next;j!=nullptr;j=j->next)
                {
                    if(j->data<Minnode->data)
                    {
                        Minnode=j;
                    }
                }
                swap(i->data,Minnode->data);
            }
            return list;
        }
        Node* removeDuplicates(Node *list)
        {
            Node * current=list;
            while(current!=nullptr&&current->next!=nullptr)
            {
            Node * remaining=current;
            while(remaining->next!=nullptr)
            {
                if(current->data==remaining->next->data)
                {
                    Node * nodetoremove=remaining->next;
                    remaining->next=nodetoremove->next;
                    delete nodetoremove;
                }
                else{
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
                return list1;
            } else {
                list2->next = mergeLists(list1, list2->next);
                return list2;
            }
        }
        Node* interestLists(Node *list1, Node *list2)
        {
            LinkList intersection;
            while(list1!=nullptr)
            {
                Node * head=list2;
                Node * innerlist=head;
                while(innerlist!=nullptr)
                {
                    if(list1->data==innerlist->data)
                    {
                        Node * similar=list1;
                        if(!intersection.findNode(similar->data))
                        {
                        intersection.insertAtEnd(similar->data);
                        }
                    }
                    innerlist=innerlist->next;
                }
                list1=list1->next;
            }
            intersection.displayList();
            return intersection.GetHead();
        }
};
int main() {
    LinkList list;
    LinkList list2;
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
    list2.reverseList();
    list2.displayList();
    Node * first=list2.GetHead();
    list2.sortList(first);
    list2.displayList();
    list2.removeDuplicates(first);
    list2.displayList();
    
    Node * list3node=list.mergeLists(list.GetHead(),list2.GetHead());
    while(list3node!=nullptr)
    {
        cout<<list3node->data<<" ";
        list3node=list3node->next;
    }
}

