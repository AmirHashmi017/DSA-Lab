def QuickSort(Arr,start,end):
    if(start<end):
        pivot=Partition(Arr,start,end)
        QuickSort(Arr,start,pivot)
        QuickSort(Arr,pivot+1,end)

def Partition(Arr,start,end):
    endpivot=Arr[end-1]
    i=start-1
    for j in range(start,end-1,1):
        if(Arr[j]<=endpivot):
            i+=1
            Arr[i],Arr[j]=Arr[j],Arr[i]
    Arr[i+1],Arr[end-1]=Arr[end-1],Arr[i+1]
    return i+1

Arr=[1,9,8,4,5,6,7]
QuickSort(Arr,0,7)
print(Arr)
        
