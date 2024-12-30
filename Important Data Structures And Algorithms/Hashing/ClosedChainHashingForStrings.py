def GetStringAscii(word):
    return sum(ord(char) for char in word)
def HashFunction(Hashtable, array):
    for i in range(len(array)):
        tsize = len(Hashtable)
        index = GetStringAscii(array[i]) % tsize
        if(CalculateLoadFactor(Hashtable)>0.75):
            Hashtable = Rehashing(Hashtable)
            tsize = len(Hashtable)
            index = GetStringAscii(array[i]) % tsize
        if Hashtable[index] is None:
            Hashtable[index] = array[i]
            
        else:
            LinearProbing(array[i], index, Hashtable)
            # QuadraticProbing(array[i], index, Hashtable)
            # DoubleHashing(array[i], index, Hashtable)
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
    return 7 - (GetStringAscii(value) % 7)

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
    index = GetStringAscii(value) % tsize
    if Hashtable[index] == value:
        return index
    else:
        return FindLinearProbing(value, index, Hashtable)
        # return FindQuadraticProbing(value, index, Hashtable)
        # return FindDoubleHashing(value, index, Hashtable)
    
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


# Test String Array
Array = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
tsize = 7

# Test Linear Probing
print("Testing Linear Probing")
hashtable_linear = [None] * tsize
hashtable_linear=HashFunction(hashtable_linear, Array)
print("Hash Table (Linear Probing):", hashtable_linear)
print("Search for 'banana':", SearchValue(hashtable_linear, "banana"))
print("Search for 'elderberry':", SearchValue(hashtable_linear, "elderberry"))
print("Search for non-existent value 'kiwi':", SearchValue(hashtable_linear, "kiwi"))
print()

# Test Quadratic Probing
# print("Testing Quadratic Probing")
# hashtable_quadratic = [None] * tsize
# HashFunction(hashtable_quadratic, Array)
# print("Hash Table (Quadratic Probing):", hashtable_quadratic)
# print("Search for 'banana':", SearchValue(hashtable_quadratic, "banana"))
# print("Search for 'elderberry':", SearchValue(hashtable_quadratic, "elderberry"))
# print("Search for non-existent value 'kiwi':", SearchValue(hashtable_quadratic, "kiwi"))
# print()

# Test Double Hashing
# print("Testing Double Hashing")
# hashtable_double = [None] * tsize
# HashFunction(hashtable_double, Array)
# print("Hash Table (Double Hashing):", hashtable_double)
# print("Search for 'banana':", SearchValue(hashtable_double, "banana"))
# print("Search for 'elderberry':", SearchValue(hashtable_double, "elderberry"))
# print("Search for non-existent value 'kiwi':", SearchValue(hashtable_double, "kiwi"))
# print()

