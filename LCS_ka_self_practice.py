#LONGEST COMMON SUBSEQUENCE
#USING RECURSION
#IT TAKES O(2^n)time complexity
def LCS(s,t,p,q):
    if(p==0 or q==0):
        return 0
    elif s[p-1]==t[q-1]:
        return 1+LCS(s,t,p-1,q-1)
    else:
        return max(LCS(s,t,p,q-1),LCS(s,t,p-1,q))

l=input("Enter string")
r=input("Enter string")
print(LCS(l,r,len(l),len(r)))

def LCS(x,y):
    m=len(x)
    n=len(y)
    L=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif x[i-1]==y[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])


    return L[m][n]

x="TUSHAR"
y="TFDSHWE"
print(LCS(x,y))
