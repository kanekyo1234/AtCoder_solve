import collections
na,nb=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


c=a+b
s=len(set(c))
c=collections.Counter(c)

count=0

for v in c.values():
    if 2<=v:
        count+=1
print(count/s)