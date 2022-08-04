#Binary serach in an array arranged in ascending order.
def binary(arr,n):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(low+high)//2

        if arr[mid]<n:
            low=mid+1
        elif arr[mid]>n:
            high=mid-1
        else:
            return mid
    return -1


li=[12,23,44,67,69,87,90]
x=int(input("Enter element to search"))
t=binary(li,x)
if t!=-1:
    print("Element found at position %d"%t)
else:
    print("Element not found")
  
