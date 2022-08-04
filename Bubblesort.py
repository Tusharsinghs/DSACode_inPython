#Bubble Sort
def bubble(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr

li=[12,5,14,89,3,90,12,45,856,3,25]            
c=bubble(li)        
print("Sorted array is",c)
