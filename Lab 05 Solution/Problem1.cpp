#include<iostream>
#include<vector>
#include <string>
#include<algorithm>
using namespace std;
int main()
{
    vector<string>vec;
    int option;
    string element;
    while(true)
    {
    cout<<" 1. Add Element"<<endl;
    cout<<" 2. Remove Element"<<endl;
    cout<<" 3. Exit"<<endl;
    cout<<" Enter Option Number: ";
    cin>>option;
    if(option==1)
    {
        cout<<"Enter Element you want to Add: ";
        cin.ignore();
        getline(cin,element);
        vec.push_back(element);
        cout<<"Vector Size is: "<<vec.size();
        cout<<"\n Vector Capacity is: "<<vec.capacity()<<endl;
    }
    else if(option==2)
    {
        cout<<"Enter Element you want to remove: ";
        cin.ignore();
        getline(cin,element);
        auto removeindex = find(vec.begin(), vec.end(),element);
        vec.erase(removeindex);
        cout<<"Vector Size is: "<<vec.size();
        cout<<"\n Vector Capacity is: "<<vec.capacity()<<endl;
    }
    else if(option==3)
    {
        break;
    }
    }
    return 0;
}