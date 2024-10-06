#include<iostream>
#include<vector>
using namespace std;
void FindValue(vector<int>vec,int value)
{
    bool IsFind=false;
    for(int i=0;i<vec.size();i++)
    {
        if(vec[i]==value)
        {
            cout<<"You Number found at Index: "<<i;
            IsFind=true;
            break;
        }
    }
    if(!IsFind)
    cout<<"Number not Found";
}
int main()
{
    vector<int>vec={5,2,8,11,13,16,19};
    int value=8;
    FindValue(vec,value);
}