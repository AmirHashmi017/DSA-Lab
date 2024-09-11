import funcs
import Save_In_CSV
def SelectionSort(array,start, end):
    for i in range(start,end,1):
        minimumindex=i
        for j in range(i+1,end,1):
            if(array[j]<array[minimumindex]):
                minimumindex=j
        array[i],array[minimumindex]=array[minimumindex],array[i]
    return array

import time
start_time = time.time()
arr=funcs.RandomArray(30000)
n=30000
result=SelectionSort(arr,0,len(arr))
end_time = time.time()
runtime = end_time - start_time
print("Runtime of Selection Sort at",n,"is",runtime,"seconds")
print(result)
Save_In_CSV.CSV_Write("SortedSelectionSort.csv",result)