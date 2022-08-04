#Quick sorting
def partition(l,r,arr):
    pivot,ptr=arr[r],l  #last element willl be pivot first will be ptr
    for i in range(l,r):
        if arr[i]<=pivot:
            arr[i],arr[ptr]
            ptr+=1
    arr[ptr],arr[r]=arr[r],arr[ptr]
    return ptr

def quick(l,r,arr):
    if len(arr)==1:
        return arr
    if l<r:
        pi=partition(l,r,arr)
        quick(l,pi-1,arr)
        quick(pi+1,r,arr)
    return arr
li=[12,6,89,34,56,0,78]
print(quick(0,len(li)-1,li))
