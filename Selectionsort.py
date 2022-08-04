#SelectionSort
def selection(arr):
    for i in range(0,len(arr)-1):
        indexOfmin=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[indexOfmin]):
                indexOfmin=j
        temp=arr[i]
        arr[i]=arr[indexOfmin]
        arr[indexOfmin]=temp
    return arr
            
            
li=[17,45,3,87,34,90,36]
print("Sorted aray is",selection(li))
