def LinearSearch(array,value):
    for i in range(len(array)):
        if(array[i]==value):
            return i
    return "Not Found"

def BinarySearch(Array,value):
    start=0
    end=len(Array)-1
    while(start<=end):
        mid=(start+end)//2
        if(Array[mid]==value):
            return mid
        elif(value<Array[mid]):
            end=mid-1
        elif(value>Array[mid]):
            start=mid+1
    return "Not Found"


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    print("Linear Search Results:")
    print("Searching for 30:", LinearSearch(arr, 30))  
    print("Searching for 70:", LinearSearch(arr, 70)) 
    print("Searching for 100:", LinearSearch(arr, 100)) 
    
    print("\nBinary Search Results (array must be sorted):")
    print("Searching for 30:", BinarySearch(arr, 30))
    print("Searching for 70:", BinarySearch(arr, 70))
    print("Searching for 100:", BinarySearch(arr, 100))
        