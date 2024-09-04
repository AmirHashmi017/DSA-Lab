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
print(Sort4([1,9,11,2,4,5,-3,-1]))
#Problem 5
def StringReverse(str, starting,ending):
    reverse=str[ending:starting-1:-1]
    return reverse
#Driver
# print(StringReverse("University of Engineering and Technology Lahore",27,40))



        
        




