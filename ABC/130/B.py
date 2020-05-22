a,b=map(int,input().split())
c=list(map(int,input().split()))
count=1
sum=0
for i in range(a):
    sum+=c[i]
    if(sum<=b):
        count+=1
print(count)