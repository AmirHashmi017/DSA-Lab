import funcs
import Save_In_CSV
def InsertionSort(array,start, end):
    for i in range(start+1,end,1):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array

import time
start_time = time.time()
arr=funcs.RandomArray(30000)
n=30000
result=InsertionSort(arr,0,len(arr))
end_time = time.time()
runtime = end_time - start_time
print("Runtime of Insertion Sort at",n,"is",runtime,"seconds")
print(result)
Save_In_CSV.CSV_Write("SortedInsertionSort.csv",result)
