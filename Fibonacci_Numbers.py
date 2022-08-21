#Recursion Problem
def fibo(n):
    if n<=1:
        return n
    else:
        #new_last=second_last+last
        #second_last=last
        return fibo(n-1)+fibo(n-2)
n=5
for i in range(n):
    print(fibo(i))

#Dynamic Programming
def fibo(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(fibo(5))
