import funcs
import Save_In_CSV
def InsertionSort(array,start, end):
    for i in range(start+1,end,1):
        key=array[i]
        j=i-1
        while j>=start and array[j]>key:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array

def main():
    import time
    n=30000
    arr=funcs.RandomArray(n)
    start_time = time.time()
    result=InsertionSort(arr,0,len(arr))
    end_time = time.time()
    runtime = end_time - start_time
    print("Runtime of Insertion Sort at",n,"is",runtime,"seconds")
    print(result)
    Save_In_CSV.CSV_Write("SortedInsertionSort.csv",result)

if __name__ == '__main__':
    main()