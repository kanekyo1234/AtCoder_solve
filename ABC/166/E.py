import collections
n=int(input())
a=list(map(int,input().split()))
ans=0
b=[]
for i in range(n):
    b.append(abs(a[i]-i+1))
#print(b)
ans=0
b=collections.Counter(b)
for i in b.values():
    ans+=i*(i-1)//2
print(ans)

#print(ans)