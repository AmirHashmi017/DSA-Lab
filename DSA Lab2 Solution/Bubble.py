import funcs
import Save_In_CSV
def BubbleSort(array,start, end):
    for i in range(start,end-1,1):

        for j in range(start,end-i-1,1):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
    return array

import time
n=30000
arr=funcs.RandomArray(n)
start_time = time.time()
result=BubbleSort(arr,0,len(arr))
end_time = time.time()
runtime = end_time - start_time
print("Runtime of Bubble Sort at",n,"is",runtime,"seconds")
print(result)
Save_In_CSV.CSV_Write("SortedBubbleSort.csv",result)