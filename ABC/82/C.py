import collections

n=int(input())
a=list(map(int,input().split()))

a_count=collections.Counter(a)
count=0
for key ,atai in a_count.items():
    if key<=atai:
        count+=key
    
print(n-count)
