

import collections

n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a.append(a[i]-1)
    a.append(a[i]+1)

a_count=collections.Counter(a)
print(max(a_count.values()))