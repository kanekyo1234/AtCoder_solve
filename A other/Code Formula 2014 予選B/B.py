s=str(input())
n=len(s)#4
k=0
g=0
for i in range(0,n):
    if i%2!=1:
        k+=int(s[n-i-1])
    else:
        g+=int(s[n-i-1])
print(g,k)