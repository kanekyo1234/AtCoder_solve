import collections
n=int(input())
a=list(map(int,input().split()))

d=collections.Counter(a)
#print(d)
ans=0
for v in d.values():
    ans+=v*(v-1)//2
#print(ans)

for i in range(n):
    ans2=ans
    v=d[a[i]]
    ans2-=v*(v-1)//2
    v-=1
    ans2+=v*(v-1)//2
    print(ans2)