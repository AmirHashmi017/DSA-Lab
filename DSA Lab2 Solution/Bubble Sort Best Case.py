def BubbleSort(array, start, end):
    for i in range(start, end-1, 1):
        swapped = False

        for j in range(start, end-i-1, 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True  
        if not swapped:
            break

    return array
#Driver
print(BubbleSort([5,7,9,3,1,2,4,5,6],0,9))