import math
import copy
n=int(input())
x=list(map(int,input().split()))
a=x.copy()
ansl=[]
for i in range(n-1):
    ans=0
    x=a.copy()
    for j in range(0,len(x)-2):
        print("DFGHJ")
        ans+=(x[j+1]-x[j])
        x.pop(j)
    ansl.append(ans)
kai=math.factorial(n-1)
print(ansl)
print(kai)
print(sum(ansl)//kai)