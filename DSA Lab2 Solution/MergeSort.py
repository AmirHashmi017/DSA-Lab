import funcs
import Save_In_CSV
def MergeSort(array,start,end):
    n=end-start
    if(n<=0):
        return
    mid=int((start+end)/2)
    MergeSort(array,start,mid)
    MergeSort(array,mid+1,end)
    Merge(array,start,mid+1,end)
def Merge(array, p, q, r):
    LeftArray=array[p:q]
    RightArray=array[q:r+1]
    i=0
    j=0
    mergedindex=p
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
def main():
    import time
    n=30000
    arr=funcs.RandomArray(n)
    start_time = time.time()
    MergeSort(arr,0,len(arr))
    end_time = time.time()
    runtime = end_time - start_time
    print("Runtime of Merge Sort at",n,"is",runtime,"seconds")
    print(arr)
    Save_In_CSV.CSV_Write("SortedMergeSort.csv",arr)

if __name__ == '__main__':
    main()

