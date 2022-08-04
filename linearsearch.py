arr=[12,45,67,23,8,1,0]
l=len(arr)
x=int(input("Enter element to search"))
for i in range(l):
    if arr[i]==x:
        print("Element found at %d position"%i)
        break
else:
    print("Not found")
    
