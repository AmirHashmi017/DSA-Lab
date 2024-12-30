#Task01
def CountingSort(inputarray):
    minimumvalue = min(inputarray)
    maximumvalue = max(inputarray)
    
    elementsrange = maximumvalue - minimumvalue + 1
    count = [0] * elementsrange
    output = [0] * len(inputarray)

    for i in range(0,len(inputarray),1):
        shiftedvalue = inputarray[i] - minimumvalue
        count[shiftedvalue] += 1

    for i in range(1, len(count),1):
        count[i] += count[i - 1]

    for i in range(len(inputarray) - 1, -1, -1):
        shiftedvalue = inputarray[i] - minimumvalue
        count[shiftedvalue] -= 1
        output[count[shiftedvalue]] = inputarray[i]

    return output

#Driver
arr=[-5, -10, 0, -3, 8, 5,-1, 10]
print(CountingSort(arr))

#Task 02

def RadixSort(inputarray):
    maximumvalue = max(inputarray)
    significant = 1
    while maximumvalue // significant > 0:
        CountingSortForRadix(inputarray, significant)
        significant *= 10  
    return inputarray

def CountingSortForRadix(inputarray, significant):
    count = [0] * 10
    output = [0] * len(inputarray)

    for i in range(len(inputarray)):
        digit = (inputarray[i] // significant) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(inputarray) - 1, -1, -1):
        digit = (inputarray[i] // significant) % 10
        count[digit] -= 1
        output[count[digit]] = inputarray[i]

    for i in range(len(inputarray)):
        inputarray[i] = output[i]


#Driver
arr=[110, 45, 65,50, 90,602, 24, 2, 66]
print(RadixSort(arr))


#Task 03

def BucketSort(Arr):
    n = len(Arr)
    buckets = [[] for i in range(n)]

    for i in range(n):
        index = int(Arr[i] * n)
        buckets[index].append(Arr[i])

    for i in range(n):
        buckets[i] = InsertionSort(buckets[i])
    output = []
    for i in range(n):
        output.extend(buckets[i])
    
    return output

def InsertionSort(Arr):
    for i in range(1, len(Arr)):
        key = Arr[i]
        j = i - 1
        while j >= 0 and Arr[j]>key:
            Arr[j + 1] = Arr[j]
            j -= 1
        Arr[j + 1] = key
    return Arr

# Driver
Arr=[0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(BucketSort(Arr))