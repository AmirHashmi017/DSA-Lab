#include<iostream>
#include<vector>
using namespace std;
void DisplayVector(vector<int>vec)
{
    for(int i=0;i<vec.size();i++)
    {
        cout<<vec[i]<<" ";
    }
}
void ReverseVector(vector<int>& vec1)
{
    for(int i=vec1.size()-1;i>=vec1.size()/2;i--)
    {
        int j=vec1.size()-1-i;
        int swap=vec1[j];
        vec1[j]=vec1[i];
        vec1[i]=swap;
    }
}
void AscendingSort(vector<int>& vec2)
{
    for(int i=0;i<vec2.size()-1;i++)
    {
        int min_index=i;
        for(int j=i+1;j<vec2.size();j++)
        {
            if(vec2[j]<vec2[min_index])
            {
                min_index=j;
            }
        }
        int swap=vec2[i];
        vec2[i]=vec2[min_index];
        vec2[min_index]=swap;
    }
}
void RemoveDuplicates(vector<int>& vec)
{
    for(int i=0;i<vec.size()-1;i++)
    {
        for(int j=i+1;j<vec.size();j++)
        {
            if(vec[i]==vec[j])
            {
                vec.erase(vec.begin() + j); 
                break;
            }
        }        
    }
}
int main()
{
    vector<int>vec1={20,10,40,50,20,90,40,70};
    ReverseVector(vec1);
    cout<<" Reversed Vector: ";
    DisplayVector(vec1);
    vector<int>vec2={20,10,40,50,20,90,40,70};
    AscendingSort(vec2);
    cout<<"\n Sorted Vector: ";
    DisplayVector(vec2);
    vector<int>vec3={20,10,40,50,20,90,40,70};
    RemoveDuplicates(vec3);
    cout<<"\n After Removing Duplicates: ";
    DisplayVector(vec3);
}