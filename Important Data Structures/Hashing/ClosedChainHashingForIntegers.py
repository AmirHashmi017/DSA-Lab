def HashFunction(Hashtable, array):
    for i in range(len(array)):
        tsize=len(Hashtable)
        index = array[i] % tsize
        if(CalculateLoadFactor(Hashtable)>=0.75):
            Hashtable=Rehashing(Hashtable)
            tsize=len(Hashtable)
            index = array[i] % tsize
        if Hashtable[index] is None:
            Hashtable[index] = array[i]
        else:
            # LinearProbing(array[i], index, Hashtable)
            # QuadraticProbing(array[i], index, Hashtable)
            DoubleHashing(array[i], index, Hashtable)
    return Hashtable

def CalculateLoadFactor(hashtable):
    elementscount=0
    for element in hashtable:
        if(element!=None):
            elementscount+=1
    LoadFactor=elementscount/len(hashtable)
    return LoadFactor

def Rehashing(hashtable):
    newtsize=len(hashtable)*2
    newhashtable=[None]*newtsize
    array=[]
    for element in hashtable:
        if(element!=None):
            array.append(element)
    HashFunction(newhashtable,array)
    return newhashtable


def LinearProbing(value, current_index, Hashtable):
    tsize = len(Hashtable)
    for j in range(1, tsize):
        new_index = (current_index + j) % tsize
        if Hashtable[new_index] is None:
            Hashtable[new_index] = value
            return

def QuadraticProbing(value, current_index, Hashtable):
    tsize = len(Hashtable)
    for j in range(1, tsize):
        new_index = (current_index + j ** 2) % tsize
        if Hashtable[new_index] is None:
            Hashtable[new_index] = value
            return

def GetDoubleHash(value):
    return 7 - (value % 7)

def DoubleHashing(value, current_index, Hashtable):
    tsize = len(Hashtable)
    step_size = GetDoubleHash(value)
    for j in range(1, tsize):
        new_index = (current_index + j * step_size) % tsize
        if Hashtable[new_index] is None:
            Hashtable[new_index] = value
            return

def SearchValue(Hashtable, value):
    tsize = len(Hashtable)
    index = value % tsize
    if Hashtable[index] == value:
        return index
    else:
        # return FindLinearProbing(value, index, Hashtable)
        # return FindQuadraticProbing(value, index, Hashtable)
        return FindDoubleHashing(value, index, Hashtable)
    
def FindLinearProbing(value, current_index, Hashtable):
    tsize = len(Hashtable)
    for j in range(1, tsize):
        new_index = (current_index + j) % tsize
        if Hashtable[new_index] == value:
            return new_index
    return "Not Found"

def FindQuadraticProbing(value, current_index, Hashtable):
    tsize = len(Hashtable)
    for j in range(1, tsize):
        new_index = (current_index + j ** 2) % tsize
        if Hashtable[new_index] == value:
            return new_index
    return "Not Found"

def FindDoubleHashing(value, current_index, Hashtable):
    tsize = len(Hashtable)
    step_size = GetDoubleHash(value)
    for j in range(1, tsize):
        new_index = (current_index + j * step_size) % tsize
        if Hashtable[new_index] == value:
            return new_index
    return "Not Found"


# Testing Array
Array = [1, 3, 5, 2, 14, 19, 27]
tsize = len(Array)

# Test Linear Probing
# print("Testing Linear Probing")
# hashtable_linear = [None] * tsize
# HashFunction(hashtable_linear, Array)
# print("Hash Table (Linear Probing):", hashtable_linear)
# print("Search for value 5:", SearchValue(hashtable_linear, 5))
# print("Search for value 14:", SearchValue(hashtable_linear, 14))
# print("Search for non-existent value 10:", SearchValue(hashtable_linear, 10))
# print()

# Test Quadratic Probing
# print("Testing Quadratic Probing")
# hashtable_quadratic = [None] * tsize
# HashFunction(hashtable_quadratic, Array)
# print("Hash Table (Quadratic Probing):", hashtable_quadratic)
# print("Search for value 5:", SearchValue(hashtable_quadratic, 5))
# print("Search for value 14:", SearchValue(hashtable_quadratic, 14))
# print("Search for non-existent value 10:", SearchValue(hashtable_quadratic, 10))
# print()

# Test Double Hashing
print("Testing Double Hashing")
hashtable_double = [None] * tsize
hashtable_double=HashFunction(hashtable_double, Array)
print("Hash Table (Double Hashing):", hashtable_double)
print("Search for value 5:", SearchValue(hashtable_double, 5))
print("Search for value 14:", SearchValue(hashtable_double, 14))
print("Search for non-existent value 10:", SearchValue(hashtable_double, 10))
print()
