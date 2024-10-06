def RemoveNegatives(numbers):
    numbers=[num for num in numbers if num>=0]
    return numbers
def FindMaximum(numbers):
    for i in range(0,len(numbers)-1,1):
        if(numbers[i]>numbers[i+1]):
            numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
    return numbers[len(numbers)-1]

def FindMinimum(numbers):
    for i in range(0,len(numbers)-1,1):
        if(numbers[i]<=numbers[i+1]):
            numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
    return numbers[len(numbers)-1]
def FindAverage(numbers):
    Average=sum(numbers)/len(numbers)
    return Average

#Driver
numbers=[3,2,4,5,7,9,-11,2,-10]
print(f"Maximum Number: {FindMaximum(numbers)}")
print(f"Minimum Number: {FindMinimum(numbers)}")
print(f"Average of Numbers: {FindAverage(numbers)}")
newnumbers=[3,2,4,5,7,9,-11,2,-10]
print(f"After removal of negatives Numbers are: {RemoveNegatives(newnumbers)}")