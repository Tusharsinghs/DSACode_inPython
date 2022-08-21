#Simple recursive function
def binomialCoeff(n,k):
    if k>n:
        return 0
    if k==0 or k==n:
        return 1
    return binomialCoeff(n-1,k-1)+binomialCoeff(n-1,k)

n=5
k=2
print("Value of C(%d,%d) is %d"%(n,k,binomialCoeff(n,k)))
        
#Using Dynamic Programming
def binomialCoeff(n,k):
    C=[[0 for x in range(k+1)]for x in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                C[i][j]=1

            else:
                C[i][j]=C[i-1][j-1]+C[i-1][j]
    return C[n][k]

n=5
k=4
print("Value of C(%d,%d) is %d"%(n,k,binomialCoeff(n,k)))
