def KSelect(Arr,k):
    pivot_index=Partition(Arr,0,len(Arr))
    pivotvalue=Arr[pivot_index]
    leftarr=Arr[:pivot_index]
    rightarr=Arr[pivot_index+1:]
    if(len(leftarr)==k-1):
        return pivotvalue
    elif(len(leftarr)>k-1):
        return KSelect(leftarr,k)
    elif(len(leftarr)<k-1):
        return KSelect(rightarr,k-len(leftarr)-1)
    
def Partition(Arr,start,end):
    end_pivot=Arr[end-1]
    i=start-1
    for j in range(0,end-1,1):
        if(Arr[j]<=end_pivot):
            i+=1
            Arr[i],Arr[j]=Arr[j],Arr[i]
    Arr[i+1],Arr[end-1]=Arr[end-1],Arr[i+1]
    return i+1

arr = [12, 3, 5, 7, 19, 10]
k = 5
print(f"The {k}-th smallest element is: {KSelect(arr, k)}")