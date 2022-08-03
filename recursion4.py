#Print all possible strings of length k that can be formed from a set of n characters
def printAllKLength(set, k):
    n = len(set)
    printAllKLengthRec(set, "", n, k)
def printAllKLengthRec(set, prefix, n, k):
    if (k == 0):
        print(prefix)
        return
    for i in range(n):
        newPrefix = prefix + set[i]
        printAllKLengthRec(set, newPrefix, n, k - 1)
 
print("First Test")
set1 = ['a', 'b']
k = 3
printAllKLength(set1, k)
     
print("\nSecond Test")
set2 = ['a', 'b', 'c', 'd']
k = 1
printAllKLength(set2, k)
 
