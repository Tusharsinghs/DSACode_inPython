#Check if a number is palindrome or not
def num(n,r):
    if n==0:
        return r
    else:
        return num(n//10,r*10+n%10)

x=int(input())
li=num(x,0)
if li==x:
    print("Number is paindrome")
else:
    print("Not palindrome")
