#Program to find factorial of a number
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n

x=int(input("Enter number"))
f=fact(x)
print("Factorial of %d is %d"%(x,f))

    
