n=int(input())

p=list(map(int,input().split()))
count=0
jugh=0
for i in range(n):
    if p[i]==i+1:
        if jugh!=1:
            jugh=1
            count+=1
        else:
            jugh=0
    else:
        jugh=0

print(count)