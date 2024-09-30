def KSelect(Arr,k):
    pivot=Partition(Arr,0,len(Arr))
    l=pivot-1
    r=len(Arr)-(pivot+1)
    if(r==k-1):
        return Arr[pivot]
    if(pivot>k-1):
