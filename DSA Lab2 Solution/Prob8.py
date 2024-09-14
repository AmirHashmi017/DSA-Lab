import funcs
import Insertion
import MergeSort
import time
def CalclulateTime(sortingfunction,array,start,end):
    starttime=time.time()
    sortingfunction(array,start,end)
    endtime=time.time()
    runtime=endtime-starttime
    return runtime
#Reading from file
given_file = open (file = 'words.txt', mode = 'r')
lines = given_file. readlines ()
words = []
for s in lines:
    words.append(s.strip())

InsertionWords=words.copy()
MergeWords=words.copy()
#Sorting using Insertion sort before Shuffling and calculating time
Insertionruntimebeforeshuffling=CalclulateTime(Insertion.InsertionSort,InsertionWords,0,len(InsertionWords))
print("RunTime of Insertion Sort Before Shuffling is: ",Insertionruntimebeforeshuffling)
print(InsertionWords)
#Sorting using Merge sort before Shuffling and calculating time
Mergeruntimebeforeshuffling=CalclulateTime(MergeSort.MergeSort,MergeWords,0,len(MergeWords))
print("RunTime of Merge Sort Before Shuffling is: ",Mergeruntimebeforeshuffling)
print(MergeWords)
#Shuffling Array
ShuffledInsertionWords=funcs.ShuffleArray(InsertionWords,0,len(InsertionWords)-1)
ShuffledMergeWords=funcs.ShuffleArray(MergeWords,0,len(MergeWords)-1)
#Sorting using Insertion sort after Shuffling and calculating time
Insertionruntimeaftershuffling=CalclulateTime(Insertion.InsertionSort,ShuffledInsertionWords,0,len(ShuffledInsertionWords))
print("RunTime of Insertion Sort after Shuffling is: ",Insertionruntimeaftershuffling)
print(ShuffledInsertionWords)
#Sorting using Merge sort after Shuffling and calculating time
Mergeruntimeaftershuffling=CalclulateTime(MergeSort.MergeSort,ShuffledMergeWords,0,len(ShuffledMergeWords))
print("RunTime of Merge Sort after Shuffling is: ",Mergeruntimeaftershuffling)
print(ShuffledMergeWords)
#Comparing both before and after shuffling
if Insertionruntimeaftershuffling > Insertionruntimebeforeshuffling:
    print("Insertion Sort took longer after shuffling.")
else:
    print("Insertion Sort was faster after shuffling.")

if Mergeruntimeaftershuffling > Mergeruntimebeforeshuffling:
    print("Merge Sort took longer after shuffling.")
else:
    print("Merge Sort was faster after shuffling.")

