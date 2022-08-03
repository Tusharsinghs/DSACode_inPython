#Print a pattern without using any loop
def pattern(n):
    if n==0:
        return '*'
    else:
        return (n+1)*'*'

n=int(input())
if n<0:
    print("Please enter valid number")
else:
    for i in range(n):
        print(pattern(i))
