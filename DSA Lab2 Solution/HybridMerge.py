import funcs
import Save_In_CSV
def HybridMergeSort(array,start,end,n=6):
    if(end-start<=6):
        InsertionSort(array,start,end)
    else:
        mid=int((start+end)/2)
        HybridMergeSort(array,start,mid)
        HybridMergeSort(array,mid+1,end)
        Merge(array,start,mid+1,end)
        
def Merge(array,p,q,r):
    LeftArray=array[p:q]
    RightArray=array[q:r+1]
    mergedindex=p
    i=0
    j=0
    while (i<len(LeftArray) and j<len(RightArray)):
        if(LeftArray[i]<=RightArray[j]):
            array[mergedindex]=LeftArray[i]
            i+=1
        else:
            array[mergedindex]=RightArray[j]
            j+=1
        mergedindex+=1
    while i<len(LeftArray):
        array[mergedindex]=LeftArray[i]
        i+=1
        mergedindex+=1
    while j<len(RightArray):
        array[mergedindex]=RightArray[j]
        j+=1
        mergedindex+=1
def InsertionSort(array,start,end):
    for i in range(start+1,end+1,1):
        key=array[i]
        j=i-1
        while j>=start and array[j]>key:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
        
def main():
    import time
    n=30000
    arr=funcs.RandomArray(n)
    start_time = time.time()
    HybridMergeSort(arr,0,len(arr)-1)
    end_time = time.time()
    runtime = end_time - start_time
    print("Runtime of Hybrid Merge Sort at",n,"is",runtime,"seconds")
    print(arr)
    Save_In_CSV.CSV_Write("SortedHybridMergeSort.csv",arr)

if __name__ == '__main__':
    main()
