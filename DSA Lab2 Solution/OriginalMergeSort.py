import funcs
def MergeSort(array):
    n=len(array)
    if n<=1:
        return array
    mid=n//2
    LeftArray=MergeSort(array[0:mid])
    RightArray=MergeSort(array[mid:n])
    return Merge(LeftArray,RightArray)

def Merge(LeftArray,RightArray):
    i=0
    j=0
    sorted=[]
    while (i<len(LeftArray) and j<len(RightArray)):
        if LeftArray[i]<=RightArray[j]:
            sorted.append(LeftArray[i])
            i+=1
        else:
            sorted.append(RightArray[j])
            j+=1
    while i<len(LeftArray):
        sorted.append(LeftArray[i])
        i+=1
    while j<len(RightArray):
        sorted.append(RightArray[j])
        j+=1
    return sorted

#Driver
n=100
array=funcs.RandomArray(n)
print(MergeSort(array))

