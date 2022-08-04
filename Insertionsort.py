#Insertionsort
def insertion(arr):
    for i in range(1,len(arr)):
        first=arr[i]
        j=i-1
        while j>=0 and first<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=first
        

li=[17,45,3,87,34,90,36]
insertion(li)
lst=[]
print("Sorted array is")
for i in range(len(li)):
    lst.append(li[i])
print(lst)
        
