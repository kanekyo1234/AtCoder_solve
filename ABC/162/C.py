import math
k=int(input())
k+=1
ans=0
for i in range(1,k):
    for j in range(1,k):
        for z in range(1,k):
            ans+=math.gcd(math.gcd(i,j),z)
print(ans)