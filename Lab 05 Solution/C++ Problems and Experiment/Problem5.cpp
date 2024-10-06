#include<iostream>
#include<vector>
using namespace std;
void DisplayMatrix(vector<vector<int>>matrix)
{
    for(int i=0;i<matrix.size();i++)
    {
        for(int j=0;j<matrix[i].size();j++)
        {
            cout<<matrix[i][j]<<" ";
        }
        cout<<"\n";
    }
}
void AddRow(vector<vector<int>>& matrix,vector<int>row)
{
    matrix.push_back(row);
}
void AddColumn(vector<vector<int>>& matrix,vector<int>column)
{
    if(matrix.size()==column.size())
    {
        for(int i=0;i<matrix.size();i++)
        {
            matrix[i].push_back(column[i]);
        }
        cout<<"\nMatrix After adding Column"<<endl;
    }
    else
    cout<<"Column Size is greater.Column can't be added."<<endl;
}
vector<vector<int>> MatrixTranspose(vector<vector<int>>matrix)
{
    vector<vector<int>>transposed_matrix=matrix;
    for(int i=0;i<matrix.size();i++)
    {
        for(int j=0;j<matrix[i].size();j++)
        {
            transposed_matrix[i][j]=matrix[j][i];
        }
    }
    return transposed_matrix;
}
int main()
{
    vector<vector<int>>matrix={{1,2,3},{4,5,6}};
    cout<<"Default Matrix"<<endl;
    DisplayMatrix(matrix);
    AddRow(matrix,{7,8,9});
    AddRow(matrix,{3,2,1});
    cout<<"Matrix After Adding 2 Rows"<<endl;
    DisplayMatrix(matrix);
    AddColumn(matrix,{1,3,9,3});
    DisplayMatrix(matrix);
    cout<<"Transposed Matrix"<<endl;
    DisplayMatrix(MatrixTranspose(matrix));
}