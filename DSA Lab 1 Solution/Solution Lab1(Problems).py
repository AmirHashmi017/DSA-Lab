#Problem 1
def SearchA(Arr,x):
    indices=[]
    for i in range(len(Arr)):
        if(Arr[i]==x):
            indices.append(i)
    return indices
#Driver
# print(SearchA([22,2,1,7,11,13,5,2,9],2))
#Problem 2
def SearchB(Arr,x):
    indices=[]
    for i in range(len(Arr)):
        if(Arr[i]==x):
            indices.append(i)
        if(Arr[i]>x):
            return indices
    return indices
#Driver
# print(SearchB([22,2,1,7,11,13,5,2,9],2))
#Problem 3
def Minimum(Arr,starting,ending):
    minimumvalue=Arr[starting]
    minimumindex=starting
    for i in range(starting,ending+1,1):
        # print(Arr[i])
            if(Arr[i]<minimumvalue):
                minimumvalue=Arr[i]
                minimumindex=i
    return minimumindex
#Driver
# print(Minimum([3,4,7,8,0,1,23,-2,-5],4,7))
#Problem 4
def Sort4(Arr):
    minimumindex=0
    sortedarray=[]
    while(len(Arr)>0):
        minimumindex=Minimum(Arr,0,len(Arr)-1)
        minimumvalue=Arr[minimumindex]
        sortedarray.append(minimumvalue)
        Arr.remove(minimumvalue)
    return sortedarray
#Driver
# print(Sort4([1,9,11,2,4,5,-3,-1]))
#Problem 5
def StringReverse(str, starting,ending):
    reverse=str[ending:starting-1:-1]
    return reverse
#Driver
# print(StringReverse("University of Engineering and Technology Lahore",27,40))
#Problem 6 (Iterative)
def SumIterative(number):
    sum=0
    while(number>0):
        sum+=number%10
        number=int(number/10)
    return sum 
#Driver
# print(SumIterative(1524))
#Problem 6 (Recursive)
def SumRecursive(number):
    if number == 0:
        return 0
    return int(number % 10) + SumRecursive(int(number/10))
# Driver
# print(SumRecursive(1524))
#Problem 7(Column Wise)
def ColumnWiseSum(Mat):
    column_sum=[]
    sum=0
    for i in range (len(Mat)):
        sum=0
        for j in range(len (Mat[0])):
            sum+=Mat[j][i]
        column_sum.append(sum)
    return column_sum
# Driver
# matrix=[[1,13,13],[5,11,6],[4,4,9]]
# print(ColumnWiseSum(matrix))
#Problem 7(Row Wise)
def RowWiseSum(Mat):
    column_sum=[]
    sum=0
    for i in range (len(Mat)):
        sum=0
        for j in range(len (Mat[0])):
            sum+=Mat[i][j]
        column_sum.append(sum)
    return column_sum
# Driver
# matrix=[[1,13,13],[5,11,6],[4,4,9]]
# print(RowWiseSum(matrix))
#Problem 8
def SortedMerge(Arr1, Arr2):
    mergedarray=[]
    i=0
    j=0
    while(i<len(Arr1) and j<len(Arr2)):
        if Arr1[i]<Arr2[j]:
            mergedarray.append(Arr1[i])
            i+=1
        else:
            mergedarray.append(Arr2[j])
            j+=1
    while i<len(Arr1):
        mergedarray.append(Arr1[i])
        i+=1
    while j<len(Arr2):
        mergedarray.append(Arr2[j])
        j+=1
    return mergedarray
#Driver
# A = [0,3,4,10,11]
# B = [1,8,13,24]
# print (SortedMerge(A,B))
#Problem 9
def PalindromRecursive(inputstr):
    if(len(inputstr)<=1):
        return True
    elif(inputstr[0]==inputstr[-1]):
        return PalindromRecursive(inputstr[1:-1])
    return False
#Driver
# if PalindromRecursive("radar"):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
#Problem 10
def Sort10(Arr):
    positivenumbers=[]
    negativenumbers=[]
    result=[]
    for i in range(len(Arr)):
        if(Arr[i]<0):
            negativenumbers.append(Arr[i])
        else:
            positivenumbers.append(Arr[i])
    positivenumbers=Sort4(positivenumbers)
    negativenumbers=Sort4(negativenumbers)
    i=0
    j=0
    while (i<len(positivenumbers)and j<len(negativenumbers)):
        result.append(negativenumbers[j])
        result.append(positivenumbers[i])
        i+=1
        j+=1
    while i < len(negativenumbers):
        result.append(negativenumbers[i])
        i += 1
    while j < len(positivenumbers):
        result.append(positivenumbers[j])
        j+=1
    return result

#Driver
# print(Sort10([10, -1, 9, 20, -3, -8, 22, 9, 7]))







            

        
        




