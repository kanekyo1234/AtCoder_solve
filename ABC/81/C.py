import collections

n,k=map(int,input().split())

a=list(map(int,input().split()))

a_count=collections.Counter(a)

aco=sorted(a_count.values())
ans=0
#for i in range(len(a_count)-k):

for i in range(len(aco)-k):
    ans+=aco[i]
    

print(ans)