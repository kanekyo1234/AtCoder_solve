import collections
n=int(input())
a=[int(input()) for _ in range(n)]
a=collections.Counter(a)
ans=0
for v in a.values():
    ans+=v-1
print(ans)