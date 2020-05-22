a,b=list(map(int,input().split()))
c=list(int(i) for i in input().split())  
c.sort(reverse=True)
count=0
for i in range(b):
    count+=c[i]
print(count)