import random
def RandomArray(size):
    array=[]
    for i in range(0,size,1):
        array.append(random.randint(-15000,15000))
    return array